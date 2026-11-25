# 盖体局部避让布尔与拓扑诊断

- 生成时间 UTC：2026-11-25T00:15:00.427085+00:00
- 原始 STEP 只读；仅对盖体副本执行布尔诊断。
- 目标：检查 0 / 0.2 mm 两个失败候选的体积守恒、实体碎片和空间位置。
- 快门输入件仅作 +X 10 mm 静态包络，不代表动态扫掠体。

|余量 mm|状态|原盖体体积|交叠体积|切后体积|碎片体积和|体积守恒误差|碎片数|新增几何体积|
|---:|---|---:|---:|---:|---:|---:|---:|---:|
|0.0|diagnosed|3837.568095|186.323214|3651.244709|3651.244701|0.00018|2|0.0|
  - 碎片 0: 体积 3636.864858 mm³，质心 [3.44278, -0.0, 19.38206] mm，包围盒 [-19.5, -14.95, 14.9, 37.06263, 14.95, 20.9]，面数 40，有效=True
  - 碎片 1: 体积 14.379843 mm³，质心 [34.49869, -0.0, 19.19876] mm，包围盒 [33.5, -2.0, 18.3, 35.5, 2.0, 20.1]，面数 7，有效=True
  - 碎片 0–1 最小距离：6.263932 mm
|0.2|diagnosed|3837.568095|223.298909|3614.268983|3614.268979|0.000207|2|0.0|
  - 碎片 0: 体积 3605.052979 mm³，质心 [3.21183, -0.0, 19.38872] mm，包围盒 [-19.5, -14.95, 14.9, 36.89063, 14.95, 20.9]，面数 70，有效=True
  - 碎片 1: 体积 9.216 mm³，质心 [34.5, -0.0, 19.1] mm，包围盒 [33.7, -1.8, 18.3, 35.3, 1.8, 19.9]，面数 6，有效=True
  - 碎片 0–1 最小距离：6.730228 mm

## 机器可读结果

~~~json
{
  "generated_utc": "2026-11-25T00:15:00.427085+00:00",
  "source": "source/leica_m3_light_meter.stp (read-only)",
  "cover_solid_index": 4,
  "moving_shutter_solid_index": 3,
  "moving_shutter_translation_mm": [
    10,
    0,
    0
  ],
  "purpose": "Diagnose rejected boolean relief candidates; not a design approval.",
  "results": [
    {
      "clearance_mm": 0.0,
      "original_cover_volume_mm3": 3837.568095,
      "cutter_valid": true,
      "cutter_volume_mm3": 2270.227233,
      "cover_cutter_intersection_volume_mm3": 186.323214,
      "cut_shape_type": "Compound",
      "cut_valid": true,
      "cut_reported_volume_mm3": 3651.244709,
      "component_volume_sum_mm3": 3651.244701,
      "volume_conservation_error_mm3": 0.00018,
      "components": [
        {
          "index": 0,
          "volume_mm3": 3636.864858,
          "area_mm2": 3386.494527,
          "bbox_mm": [
            -19.5,
            -14.95,
            14.9,
            37.06263,
            14.95,
            20.9
          ],
          "center_of_mass_mm": [
            3.44278,
            -0.0,
            19.38206
          ],
          "face_count": 40,
          "shell_count": 1,
          "valid": true
        },
        {
          "index": 1,
          "volume_mm3": 14.379843,
          "area_mm2": 37.405336,
          "bbox_mm": [
            33.5,
            -2.0,
            18.3,
            35.5,
            2.0,
            20.1
          ],
          "center_of_mass_mm": [
            34.49869,
            -0.0,
            19.19876
          ],
          "face_count": 7,
          "shell_count": 1,
          "valid": true
        }
      ],
      "pairwise_component_clearances_mm": [
        {
          "a": 0,
          "b": 1,
          "distance_mm": 6.263932
        }
      ],
      "remaining_vs_moving_overlap_mm3": 0.0,
      "cut_vs_original_common_volume_mm3": 3651.244709,
      "lost_cover_volume_mm3": 186.323214,
      "added_geometry_volume_mm3": 0.0,
      "lost_region_bbox_mm": [
        29.672,
        -8.5,
        18.3,
        39.45,
        8.5,
        20.9
      ],
      "added_region_bbox_mm": null,
      "status": "diagnosed"
    },
    {
      "clearance_mm": 0.2,
      "original_cover_volume_mm3": 3837.568095,
      "cutter_valid": true,
      "cutter_volume_mm3": 2680.488528,
      "cover_cutter_intersection_volume_mm3": 223.298909,
      "cut_shape_type": "Compound",
      "cut_valid": true,
      "cut_reported_volume_mm3": 3614.268983,
      "component_volume_sum_mm3": 3614.268979,
      "volume_conservation_error_mm3": 0.000207,
      "components": [
        {
          "index": 0,
          "volume_mm3": 3605.052979,
          "area_mm2": 3370.038957,
          "bbox_mm": [
            -19.5,
            -14.95,
            14.9,
            36.89063,
            14.95,
            20.9
          ],
          "center_of_mass_mm": [
            3.21183,
            -0.0,
            19.38872
          ],
          "face_count": 70,
          "shell_count": 1,
          "valid": true
        },
        {
          "index": 1,
          "volume_mm3": 9.216,
          "area_mm2": 28.16,
          "bbox_mm": [
            33.7,
            -1.8,
            18.3,
            35.3,
            1.8,
            19.9
          ],
          "center_of_mass_mm": [
            34.5,
            -0.0,
            19.1
          ],
          "face_count": 6,
          "shell_count": 1,
          "valid": true
        }
      ],
      "pairwise_component_clearances_mm": [
        {
          "a": 0,
          "b": 1,
          "distance_mm": 6.730228
        }
      ],
      "remaining_vs_moving_overlap_mm3": 0.0,
      "cut_vs_original_common_volume_mm3": 3614.268983,
      "lost_cover_volume_mm3": 223.298909,
      "added_geometry_volume_mm3": 0.0,
      "lost_region_bbox_mm": [
        20.88953,
        -14.63492,
        18.3,
        39.45,
        14.63492,
        20.9
      ],
      "added_region_bbox_mm": null,
      "status": "diagnosed"
    }
  ],
  "interpretation_limits": [
    "Component separation is a topological result, not proof that a split cover is mechanically unusable.",
    "A zero-distance component pair can indicate touching faces/edges; it is not a robust structural bridge.",
    "Volume conservation and symmetric-difference checks are required to detect malformed boolean output.",
    "The cutter is a translated static shutter solid, not a validated dynamic swept envelope.",
    "No cover/body fit, wall thickness, fasteners, assembly sequence, printability, or dynamic mechanism is approved.",
    "No source geometry is modified and no STEP candidate is exported."
  ]
}
~~~

## 解释边界

- Component separation is a topological result, not proof that a split cover is mechanically unusable.
- A zero-distance component pair can indicate touching faces/edges; it is not a robust structural bridge.
- Volume conservation and symmetric-difference checks are required to detect malformed boolean output.
- The cutter is a translated static shutter solid, not a validated dynamic swept envelope.
- No cover/body fit, wall thickness, fasteners, assembly sequence, printability, or dynamic mechanism is approved.
- No source geometry is modified and no STEP candidate is exported.
