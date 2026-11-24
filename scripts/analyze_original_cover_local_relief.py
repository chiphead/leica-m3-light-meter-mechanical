#!/usr/bin/env python3
"""Screen local reliefs in a copy of the original cover around the translated shutter input.

The source STEP and all frozen/source solids remain read-only. Positive 3D offsets
are built with OpenCascade's BRepOffsetAPI rather than a non-existent CadQuery
Solid.offset3D method.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

import cadquery as cq
from OCP.BRepOffsetAPI import BRepOffsetAPI_MakeOffsetShape
from OCP.BRepOffset import BRepOffset_Skin
from OCP.GeomAbs import GeomAbs_JoinType

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/ORIGINAL_COVER_LOCAL_RELIEF_SCREEN.md"
EPS = 1e-7
OFFSET_TOL = 1e-3


def measure(a, b):
    overlap = float(a.intersect(b).Volume())
    return overlap, (0.0 if overlap > EPS else float(a.distance(b)))


def expanded_cutter(shape, clearance):
    """Return a valid, closed, expanded solid using OCCT's 3D offset builder."""
    if clearance <= EPS:
        return shape
    builder = BRepOffsetAPI_MakeOffsetShape()
    builder.PerformByJoin(
        shape.wrapped,
        float(clearance),
        OFFSET_TOL,
        BRepOffset_Skin,
        False,
        False,
        GeomAbs_JoinType.GeomAbs_Arc,
        False,
    )
    if not builder.IsDone():
        raise RuntimeError("OpenCascade 3D offset builder did not complete")
    result = cq.Shape.cast(builder.Shape())
    solids = result.Solids()
    if not result.isValid() or len(solids) != 1:
        raise RuntimeError(
            f"Offset cutter is not one valid solid: valid={result.isValid()}, "
            f"solid_count={len(solids)}, shape_type={result.ShapeType()}"
        )
    return solids[0]


def bbox_values(shape):
    box = shape.BoundingBox()
    return [round(float(v), 4) for v in (
        box.xmin, box.ymin, box.zmin, box.xmax, box.ymax, box.zmax
    )]


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")

    # Source/frozen geometry is read-only. Only a copy of the original cover is cut.
    cover = solids[4]
    body = solids[5]
    moving = solids[3].translate(cq.Vector(10.0, 0.0, 0.0))
    fixed = {
        "encoder_button": solids[1],
        "encoder_dial": solids[2],
        "encoder_bracket": solids[6],
    }
    base_overlap, _ = measure(cover, moving)
    rows = []

    for clearance in (0.0, 0.2, 0.3, 0.5, 0.8):
        row = {"clearance_mm": clearance, "status": "not_run"}
        try:
            cutter = expanded_cutter(moving, clearance)
            row.update({
                "cutter_valid": bool(cutter.isValid()),
                "cutter_solid_count": len(cutter.Solids()),
                "cutter_volume_mm3": round(float(cutter.Volume()), 6),
                "cutter_body_overlap_mm3": round(float(cutter.intersect(body).Volume()), 6),
            })
            candidate = cover.cut(cutter).clean()
            row.update({
                "candidate_valid": bool(candidate.isValid()),
                "candidate_solid_count": len(candidate.Solids()),
                "candidate_volume_mm3": round(float(candidate.Volume()), 6),
                "removed_cover_volume_mm3": round(float(cover.Volume() - candidate.Volume()), 6),
                "remaining_cover_vs_moving_mm3": round(measure(candidate, moving)[0], 6),
                "remaining_cover_vs_cutter_mm3": round(measure(candidate, cutter)[0], 6),
                "candidate_vs_body_distance_mm": round(measure(candidate, body)[1], 5),
                "candidate_bbox_mm": bbox_values(candidate),
                "fixed_checks": {},
            })
            for name, obstacle in fixed.items():
                overlap, distance = measure(candidate, obstacle)
                row["fixed_checks"][name] = {
                    "overlap_mm3": round(overlap, 6),
                    "distance_mm": round(distance, 5),
                }
            row["status"] = "screened"
            row["geometrically_valid_candidate"] = (
                row["cutter_valid"]
                and row["cutter_solid_count"] == 1
                and row["candidate_valid"]
                and row["candidate_solid_count"] == 1
                and row["remaining_cover_vs_moving_mm3"] <= EPS
                and row["remaining_cover_vs_cutter_mm3"] <= EPS
                and row["cutter_body_overlap_mm3"] <= EPS
                and all(x["overlap_mm3"] <= EPS for x in row["fixed_checks"].values())
            )
        except Exception as exc:
            row["status"] = "failed"
            row["error"] = f"{type(exc).__name__}: {exc}"
        rows.append(row)

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": "source/leica_m3_light_meter.stp (read-only)",
        "base_cover_shutter_overlap_mm3": round(base_overlap, 6),
        "method": "OpenCascade BRepOffsetAPI_MakeOffsetShape positive 3D offset; subtract only from a copy of the original cover.",
        "offset_tolerance_mm": OFFSET_TOL,
        "candidate_clearances_mm": [0.0, 0.2, 0.3, 0.5, 0.8],
        "rows": rows,
        "limitations": [
            "This is a local-relief geometry screen, not a production cover design.",
            "The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.",
            "Offset success does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.",
            "The cover/body mating interface must be reviewed separately; the body is never modified.",
            "A split cover candidate is rejected even if each resulting solid is individually valid.",
            "No STEP candidate is exported at this stage."
        ]
    }

    lines = [
        "# 原始盖体局部避让候选筛查", "",
        f"- 生成时间 UTC：{report['generated_utc']}",
        "- 原始 STEP 只读；仅对原盖体副本执行切除。",
        f"- 原始盖体与 +X 10 mm 快门输入件交叠：{base_overlap:.6f} mm³。",
        "- 偏置方法：OpenCascade BRepOffsetAPI_MakeOffsetShape 正向三维偏置。",
        "- 候选余量：0、0.2、0.3、0.5、0.8 mm；本轮不导出 STEP。", "",
        "|余量 mm|状态|切刀实体数|切刀-主体交叠 mm³|去除盖体 mm³|剩余交叠 mm³|盖体实体数|候选-主体间距 mm|几何初筛|",
        "|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for x in rows:
        lines.append(
            f"|{x['clearance_mm']:.1f}|{x['status']}|"
            f"{x.get('cutter_solid_count', '-')}"
            f"|{x.get('cutter_body_overlap_mm3', '-')}"
            f"|{x.get('removed_cover_volume_mm3', '-')}"
            f"|{x.get('remaining_cover_vs_cutter_mm3', '-')}"
            f"|{x.get('candidate_solid_count', '-')}"
            f"|{x.get('candidate_vs_body_distance_mm', '-')}"
            f"|{'通过初筛' if x.get('geometrically_valid_candidate') else '未通过/待复核'}|"
        )
        if x.get("error"):
            lines.append(f"\n- {x['clearance_mm']:.1f} mm 失败原因：{x['error']}")
    lines += [
        "", "## 完整机器结果", "", "~~~json",
        json.dumps(report, ensure_ascii=False, indent=2), "~~~", "",
        "## 接受条件", "",
        "- 偏置切刀必须是有效单一实体。",
        "- 切后盖体必须保持单一有效实体，且与快门输入件无残余交叠。",
        "- 切刀不得侵入机身主体；盖体与主体的原始配合关系仍需人工审查。",
        "- 不满足任一条件的候选均不导出 STEP。", "",
        "## 限制", "",
        *[f"- {x}" for x in report["limitations"]], ""
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    for row in rows:
        print(json.dumps(row, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
