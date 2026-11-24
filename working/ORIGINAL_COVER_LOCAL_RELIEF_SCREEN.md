# 原始盖体局部避让候选筛查

- 生成时间 UTC：2026-11-24T15:54:28.910558+00:00
- 原始 STEP 只读；只对原盖体副本执行切除。
- 原始盖体与 +X 10 mm 快门输入件交叠：186.323214 mm³。
- 候选：按 0、0.2、0.3、0.5、0.8 mm 余量构造快门件 B-rep 偏置切刀。
- 本轮不导出 STEP；先验证偏置内核、实体有效性、主体界面及冻结编码器避让。

|目标余量 mm|状态|有效/实体数|去除盖体体积 mm³|剩余盖体-快门交叠 mm³|切刀-主体交叠 mm³|候选-主体间距 mm|几何筛查|
|---:|---|---|---:|---:|---:|---:|---|
|0.0|screened|True/2|186.323393|0.0|0.0|0.0|未通过/待复核|
|0.2|failed|False/-|-|-|-|-|未通过/待复核|

- 0.2 mm 失败原因：AttributeError: 'Solid' object has no attribute 'offset3D'
|0.3|failed|False/-|-|-|-|-|未通过/待复核|

- 0.3 mm 失败原因：AttributeError: 'Solid' object has no attribute 'offset3D'
|0.5|failed|False/-|-|-|-|-|未通过/待复核|

- 0.5 mm 失败原因：AttributeError: 'Solid' object has no attribute 'offset3D'
|0.8|failed|False/-|-|-|-|-|未通过/待复核|

- 0.8 mm 失败原因：AttributeError: 'Solid' object has no attribute 'offset3D'

## 完整机器结果

~~~json
{
  "generated_utc": "2026-11-24T15:54:28.910558+00:00",
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "base_cover_shutter_overlap_mm3": 186.323214,
  "method": "Subtract the translated shutter-input B-rep or its 3D offset from a copy of the original cover; do not alter the body or frozen parts.",
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
      "candidate_valid": true,
      "candidate_solid_count": 2,
      "candidate_volume_mm3": 3651.244703,
      "removed_cover_volume_mm3": 186.323393,
      "remaining_cover_vs_moving": 0.0,
      "candidate_vs_body_distance_mm": 0.0,
      "candidate_bbox_mm": [
        -19.5,
        -14.95,
        14.9,
        37.0626,
        14.95,
        20.9
      ],
      "cutter_body_overlap_mm3": 0.0,
      "fixed_checks": {
        "body": {
          "overlap_mm3": 0.0,
          "distance_mm": 0.0
        },
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
      "status": "failed",
      "error": "AttributeError: 'Solid' object has no attribute 'offset3D'"
    },
    {
      "clearance_mm": 0.3,
      "status": "failed",
      "error": "AttributeError: 'Solid' object has no attribute 'offset3D'"
    },
    {
      "clearance_mm": 0.5,
      "status": "failed",
      "error": "AttributeError: 'Solid' object has no attribute 'offset3D'"
    },
    {
      "clearance_mm": 0.8,
      "status": "failed",
      "error": "AttributeError: 'Solid' object has no attribute 'offset3D'"
    }
  ],
  "limitations": [
    "This is a local-relief geometry screen, not a production cover design.",
    "The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.",
    "Offset failures are reported and are not replaced by guessed box cuts.",
    "A valid single solid does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.",
    "The cover/body mating interface must be reviewed separately; the body is never modified.",
    "No STEP candidate is exported at this stage."
  ]
}
~~~

## 设计判断规则

- 若偏置切刀与主体相交，该余量候选不接受，避免把原盖体/主体配合面误切掉。
- 若偏置后盖体分裂、无效或仍与快门件交叠，不进入 STEP 导出。
- 若所有余量均失败，下一步改为基于盖体面拓扑设计局部开口/分型，而不是扩大盲目切除。
- 即使几何筛查通过，仍需人工确认最小壁厚、外观连续性、定位、紧固和拆装方向。

## 限制

- This is a local-relief geometry screen, not a production cover design.
- The cutter follows the translated shutter-input solid; it is not a validated dynamic swept envelope.
- Offset failures are reported and are not replaced by guessed box cuts.
- A valid single solid does not establish adequate wall thickness, stiffness, fastener layout, assembly access, or printability.
- The cover/body mating interface must be reviewed separately; the body is never modified.
- No STEP candidate is exported at this stage.
