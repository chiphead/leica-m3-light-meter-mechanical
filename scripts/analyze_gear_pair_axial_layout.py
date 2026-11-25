#!/usr/bin/env python3
"""Build and audit a first involute 1:1 gear-pair candidate against the immutable STEP baseline."""
from __future__ import annotations
import math
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
STEP = ROOT / "source/leica_m3_light_meter.stp"
REPORT = ROOT / "working/GEAR_PAIR_AXIAL_LAYOUT_AUDIT.md"
CANDIDATE_STEP = ROOT / "working/GEAR_PAIR_M05_20T_LAYOUT_CANDIDATE.step"
MODULE, TEETH, PRESSURE_ANGLE_DEG, FACE_WIDTH = 0.5, 20, 20.0, 1.5
INPUT_CENTER, OUTPUT_CENTER = (34.5, 0.0), (24.5, 0.0)
Z_STARTS = [round(10.0 + i * 0.25, 4) for i in range(41)]
FROZEN_SOLIDS = {"encoder_body": 1, "encoder_dial": 2, "encoder_bracket": 6}
TOL = 1e-6

def involute(a):
    return math.tan(a) - a

def gear_outline(module, teeth, pressure_deg, phase, samples=12):
    """Sample true involute flanks; root fillets/backlash are omitted at layout stage."""
    alpha = math.radians(pressure_deg)
    rp, rb, ra, rf = module * teeth / 2.0, module * teeth / 2.0 * math.cos(alpha), module * teeth / 2.0 + module, module * teeth / 2.0 - 1.25 * module
    half_base = math.pi / (2.0 * teeth) + involute(alpha)
    half_root = half_base + math.radians(1.4)
    def half_width(radius):
        pressure = math.acos(max(-1.0, min(1.0, rb / radius)))
        return math.pi / (2.0 * teeth) + involute(alpha) - involute(pressure)
    points, pitch = [], 2.0 * math.pi / teeth
    for tooth in range(teeth):
        center = phase + tooth * pitch
        points.append((rf * math.cos(center-half_root), rf * math.sin(center-half_root)))
        radii = [rb + (ra-rb)*i/samples for i in range(samples+1)]
        for radius in radii:
            a = center - half_width(radius)
            points.append((radius*math.cos(a), radius*math.sin(a)))
        tip = half_width(ra)
        for i in range(1,5):
            a = center - tip + 2.0*tip*i/4.0
            points.append((ra*math.cos(a), ra*math.sin(a)))
        for radius in reversed(radii):
            a = center + half_width(radius)
            points.append((radius*math.cos(a), radius*math.sin(a)))
        points.append((rf*math.cos(center+half_root), rf*math.sin(center+half_root)))
        next_start = center + pitch - half_root
        for i in range(1,4):
            a = center + half_root + (next_start-(center+half_root))*i/4.0
            points.append((rf*math.cos(a), rf*math.sin(a)))
    return points

def make_gear(center, z0, phase):
    return cq.Workplane("XY").polyline(gear_outline(MODULE, TEETH, PRESSURE_ANGLE_DEG, phase)).close().extrude(FACE_WIDTH).val().translate((center[0], center[1], z0))

def overlap(a,b):
    try: return float(a.intersect(b).Volume()), float(a.distance(b)), None
    except Exception as exc: return None, None, str(exc)

