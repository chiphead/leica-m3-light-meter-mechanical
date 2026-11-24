#!/usr/bin/env python3
"""Screen local reliefs in the original cover around the translated shutter input."""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/ORIGINAL_COVER_LOCAL_RELIEF_SCREEN.md"
EPS = 1e-7


def measure(a, b):
    overlap = float(a.intersect(b).Volume())
    return overlap, (0.0 if overlap > EPS else float(a.distance(b)))


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")

    # Frozen/source geometry is read-only. Only the cover candidate is cut.
    cover = solids[4]
    body = solids[5]
    moving = solids[3].translate(cq.Vector(10.0, 0.0, 0.0))
    fixed = {
        "body": body,
        "encoder_button": solids[1],
        "encoder_dial": solids[2],
        "encoder_bracket": solids[6],
    }
    base_overlap, _ = measure(cover, moving)
    rows = []

    for clearance in (0.0, 0.2, 0.3, 0.5, 0.8):
        row = {"clearance_mm": clearance, "status": "not_run"}
        try:
            cutter = moving if clearance == 0.0 else moving.offset3D(clearance, kind="arc")
            cutter_solids = cutter.Solids()
            row["cutter_valid"] = bool(cutter.isValid())
            row["cutter_solid_count"] = len(cutter_solids)
            if not row["cutter_valid"] or len(cutter_solids) != 1:
                raise RuntimeError("Offset cutter is not one valid solid")
            candidate = cover.cut(cutter).clean()
            row.update({
                "candidate_valid": bool(candidate.isValid()),
                "candidate_solid_count": len(candidate.Solids()),
                "candidate_volume_mm3": round(float(candidate.Volume()), 6),
                "removed_cover_volume_mm3": round(float(cover.Volume() - candidate.Volume()), 6),
                "remaining_cover_vs_moving": measure(candidate, moving)[0],
                "candidate_vs_body_distance_mm": measure(candidate, body)[1],
                "candidate_bbox_mm": [round(float(v), 4) for v in (
                    candidate.BoundingBox().xmin, candidate.BoundingBox().ymin,
                    candidate.BoundingBox().zmin, candidate.BoundingBox().xmax,
                    candidate.BoundingBox().ymax, candidate.BoundingBox().zmax)],
                "cutter_body_overlap_mm3": round(float(cutter.intersect(body).Volume()), 6),
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
                row["candidate_valid"] and row["candidate_solid_count"] == 1
                and row["remaining_cover_vs_moving"] <= EPS
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
        "method": "Subtract the translated shutter-input B-rep or its 3D offset from a copy of the original cover; do not alter the body or frozen parts.",
        "candidate_clearances_mm": [0.0, 0.2, 0.3, 0.5, 0.8],
        "rows": rows,
        "limitations": [
            "This is a local-relief geometry screen, not a production cover design.",
            "The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.",
            "Offset failures are reported and are not replaced by guessed box cuts.",
            "A valid single solid does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.",
            "The cover/body mating interface must be reviewed separately; the body is never modified.",
            "No STEP candidate is exported at this stage."
        ]
    }
    lines = [
        "# 原始盖体局部避让候选筛查", "",
        f"- 生成时间 UTC：{report['generated_utc']}",
        "- 原始 STEP 只读；只对原盖体副本执行切除。",
        f"- 原始盖体与 +X 10 mm 快门输入件交叠：{base_overlap:.6f} mm³。",
        "- 候选：按 0、0.2、0.3、0.5、0.8 mm 余量构造快门件 B-rep 偏置切刀。",
        "- 本轮不导出 STEP；先验证偏置内核、实体有效性、主体界面及冻结编码器避让。", "",
        "|目标余量 mm|状态|有效/实体数|去除盖体体积 mm³|剩余盖体-快门交叠 mm³|切刀-主体交叠 mm³|候选-主体间距 mm|几何筛查|",
        "|---:|---|---|---:|---:|---:|---:|---|",
    ]
    for x in rows:
        lines.append(
            f"|{x['clearance_mm']:.1f}|{x['status']}|"
            f"{x.get('candidate_valid', False)}/{x.get('candidate_solid_count', '-')}"
            f"|{x.get('removed_cover_volume_mm3', '-')}"
            f"|{x.get('remaining_cover_vs_moving', '-')}"
            f"|{x.get('cutter_body_overlap_mm3', '-')}"
            f"|{x.get('candidate_vs_body_distance_mm', '-')}"
            f"|{'通过初筛' if x.get('geometrically_valid_candidate') else '未通过/待复核'}|"
        )
        if x.get("error"):
            lines.append(f"\n- {x['clearance_mm']:.1f} mm 失败原因：{x['error']}")
    lines += ["", "## 完整机器结果", "", "~~~json",
              json.dumps(report, ensure_ascii=False, indent=2), "~~~", "",
              "## 设计判断规则", "",
              "- 若偏置切刀与主体相交，该余量候选不接受，避免把原盖体/主体配合面误切掉。",
              "- 若偏置后盖体分裂、无效或仍与快门件交叠，不进入 STEP 导出。",
              "- 若所有余量均失败，下一步改为基于盖体面拓扑设计局部开口/分型，而不是扩大盲目切除。",
              "- 即使几何筛查通过，仍需人工确认最小壁厚、外观连续性、定位、紧固和拆装方向。", "",
              "## 限制", "",
              *[f"- {x}" for x in report["limitations"]], ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    for row in rows:
        print(json.dumps(row, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
