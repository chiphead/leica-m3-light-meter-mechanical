#!/usr/bin/env python3
"""Vertical placement sensitivity scan; original STEP remains read-only."""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"source/leica_m3_light_meter.stp"
OUT=ROOT/"working/SHUTTER_VERTICAL_CLEARANCE_SCAN.md"
def bb(s):
 b=s.BoundingBox()
 return [round(float(v),4) for v in (b.xmin,b.ymin,b.zmin,b.xmax,b.ymax,b.zmax)]
def main():
 solids=cq.importers.importStep(str(SOURCE)).val().Solids()
 if len(solids)!=7: raise RuntimeError(f"Expected 7 solids, got {len(solids)}")
 cover=solids[4]; shutter=solids[3].translate(cq.Vector(10,0,0)); rows=[]
 for i in range(-24,25):
  dz=round(i*.25,3); moved=shutter.translate(cq.Vector(0,0,dz))
  inter=cover.intersect(moved); vol=float(inter.Volume())
  dist=float(cover.distance(moved)) if vol<=1e-7 else 0.0
  rows.append({"dz_mm":dz,"intersection_mm3":round(vol,6),"minimum_distance_mm":round(dist,5)})
 neg=next((r for r in rows if r["dz_mm"]<0 and r["intersection_mm3"]<=1e-7),None)
 pos=next((r for r in rows if r["dz_mm"]>0 and r["intersection_mm3"]<=1e-7),None)
 lines=["# 快门输入件垂直位置敏感性扫描","",f"- 生成时间 UTC：{datetime.now(timezone.utc).isoformat()}","- 原始 STEP 只读；快门输入件副本先沿 X 平移 +10 mm，再做 Z 方向虚拟扫描。","- Z 扫描范围 −6～+6 mm，步长 0.25 mm。",f"- 盖体包围盒：{bb(cover)}",f"- 当前快门件包围盒：{bb(shutter)}",f"- 向下首个无交叠采样：{neg}",f"- 向上首个无交叠采样：{pos}","","|Z偏移(mm)|交叠体积(mm³)|最小距离(mm)|","|---:|---:|---:|"]
 for r in rows: lines.append(f"|{r['dz_mm']:.2f}|{r['intersection_mm3']:.6f}|{r['minimum_distance_mm']:.5f}|")
 lines += ["","## 限制","- 这是整件刚体位置敏感性扫描，不是装配建议。","- 无交叠不代表具有可制造间隙。","- 不验证真实齿轮啮合、轴、连杆、轴承支撑、相机耦合或装配路径。","- 原始 STEP 与冻结零件未修改。"]
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text("\n".join(lines)+"\n",encoding="utf-8")
 print(json.dumps({"negative_clear":neg,"positive_clear":pos,"near_zero":[r for r in rows if abs(r["dz_mm"])<=2]}))
if __name__=="__main__": main()