def main():
    if not STEP.is_file(): raise FileNotFoundError(STEP)
    solids = cq.importers.importStep(str(STEP)).val().Solids()
    if len(solids) != 7: raise RuntimeError(f"Expected 7 source solids, found {len(solids)}")
    body, cover, shutter = solids[5], solids[4], solids[3]
    moved_shutter = shutter.translate((10.0,0.0,0.0))
    frozen = {name:solids[index] for name,index in FROZEN_SOLIDS.items()}
    rows, candidates = [], {}
    for z0 in Z_STARTS:
        gi = make_gear(INPUT_CENTER,z0,0.0)
        go = make_gear(OUTPUT_CENTER,z0,math.pi+math.pi/TEETH)
        pv,pd,pe = overlap(gi,go)
        row={"z0":z0,"z1":round(z0+FACE_WIDTH,4),"pair_intersection":pv,"pair_distance":pd,"pair_error":pe,
             "valid":bool(gi.isValid() and go.isValid()),"frozen":{},"body":{},"cover":{},"moved_disc":{}}
        frozen_clear=True
        for name,solid in frozen.items():
            for gname,gear in (("input",gi),("output",go)):
                v,d,e=overlap(gear,solid)
                row["frozen"][f"{gname}_{name}"]={"overlap":v,"distance":d,"error":e}
                if e or v is None or v>TOL: frozen_clear=False
        body_values,cover_values,disc_values=[],[],[]
        for gname,gear in (("input",gi),("output",go)):
            v,d,e=overlap(gear,body); row["body"][gname]={"overlap":v,"distance":d,"error":e}
            if v is not None: body_values.append(v)
            v,d,e=overlap(gear,cover); row["cover"][gname]={"overlap":v,"distance":d,"error":e}
            if v is not None: cover_values.append(v)
            v,d,e=overlap(gear,moved_shutter); row["moved_disc"][gname]={"overlap":v,"distance":d,"error":e}
            if v is not None: disc_values.append(v)
        row["frozen_clear"]=frozen_clear
        row["body_total"]=sum(body_values) if len(body_values)==2 else None
        row["cover_total"]=sum(cover_values) if len(cover_values)==2 else None
        row["disc_total"]=sum(disc_values) if len(disc_values)==2 else None
        row["pair_ok"]=pe is None and pv is not None and pv<=TOL
        rows.append(row); candidates[z0]=(gi,go)
    eligible=[r for r in rows if r["valid"] and r["pair_ok"] and r["frozen_clear"]]
    body_clear=[r for r in eligible if r["body_total"] is not None and r["body_total"]<=TOL]
    selected=min(body_clear,key=lambda r:r["z0"]) if body_clear else None
    if selected:
        cq.exporters.export(cq.Compound.makeCompound(list(candidates[selected["z0"]])),str(CANDIDATE_STEP),exportType="STEP")
    elif CANDIDATE_STEP.exists(): CANDIDATE_STEP.unlink()
    lines=[
      "# 渐开线齿轮副轴向布局审计","",f"- 生成时间 UTC：{datetime.now(timezone.utc).isoformat()}",
      "- 原始 STEP 只读；未修改 source/。",
      "- 本轮以渐开线齿形替代 Ø11 mm 圆柱毛坯探针，进行真实 B-rep 交叠与距离检查。","",
      "## 固定设计输入","",
      f"- 输入轴心：{INPUT_CENTER} mm；输出轴心：{OUTPUT_CENTER} mm；中心距：{math.dist(INPUT_CENTER,OUTPUT_CENTER):.4f} mm。",
      f"- 齿轮：m={MODULE}，z={TEETH}/{TEETH}，压力角={PRESSURE_ANGLE_DEG}°；分度圆直径 10.0 mm，齿顶圆直径 11.0 mm。",
      f"- 齿宽：{FACE_WIDTH:.2f} mm（首轮布局值，不是最终制造尺寸）。",
      "- 齿廓为采样渐开线；未加入齿根圆角、齿侧间隙、齿顶修缘和制造补偿。",
      "- 输入相位 0°，输出相位 189°（等效 9°），用于中心连线处齿-槽相位配对。",
      "- 编码器本体、编码器转盘、编码器支架为冻结实体；主体和盖体为可重构结构。","",
      "## 轴向扫描结果","",
      "| Z 下表面 | Z 上表面 | 齿轮副相交 mm³ | 冻结实体无干涉 | 主体相交合计 mm³ | 盖体相交合计 mm³ | 平移快门盘相交合计 mm³ |",
      "|---:|---:|---:|:---:|---:|---:|---:|"
    ]
    for r in rows:
        def f(v): return "ERR" if v is None else f"{v:.6f}"
        lines.append(f"| {r['z0']:.2f} | {r['z1']:.2f} | {f(r['pair_intersection'])} | {'是' if r['frozen_clear'] else '否'} | {f(r['body_total'])} | {f(r['cover_total'])} | {f(r['disc_total'])} |")
    lines += ["","## 当前选择",""]
    if selected:
        lines += [
          f"- 暂定布局平面：Z={selected['z0']:.2f}…{selected['z1']:.2f} mm。",
          "- 选择依据：齿轮实体有效、齿轮副无正体积相交、与已建模冻结编码器实体无正体积相交、与当前主体无正体积相交；在符合条件的位置中选择最低 Z。",
          f"- 主体最小距离：输入 {selected['body']['input']['distance']:.6f} mm；输出 {selected['body']['output']['distance']:.6f} mm。",
          f"- 与平移后原快门盘相交体积合计：{selected['disc_total']:.6f} mm³；这表示输入盘需要重构连接/局部让位，不代表已解决。",
          f"- 已导出候选齿轮副：{CANDIDATE_STEP.relative_to(ROOT)}（仅两只齿轮实体）。"
        ]
    else:
        lines += ["- 未找到同时满足齿轮副有效、冻结编码器无干涉且主体无正体积相交的 Z 平面。","- 不导出候选 STEP；需先研究主体局部结构和齿轮轴向层级。"]
    lines += [
      "","## 解释边界","",
      "- 本报告是齿形与轴向空间的第一轮 CAD 内核审计，不是完整传动匣或整机装配。",
      "- 主体/盖体均是 CNC 外壳重构对象；相交体积用于定位需要重构的区域，不授权直接切除。",
      "- 平移后的原快门盘仅用于量化空间关系；操作盘外形允许重新设计，但底面盲孔位置、孔径、孔深、开口方向和金属杆插入接口必须保留。",
      "- AS5600 PCB、磁铁、磁铁轴和真实保留空间未包含在 STEP 中；其位置、对准和气隙继续冻结。",
      "- 未验证齿根强度、齿侧间隙、材料、摩擦、回差、轴承/轴套、支架刚度、金属杆运动包络及相机全行程。",
      "- 若导出候选 STEP，它只含两只渐开线齿轮，不含轴、轮毂、支架、快门盘或外壳，不能直接加工。",""
    ]
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\n".join(lines),encoding="utf-8")

if __name__=="__main__": main()
