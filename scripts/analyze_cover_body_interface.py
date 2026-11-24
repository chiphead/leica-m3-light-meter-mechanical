#!/usr/bin/env python3
"""Map the original cover/body mating interface and candidate mounting regions.

Read-only geometry audit. No source solid is changed and no STEP is exported.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/COVER_BODY_INTERFACE_AUDIT.md"
CONTACT_TOL = 0.03
NEAR_TOL = 0.50


def bbox(shape):
    b = shape.BoundingBox()
    return [round(float(v), 4) for v in
            (b.xmin, b.ymin, b.zmin, b.xmax, b.ymax, b.zmax)]


def face_info(face, index, other):
    surf = face.geomType()
    try:
        center = face.Center()
        c = [round(float(v), 4) for v in (center.x, center.y, center.z)]
    except Exception:
        c = None
    normal = None
    if surf == "PLANE":
        try:
            n = face.normalAt()
            normal = [round(float(v), 5) for v in (n.x, n.y, n.z)]
        except Exception:
            pass
    try:
        distance = float(face.distance(other))
    except Exception:
        distance = 1e9
    return {
        "face": index, "surface": surf,
        "area_mm2": round(float(face.Area()), 5),
        "center_mm": c, "normal": normal,
        "bbox_mm": bbox(face), "distance_to_other_mm": round(distance, 5),
        "contact_candidate": distance <= CONTACT_TOL,
        "near_candidate": distance <= NEAR_TOL,
    }


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 solids, got {len(solids)}")
    cover, body = solids[4], solids[5]
    common = cover.intersect(body)
    cover_faces = [face_info(f, i, body) for i, f in enumerate(cover.Faces())]
    body_faces = [face_info(f, i, cover) for i, f in enumerate(body.Faces())]
    cover_near = [x for x in cover_faces if x["near_candidate"]]
    body_near = [x for x in body_faces if x["near_candidate"]]
    cover_contact = [x for x in cover_faces if x["contact_candidate"]]
    body_contact = [x for x in body_faces if x["contact_candidate"]]
    # A candidate mounting land is only a planar cover face near the body;
    # it is not automatically suitable for a screw or boss.
    lands = [x for x in cover_near if x["surface"] == "PLANE" and
             x["area_mm2"] >= 4.0]
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": "source/leica_m3_light_meter.stp (read-only)",
        "cover_solid_index": 4, "body_solid_index": 5,
        "cover_volume_mm3": round(float(cover.Volume()), 5),
        "body_volume_mm3": round(float(body.Volume()), 5),
        "intersection_volume_mm3": round(float(common.Volume()), 7),
        "intersection_solid_count": len(common.Solids()),
        "cover_face_count": len(cover_faces), "body_face_count": len(body_faces),
        "contact_tolerance_mm": CONTACT_TOL, "near_tolerance_mm": NEAR_TOL,
        "cover_contact_faces": cover_contact, "body_contact_faces": body_contact,
        "cover_near_faces": cover_near, "body_near_faces": body_near,
        "candidate_planar_lands": lands,
        "limitations": [
            "Face-to-solid distance identifies proximity, not a mating-face pair or design intent.",
            "Coincident/near faces can be original fit surfaces; do not cut or offset them automatically.",
            "Candidate planar lands are not approved screw locations; edge distance, wall thickness, access and load path remain unverified.",
            "No assembly direction is inferred from static geometry.",
            "All source solids remain read-only; no STEP candidate is exported."
        ]
    }
    lines = [
        "# 原盖体与主体配合界面审计", "",
        f"- 生成时间 UTC：{report['generated_utc']}",
        "- 原始 STEP 只读；仅测量盖体 #85 与主体 #86。",
        f"- 盖体/主体实体交叠体积：{report['intersection_volume_mm3']} mm³。",
        f"- 盖体面数：{len(cover_faces)}；主体面数：{len(body_faces)}。",
        f"- 接触候选阈值：{CONTACT_TOL} mm；近邻阈值：{NEAR_TOL} mm。", "",
        "## 盖体接触候选面",
        "|面号|曲面|面积 mm²|中心 mm|法向|包围盒 mm|到主体距离 mm|",
        "|---:|---|---:|---|---|---|---:|"
    ]
    for x in cover_contact:
        lines.append(f"|{x['face']}|{x['surface']}|{x['area_mm2']}|{x['center_mm']}|{x['normal']}|{x['bbox_mm']}|{x['distance_to_other_mm']}|")
    lines += ["", "## 盖体近邻平面候选（面积 ≥ 4 mm²）",
        "|面号|面积 mm²|中心 mm|法向|包围盒 mm|距离 mm|",
        "|---:|---:|---|---|---|---:|"]
    for x in lands:
        lines.append(f"|{x['face']}|{x['area_mm2']}|{x['center_mm']}|{x['normal']}|{x['bbox_mm']}|{x['distance_to_other_mm']}|")
    lines += ["", "## 主体接触候选面",
        "|面号|曲面|面积 mm²|中心 mm|法向|包围盒 mm|到盖体距离 mm|",
        "|---:|---|---:|---|---|---|---:|"]
    for x in body_contact:
        lines.append(f"|{x['face']}|{x['surface']}|{x['area_mm2']}|{x['center_mm']}|{x['normal']}|{x['bbox_mm']}|{x['distance_to_other_mm']}|")
    lines += ["", "## 完整机器结果", "", "~~~json",
              json.dumps(report, ensure_ascii=False, indent=2), "~~~", "",
              "## 解释边界", "", *[f"- {x}" for x in report["limitations"]], ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)
    print(json.dumps({"cover_contact_faces": cover_contact,
                      "candidate_planar_lands": lands,
                      "body_contact_faces": body_contact}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
