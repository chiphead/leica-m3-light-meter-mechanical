#!/usr/bin/env python3
"""Locate body regions blocking the cover during +Z removal; source STEP stays read-only."""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"source/leica_m3_light_meter.stp"
OUT=ROOT/"working/COVER_VERTICAL_REMOVAL_OBSTACLE_AUDIT.md"
LIFTS=[0.45,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.25]
def bb(s):
 b=s.BoundingBox()
 return [round(float(x),4) for x in (b.xmin,b.ymin,b.zmin,b.xmax,b.ymax,b.zmax)]
def main():
 solids=cq.importers.importStep(str(SRC)).val().Solids()
 if len(solids)!=7: raise RuntimeError(f"Expected 7 solids, got {len(solids)}")
 cover,body=solids[4],solids[5]; rows=[]
 for dz in LIFTS:
  moved=cover.translate(cq.Vector(0,0,dz)); common=moved.intersect(body)
  comps=[{"volume_mm3":round(float(s.Volume()),7),"bbox_mm":bb(s)} for s in common.Solids()]
  hits=[]
  for fi,f in enumerate(body.Faces()):
   try:
    hit=moved.intersect(f); area=float(hit.Area()); vol=float(hit.Volume())
   except Exception: continue
   if area>1e-5 or vol>1e-6:
    hits.append({"body_face":fi,"surface":f.geomType(),"intersection_area_mm2":round(area,6),
     "intersection_volume_mm3":round(vol,7),"face_bbox_mm":bb(f)})
  rows.append({"lift_mm":dz,"volume_mm3":round(float(common.Volume()),7),
   "intersection_bbox_mm":bb(common) if common.Solids() else None,"components":comps,"body_face_hits":hits})
 report={"generated_utc":datetime.now(timezone.utc).isoformat(),"cover_solid_index":4,"body_solid_index":5,
  "source":"original STEP, read-only","samples":rows,
  "limitations":["Static overlap regions only; not a continuous extraction trajectory.",
   "Intersecting face IDs do not establish functional design intent.","No source geometry modified; no STEP exported."]}
 lines=["# 盖体垂直拔出障碍区域审计","",f"- 生成时间 UTC：{report['generated_utc']}",
 "- 原始 STEP 只读；盖体 #85、主体 #86。","- 对拔出路径中多个交叠高度提取包围盒、连通体和主体面索引。"]
 for r in rows:
  lines += ["",f"## 上移 {r['lift_mm']} mm",f"- 交叠体积：{r['volume_mm3']} mm³",
   f"- 交叠包围盒：{r['intersection_bbox_mm']}","- 连通体："+json.dumps(r["components"],ensure_ascii=False),
   "- 主体命中面："+", ".join(f"Face {x['body_face']} ({x['surface']}, area={x['intersection_area_mm2']} mm²)" for x in r["body_face_hits"])]
 lines += ["","## 机器可读数据","~~~json",json.dumps(report,ensure_ascii=False,indent=2),"~~~","",
 "## 限制",*[f"- {x}" for x in report["limitations"]]]
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text("\n".join(lines),encoding="utf-8")
 print(json.dumps(rows,ensure_ascii=False))
if __name__=="__main__": main()
