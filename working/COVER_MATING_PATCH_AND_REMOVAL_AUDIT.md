# 盖体真实配合面与垂直拆卸路径审计

- 生成时间 UTC：2026-11-25T00:28:38.472039+00:00
- 原始 STEP 只读；盖体 #85、主体 #86。
- 基准交叠体积：0.0 mm³。
- 面对面实际重合候选：5 对（共同面积阈值 > 0.01 mm²）。

## 实际重合面片（按共同面积降序）
|盖体面|主体面|曲面类型|共同面积 mm²|盖体面面积|主体面面积|面间距 mm|
|---:|---:|---|---:|---:|---:|---:|
|20|2|PLANE / PLANE|198.14716|1311.24095|213.4486|0.0|
|17|94|PLANE / PLANE|14.4|19.2|35.54672|0.0|
|18|3|PLANE / PLANE|14.4|19.2|35.54672|0.0|
|15|39|PLANE / PLANE|9.6|9.6|532.31915|0.0|
|16|36|PLANE / PLANE|9.6|9.6|448.97446|0.0|

## +Z 垂直拔出扫描
|盖体上移 mm|交叠体积 mm³|交叠实体数|
|---:|---:|---:|
|0.05|0.0|0|
|0.1|0.0|0|
|0.15|0.0|0|
|0.2|0.0|0|
|0.25|0.0|0|
|0.3|0.0|0|
|0.35|0.0|0|
|0.4|0.0|0|
|0.45|1.44|2|
|0.5|2.88|2|
|0.55|4.32|2|
|0.6|5.76|2|
|0.65|7.2|2|
|0.7|8.64|2|
|0.75|10.08|2|
|0.8|11.52|2|
|0.85|12.96|2|
|0.9|14.4|2|
|0.95|15.84|2|
|1.0|17.28|2|
|1.25|24.4794998|2|
|1.5|31.570493|2|
|1.75|36.1759086|2|
|2.0|36.48|2|
|2.25|32.945202|2|
|2.5|25.915994|2|
|2.75|18.72|2|
|3.0|11.52|2|
|3.25|4.32|2|
|3.5|0.0|0|
|3.75|0.0|0|
|4.0|0.0|0|
|4.25|0.0|0|
|4.5|0.0|0|
|4.75|0.0|0|
|5.0|0.0|0|
|5.25|0.0|0|
|5.5|0.0|0|
|5.75|0.0|0|
|6.0|0.0|0|

- 首个采样无交叠位置：0.05 mm。

## 完整机器结果

