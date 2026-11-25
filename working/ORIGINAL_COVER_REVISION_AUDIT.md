# 原始外壳盖子改造专项审计

- 生成时间（UTC）：2026-11-25T00:13:18.119340+00:00
- 原始 STEP：只读；未修改、未导出任何改版实体。
- 目标：以原始盖子 #85 为设计基体，检查右移后的快门输入模块及高位齿轮包络。
- 约束：主体 #86、编码器机构、AS5600/磁铁基准、TSL2591 光路及所有已验证电子件保持冻结。
- 齿轮轴心：输出 (24.5, 0)，输入 (34.5, 0)，中心距 10 mm。
- 齿轮毛坯探针：Ø11 x 2 mm，Z=21…23 mm；仅用于空间检查，不代表真实齿形。

## 原始盖子包围盒（mm）

- Min：[-19.5, -14.95, 14.9]
- Max：[39.45, 14.95, 20.9]

## 盖子与改造机构的实体检查

|检查对象|交叠体积 (mm³)|交叠实体数|交叠区域包围盒 min/max (mm)|最小距离 (mm)|说明|
|---|---:|---:|---|---:|---|
|original cover vs +10 mm translated shutter input module|186.323213776|1|[29.672, -8.5, 18.3, 39.45, 8.5, 20.9]|0.0|实体空间探针|
|original cover vs output gear blank Ø11 x 2 at Z=21..23|0.0|0|None|3.201562|实体空间探针|
|original cover vs input gear blank Ø11 x 2 at Z=21..23|0.0|0|None|0.1|实体空间探针|
|original cover vs output axial probe Ø2 from Z=20.9|0.0|0|None|7.7|实体空间探针|
|original cover vs input axial probe Ø2 from Z=20.9|0.0|0|None|0.271374|实体空间探针|
|original cover vs fixed encoder button|0.0|0|None|17.6|实体空间探针|
|original cover vs fixed encoder dial|0.0|0|None|15.1|实体空间探针|
|original cover vs fixed encoder bracket|0.0|0|None|7.4|实体空间探针|
|original cover vs original main body (baseline fit; not automatically a collision)|0.0|0|None|0.0|原始盖体/主体配合基线，不能简单当作碰撞|

## 盖子面级交叠定位

|障碍物|盖子面枚举|曲面类型|边界交叠面积 (mm²)|盖子面包围盒 min/max (mm)|
|---|---:|---|---:|---|
|translated_shutter_input|14|CYLINDER|41.35193493|[15.8, -8.7, 18.3, 33.2, 8.7, 20.9]|
|translated_shutter_input|20|PLANE|228.30718124|[-19.5, -14.95, 18.3, 39.45, 14.95, 18.3]|
|translated_shutter_input|21|PLANE|102.68274329|[32.5122, -12.6217, 18.9178, 39.45, 12.6217, 20.9]|
|translated_shutter_input|22|CYLINDER|14.52112559|[24.5, -14.95, 18.3, 39.45, 14.95, 20.9]|
|translated_shutter_input|25|PLANE|12.54660683|[-19.5, -14.95, 20.9, 32.5122, 14.95, 20.9]|

## 机器可读结果

