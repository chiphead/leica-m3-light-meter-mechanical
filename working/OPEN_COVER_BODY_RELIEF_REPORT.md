# 双开口上盖精确机身避让分析

- 生成时间（UTC）：2026-11-24T13:13:11.672815+00:00
- 输入：source/leica_m3_light_meter.stp（只读）
- 内核：CadQuery/OpenCascade
- 运动扫掠半径：31.996925 mm
- 环框内/外半径：32.496925/33.996925 mm
- Z范围：14.900000…20.900000 mm
- 方法：对双开口环框候选执行 Boolean fuse，再仅从盖体候选中扣除机身主体 B-rep
- 主体和原始 STEP 均不修改；扣除后接口为零制造间隙，不等于生产公差。

|开口余量|桥外扩|原始有效/实体数|原始机身交叠 mm³|避让后有效/实体数|避让后机身交叠 mm³|运动总成交叠 mm³|STEP候选|
|---:|---:|---:|---:|---:|---:|---:|---|
|2.5°|1.0 mm|True/1|21.051540173|True/1|0.0|0.0|working/open_cover_candidates/open_cover_gap2.5deg_bridge1mm.step|
|2.5°|2.0 mm|True/1|35.085900288|True/1|0.0|0.0|working/open_cover_candidates/open_cover_gap2.5deg_bridge2mm.step|
|5.0°|1.0 mm|True/1|20.91061317|True/1|0.0|0.0|working/open_cover_candidates/open_cover_gap5deg_bridge1mm.step|
|5.0°|2.0 mm|True/1|34.851021949|True/1|0.0|0.0|working/open_cover_candidates/open_cover_gap5deg_bridge2mm.step|

## 完整结果

[
  {
    "gap_margin_deg": 2.5,
    "gap_ranges_deg": [
      [
        147.5,
        162.5
      ],
      [
        197.5,
        212.5
      ]
    ],
    "bridge_outer_offset_mm": 1.0,
    "raw_valid": true,
    "raw_solid_count": 1,
    "raw_body_intersection_mm3": 21.051540173,
    "relieved_valid": true,
    "relieved_solid_count": 1,
    "relieved_volume_mm3": 1861.89295568,
    "removed_body_volume_mm3": 21.051540173,
    "relieved_body_intersection_mm3": 0.0,
    "moving_assembly_intersection_mm3": 0.0,
    "fixed_geometry_checks": [
      {
        "obstacle": "encoder_button",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_dial",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_bracket",
        "intersection_volume_mm3": 0.0
      }
    ],
    "pin_envelope_intersection_mm3": 0.0,
    "error": null,
    "raw_volume_mm3": 1882.944495853,
    "step_file": "working/open_cover_candidates/open_cover_gap2.5deg_bridge1mm.step",
    "stl_file": "working/open_cover_candidates/open_cover_gap2.5deg_bridge1mm.stl"
  },
  {
    "gap_margin_deg": 2.5,
    "gap_ranges_deg": [
      [
        147.5,
        162.5
      ],
      [
        197.5,
        212.5
      ]
    ],
    "bridge_outer_offset_mm": 2.0,
    "raw_valid": true,
    "raw_solid_count": 1,
    "raw_body_intersection_mm3": 35.085900288,
    "relieved_valid": true,
    "relieved_solid_count": 1,
    "relieved_volume_mm3": 1958.10595875,
    "removed_body_volume_mm3": 35.085900288,
    "relieved_body_intersection_mm3": 0.0,
    "moving_assembly_intersection_mm3": 0.0,
    "fixed_geometry_checks": [
      {
        "obstacle": "encoder_button",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_dial",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_bracket",
        "intersection_volume_mm3": 0.0
      }
    ],
    "pin_envelope_intersection_mm3": 0.0,
    "error": null,
    "raw_volume_mm3": 1993.191859038,
    "step_file": "working/open_cover_candidates/open_cover_gap2.5deg_bridge2mm.step",
    "stl_file": "working/open_cover_candidates/open_cover_gap2.5deg_bridge2mm.stl"
  },
  {
    "gap_margin_deg": 5.0,
    "gap_ranges_deg": [
      [
        145.0,
        165.0
      ],
      [
        195.0,
        215.0
      ]
    ],
    "bridge_outer_offset_mm": 1.0,
    "raw_valid": true,
    "raw_solid_count": 1,
    "raw_body_intersection_mm3": 20.91061317,
    "relieved_valid": true,
    "relieved_solid_count": 1,
    "relieved_volume_mm3": 1861.098606881,
    "removed_body_volume_mm3": 20.91061317,
    "relieved_body_intersection_mm3": 0.0,
    "moving_assembly_intersection_mm3": 0.0,
    "fixed_geometry_checks": [
      {
        "obstacle": "encoder_button",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_dial",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_bracket",
        "intersection_volume_mm3": 0.0
      }
    ],
    "pin_envelope_intersection_mm3": 0.0,
    "error": null,
    "raw_volume_mm3": 1882.00922005,
    "step_file": "working/open_cover_candidates/open_cover_gap5deg_bridge1mm.step",
    "stl_file": "working/open_cover_candidates/open_cover_gap5deg_bridge1mm.stl"
  },
  {
    "gap_margin_deg": 5.0,
    "gap_ranges_deg": [
      [
        145.0,
        165.0
      ],
      [
        195.0,
        215.0
      ]
    ],
    "bridge_outer_offset_mm": 2.0,
    "raw_valid": true,
    "raw_solid_count": 1,
    "raw_body_intersection_mm3": 34.851021949,
    "relieved_valid": true,
    "relieved_solid_count": 1,
    "relieved_volume_mm3": 1992.846159135,
    "removed_body_volume_mm3": 34.851021949,
    "relieved_body_intersection_mm3": 0.0,
    "moving_assembly_intersection_mm3": 0.0,
    "fixed_geometry_checks": [
      {
        "obstacle": "encoder_button",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_dial",
        "intersection_volume_mm3": 0.0
      },
      {
        "obstacle": "encoder_bracket",
        "intersection_volume_mm3": 0.0
      }
    ],
    "pin_envelope_intersection_mm3": 0.0,
    "error": null,
    "raw_volume_mm3": 2027.697181084,
    "step_file": "working/open_cover_candidates/open_cover_gap5deg_bridge2mm.step",
    "stl_file": "working/open_cover_candidates/open_cover_gap5deg_bridge2mm.stl"
  }
]

## 限制

- 单一有效 B-rep 仅代表拓扑/几何内核有效，不代表结构强度、刚度或疲劳寿命。
- 未设计安装耳、螺钉、定位面、密封、工具可达性及装配顺序。
- 未加入制造间隙；扣除机身得到的是零间隙贴合界面。
- 环框高度沿用旧盖包围盒，仅为探索参数，不是最终高度。
- 未评估打印方向、材料各向异性、支撑和后处理。
