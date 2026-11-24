#!/usr/bin/env python3
"""Check shutter Z offsets against the cover, body, and fixed encoder parts."""
from pathlib import Path
from datetime import datetime, timezone
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/SHUTTER_MULTI_COMPONENT_SCAN.md"
EPS = 1e-7


def bbox(shape):
    b = shape.BoundingBox()
    return [round(float(v), 4) for v in (b.xmin, b.ymin, b.zmin, b.xmax, b.ymax, b.zmax)]


def measure(a, b):
    volume = float(a.intersect(b).Volume())
    distance = 0.0 if volume > EPS else float(a.distance(b))
    return {"volume": volume, "distance": distance}


def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 solids, got {len(solids)}")

    shutter_base = solids[3].translate(cq.Vector(10, 0, 0))
    obstacles = {
        "cover": solids[4],
        "body": solids[5],
        "encoder_button": solids[1],
        "encoder_dial": solids[2],
        "encoder_bracket": solids[6],
    }
    rows = []
    for i in range(-24, 25):
        dz = round(i * 0.25, 3)
        shutter = shutter_base.translate(cq.Vector(0, 0, dz))
        checks = {name: measure(shutter, shape) for name, shape in obstacles.items()}
        rows.append({"dz": dz, "checks": checks})

    # Cover and encoder parts are treated as clearance obstacles. The body is
    # reported separately because its original interface may include intended contact.
    def clear_of_fixed_parts(row):
        return all(row["checks"][name]["volume"] <= EPS
                   for name in ("cover", "encoder_button", "encoder_dial", "encoder_bracket"))

    clear_rows = [r for r in rows if clear_of_fixed_parts(r)]
    preferred = min(clear_rows, key=lambda r: abs(r["dz"] + 3.0)) if clear_rows else None
    upward = min((r for r in clear_rows if r["dz"] > 0), key=lambda r: r["dz"], default=None)
    downward = max((r for r in clear_rows if r["dz"] < 0), key=lambda r: r["dz"], default=None)

    lines = [
        "# 快门输入件多组件垂直位置扫描", "",
        f"- 生成时间 UTC：{datetime.now(timezone.utc).isoformat()}",
        "- 原始 STEP 只读；快门输入件副本先沿 X 平移 +10 mm，再按 Z 偏移扫描。",
        "- 扫描范围 −6～+6 mm，步长 0.25 mm；不修改任何原始实体。",
        f"- 快门输入件基准包围盒：{bbox(shutter_base)}",
        "- 检查对象：原盖体、原机身主体、编码器按钮、编码器转盘、编码器支架。",
        "- 盖体和编码器零件作为避让对象；机身主体单独报告，因为原始结构可能存在设计接触。",
        "",
        "## 避让结果", "",
        f"- 首个向下无盖体/编码器实体交叠采样：{downward}",
        f"- 首个向上无盖体/编码器实体交叠采样：{upward}",
        f"- 最接近 −3 mm 且无盖体/编码器实体交叠的采样：{preferred}",
        "",
        "## 全部偏移的实体交叠体积与间距", "",
        "|Z偏移|盖体交叠 mm³|盖体间距 mm|机身交叠 mm³|机身间距 mm|编码器按钮交叠 mm³|按钮间距 mm|编码器转盘交叠 mm³|转盘间距 mm|编码器支架交叠 mm³|支架间距 mm|",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        c = row["checks"]
        vals = [f"{row['dz']:.2f}"]
        for name in ("cover", "body", "encoder_button", "encoder_dial", "encoder_bracket"):
            vals.extend((f"{c[name]['volume']:.4f}", f"{c[name]['distance']:.4f}"))
        lines.append("|" + "|".join(vals) + "|")

    lines += [
        "", "## 关键候选位置", "",
        "|Z偏移|对象|交叠体积 mm³|最小距离 mm|",
        "|---:|---|---:|---:|",
    ]
    candidate_rows = []
    for target in (-3.0, -2.75, 5.0, 0.0):
        row = min(rows, key=lambda r: abs(r["dz"] - target))
        for name, result in row["checks"].items():
            candidate_rows.append((row["dz"], name, result))
    for dz, name, result in candidate_rows:
        lines.append(f"|{dz:.2f}|{name}|{result['volume']:.6f}|{result['distance']:.5f}|")

    lines += [
        "", "## 解释边界", "",
        "- 这是刚体包络扫描，不是装配建议；不代表快门联动件允许整体升降或下降。",
        "- 机身主体的交叠/接触必须结合原始装配界面判断，不能简单视为可切除干涉。",
        "- 零交叠不等于具有制造间隙；本扫描未加入公差、轴承、真实齿轮、轴、连杆、磁铁及相机耦合约束。",
        "- 编码器零件仅按原 STEP 固定位置检查；未验证动态运动包络。",
        "- 原始 STEP 与冻结零件未修改。",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"rows={len(rows)}; downward={downward}; upward={upward}; preferred={preferred}")


if __name__ == "__main__":
    main()
