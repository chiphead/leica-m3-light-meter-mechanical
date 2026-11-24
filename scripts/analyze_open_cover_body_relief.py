#!/usr/bin/env python3
"""Validate exact main-body relief for the four open-ring cover candidates."""
from __future__ import annotations
import json
import math
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
STEP = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/OPEN_COVER_BODY_RELIEF_REPORT.md"


def main():
    solids = cq.importers.importStep(str(STEP)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    shutter_dial = solids[3].translate(cq.Vector(10.0, 0.0, 0.0))
    main_body = solids[5]
    fixed_parts = {"encoder_button": solids[1], "encoder_dial": solids[2], "encoder_bracket": solids[6]}
    pin_envelope = cq.Solid.makeCylinder(0.9, 3.8, cq.Vector(28.0, 0.0, 17.1), cq.Vector(0, 0, 1))

    cx, cy = 34.5, 0.0
    bridge_span_y, bridge_z_min, bridge_thickness = 6.0, 18.0, 0.6
    shaft_diameter, shaft_z_min, shaft_z_max = 1.8, 18.0, 21.2
    gear_diameter, gear_z_min, gear_width = 11.0, 21.0, 2.0
    bridge = cq.Solid.makeBox(1.0, bridge_span_y, bridge_thickness,
                              cq.Vector(cx - 0.5, -bridge_span_y / 2, bridge_z_min))
    shaft = cq.Solid.makeCylinder(shaft_diameter / 2, shaft_z_max - shaft_z_min,
                                  cq.Vector(cx, cy, shaft_z_min), cq.Vector(0, 0, 1))
    gear = cq.Solid.makeCylinder(gear_diameter / 2, gear_width,
                                 cq.Vector(cx, cy, gear_z_min), cq.Vector(0, 0, 1))
    moving = shutter_dial.fuse(bridge).fuse(shaft).fuse(gear)
    if not moving.isValid() or len(moving.Solids()) != 1:
        raise RuntimeError("Moving dial/bridge/shaft/gear assembly is not one valid solid")

    radial = []
    for vertex in moving.Vertices():
        p = vertex.Center()
        radial.append(math.hypot(p.x - cx, p.y - cy))
    for edge in moving.Edges():
        try:
            if edge.geomType() == "CIRCLE":
                p = edge.Center()
                radial.append(math.hypot(p.x - cx, p.y - cy) + float(edge.radius()))
        except Exception:
            pass
    moving_radius = max(radial)
    old_cover_bbox = solids[4].BoundingBox()
    z_min, height = float(old_cover_bbox.zmin), float(old_cover_bbox.zlen)
    inner_radius, outer_radius = moving_radius + 0.5, moving_radius + 2.0

    rows = []
    for margin in (2.5, 5.0):
        gaps = ((150.0 - margin, 160.0 + margin), (200.0 - margin, 210.0 + margin))
        for bridge_offset in (1.0, 2.0):
            row = {"gap_margin_deg": margin, "gap_ranges_deg": [list(x) for x in gaps],
                   "bridge_outer_offset_mm": bridge_offset, "raw_valid": False,
                   "raw_solid_count": None, "raw_body_intersection_mm3": None,
                   "relieved_valid": False, "relieved_solid_count": None,
                   "relieved_volume_mm3": None, "removed_body_volume_mm3": None,
                   "relieved_body_intersection_mm3": None, "moving_assembly_intersection_mm3": None,
                   "fixed_geometry_checks": [], "pin_envelope_intersection_mm3": None, "error": None}
            try:
                outer = cq.Solid.makeCylinder(outer_radius, height, cq.Vector(cx, cy, z_min), cq.Vector(0, 0, 1))
                inner = cq.Solid.makeCylinder(inner_radius, height, cq.Vector(cx, cy, z_min), cq.Vector(0, 0, 1))
                frame = outer.cut(inner)
                bridge_pieces = []
                for start, end in gaps:
                    gap_outer = cq.Solid.makeCylinder(outer_radius + 0.01, height + 0.02,
                        cq.Vector(cx, cy, z_min - 0.01), cq.Vector(0, 0, 1), end - start).rotate(
                        (cx, cy, 0), (cx, cy, 1), start)
                    gap_inner = cq.Solid.makeCylinder(inner_radius - 0.01, height + 0.02,
                        cq.Vector(cx, cy, z_min - 0.01), cq.Vector(0, 0, 1), end - start).rotate(
                        (cx, cy, 0), (cx, cy, 1), start)
                    frame = frame.cut(gap_outer.cut(gap_inner))
                    pts = []
                    for radius, angle in ((outer_radius - 0.5, start), (outer_radius + bridge_offset, start),
                                          (outer_radius + bridge_offset, end), (outer_radius - 0.5, end)):
                        a = math.radians(angle)
                        pts.append(cq.Vector(cx + radius * math.cos(a), cy + radius * math.sin(a), z_min))
                    wire = cq.Wire.makePolygon(pts + [pts[0]])
                    face = cq.Face.makeFromWires(wire)
                    bridge_pieces.append(cq.Solid.extrudeLinear(face.outerWire(), [], cq.Vector(0, 0, height)))
                for piece in bridge_pieces:
                    frame = frame.fuse(piece)
                frame = frame.clean()
                raw_body_overlap = float(frame.intersect(main_body).Volume())
                relieved = frame.cut(main_body).clean()
                row.update({
                    "raw_valid": bool(frame.isValid()), "raw_solid_count": len(frame.Solids()),
                    "raw_volume_mm3": round(float(frame.Volume()), 9),
                    "raw_body_intersection_mm3": round(raw_body_overlap, 9),
                    "relieved_valid": bool(relieved.isValid()), "relieved_solid_count": len(relieved.Solids()),
                    "relieved_volume_mm3": round(float(relieved.Volume()), 9),
                    "removed_body_volume_mm3": round(float(frame.Volume()) - float(relieved.Volume()), 9),
                    "relieved_body_intersection_mm3": round(float(relieved.intersect(main_body).Volume()), 9),
                    "moving_assembly_intersection_mm3": round(float(relieved.intersect(moving).Volume()), 9),
                    "pin_envelope_intersection_mm3": round(float(relieved.intersect(pin_envelope).Volume()), 9),
                })
                for name, obstacle in fixed_parts.items():
                    row["fixed_geometry_checks"].append({
                        "obstacle": name, "intersection_volume_mm3": round(float(relieved.intersect(obstacle).Volume()), 9)})
            except Exception as exc:
                row["error"] = str(exc)
            rows.append(row)

    lines = ["# 双开口上盖精确机身避让分析", "",
             f"- 生成时间（UTC）：{datetime.now(timezone.utc).isoformat()}",
             "- 输入：source/leica_m3_light_meter.stp（只读）",
             "- 内核：CadQuery/OpenCascade",
             f"- 运动扫掠半径：{moving_radius:.6f} mm",
             f"- 环框内/外半径：{inner_radius:.6f}/{outer_radius:.6f} mm",
             f"- Z范围：{z_min:.6f}…{z_min + height:.6f} mm",
             "- 方法：对双开口环框候选执行 Boolean fuse，再仅从盖体候选中扣除机身主体 B-rep",
             "- 主体和原始 STEP 均不修改；扣除后接口为零制造间隙，不等于生产公差。", "",
             "|开口余量|桥外扩|原始有效/实体数|原始机身交叠 mm³|避让后有效/实体数|避让后机身交叠 mm³|运动总成交叠 mm³|",
             "|---:|---:|---:|---:|---:|---:|---:|"]
    for x in rows:
        lines.append(f"|{x['gap_margin_deg']}°|{x['bridge_outer_offset_mm']} mm|{x['raw_valid']}/{x['raw_solid_count']}|"
                     f"{x['raw_body_intersection_mm3']}|{x['relieved_valid']}/{x['relieved_solid_count']}|"
                     f"{x['relieved_body_intersection_mm3']}|{x['moving_assembly_intersection_mm3']}|")
    lines += ["", "## 完整结果", "", json.dumps(rows, ensure_ascii=False, indent=2), "",
              "## 限制", "",
              "- 单一有效 B-rep 仅代表拓扑/几何内核有效，不代表结构强度、刚度或疲劳寿命。",
              "- 未设计安装耳、螺钉、定位面、密封、工具可达性及装配顺序。",
              "- 未加入制造间隙；扣除机身得到的是零间隙贴合界面。",
              "- 环框高度沿用旧盖包围盒，仅为探索参数，不是最终高度。",
              "- 未评估打印方向、材料各向异性、支撑和后处理。", ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    for row in rows:
        print(json.dumps(row, ensure_ascii=False))
    passed = all(x["error"] is None and x["relieved_valid"] and x["relieved_solid_count"] == 1
                 and x["relieved_body_intersection_mm3"] <= 1e-6
                 and x["moving_assembly_intersection_mm3"] <= 1e-6
                 and x["pin_envelope_intersection_mm3"] <= 1e-6
                 and all(y["intersection_volume_mm3"] <= 1e-6 for y in x["fixed_geometry_checks"])
                 for x in rows)
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