~~~json
{
  "generated_utc": "2026-11-25T00:28:38.472039+00:00",
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "cover_solid_index": 4,
  "body_solid_index": 5,
  "baseline_intersection_volume_mm3": 0.0,
  "cover_face_count": 34,
  "body_face_count": 147,
  "face_distance_tolerance_mm": 0.03,
  "minimum_reported_shared_area_mm2": 0.01,
  "coincident_face_pairs": [
    {
      "cover_face": 20,
      "body_face": 2,
      "cover_surface": "PLANE",
      "body_surface": "PLANE",
      "cover_area_mm2": 1311.24095,
      "body_area_mm2": 213.4486,
      "shared_area_mm2": 198.14716,
      "face_distance_mm": 0.0,
      "cover_bbox_mm": [
        -19.5,
        -14.95,
        18.3,
        39.45,
        14.95,
        18.3
      ],
      "body_bbox_mm": [
        -19.5,
        -15.15,
        18.3,
        17.0738,
        15.15,
        18.3
      ]
    },
    {
      "cover_face": 17,
      "body_face": 94,
      "cover_surface": "PLANE",
      "body_surface": "PLANE",
      "cover_area_mm2": 19.2,
      "body_area_mm2": 35.54672,
      "shared_area_mm2": 14.4,
      "face_distance_mm": 0.0,
      "cover_bbox_mm": [
        -2.5,
        12.55,
        16.7,
        9.5,
        12.55,
        18.3
      ],
      "body_bbox_mm": [
        -15.0,
        12.55,
        17.1,
        14.6223,
        12.55,
        18.3
      ]
    },
    {
      "cover_face": 18,
      "body_face": 3,
      "cover_surface": "PLANE",
      "body_surface": "PLANE",
      "cover_area_mm2": 19.2,
      "body_area_mm2": 35.54672,
      "shared_area_mm2": 14.4,
      "face_distance_mm": 0.0,
      "cover_bbox_mm": [
        -2.5,
        -12.55,
        16.7,
        9.5,
        -12.55,
        18.3
      ],
      "body_bbox_mm": [
        -15.0,
        -12.55,
        17.1,
        14.6223,
        -12.55,
        18.3
      ]
    },
    {
      "cover_face": 15,
      "body_face": 39,
      "cover_surface": "PLANE",
      "body_surface": "PLANE",
      "cover_area_mm2": 9.6,
      "body_area_mm2": 532.31915,
      "shared_area_mm2": 9.6,
      "face_distance_mm": 0.0,
      "cover_bbox_mm": [
        -2.5,
        -13.75,
        14.9,
        9.5,
        -13.75,
        15.7
      ],
      "body_bbox_mm": [
        -15.0,
        -13.75,
        -1.0,
        27.5,
        -13.75,
        16.1
      ]
    },
    {
      "cover_face": 16,
      "body_face": 36,
      "cover_surface": "PLANE",
      "body_surface": "PLANE",
      "cover_area_mm2": 9.6,
      "body_area_mm2": 448.97446,
      "shared_area_mm2": 9.6,
      "face_distance_mm": 0.0,
      "cover_bbox_mm": [
        -2.5,
        13.75,
        14.9,
        9.5,
        13.75,
        15.7
      ],
      "body_bbox_mm": [
        -15.0,
        13.75,
        3.0,
        27.5,
        13.75,
        16.1
      ]
    }
  ],
  "coincident_pair_count": 5,
  "pull_off_direction": "+Z (cover translated upward relative to fixed body)",
  "pull_off_scan_mm": [
    {
      "z_lift_mm": 0.05,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.1,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.15,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.2,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.25,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.3,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.35,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.4,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 0.45,
      "intersection_volume_mm3": 1.44,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.5,
      "intersection_volume_mm3": 2.88,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.55,
      "intersection_volume_mm3": 4.32,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.6,
      "intersection_volume_mm3": 5.76,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.65,
      "intersection_volume_mm3": 7.2,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.7,
      "intersection_volume_mm3": 8.64,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.75,
      "intersection_volume_mm3": 10.08,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.8,
      "intersection_volume_mm3": 11.52,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.85,
      "intersection_volume_mm3": 12.96,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.9,
      "intersection_volume_mm3": 14.4,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 0.95,
      "intersection_volume_mm3": 15.84,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 1.0,
      "intersection_volume_mm3": 17.28,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 1.25,
      "intersection_volume_mm3": 24.4794998,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 1.5,
      "intersection_volume_mm3": 31.570493,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 1.75,
      "intersection_volume_mm3": 36.1759086,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 2.0,
      "intersection_volume_mm3": 36.48,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 2.25,
      "intersection_volume_mm3": 32.945202,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 2.5,
      "intersection_volume_mm3": 25.915994,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 2.75,
      "intersection_volume_mm3": 18.72,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 3.0,
      "intersection_volume_mm3": 11.52,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 3.25,
      "intersection_volume_mm3": 4.32,
      "intersection_solid_count": 2
    },
    {
      "z_lift_mm": 3.5,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 3.75,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 4.0,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 4.25,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 4.5,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 4.75,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 5.0,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 5.25,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 5.5,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 5.75,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    },
    {
      "z_lift_mm": 6.0,
      "intersection_volume_mm3": 0.0,
      "intersection_solid_count": 0
    }
  ],
  "first_sampled_collision_free_lift_mm": 0.05,
  "first_sampled_interference_lift_mm": 0.45,
  "limitations": [
    "Face common-area Boolean detects exact coincident patches; tolerance-near but noncoincident surfaces may be omitted.",
    "A zero-volume sampled pose does not prove continuous collision-free motion between samples.",
    "The +Z scan tests a rigid vertical pull-off only; it does not prove fastener release, elastic snap-fit release, or manufacturability.",
    "No screw, boss, latch, or split-line locations are inferred or approved.",
    "All source solids remain read-only; no STEP candidate is exported."
  ]
}
~~~

## 解释边界

- Face common-area Boolean detects exact coincident patches; tolerance-near but noncoincident surfaces may be omitted.
- A zero-volume sampled pose does not prove continuous collision-free motion between samples.
- The +Z scan tests a rigid vertical pull-off only; it does not prove fastener release, elastic snap-fit release, or manufacturability.
- No screw, boss, latch, or split-line locations are inferred or approved.
- All source solids remain read-only; no STEP candidate is exported.
