#!/usr/bin/env python3
"""Section the cover/shutter interference to distinguish a local notch from a broad structural conflict."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/COVER_SHUTTER_INTERFERENCE_SECTIONS.md"

def bbox(shape):
    b = shape.BoundingBox()
    return [round(float(v), 4) for v in (b.xmin,b.ymin,b.zmin,b.xmax,b.ymax,b.zmax)]

def slab_xz(y, half, bounds):
    xmin,ymin,zmin,xmax,ymax,zmax = bounds
    return cq.Solid.makeBox(xmax-xmin, 2*half, zmax-zmin,
                            cq.Vector(xmin,y-half,zmin))

def slab_xy(z, half, bounds):
    xmin,ymin,zmin,xmax,ymax,zmax = bounds
    return cq.Solid.makeBox(xmax-xmin, ymax-ymin, 2*half,
                            cq.Vector(xmin,ymin,z-half))

def section_rows(overlap, bounds, axis, values, half=0.05):
    rows=[]
    for value in values:
        slab = slab_xz(value,half,bounds) if axis=="y" else slab_xy(value,half,bounds)
        part=overlap.intersect(slab)
        rows.append({"at_mm":round(value,3),
                     "area_estimate_mm2":round(float(part.Volume())/(2*half),5),
                     "component_count":len(part.Solids()),
                     "section_bbox_mm":bbox(part) if part.Volume()>1e-8 else None})
    return rows

def main():
    solids=cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids)!=7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    cover=solids[4]
    shutter=solids[3].translate(cq.Vector(10,0,0))
    overlap=cover.intersect(shutter)
    if overlap.Volume()<=1e-8:
        raise RuntimeError("Expected the previously reported cover/shutter overlap")
    bb=bbox(overlap)
    xmin,ymin,zmin,xmax,ymax,zmax=bb
    cover_volume=float(cover.Volume())
    overlap_volume=float(overlap.Volume())
    # Sections pass through the actual intersection B-rep, not the whole dial.
    y_values=[round(y,2) for y in [ymin+0.25+i*0.5 for i in range(max(0,int((ymax-ymin-0.5)/0.5)+1))]]
    z_values=[round(z,2) for z in [zmin+0.1+i*0.2 for i in range(max(0,int((zmax-zmin-0.2)/0.2)+1))]]
    face_rows=[]
    for i,face in enumerate(overlap.Faces()):
        b=face.BoundingBox()
        face_rows.append({"face":i,"type":face.geomType(),"area_mm2":round(float(face.Area()),5),
                          "bbox_mm":bbox(face)})
    face_rows.sort(key=lambda x:x["area_mm2"],reverse=True)
    report={
      "generated_utc":datetime.now(timezone.utc).isoformat(),
      "source":"source/leica_m3_light_meter.stp (read-only)",
      "translation_mm":[10,0,0],
      "cover_bbox_mm":bbox(cover),
      "translated_shutter_bbox_mm":bbox(shutter),
      "intersection_volume_mm3":round(overlap_volume,6),
      "intersection_fraction_of_cover_volume":round(overlap_volume/cover_volume,6),
      "intersection_solid_count":len(overlap.Solids()),
      "intersection_bbox_mm":bb,
      "intersection_faces_largest_first":face_rows[:20],
      "y_sections_xz":section_rows(overlap,bb,"y",y_values),
      "z_sections_xy":section_rows(overlap,bb,"z",z_values),
      "interpretation_limits":[
        "Sections are numerical area estimates from 0.1 mm thick B-rep slabs.",
        "A section area profile localizes overlap but does not define a manufacturable cut.",
        "The translated shutter solid is a whole-part placement probe; it does not prove the final linkage geometry or assembly path.",
        "The source STEP and frozen components are not modified."
      ]
    }
    lines=["# 盖子与右移快门输入件干涉截面诊断","",
      f"- 生成时间（UTC）：{report['generated_utc']}",
      "- 原始 STEP 只读；本报告不创建或修改实体。",
      f"- 实体交叠：{report['intersection_volume_mm3']} mm³；占盖子体积 {report['intersection_fraction_of_cover_volume']*100:.2f}%。",
      f"- 交叠包围盒：{bb}（Xmin,Ymin,Zmin,Xmax,Ymax,Zmax，mm）","",
      "## 沿 Y 的 X-Z 截面（每片厚 0.1 mm）","",
      "|Y (mm)|截面积估算 (mm²)|连通组件|截面包围盒|","|---:|---:|---:|---|"]
    for x in report["y_sections_xz"]:
      lines.append(f"|{x['at_mm']}|{x['area_estimate_mm2']}|{x['component_count']}|{x['section_bbox_mm']}|")
    lines += ["","## 沿 Z 的 X-Y 截面（每片厚 0.1 mm）","",
      "|Z (mm)|截面积估算 (mm²)|连通组件|截面包围盒|","|---:|---:|---:|---|"]
    for x in report["z_sections_xy"]:
      lines.append(f"|{x['at_mm']}|{x['area_estimate_mm2']}|{x['component_count']}|{x['section_bbox_mm']}|")
    lines += ["","## 交叠实体面片（按面积降序）","",
      "|面|类型|面积 (mm²)|包围盒|","|---:|---|---:|---|"]
    for x in report["intersection_faces_largest_first"]:
      lines.append(f"|{x['face']}|{x['type']}|{x['area_mm2']}|{x['bbox_mm']}|")
    lines += ["","## 原始数据","", "```json",json.dumps(report,ensure_ascii=False,indent=2),"```","",
      "## 限制",""]+[f"- {x}" for x in report["interpretation_limits"]]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"intersection_volume_mm3":report["intersection_volume_mm3"],
      "intersection_bbox_mm":bb,"y_sections_xz":report["y_sections_xz"],
      "z_sections_xy":report["z_sections_xy"]},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
