#!/usr/bin/env python3
"""Search in-envelope side-lane bridges for the original cover after shutter relief.

The source STEP and all frozen solids remain read-only. The only modified shape is
a derived copy of cover solid #85. Candidate bridges are constrained to the
original cover bounding box and are rejected on any body, shutter, or encoder
intersection. This is a geometric topology screen, not a strength approval.
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/COVER_SIDE_LANE_BRIDGE_SEARCH.md"
EPS = 1e-6


def box(shape):
    b = shape.BoundingBox()
    return [round(float(v), 4) for v in
            (b.xmin, b.ymin, b.zmin, b.xmax, b.ymax, b.zmax)]


def overlap(a, b):
    return float(a.intersect(b).Volume())


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    cover, body = solids[4], solids[5]
    shutter = solids[3].translate(cq.Vector(10, 0, 0))
    fixed = {"encoder_button": solids[1], "encoder_dial": solids[2],
             "encoder_bracket": solids[6]}
    cover_box = cover.BoundingBox()
    # Static local relief is used only as a starting point; candidates must
    # reconnect the resulting pieces without entering the shutter solid.
    relieved = cover.cut(shutter).clean()
    if not relieved.isValid():
        raise RuntimeError("Base relief B-rep is invalid")
    components = relieved.Solids()
    if len(components) < 2:
        raise RuntimeError(f"Expected disconnected relief result, got {len(components)} solids")

    rows = []
    # Side lanes are outside the measured shutter width (|Y| <= 8.5 mm).
    # Sweep bridge thickness/height while staying within the original cover envelope.
    for side in (-1, 1):
        for y_inner in (8.55, 8.8, 9.2):
            for y_outer in (13.5, 14.0, 14.5):
                if y_outer <= y_inner:
                    continue
                for z0 in (14.9, 16.0, 17.0, 17.8, 18.3):
                    for z1 in (18.3, 19.0, 20.0, 20.9):
                        if z1 <= z0:
                            continue
                        for x0, x1 in ((27.0, 37.0), (29.0, 37.0), (27.0, 39.0)):
                            bridge = cq.Solid.makeBox(
                                x1-x0, y_outer-y_inner, z1-z0,
                                cq.Vector(x0, y_inner if side > 0 else -y_outer, z0)
                            )
                            candidate = relieved.fuse(bridge).clean()
                            row = {
                                "side": "positive_y" if side > 0 else "negative_y",
                                "x_range_mm": [x0, x1],
                                "abs_y_range_mm": [y_inner, y_outer],
                                "z_range_mm": [z0, z1],
                                "valid": bool(candidate.isValid()),
                                "solid_count": len(candidate.Solids()),
                                "volume_mm3": round(float(candidate.Volume()), 6),
                                "body_overlap_mm3": round(overlap(candidate, body), 6),
                                "shutter_overlap_mm3": round(overlap(candidate, shutter), 6),
                                "fixed_overlap_mm3": {
                                    name: round(overlap(candidate, obstacle), 6)
                                    for name, obstacle in fixed.items()
                                },
                                "bbox_mm": box(candidate),
                            }
                            cb = candidate.BoundingBox()
                            row["inside_original_cover_bbox"] = (
                                cb.xmin >= cover_box.xmin-EPS and cb.xmax <= cover_box.xmax+EPS
                                and cb.ymin >= cover_box.ymin-EPS and cb.ymax <= cover_box.ymax+EPS
                                and cb.zmin >= cover_box.zmin-EPS and cb.zmax <= cover_box.zmax+EPS
                            )
                            row["passes_geometric_screen"] = (
                                row["valid"] and row["solid_count"] == 1
                                and row["body_overlap_mm3"] <= EPS
                                and row["shutter_overlap_mm3"] <= EPS
                                and all(v <= EPS for v in row["fixed_overlap_mm3"].values())
                                and row["inside_original_cover_bbox"]
                            )
                            rows.append(row)

    passed = [r for r in rows if r["passes_geometric_screen"]]
    passed.sort(key=lambda r: (
        r["volume_mm3"], r["z_range_mm"][1]-r["z_range_mm"][0],
        r["abs_y_range_mm"][1]-r["abs_y_range_mm"][0]
    ))
    out_dir = ROOT / "working/cover_side_lane_candidates"
    if passed:
        # Export only the best 12 candidates by added volume.
        for i, row in enumerate(passed[:12], 1):
            side = 1 if row["side"] == "positive_y" else -1
            x0,x1 = row["x_range_mm"]
            yi,yo = row["abs_y_range_mm"]
            z0,z1 = row["z_range_mm"]
            bridge = cq.Solid.makeBox(x1-x0, yo-yi, z1-z0,
                cq.Vector(x0, yi if side > 0 else -yo, z0))
            candidate = relieved.fuse(bridge).clean()
            path = out_dir / f"side_lane_candidate_{i:02d}.step"
            path.parent.mkdir(parents=True, exist_ok=True)
            cq.exporters.export(candidate, str(path), exportType="STEP")
            row["step_file"] = str(path.relative_to(ROOT))

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": "source/leica_m3_light_meter.stp (read-only)",
        "cover_bbox_mm": box(cover),
        "body_bbox_mm": box(body),
        "base_relief_solid_count": len(components),
        "base_relief_volume_mm3": round(float(relieved.Volume()), 6),
        "candidate_count": len(rows),
        "passing_candidate_count": len(passed),
        "best_candidates": passed[:12],
        "all_candidates": rows,
        "limitations": [
            "The translated shutter solid is a static placement probe, not a validated dynamic swept envelope.",
            "A bridge passing B-rep checks is not proof of adequate wall thickness, strength, fatigue life, or printability.",
            "The bridge boxes are deliberately simple search primitives, not finished filleted ribs.",
            "No fastener, insert, gasket, assembly path, or manufacturing tolerance is validated.",
            "The original cover/body mating faces are not intentionally cut; body collision is a hard rejection.",
        ],
    }
    lines = [
        "# 原始上盖侧向绕行连接筋搜索", "",
        f"- 生成时间 UTC：{report['generated_utc']}",
        "- 原始 STEP 只读；只在 #85 派生副本上测试。",
        f"- 原盖体包围盒：{report['cover_bbox_mm']}",
        f"- 避让后基础实体数：{len(components)}",
        f"- 搜索候选：{len(rows)}；通过全部几何初筛：{len(passed)}", "",
        "|排名|侧向|X范围|绝对Y范围|Z范围|实体数|机身交叠|快门交叠|包围盒内|STEP|",
        "|---:|---|---|---|---|---:|---:|---:|---|---|",
    ]
    for i, r in enumerate(passed[:12], 1):
        lines.append(
            f"|{i}|{r['side']}|{r['x_range_mm']}|{r['abs_y_range_mm']}|{r['z_range_mm']}|"
            f"{r['solid_count']}|{r['body_overlap_mm3']}|{r['shutter_overlap_mm3']}|"
            f"{r['inside_original_cover_bbox']}|{r.get('step_file','未导出')}|"
        )
    if not passed:
        lines.append("|—|无|—|—|—|—|—|—|—|未导出|")
    lines += ["", "## 解释边界", ""] + [f"- {x}" for x in report["limitations"]]
    lines += ["", "## 机器可读结果", "", "```json",
              json.dumps(report, ensure_ascii=False, indent=2), "```", ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"candidate_count": len(rows), "passing_candidate_count": len(passed),
                      "best_candidates": passed[:12]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
