# 原始盖体局部避让候选筛查

- 生成时间 UTC：2026-11-24T16:11:33.054125+00:00
- 原始 STEP 只读；仅对原盖体副本执行切除。
- 原始盖体与 +X 10 mm 快门输入件交叠：186.323214 mm³。
- 偏置方法：OpenCascade BRepOffsetAPI_MakeOffsetShape 正向三维偏置。
- 候选余量：0、0.2、0.3、0.5、0.8 mm；本轮不导出 STEP。

|余量 mm|状态|切刀实体数|切刀-主体交叠 mm³|去除盖体 mm³|剩余交叠 mm³|盖体实体数|候选-主体间距 mm|几何初筛|
|---:|---|---:|---:|---:|---:|---:|---:|---|
|0.0|screened|1|0.0|186.323393|0.0|2|0.0|未通过/待复核|
|0.2|screened|1|0.0|-585.588424|0.0|2|0.0|未通过/待复核|
|0.3|failed|1|16.472146|-|-|-|-|未通过/待复核|

- 0.3 mm 失败原因：StdFail_NotDone: 
|0.5|failed|1|52.796693|-|-|-|-|未通过/待复核|

- 0.5 mm 失败原因：StdFail_NotDone: 
|0.8|failed|1|114.286303|-|-|-|-|未通过/待复核|

- 0.8 mm 失败原因：StdFail_NotDone: 

## 完整机器结果

~~~json
{
  "generated_utc": "2026-11-24T16:11:33.054125+00:00",
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "base_cover_shutter_overlap_mm3": 186.323214,
  "method": "OpenCascade BRepOffsetAPI_MakeOffsetShape positive 3D offset; subtract only from a copy of the original cover.",
  "offset_tolerance_mm": 0.001,
  "candidate_clearances_mm": [
    0.0,
    0.2,
    0.3,
    0.5,
    0.8
  ],
  "rows": [
    {
      "clearance_mm": 0.0,
      "status": "screened",
      "cutter_valid": true,
      "cutter_solid_count": 1,
      "cutter_volume_mm3": 2270.227233,
      "cutter_body_overlap_mm3": 0.0,
      "candidate_valid": true,
      "candidate_solid_count": 2,
      "candidate_volume_mm3": 3651.244703,
      "removed_cover_volume_mm3": 186.323393,
      "remaining_cover_vs_moving_mm3": 0.0,
      "remaining_cover_vs_cutter_mm3": 0.0,
      "candidate_vs_body_distance_mm": 0.0,
      "candidate_bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "fixed_checks": {
        "encoder_button": {
          "overlap_mm3": 0.0,
          "distance_mm": 17.6
        },
        "encoder_dial": {
          "overlap_mm3": 0.0,
          "distance_mm": 15.1
        },
        "encoder_bracket": {
          "overlap_mm3": 0.0,
          "distance_mm": 7.4
        }
      },
      "geometrically_valid_candidate": false
    },
    {
      "clearance_mm": 0.2,
      "status": "screened",
      "cutter_valid": true,
      "cutter_solid_count": 1,
      "cutter_volume_mm3": 2680.488528,
      "cutter_body_overlap_mm3": 0.0,
      "candidate_valid": false,
      "candidate_solid_count": 2,
      "candidate_volume_mm3": 3206.089912,
      "removed_cover_volume_mm3": -585.588424,
      "remaining_cover_vs_moving_mm3": 0.0,
      "remaining_cover_vs_cutter_mm3": 0.0,
      "candidate_vs_body_distance_mm": 0.0,
      "candidate_bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        39.45,
        14.95,
        20.9
      ],
      "fixed_checks": {
        "encoder_button": {
          "overlap_mm3": 0.0,
          "distance_mm": 17.6
        },
        "encoder_dial": {
          "overlap_mm3": 0.0,
          "distance_mm": 15.1
        },
        "encoder_bracket": {
          "overlap_mm3": 0.0,
          "distance_mm": 7.4
        }
      },
      "geometrically_valid_candidate": false
    },
    {
      "clearance_mm": 0.3,
      "status": "failed",
      "cutter_valid": true,
      "cutter_solid_count": 1,
      "cutter_volume_mm3": 2890.16565,
      "cutter_body_overlap_mm3": 16.472146,
      "error": "StdFail_NotDone: "
    },
    {
      "clearance_mm": 0.5,
      "status": "failed",
      "cutter_valid": true,
      "cutter_solid_count": 1,
      "cutter_volume_mm3": 3318.77851,
      "cutter_body_overlap_mm3": 52.796693,
      "error": "StdFail_NotDone: "
    },
    {
      "clearance_mm": 0.8,
      "status": "failed",
      "cutter_valid": true,
      "cutter_solid_count": 1,
      "cutter_volume_mm3": 3985.341322,
      "cutter_body_overlap_mm3": 114.286303,
      "error": "StdFail_NotDone: "
    }
  ],
  "limitations": [
    "This is a local-relief geometry screen, not a production cover design.",
    "The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.",
    "Offset success does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.",
    "The cover/body mating interface must be reviewed separately; the body is never modified.",
    "A split cover candidate is rejected even if each resulting solid is individually valid.",
    "No STEP candidate is exported at this stage."
  ]
}
~~~

## 接受条件

- 偏置切刀必须是有效单一实体。
- 切后盖体必须保持单一有效实体，且与快门输入件无残余交叠。
- 切刀不得侵入机身主体；盖体与主体的原始配合关系仍需人工审查。
- 不满足任一条件的候选均不导出 STEP。

## 限制

- This is a local-relief geometry screen, not a production cover design.
- The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.
- Offset success does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.
- The cover/body mating interface must be reviewed separately; the body is never modified.
- A split cover candidate is rejected even if each resulting solid is individually valid.
- No STEP candidate is exported at this stage.
