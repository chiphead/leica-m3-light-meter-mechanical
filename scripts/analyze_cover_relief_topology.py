#!/usr/bin/env python3
"""Diagnose topology and boolean conservation for rejected original-cover reliefs.

Read-only source STEP. No STEP candidate is exported and no frozen component is modified.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq
from OCP.BRepOffsetAPI import BRepOffsetAPI_MakeOffsetShape
from OCP.BRepOffset import BRepOffset_Skin
from OCP.GeomAbs import GeomAbs_JoinType

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"source/leica_m3_light_meter.stp"
OUT=ROOT/"working/COVER_RELIEF_TOPOLOGY_DIAGNOSTIC.md"
TOL=1e-3
EPS=1e-7

def bbox(s):
    b=s.BoundingBox()
    return [round(float(x),5) for x in (b.xmin,b.ymin,b.zmin,b.xmax,b.ymax,b.zmax)]

def offset(shape, amount):
    if amount <= EPS: return shape
    b=BRepOffsetAPI_MakeOffsetShape()
    b.PerformByJoin(shape.wrapped,float(amount),TOL,BRepOffset_Skin,False,False,
                    GeomAbs_JoinType.GeomAbs_Arc,False)
    if not b.IsDone(): raise RuntimeError("3D offset did not complete")
    s=cq.Shape.cast(b.Shape())
    if not s.isValid() or len(s.Solids())!=1:
        raise RuntimeError(f"invalid cutter valid={s.isValid()} solids={len(s.Solids())}")
    return s.Solids()[0]

def component(s, index):
    return {"index":index,"volume_mm3":round(float(s.Volume()),6),
            "area_mm2":round(float(s.Area()),6),"bbox_mm":bbox(s),
            "center_of_mass_mm":[round(float(v),5) for v in
              (s.Center().x,s.Center().y,s.Center().z)],
            "face_count":len(s.Faces()),"shell_count":len(s.Shells()),
            "valid":bool(s.isValid())}

def main():
    source=cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(source)!=7: raise RuntimeError(f"expected 7 solids, got {len(source)}")
    cover=source[4]
    moving=source[3].translate(cq.Vector(10,0,0))
    results=[]
    for clearance in (0.0,0.2):
        row={"clearance_mm":clearance,"original_cover_volume_mm3":round(float(cover.Volume()),6)}
        try:
            cutter=offset(moving,clearance)
            intersection=cover.intersect(cutter)
            cut=cover.cut(cutter)
            comps=sorted(cut.Solids(),key=lambda x:x.Volume(),reverse=True)
            sum_components=sum(float(x.Volume()) for x in comps)
            row.update({
              "cutter_valid":bool(cutter.isValid()),
              "cutter_volume_mm3":round(float(cutter.Volume()),6),
              "cover_cutter_intersection_volume_mm3":round(float(intersection.Volume()),6),
              "cut_shape_type":cut.ShapeType(),"cut_valid":bool(cut.isValid()),
              "cut_reported_volume_mm3":round(float(cut.Volume()),6),
              "component_volume_sum_mm3":round(sum_components,6),
              "volume_conservation_error_mm3":round(
                float(cover.Volume())-float(intersection.Volume())-sum_components,6),
              "components":[component(s,i) for i,s in enumerate(comps)],
              "pairwise_component_clearances_mm":[]
            })
            for i in range(len(comps)):
                for j in range(i+1,len(comps)):
                    row["pairwise_component_clearances_mm"].append({
                      "a":i,"b":j,"distance_mm":round(float(comps[i].distance(comps[j])),6)})
            row["remaining_vs_moving_overlap_mm3"]=round(float(cut.intersect(moving).Volume()),6)
            row["cut_vs_original_common_volume_mm3"]=round(float(cut.intersect(cover).Volume()),6)
            # Compare geometric set identity via symmetric-difference volume.
            lost=cover.cut(cut)
            added=cut.cut(cover)
            row["lost_cover_volume_mm3"]=round(float(lost.Volume()),6)
            row["added_geometry_volume_mm3"]=round(float(added.Volume()),6)
            row["lost_region_bbox_mm"]=bbox(lost) if lost.Solids() else None
            row["added_region_bbox_mm"]=bbox(added) if added.Solids() else None
            row["status"]="diagnosed"
        except Exception as e:
            row["status"]="failed"
            row["error"]=f"{type(e).__name__}: {e}"
        results.append(row)
    report={"generated_utc":datetime.now(timezone.utc).isoformat(),
      "source":"source/leica_m3_light_meter.stp (read-only)",
      "cover_solid_index":4,"moving_shutter_solid_index":3,
      "moving_shutter_translation_mm":[10,0,0],
      "purpose":"Diagnose rejected boolean relief candidates; not a design approval.",
      "results":results,
      "interpretation_limits":[
        "Component separation is a topological result, not proof that a split cover is mechanically unusable.",
        "A zero-distance component pair can indicate touching faces/edges; it is not a robust structural bridge.",
        "Volume conservation and symmetric-difference checks are required to detect malformed boolean output.",
        "The cutter is a translated static shutter solid, not a validated dynamic swept envelope.",
        "No cover/body fit, wall thickness, fasteners, assembly sequence, printability, or dynamic mechanism is approved.",
        "No source geometry is modified and no STEP candidate is exported."
      ]}
    lines=["# 盖体局部避让布尔与拓扑诊断","",
      f"- 生成时间 UTC：{report['generated_utc']}",
      "- 原始 STEP 只读；仅对盖体副本执行布尔诊断。",
      "- 目标：检查 0 / 0.2 mm 两个失败候选的体积守恒、实体碎片和空间位置。",
      "- 快门输入件仅作 +X 10 mm 静态包络，不代表动态扫掠体。","",
      "|余量 mm|状态|原盖体体积|交叠体积|切后体积|碎片体积和|体积守恒误差|碎片数|新增几何体积|",
      "|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in results:
      lines.append("|{clearance_mm}|{status}|{original_cover_volume_mm3}|{cover_cutter_intersection_volume_mm3}|{cut_reported_volume_mm3}|{component_volume_sum_mm3}|{volume_conservation_error_mm3}|{n}|{added_geometry_volume_mm3}|".format(
        **r,n=len(r.get("components",[]))))
      if r.get("error"): lines.append(f"\n- {r['clearance_mm']} mm error: {r['error']}")
      for c in r.get("components",[]):
        lines.append(f"  - 碎片 {c['index']}: 体积 {c['volume_mm3']} mm³，质心 {c['center_of_mass_mm']} mm，包围盒 {c['bbox_mm']}，面数 {c['face_count']}，有效={c['valid']}")
      for p in r.get("pairwise_component_clearances_mm",[]):
        lines.append(f"  - 碎片 {p['a']}–{p['b']} 最小距离：{p['distance_mm']} mm")
    lines += ["","## 机器可读结果","","~~~json",json.dumps(report,ensure_ascii=False,indent=2),"~~~",
      "","## 解释边界","",*[f"- {x}" for x in report["interpretation_limits"]],""]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text("\n".join(lines),encoding="utf-8")
    print(OUT)
    print(json.dumps(results,ensure_ascii=False))
    return 0
if __name__=="__main__": raise SystemExit(main())
