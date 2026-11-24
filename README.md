# Leica M3 Light Meter — Mechanical Design

独立机械设计仓库，源自 `chiphead/leica-m3-light-meter` 的 `cla` 分支。

## 状态

研发中（Research / Development）。当前内容包含实测基准 STEP、机械结构分析、CAD 几何检查报告及历史概念归档。它们不代表已完成制造验证或可直接投产。

## 目录

- `source/` — 原始实测 STEP 基准文件；只读，不得直接覆盖或修改。
- `working/` — 派生模型、坐标基准、设计分析与自动生成报告。
- `archive/` — 历史概念模型和旧版资料，仅供追溯，不作为当前设计基准。
- `drawings/` — 工程图。
- `releases/` — 经审查发布的模型与资料。
- `scripts/` — CAD 几何分析工具。
- `.github/workflows/` — 专用 CAD 分析工作流。

## 基准与冻结约束

`source/leica_m3_light_meter.stp` 是唯一原始几何基准。所有与实物一致且已测量验证的电子件位置、方向、尺寸，以及 TSL2591 入光孔、垂直安装槽和光路均为冻结项。任何改版必须派生到 `working/`，不得改写原始 STEP。

齿轮传动、轴系支撑、壳体局部结构等仍处于研发验证阶段。几何避碰或截面连通结果不等于最小壁厚、结构强度、装配性或制造性验证。

## 分析

本仓库使用 CadQuery 2.5.2 / OpenCascade。运行：

```bash
python -m pip install -r requirements-cad.txt
python scripts/analyze_step_geometry.py
```

报告写入 `working/STEP_GEOMETRY_REPORT.md`。工作流仅在机械源文件、分析脚本或工作流发生变更时运行。

## License

当前未附加开源许可证。除非另有书面授权，仓库内容默认保留原作者权利，不应视为已获准自由复制、修改或商用。