~~~json
{
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "kernel": "CadQuery/OpenCascade",
  "source_solid_count": 7,
  "cover_solid_index": 4,
  "body_solid_index": 5,
  "cover_bbox_mm": {
    "min": [
      -19.5,
      -14.95,
      14.9
    ],
    "max": [
      39.45,
      14.95,
      20.9
    ]
  },
  "shutter_input_translation_mm": [
    10.0,
    0.0,
    0.0
  ],
  "gear_layout": {
    "output_center_xy_mm": [
      24.5,
      0.0
    ],
    "input_center_xy_mm": [
      34.5,
      0.0
    ],
    "center_distance_mm": 10.0,
    "gear_blank_diameter_mm": 11.0,
    "gear_blank_width_mm": 2.0,
    "gear_blank_z_mm": [
      21.0,
      23.0
    ],
    "note": "Cylindrical blanks are clearance probes only, not real meshing gears."
  },
  "checks": [
    {
      "pair": "original cover vs +10 mm translated shutter input module",
      "intersection_volume_mm3": 186.323213776,
      "intersection_solid_count": 1,
      "intersection_bbox_mm": [
        29.672,
        -8.5,
        18.3,
        39.45,
        8.5,
        20.9
      ],
      "minimum_distance_mm": 0.0
    },
    {
      "pair": "original cover vs output gear blank Ø11 x 2 at Z=21..23",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 3.201562
    },
    {
      "pair": "original cover vs input gear blank Ø11 x 2 at Z=21..23",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 0.1
    },
    {
      "pair": "original cover vs output axial probe Ø2 from Z=20.9",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 7.7
    },
    {
      "pair": "original cover vs input axial probe Ø2 from Z=20.9",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 0.271374
    },
    {
      "pair": "original cover vs fixed encoder button",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 17.6
    },
    {
      "pair": "original cover vs fixed encoder dial",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 15.1
    },
    {
      "pair": "original cover vs fixed encoder bracket",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 7.4
    },
    {
      "pair": "original cover vs original main body (baseline fit; not automatically a collision)",
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0,
      "intersection_bbox_mm": null,
      "minimum_distance_mm": 0.0
    }
  ],
  "cover_face_overlap_diagnostics": [
    {
      "obstacle": "translated_shutter_input",
      "cover_face_index": 14,
      "surface_type": "CYLINDER",
      "overlap_area_mm2": 41.35193493,
      "cover_face_bbox": [
        15.8,
        -8.7,
        18.3,
        33.2,
        8.7,
        20.9
      ]
    },
    {
      "obstacle": "translated_shutter_input",
      "cover_face_index": 20,
      "surface_type": "PLANE",
      "overlap_area_mm2": 228.30718124,
      "cover_face_bbox": [
        -19.5,
        -14.95,
        18.3,
        39.45,
        14.95,
        18.3
      ]
    },
    {
      "obstacle": "translated_shutter_input",
      "cover_face_index": 21,
      "surface_type": "PLANE",
      "overlap_area_mm2": 102.68274329,
      "cover_face_bbox": [
        32.5122,
        -12.6217,
        18.9178,
        39.45,
        12.6217,
        20.9
      ]
    },
    {
      "obstacle": "translated_shutter_input",
      "cover_face_index": 22,
      "surface_type": "CYLINDER",
      "overlap_area_mm2": 14.52112559,
      "cover_face_bbox": [
        24.5,
        -14.95,
        18.3,
        39.45,
        14.95,
        20.9
      ]
    },
    {
      "obstacle": "translated_shutter_input",
      "cover_face_index": 25,
      "surface_type": "PLANE",
      "overlap_area_mm2": 12.54660683,
      "cover_face_bbox": [
        -19.5,
        -14.95,
        20.9,
        32.5122,
        14.95,
        20.9
      ]
    }
  ],
  "limitations": [
    "The original cover and body are not modified.",
    "Intersection bounding boxes localize volumetric interference; they do not define a valid cut profile.",
    "A cylindrical gear blank is only a spatial envelope; it does not validate involute tooth geometry or meshing.",
    "The Ø2 axial probes are diagnostic envelopes, not selected shaft diameters or approved shaft paths.",
    "Zero overlap is not a manufacturing clearance or assembly-path proof.",
    "Face intersection area is a boundary diagnostic and is not material removal area.",
    "No mounting ears, fasteners, split line, CNC tool access, wall thickness, stiffness, or assembly sequence are designed here."
  ]
}
~~~

## 解释边界

- The original cover and body are not modified.
- Intersection bounding boxes localize volumetric interference; they do not define a valid cut profile.
- A cylindrical gear blank is only a spatial envelope; it does not validate involute tooth geometry or meshing.
- The Ø2 axial probes are diagnostic envelopes, not selected shaft diameters or approved shaft paths.
- Zero overlap is not a manufacturing clearance or assembly-path proof.
- Face intersection area is a boundary diagnostic and is not material removal area.
- No mounting ears, fasteners, split line, CNC tool access, wall thickness, stiffness, or assembly sequence are designed here.

## 下一阶段设计决策

1. 先依据本报告确认原盖子与右移快门盘、齿轮层及轴向连接探针的真实冲突位置。
2. 只在原盖子上提出局部开口/沉台/局部增厚或盖体分型方案；不得创建没有明确安装与保护功能的独立环框。
3. 新盖子必须明确与主体的定位面、紧固方式、拆装方向和加工可达性。
4. 真实渐开线齿轮、轴段、齿轮匣和盖子改版必须联合检查后才导出候选 STEP。
