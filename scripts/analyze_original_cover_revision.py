#!/usr/bin/env python3
"""Audit the original enclosure cover against the revised shutter/gear layout.

This is a read-only geometric audit. It never edits or exports modified source solids.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/ORIGINAL_COVER_REVISION_AUDIT.md"

def volume(shape):
    return round(float(shape.Volume()), 9)

def distance(a, b):
    try:
        return round(float(a.distance(b)), 6)
    except Exception as exc:
        return f"unavailable: {exc}"

def check(a, b, label):
    return {"pair": label, "intersection_volume_mm3": volume(a.intersect(b)),
            "minimum_distance_mm": distance(a, b)}

def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    shutter_original, original_cover, main_body = solids[3], solids[4], solids[5]
    encoder_button, encoder_dial, encoder_bracket = solids[1], solids[2], solids[6]
    shutter_input = shutter_original.translate(cq.Vector(10.0, 0.0, 0.0))
    output_center, input_center = (24.5, 0.0), (34.5, 0.0)
    gear_z0, gear_width, gear_diameter = 21.0, 2.0, 11.0
    output_gear = cq.Solid.makeCylinder(gear_diameter/2, gear_width,
        cq.Vector(*output_center, gear_z0), cq.Vector(0,0,1))
    input_gear = cq.Solid.makeCylinder(gear_diameter/2, gear_width,
        cq.Vector(*input_center, gear_z0), cq.Vector(0,0,1))
    probe_diameter = 2.0
    output_probe = cq.Solid.makeCylinder(probe_diameter/2, 2.0,
        cq.Vector(*output_center, 20.9), cq.Vector(0,0,1))
    input_probe = cq.Solid.makeCylinder(probe_diameter/2, 2.0,
        cq.Vector(*input_center, 20.9), cq.Vector(0,0,1))

    pairs = [
        check(original_cover, shutter_input, "original cover vs +10 mm translated shutter input module"),
        check(original_cover, output_gear, "original cover vs output gear blank Ø11 x 2 at Z=21..23"),
        check(original_cover, input_gear, "original cover vs input gear blank Ø11 x 2 at Z=21..23"),
        check(original_cover, output_probe, "original cover vs output axial probe Ø2 from Z=20.9"),
        check(original_cover, input_probe, "original cover vs input axial probe Ø2 from Z=20.9"),
        check(original_cover, encoder_button, "original cover vs fixed encoder button"),
        check(original_cover, encoder_dial, "original cover vs fixed encoder dial"),
        check(original_cover, encoder_bracket, "original cover vs fixed encoder bracket"),
        check(original_cover, main_body, "original cover vs original main body (baseline fit; not automatically a collision)"),
    ]
    obstacles = [
        ("translated_shutter_input", shutter_input), ("output_gear_blank", output_gear),
        ("input_gear_blank", input_gear), ("output_axial_probe", output_probe),
        ("input_axial_probe", input_probe)]
    face_rows = []
    for name, obstacle in obstacles:
        for index, face in enumerate(original_cover.Faces()):
            try:
                area = float(face.intersect(obstacle).Area())
                if area > 1e-7:
                    bb = face.BoundingBox()
                    face_rows.append({"obstacle": name, "cover_face_index": index,
                        "surface_type": face.geomType(), "overlap_area_mm2": round(area,8),
                        "cover_face_bbox": [round(float(v),4) for v in
                            (bb.xmin,bb.ymin,bb.zmin,bb.xmax,bb.ymax,bb.zmax)]})
            except Exception:
                continue
    bb = original_cover.BoundingBox()
    report = {
        "source": "source/leica_m3_light_meter.stp (read-only)",
        "kernel": "CadQuery/OpenCascade", "source_solid_count": len(solids),
        "cover_solid_index": 4, "body_solid_index": 5,
        "cover_bbox_mm": {"min":[round(float(v),4) for v in (bb.xmin,bb.ymin,bb.zmin)],
                          "max":[round(float(v),4) for v in (bb.xmax,bb.ymax,bb.zmax)]},
        "shutter_input_translation_mm":[10.0,0.0,0.0],
        "gear_layout":{"output_center_xy_mm":list(output_center),"input_center_xy_mm":list(input_center),
            "center_distance_mm":10.0,"gear_blank_diameter_mm":gear_diameter,
            "gear_blank_width_mm":gear_width,"gear_blank_z_mm":[gear_z0,gear_z0+gear_width],
            "note":"Cylindrical blanks are clearance probes only, not real meshing gears."},
        "checks":pairs,"cover_face_overlap_diagnostics":face_rows,
        "limitations":[
            "The original cover and body are not modified.",
            "A cylindrical gear blank is only a spatial envelope; it does not validate involute tooth geometry or meshing.",
            "The Ø2 axial probes are diagnostic envelopes, not selected shaft diameters or approved shaft paths.",
            "Zero overlap is not a manufacturing clearance or assembly-path proof.",
            "Face intersection area is a boundary diagnostic and is not material removal area.",
            "No mounting ears, fasteners, split line, CNC tool access, wall thickness, stiffness, or assembly sequence are designed here."]}
    lines = [
        "# 原始外壳盖子改造专项审计","",
        f"- 生成时间（UTC）：{datetime.now(timezone.utc).isoformat()}",
        "- 原始 STEP：只读；未修改、未导出任何改版实体。",
        "- 目标：以原始盖子 #85 为设计基体，检查右移后的快门输入模块及高位齿轮包络。",
        "- 约束：主体 #86、编码器机构、AS5600/磁铁基准、TSL2591 光路及所有已验证电子件保持冻结。",
        "- 齿轮轴心：输出 (24.5, 0)，输入 (34.5, 0)，中心距 10 mm。",
        "- 齿轮毛坯探针：Ø11 x 2 mm，Z=21…23 mm；仅用于空间检查，不代表真实齿形。","",
        "## 原始盖子包围盒（mm）","",
        f"- Min：{report['cover_bbox_mm']['min']}",f"- Max：{report['cover_bbox_mm']['max']}","",
        "## 盖子与改造机构的实体检查","","|检查对象|交叠体积 (mm³)|最小距离 (mm)|说明|",
        "|---|---:|---:|---|"]
    for item in pairs:
        note = "原始盖体/主体配合基线，不能简单当作碰撞" if "baseline fit" in item["pair"] else "实体空间探针"
        lines.append(f"|{item['pair']}|{item['intersection_volume_mm3']}|{item['minimum_distance_mm']}|{note}|")
    lines += ["","## 盖子面级交叠定位",""]
    if face_rows:
        lines += ["|障碍物|盖子面枚举|曲面类型|边界交叠面积 (mm²)|盖子面包围盒 min/max (mm)|","|---|---:|---|---:|---|"]
        for x in face_rows:
            lines.append(f"|{x['obstacle']}|{x['cover_face_index']}|{x['surface_type']}|{x['overlap_area_mm2']}|{x['cover_face_bbox']}|")
    else:
        lines.append("当前探针未检测到可报告的盖子边界面交叠；需结合实体交叠体积和最小距离共同判断。")
    lines += ["","## 机器可读结果","","~~~json",json.dumps(report,ensure_ascii=False,indent=2),"~~~",
        "","## 解释边界",""]
    lines.extend(f"- {item}" for item in report["limitations"])
    lines += ["","## 下一阶段设计决策","",
        "1. 先依据本报告确认原盖子与右移快门盘、齿轮层及轴向连接探针的真实冲突位置。",
        "2. 只在原盖子上提出局部开口/沉台/局部增厚或盖体分型方案；不得创建没有明确安装与保护功能的独立环框。",
        "3. 新盖子必须明确与主体的定位面、紧固方式、拆装方向和加工可达性。",
        "4. 真实渐开线齿轮、轴段、齿轮匣和盖子改版必须联合检查后才导出候选 STEP。",""]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text("\n".join(lines),encoding="utf-8")
    print(f"Wrote {OUT}")
    print(json.dumps({"checks":pairs,"face_rows":len(face_rows)},ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
