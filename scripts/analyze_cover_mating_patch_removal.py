#!/usr/bin/env python3
"""Measure actual cover/body coincident face patches and vertical pull-off clearance.

Read-only audit of source STEP solids #85 (solids[4]) and #86 (solids[5]).
No source geometry is modified and no STEP is exported.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/COVER_MATING_PATCH_AND_REMOVAL_AUDIT.md"
FACE_DISTANCE_TOL = 0.03
MIN_PATCH_AREA = 0.01


def vec(v):
    return [round(float(x), 5) for x in (v.x, v.y, v.z)]


def bbox(shape):
    b = shape.BoundingBox()
    return [round(float(v), 4) for v in
            (b.xmin, b.ymin, b.zmin, b.xmax, b.ymax, b.zmax)]


def face_patch_pairs(cover, body):
    cf, bf = cover.Faces(), body.Faces()
    pairs = []
    for ci, cface in enumerate(cf):
        for bi, bface in enumerate(bf):
            try:
                d = float(cface.distance(bface))
            except Exception:
                continue
            if d > FACE_DISTANCE_TOL:
                continue
            try:
                common = cface.intersect(bface)
                area = float(common.Area())
            except Exception:
                area = 0.0
            if area > MIN_PATCH_AREA:
                pairs.append({
                    "cover_face": ci, "body_face": bi,
                    "cover_surface": cface.geomType(),
                    "body_surface": bface.geomType(),
                    "cover_area_mm2": round(float(cface.Area()), 5),
                    "body_area_mm2": round(float(bface.Area()), 5),
                    "shared_area_mm2": round(area, 5),
                    "face_distance_mm": round(d, 6),
                    "cover_bbox_mm": bbox(cface),
                    "body_bbox_mm": bbox(bface),
                })
    pairs.sort(key=lambda x: x["shared_area_mm2"], reverse=True)
    return pairs


def pull_off_scan(cover, body):
    # Dense sampling near first release; coarser sampling farther away.
    offsets = [round(i * 0.05, 3) for i in range(1, 21)]
    offsets += [round(1.0 + i * 0.25, 3) for i in range(1, 21)]
    rows = []
    first_clear = None
    first_collision_free = None
    for dz in offsets:
        moved = cover.translate(cq.Vector(0, 0, dz))
        common = moved.intersect(body)
        volume = float(common.Volume())
        solids = len(common.Solids())
        rows.append({
            "z_lift_mm": dz,
            "intersection_volume_mm3": round(volume, 7),
            "intersection_solid_count": solids,
        })
        if volume <= 1e-6 and first_collision_free is None:
            first_collision_free = dz
        if volume > 1e-6 and first_clear is None:
            first_clear = dz
    return rows, first_collision_free, first_clear


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 solids, got {len(solids)}")
    cover, body = solids[4], solids[5]
    baseline = float(cover.intersect(body).Volume())
    pairs = face_patch_pairs(cover, body)
    scan, first_free, first_collision = pull_off_scan(cover, body)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": "source/leica_m3_light_meter.stp (read-only)",
        "cover_solid_index": 4, "body_solid_index": 5,
        "baseline_intersection_volume_mm3": round(baseline, 7),
        "cover_face_count": len(cover.Faces()),
        "body_face_count": len(body.Faces()),
        "face_distance_tolerance_mm": FACE_DISTANCE_TOL,
        "minimum_reported_shared_area_mm2": MIN_PATCH_AREA,
        "coincident_face_pairs": pairs,
        "coincident_pair_count": len(pairs),
        "pull_off_direction": "+Z (cover translated upward relative to fixed body)",
        "pull_off_scan_mm": scan,
        "first_sampled_collision_free_lift_mm": first_free,
        "first_sampled_interference_lift_mm": first_collision,
        "limitations": [
            "Face common-area Boolean detects exact coincident patches; tolerance-near but noncoincident surfaces may be omitted.",
            "A zero-volume sampled pose does not prove continuous collision-free motion between samples.",
            "The +Z scan tests a rigid vertical pull-off only; it does not prove fastener release, elastic snap-fit release, or manufacturability.",
            "No screw, boss, latch, or split-line locations are inferred or approved.",
            "All source solids remain read-only; no STEP candidate is exported."
        ]
    }
    lines = [
        "# 盖体真实配合面与垂直拆卸路径审计", "",
        f"- 生成时间 UTC：{report['generated_utc']}",
        "- 原始 STEP 只读；盖体 #85、主体 #86。",
        f"- 基准交叠体积：{report['baseline_intersection_volume_mm3']} mm³。",
        f"- 面对面实际重合候选：{len(pairs)} 对（共同面积阈值 > {MIN_PATCH_AREA} mm²）。",
        "", "## 实际重合面片（按共同面积降序）",
        "|盖体面|主体面|曲面类型|共同面积 mm²|盖体面面积|主体面面积|面间距 mm|",
        "|---:|---:|---|---:|---:|---:|---:|"
    ]
    for p in pairs:
        lines.append(
            f"|{p['cover_face']}|{p['body_face']}|{p['cover_surface']} / {p['body_surface']}|"
            f"{p['shared_area_mm2']}|{p['cover_area_mm2']}|{p['body_area_mm2']}|{p['face_distance_mm']}|"
        )
    lines += [
        "", "## +Z 垂直拔出扫描",
        "|盖体上移 mm|交叠体积 mm³|交叠实体数|",
        "|---:|---:|---:|"
    ]
    for row in scan:
        lines.append(f"|{row['z_lift_mm']}|{row['intersection_volume_mm3']}|{row['intersection_solid_count']}|")
    lines += [
        "", f"- 首个采样无交叠位置：{first_free} mm。",
        "", "## 完整机器结果", "", "~~~json",
        json.dumps(report, ensure_ascii=False, indent=2), "~~~", "",
        "## 解释边界", "", *[f"- {x}" for x in report["limitations"]], ""
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)
    print(json.dumps({
        "baseline_intersection_volume_mm3": report["baseline_intersection_volume_mm3"],
        "coincident_pair_count": len(pairs),
        "largest_patches": pairs[:12],
        "pull_off_scan_mm": scan,
        "first_sampled_collision_free_lift_mm": first_free,
        "first_sampled_interference_lift_mm": first_collision
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
