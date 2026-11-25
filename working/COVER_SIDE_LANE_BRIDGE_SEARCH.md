# 原始上盖侧向绕行连接筋搜索

- 生成时间 UTC：2026-11-25T02:32:19.024479+00:00
- 原始 STEP 只读；只在 #85 派生副本上测试。
- 原盖体包围盒：[-19.5, -14.95, 14.9, 39.45, 14.95, 20.9]
- 避让后基础实体数：2
- 搜索候选：1026；通过全部几何初筛：0

|排名|侧向|X范围|绝对Y范围|Z范围|实体数|机身交叠|快门交叠|包围盒内|STEP|
|---:|---|---|---|---|---:|---:|---:|---|---|
|—|无|—|—|—|—|—|—|—|未导出|

## 解释边界

- The translated shutter solid is a static placement probe, not a validated dynamic swept envelope.
- A bridge passing B-rep checks is not proof of adequate wall thickness, strength, fatigue life, or printability.
- The bridge boxes are deliberately simple search primitives, not finished filleted ribs.
- No fastener, insert, gasket, assembly path, or manufacturing tolerance is validated.
- The original cover/body mating faces are not intentionally cut; body collision is a hard rejection.

## 机器可读结果

```json
{
  "generated_utc": "2026-11-25T02:32:19.024479+00:00",
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "cover_bbox_mm": [
    -19.5,
    -14.95,
    14.9,
    39.45,
    14.95,
    20.9
  ],
  "body_bbox_mm": [
    -19.5,
    -15.15,
    -2.2,
    45.4001,
    15.15,
    18.3
  ],
  "base_relief_solid_count": 2,
  "base_relief_volume_mm3": 3651.244703,
  "candidate_count": 1026,
  "passing_candidate_count": 0,
  "best_candidates": [],
  "all_candidates": [
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.544708,
      "body_overlap_mm3": 33.73375,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3785.884709,
      "body_overlap_mm3": 27.616483,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.204709,
      "body_overlap_mm3": 40.678099,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.695797,
      "body_overlap_mm3": 33.73375,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.035797,
      "body_overlap_mm3": 27.616483,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3869.285797,
      "body_overlap_mm3": 40.678099,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.854407,
      "body_overlap_mm3": 33.73375,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3808.194407,
      "body_overlap_mm3": 27.616483,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3892.344407,
      "body_overlap_mm3": 40.678099,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3857.764769,
      "body_overlap_mm3": 33.73375,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3824.104769,
      "body_overlap_mm3": 27.616483,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3917.164771,
      "body_overlap_mm3": 40.678099,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3765.094709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3742.324709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.864709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.245797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.475797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.945797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.404407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3764.634407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.004407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.314769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3780.544769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3851.824771,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.594709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3702.724709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.464709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.745797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3711.875797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.545797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.904407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.034407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3767.604407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3753.814769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.944769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.424771,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.994709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3671.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.944709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.145797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.195797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.025797,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.304407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3693.354407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.084407,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3714.214769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.264769,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.904771,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.395796,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.395796,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3667.325796,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.554406,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.554406,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3690.384406,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.464768,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.464768,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.20477,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3836.544708,
      "body_overlap_mm3": 37.737215,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3799.484709,
      "body_overlap_mm3": 30.619949,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3873.604709,
      "body_overlap_mm3": 44.681611,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.020864,
      "body_overlap_mm3": 37.737215,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3810.960864,
      "body_overlap_mm3": 30.619949,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3892.710864,
      "body_overlap_mm3": 44.681611,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3864.500998,
      "body_overlap_mm3": 37.737215,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.440999,
      "body_overlap_mm3": 30.619949,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3920.090999,
      "body_overlap_mm3": 44.681611,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3883.400732,
      "body_overlap_mm3": 37.737215,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3846.340732,
      "body_overlap_mm3": 30.619949,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3948.800734,
      "body_overlap_mm3": 44.681611,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3776.594708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.524709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.664709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.070864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3763.000864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.770864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.550998,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3779.480999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.150999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3823.450732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3798.380732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3876.860734,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3722.094709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.924709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3736.264709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.570864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.400864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.370864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.050998,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.880999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.750999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.950732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.780732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3811.460734,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.494709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.944709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.970864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3684.520864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3703.050864,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.450998,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.000999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.430999,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.350732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.900732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.140734,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.720863,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.720863,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.350863,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.200997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.200997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.730997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.100732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.100732,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3726.440734,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.544708,
      "body_overlap_mm3": 41.015212,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3813.084709,
      "body_overlap_mm3": 32.897946,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3894.004709,
      "body_overlap_mm3": 47.959662,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.822525,
      "body_overlap_mm3": 41.015212,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.292099,
      "body_overlap_mm3": 32.897946,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3916.612525,
      "body_overlap_mm3": 47.959662,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3888.305033,
      "body_overlap_mm3": 41.015212,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3847.673996,
      "body_overlap_mm3": 32.897946,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3948.995033,
      "body_overlap_mm3": 47.959662,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3910.806903,
      "body_overlap_mm3": 41.015212,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3870.085318,
      "body_overlap_mm3": 32.897946,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3982.206905,
      "body_overlap_mm3": 47.959662,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.094708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3760.724709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3815.464709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3802.372525,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.932099,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.072526,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3822.855033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.313997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3870.455033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.356903,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3817.725318,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3903.666905,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.594708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.124709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.064709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3742.872525,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.332099,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.672526,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3763.355033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3747.713997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3799.055033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3785.856903,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.125318,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3832.266905,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.994708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.944709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.272525,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.252099,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.552526,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.755033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.633997,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.935033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3738.256903,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.045318,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.146905,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.522524,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.452098,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.852524,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.005032,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.833996,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.235032,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.506903,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.245317,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.446905,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3811.044708,
      "body_overlap_mm3": 33.336262,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3779.084709,
      "body_overlap_mm3": 27.218995,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3843.004709,
      "body_overlap_mm3": 39.816335,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.138982,
      "body_overlap_mm3": 33.336262,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.178983,
      "body_overlap_mm3": 27.218995,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3858.678983,
      "body_overlap_mm3": 39.816335,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3833.179675,
      "body_overlap_mm3": 33.336262,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.219676,
      "body_overlap_mm3": 27.218995,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3881.119676,
      "body_overlap_mm3": 39.816335,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.434654,
      "body_overlap_mm3": 33.336262,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.474654,
      "body_overlap_mm3": 27.218995,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3904.834656,
      "body_overlap_mm3": 39.816335,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.344709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.724709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3780.964709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.438982,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.818983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.638983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.479675,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.859676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.079676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.734654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.114654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3842.794656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.344709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3700.124709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.564709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3721.438982,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.218983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.238983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3734.479676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3722.259676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.679676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3749.734654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.514654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.394656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3674.744709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.838983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.138983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.118983,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3696.879676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3692.179676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3717.559676,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.134654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.434654,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.274656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.338981,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.338981,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3666.918982,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.379674,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.379674,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.359675,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.634653,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.634653,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.074656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.044708,
      "body_overlap_mm3": 37.339728,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.684709,
      "body_overlap_mm3": 30.222461,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3863.404709,
      "body_overlap_mm3": 43.819847,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3839.464049,
      "body_overlap_mm3": 37.339728,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.10405,
      "body_overlap_mm3": 30.222461,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3882.10405,
      "body_overlap_mm3": 43.819847,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3855.826267,
      "body_overlap_mm3": 37.339728,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.466267,
      "body_overlap_mm3": 30.222461,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3908.866267,
      "body_overlap_mm3": 43.819847,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3874.070617,
      "body_overlap_mm3": 37.339728,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.710618,
      "body_overlap_mm3": 30.222461,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3936.47062,
      "body_overlap_mm3": 43.819847,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.844708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.924709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3794.764709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.264049,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3758.34405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3813.46405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3798.626267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.706267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3840.226267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.870617,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.950618,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.830619,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.844708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.324709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.364709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.264049,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3716.74405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.06405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.626267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.106267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3777.826267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3764.870617,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.350618,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3805.430619,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.244709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3682.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.66405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.46405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.14405,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.026267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3699.826267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.906267,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3723.270617,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.070618,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.510619,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.664048,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.664048,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3669.944049,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.026266,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.026266,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3696.706266,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.270617,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.270617,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.310619,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.044708,
      "body_overlap_mm3": 40.617724,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.284709,
      "body_overlap_mm3": 32.500458,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3883.804708,
      "body_overlap_mm3": 47.097898,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3859.265711,
      "body_overlap_mm3": 40.617724,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.435284,
      "body_overlap_mm3": 32.500458,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3906.005711,
      "body_overlap_mm3": 47.097898,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3879.630302,
      "body_overlap_mm3": 40.617724,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3840.699265,
      "body_overlap_mm3": 32.500458,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3937.770302,
      "body_overlap_mm3": 47.097898,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3901.476788,
      "body_overlap_mm3": 40.617724,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3862.455203,
      "body_overlap_mm3": 32.500458,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3969.87679,
      "body_overlap_mm3": 47.097898,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.344708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3756.124709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3808.564709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.565711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.275284,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3830.765711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.930302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3790.539265,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3862.530302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.776788,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3812.295203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3894.63679,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.344708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3710.524709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.164709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.565711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.675284,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.365711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.930302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.939265,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3794.130302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.776788,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.695203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.23679,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.744708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3674.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3693.965711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.195284,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.645711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3714.330302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.459265,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.410302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3736.176788,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.215203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3771.51679,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.46571,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.395283,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.44571,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.830301,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.659265,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.210301,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.676788,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.415202,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.31679,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3797.444708,
      "body_overlap_mm3": 32.610294,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.204709,
      "body_overlap_mm3": 26.493027,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.684709,
      "body_overlap_mm3": 38.347607,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.381221,
      "body_overlap_mm3": 32.610294,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3777.141221,
      "body_overlap_mm3": 26.493027,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.641221,
      "body_overlap_mm3": 38.347607,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.161837,
      "body_overlap_mm3": 32.610294,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3789.921837,
      "body_overlap_mm3": 26.493027,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3863.021837,
      "body_overlap_mm3": 38.347607,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3833.368201,
      "body_overlap_mm3": 32.610294,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.128201,
      "body_overlap_mm3": 26.493027,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3884.968203,
      "body_overlap_mm3": 38.347607,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.144708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.364709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3769.924709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.081221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.301221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3784.881221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3771.861837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3752.081837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.261837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.068201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.288201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.208203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.144709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.964709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.324709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3716.081221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.901221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.281221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.861837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3717.681837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.661837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3743.068201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3731.888201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3776.608203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.744709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3668.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3681.681221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.381221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3692.001221,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3694.461837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3690.161837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.381837,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.668201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.368201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.328203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.18122,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.18122,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3666.20122,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.961835,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.961835,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.581836,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.168201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.168201,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.528203,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3814.444708,
      "body_overlap_mm3": 36.61376,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.804709,
      "body_overlap_mm3": 29.496493,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3847.084709,
      "body_overlap_mm3": 42.351127,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3825.706288,
      "body_overlap_mm3": 36.61376,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3793.066288,
      "body_overlap_mm3": 29.496493,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3865.066288,
      "body_overlap_mm3": 42.351127,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.808428,
      "body_overlap_mm3": 36.61376,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3809.168428,
      "body_overlap_mm3": 29.496493,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3890.768428,
      "body_overlap_mm3": 42.351127,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3859.004165,
      "body_overlap_mm3": 36.61376,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.364165,
      "body_overlap_mm3": 29.496493,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3916.604167,
      "body_overlap_mm3": 42.351127,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3761.644708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.564709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3783.724709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3772.906288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.826288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.706288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3789.008428,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.928429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.408429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.204165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3784.124165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.244167,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.644708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.164709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3726.124709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.906288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.426288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.106288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.008428,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.528429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3769.808429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3758.204165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3745.724165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.644167,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.244709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.506288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3681.706288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.026288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3702.608428,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.808429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3723.728429,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.804165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.004165,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3749.564167,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.506287,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.506287,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3669.226287,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.608427,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.608427,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3694.928427,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.804164,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.804164,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.764166,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3831.444708,
      "body_overlap_mm3": 39.891756,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.404708,
      "body_overlap_mm3": 31.77449,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.484708,
      "body_overlap_mm3": 45.629188,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.507949,
      "body_overlap_mm3": 39.891756,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3809.397522,
      "body_overlap_mm3": 31.77449,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3888.967949,
      "body_overlap_mm3": 45.629188,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3865.612463,
      "body_overlap_mm3": 39.891756,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3829.401426,
      "body_overlap_mm3": 31.77449,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3919.672463,
      "body_overlap_mm3": 45.629188,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3886.410335,
      "body_overlap_mm3": 39.891756,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3850.10875,
      "body_overlap_mm3": 31.77449,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3950.010337,
      "body_overlap_mm3": 45.629188,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3773.144708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3748.764709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3797.524709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.207949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.757522,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.007949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3807.312463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.761426,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3849.712463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.110335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.46875,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3880.050337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.144708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.364709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.924709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3734.207949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.357522,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.407949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.312463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.361427,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.112463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.110335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3761.06875,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.450337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.744708,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.444709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.044709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3691.807949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.437522,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.527949,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3711.912463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.441427,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.232463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.710335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.14875,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3765.570337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.307948,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.237522,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.727948,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.412462,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.241426,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3703.432462,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.210335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.948749,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "negative_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.770337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.544713,
      "body_overlap_mm3": 33.24024,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3785.884713,
      "body_overlap_mm3": 27.24024,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.204713,
      "body_overlap_mm3": 40.185536,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.695802,
      "body_overlap_mm3": 33.24024,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.035802,
      "body_overlap_mm3": 27.24024,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3869.285802,
      "body_overlap_mm3": 40.185536,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.854444,
      "body_overlap_mm3": 33.24024,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3808.194444,
      "body_overlap_mm3": 27.24024,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3892.344444,
      "body_overlap_mm3": 40.185536,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3857.764809,
      "body_overlap_mm3": 33.24024,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3824.104809,
      "body_overlap_mm3": 27.24024,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3917.164811,
      "body_overlap_mm3": 40.185536,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3765.094713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3742.324713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.864713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.245802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.475802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.945802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.404444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3764.634444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.004444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.314809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 108.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3780.544809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 87.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3851.824811,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.594713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3702.724713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.464713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.745802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3711.875802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.545802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.904444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.034444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3767.604444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3753.814809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 64.35,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.944809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 51.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.424811,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.22,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.994713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3671.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.944713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.145802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.195802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.025802,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.304444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3693.354444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.084444,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3714.214809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 24.75,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.264809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.904811,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.7,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.395799,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.395799,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3667.3258,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.554442,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.554442,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3690.384443,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.464809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.464809,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.204811,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3836.544713,
      "body_overlap_mm3": 37.243539,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3799.484713,
      "body_overlap_mm3": 30.243539,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3873.604713,
      "body_overlap_mm3": 44.188909,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.020869,
      "body_overlap_mm3": 37.243539,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3810.960869,
      "body_overlap_mm3": 30.243539,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3892.710869,
      "body_overlap_mm3": 44.188909,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3864.501035,
      "body_overlap_mm3": 37.243539,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.441036,
      "body_overlap_mm3": 30.243539,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3920.091036,
      "body_overlap_mm3": 44.188909,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3883.400773,
      "body_overlap_mm3": 37.243539,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3846.340773,
      "body_overlap_mm3": 30.243539,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3948.800775,
      "body_overlap_mm3": 44.188909,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3776.594713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.524713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.664713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.070869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3763.000869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.770869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.551036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3779.481036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.151036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3823.450773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 119.800855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3798.380773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 95.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3876.860775,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 143.780855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3722.094713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.924713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3736.264713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.570869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.400869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.370869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.051036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.881036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.751036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.950773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 70.791414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.780773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 56.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3811.460775,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.961414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.494713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.944713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.970869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3684.520869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3703.050869,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.451036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.001036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.431036,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.350773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 27.227467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.900773,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.140775,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 32.677467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.720866,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.720866,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.350867,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.201034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.201034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.731034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.100772,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.100772,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3726.440774,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.544713,
      "body_overlap_mm3": 40.521457,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3813.084713,
      "body_overlap_mm3": 32.521457,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3894.004713,
      "body_overlap_mm3": 47.466913,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.82253,
      "body_overlap_mm3": 40.521457,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.292104,
      "body_overlap_mm3": 32.521457,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3916.61253,
      "body_overlap_mm3": 47.466913,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3888.30507,
      "body_overlap_mm3": 40.521457,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3847.674034,
      "body_overlap_mm3": 32.521457,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3948.99507,
      "body_overlap_mm3": 47.466913,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3910.806944,
      "body_overlap_mm3": 40.521457,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3870.085358,
      "body_overlap_mm3": 32.521457,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3982.206946,
      "body_overlap_mm3": 47.466913,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.094713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3760.724713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3815.464713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3802.37253,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.932104,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.072531,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3822.85507,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.314034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3870.45507,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.356944,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 130.410012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3817.725358,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 104.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3903.666946,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 156.590012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.594713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.124713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.064713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3742.87253,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.332104,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.672531,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3763.35507,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3747.714034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3799.055071,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3785.856944,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 77.060462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.125358,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3832.266946,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 92.530462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.994713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.944713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.27253,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.252104,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.552531,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.75507,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.634034,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.935071,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3738.256944,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 29.638639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.045358,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.146946,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 35.588639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.522528,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.452102,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.852528,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.005069,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.834033,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.235069,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.506943,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.245358,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.55,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.446945,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3811.044713,
      "body_overlap_mm3": 32.842752,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3779.084713,
      "body_overlap_mm3": 26.842752,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3843.004713,
      "body_overlap_mm3": 39.323782,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.138987,
      "body_overlap_mm3": 32.842752,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3788.178987,
      "body_overlap_mm3": 26.842752,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3858.678987,
      "body_overlap_mm3": 39.323782,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3833.17971,
      "body_overlap_mm3": 32.842752,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.21971,
      "body_overlap_mm3": 26.842752,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3881.11971,
      "body_overlap_mm3": 39.323782,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3848.434692,
      "body_overlap_mm3": 32.842752,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.474692,
      "body_overlap_mm3": 26.842752,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3904.834694,
      "body_overlap_mm3": 39.323782,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.344713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.724713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3780.964713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.438987,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.818987,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.638987,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.47971,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.859711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.079711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.734692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 103.4,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.114692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3842.794694,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.344713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3700.124713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.564713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3721.438987,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.218988,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.238988,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3734.47971,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3722.259711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.679711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3749.734692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 61.1,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.514692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 48.88,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.394694,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3674.744713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.838987,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.138988,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.118988,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3696.87971,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3692.179711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3717.559711,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.134692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.434692,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 18.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.274694,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.338985,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.338985,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3666.918985,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.379709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.379709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3689.359709,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.634691,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.634691,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.074693,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.044713,
      "body_overlap_mm3": 36.846051,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.684713,
      "body_overlap_mm3": 29.846051,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3863.404713,
      "body_overlap_mm3": 43.327155,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3839.464054,
      "body_overlap_mm3": 36.846051,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.104055,
      "body_overlap_mm3": 29.846051,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3882.104055,
      "body_overlap_mm3": 43.327155,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3855.826302,
      "body_overlap_mm3": 36.846051,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.466302,
      "body_overlap_mm3": 29.846051,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3908.866302,
      "body_overlap_mm3": 43.327155,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3874.070656,
      "body_overlap_mm3": 36.846051,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.710656,
      "body_overlap_mm3": 29.846051,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3936.470658,
      "body_overlap_mm3": 43.327155,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.844713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.924713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3794.764713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.264054,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3758.344055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3813.464055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3798.626302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3774.706302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3840.226302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.870656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 114.300855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3792.950656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 91.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.830658,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 137.180855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.844713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.324713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.364713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.264054,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3716.744055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.064055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3746.626302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.106302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3777.826302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3764.870656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.541414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3751.350656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 54.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3805.430658,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 81.061414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.244713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3682.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.664055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.464055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.144055,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.026302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3699.826302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.906302,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3723.270656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.070656,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 20.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.510658,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.177467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.664052,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.664052,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3669.944052,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.026301,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.026301,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3696.706301,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.270655,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.270655,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.310657,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.044713,
      "body_overlap_mm3": 40.123969,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.284713,
      "body_overlap_mm3": 32.12397,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3883.804713,
      "body_overlap_mm3": 46.605158,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3859.265716,
      "body_overlap_mm3": 40.123969,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3820.435289,
      "body_overlap_mm3": 32.12397,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3906.005716,
      "body_overlap_mm3": 46.605158,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3879.630337,
      "body_overlap_mm3": 40.123969,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3840.6993,
      "body_overlap_mm3": 32.12397,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3937.770337,
      "body_overlap_mm3": 46.605158,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3901.476826,
      "body_overlap_mm3": 40.123969,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3862.455241,
      "body_overlap_mm3": 32.12397,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3969.876828,
      "body_overlap_mm3": 46.605158,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.344713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3756.124713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3808.564713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3796.565716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3770.275289,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3830.765716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.930337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3790.5393,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3862.530337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3838.776826,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 124.910012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3812.295241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 100.32,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3894.636828,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 149.990012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3725.344713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3710.524713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.164713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.565716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.675289,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.365716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.930337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.9393,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3794.130337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.776826,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 73.810462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.695241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 59.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.236828,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 88.630462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3679.744713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3674.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3693.965716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3688.195289,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.645716,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3714.330337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.4593,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.410337,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3736.176826,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.215241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 22.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3771.516828,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 34.088639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.465713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.395288,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3673.445713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.830335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.659299,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.210335,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.676826,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.415241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        8.8,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3737.316828,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3797.444713,
      "body_overlap_mm3": 32.139793,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3768.204713,
      "body_overlap_mm3": 26.139793,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.684713,
      "body_overlap_mm3": 37.878134,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.381225,
      "body_overlap_mm3": 32.139793,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3777.141226,
      "body_overlap_mm3": 26.139793,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.641226,
      "body_overlap_mm3": 37.878134,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.161874,
      "body_overlap_mm3": 32.139793,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3789.921874,
      "body_overlap_mm3": 26.139793,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3863.021874,
      "body_overlap_mm3": 37.878134,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3833.368242,
      "body_overlap_mm3": 32.139793,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3804.128242,
      "body_overlap_mm3": 26.139793,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3884.968244,
      "body_overlap_mm3": 37.878134,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.144713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3730.364713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3769.924713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3759.081226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.301226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3784.881226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3771.861874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3752.081874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.261874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.068242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 94.6,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.288242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 75.68,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.208244,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 113.52,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3707.144713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.964713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3718.324713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3716.081226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.901226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.281226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.861874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3717.681874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.661874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3743.068242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.9,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3731.888242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 44.72,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3776.608244,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 67.08,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.744713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3668.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3681.681226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.381226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3692.001226,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3694.461874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3690.161874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.381874,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3708.668242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.5,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.368242,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 17.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.328244,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 25.8,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.181223,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3660.181223,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3666.201223,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.961872,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.961872,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.581873,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.168241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3687.168241,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        13.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3709.528243,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3814.444713,
      "body_overlap_mm3": 36.143092,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3781.804713,
      "body_overlap_mm3": 29.143092,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3847.084713,
      "body_overlap_mm3": 41.881521,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3825.706293,
      "body_overlap_mm3": 36.143092,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3793.066293,
      "body_overlap_mm3": 29.143092,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3865.066293,
      "body_overlap_mm3": 41.881521,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3841.808465,
      "body_overlap_mm3": 36.143092,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3809.168466,
      "body_overlap_mm3": 29.143092,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3890.768466,
      "body_overlap_mm3": 41.881521,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3859.004205,
      "body_overlap_mm3": 36.143092,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3826.364206,
      "body_overlap_mm3": 29.143092,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3916.604207,
      "body_overlap_mm3": 41.881521,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3761.644713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3739.564713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3783.724713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3772.906293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3750.826293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3801.706293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3789.008466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3766.928466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3827.408466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3806.204205,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 105.500855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3784.124206,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 84.48,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3853.244207,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 126.620855,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3713.644713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3701.164713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3726.124713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3724.906293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3712.426293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3744.106293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3741.008466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3728.528466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3769.808466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3758.204205,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 62.341414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3745.724206,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 49.92,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.644207,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 74.821414,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3675.244713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3670.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3680.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.506293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3681.706293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3698.026293,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3702.608466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3697.808466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3723.728466,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3719.804205,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 23.977467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3715.004206,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 19.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3749.564207,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 28.777467,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.50629,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3662.50629,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3669.22629,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.608464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3678.608464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3694.928464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.804205,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3695.804205,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.0
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.764207,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3831.444713,
      "body_overlap_mm3": 39.42101,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3795.404713,
      "body_overlap_mm3": 31.42101,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3867.484713,
      "body_overlap_mm3": 45.15954,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3845.507954,
      "body_overlap_mm3": 39.42101,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3809.397527,
      "body_overlap_mm3": 31.42101,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3888.967954,
      "body_overlap_mm3": 45.15954,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3865.6125,
      "body_overlap_mm3": 39.42101,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3829.401464,
      "body_overlap_mm3": 31.42101,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3919.6725,
      "body_overlap_mm3": 45.15954,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3886.410376,
      "body_overlap_mm3": 39.42101,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3850.108791,
      "body_overlap_mm3": 31.42101,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        14.9,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3950.010378,
      "body_overlap_mm3": 45.15954,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3773.144713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3748.764713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3797.524713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3787.207954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3762.757527,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3819.007954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3807.3125,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3782.761464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3849.7125,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3828.110376,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 116.110012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3803.468791,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 93.28,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        16.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3880.050378,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 139.430012,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.144713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.364713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.924713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3734.207954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3720.357528,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3755.407954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3754.3125,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3740.361464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3786.112501,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3775.110376,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 68.610462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3761.068791,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 55.12,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.0,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3816.450378,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 82.390462,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3677.744713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.444713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        18.3
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3683.044713,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3691.807954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3686.437528,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3704.527954,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3711.9125,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.441464,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3735.232501,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3732.710376,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 26.388639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3727.148791,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 21.2,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        17.8,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3765.570378,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 31.688639,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.307951,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3665.237526,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        19.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3672.727952,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.412499,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3685.241463,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.0
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3703.432499,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3706.210376,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        29.0,
        37.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3705.94879,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    },
    {
      "side": "positive_y",
      "x_range_mm": [
        27.0,
        39.0
      ],
      "abs_y_range_mm": [
        9.2,
        14.5
      ],
      "z_range_mm": [
        18.3,
        20.9
      ],
      "valid": true,
      "solid_count": 2,
      "volume_mm3": 3733.770378,
      "body_overlap_mm3": 0.0,
      "shutter_overlap_mm3": 0.0,
      "fixed_overlap_mm3": {
        "encoder_button": 0.0,
        "encoder_dial": 0.0,
        "encoder_bracket": 0.0
      },
      "bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.0,
        14.95,
        20.9
      ],
      "inside_original_cover_bbox": true,
      "passes_geometric_screen": false
    }
  ],
  "limitations": [
    "The translated shutter solid is a static placement probe, not a validated dynamic swept envelope.",
    "A bridge passing B-rep checks is not proof of adequate wall thickness, strength, fatigue life, or printability.",
    "The bridge boxes are deliberately simple search primitives, not finished filleted ribs.",
    "No fastener, insert, gasket, assembly path, or manufacturing tolerance is validated.",
    "The original cover/body mating faces are not intentionally cut; body collision is a hard rejection."
  ]
}
```
