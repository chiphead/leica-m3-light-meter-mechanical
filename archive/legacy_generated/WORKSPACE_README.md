# Mechanical design workspace

This directory contains the independent mechanical-design work for the Leica M3 light meter. It is intentionally isolated from firmware, UI assets, existing documentation, and build scripts.

## Scope

- Parametric mechanical architecture and component interfaces
- Display / USB-C positioning references
- TSL2591 optical mounting concept
- AS5600 and magnet alignment
- Bottom rotary linkage assembly
- Cold-shoe mounting and passive heat-spreading concept
- Top encoder with an independent center button
- Enclosure and assembly constraints

## Status

This is a **mechanical architecture and parameter baseline**, not a released printable enclosure. Provisional dimensions are explicitly marked. Replace them with measurements from the actual modules before manufacturing.

## Files

- [V0.6 mechanical architecture](V0.6_MECHANICAL_ARCHITECTURE.md)
- [V0.6 parameter baseline](V0.6_PARAMETERS.json)
- [V0.6 CAD build instructions](V0.6_CAD_README.md)
- [FreeCAD reference-model macro](build_v06_reference.FCMacro)
- [V0.7 sensor CAD instructions](V0.7_SENSOR_CAD_README.md)
- [TSL2591 / chip-down AS5600 reference macro](build_v07_sensor_reference.FCMacro)

No existing project files are modified by this directory.

- [V0.8 optical test coupons](V0.8_OPTICAL_TEST_README.md)
- [TSL2591 optical reference review](OPTICAL_REFERENCE_REVIEW.md)
- [V0.8 FreeCAD optical coupon macro](build_v08_optical_test_coupons.FCMacro)
- [V0.9 bottom stepped rotor CAD instructions](V0.9_BOTTOM_ROTOR_CAD_README.md)
- [V0.9 bottom stepped rotor FreeCAD macro](build_v09_bottom_rotor_reference.FCMacro)
- [V1.0 dual-thrust rotor design notes](V1.0_DUAL_THRUST_ROTOR_README.md)
- [V1.0 dual-thrust rotor FreeCAD macro](build_v10_dual_thrust_bottom_rotor.FCMacro)
- [V1.1 top encoder and independent button notes](V1.1_TOP_ENCODER_BUTTON_README.md)
- [V1.1 top encoder and independent button FreeCAD macro](build_v11_top_encoder_independent_button.FCMacro)
- [V1.2 E8H8 horizontal encoder and wheel design](V1.2_E8H8_ENCODER_WHEEL_README.md)
- [V1.2 E8H8 horizontal encoder FreeCAD macro](build_v12_e8h8_horizontal_encoder_wheel.FCMacro)
- [V1.3 E8H7 integrated reference stack](V1.3_E8H7_INTEGRATED_REFERENCE_STACK_README.md)
- [V1.3 E8H7 integrated reference stack FreeCAD macro](build_v13_e8h7_integrated_reference_stack.FCMacro)

- [V1.4 E8H7 integrated assembly with dual-thrust bottom rotor](V1.4_E8H7_DUAL_THRUST_INTEGRATED_ASSEMBLY_README.md)
- [V1.4 FreeCAD macro](build_v14_e8h7_dual_thrust_integrated_assembly.FCMacro)

- [V1.5 E8H7 axial endplay assembly](V1.5_E8H7_AXIAL_ENDPLAY_ASSEMBLY_README.md)
- [V1.5 FreeCAD macro](build_v15_e8h7_axial_endplay_assembly.FCMacro)

- [V1.6 E8H7 retainer seat and upper-washer locating recess](V1.6_E8H7_RETAINER_SEAT_ASSEMBLY_README.md)
- [V1.6 FreeCAD macro](build_v16_e8h7_retainer_seat_assembly.FCMacro)

- [V1.7 E8H7 keyed thrust-washer assembly](V1.7_E8H7_KEYED_WASHER_ASSEMBLY_README.md)
- [V1.7 FreeCAD macro](build_v17_e8h7_keyed_washer_assembly.FCMacro)

- [V1.8 V1.7 keyed-washer manufacturability review](V1.8_V17_KEYED_WASHER_MANUFACTURABILITY_REVIEW.md)

- [V1.9 E8H7 retainer fastener and linkage envelope study](V1.9_E8H7_RETainer_FASTENER_STUDY_README.md)
- [V1.9 FreeCAD macro](build_v19_e8h7_retainer_fastener_study.FCMacro)

- [V2.0 full internal layout study](V2.0_FULL_INTERNAL_LAYOUT_README.md)
- [V2.0 FreeCAD macro](build_v20_full_internal_layout.FCMacro)

- [V2.1 display / USB-C interface constraint audit](V2.1_DISPLAY_USB_INTERFACE_AUDIT.md)

- [V2.2 display placement and vertical-stack study](V2.2_DISPLAY_PLACEMENT_STACK_STUDY.md)

- [V2.3 display placement collision audit](V2.3_DISPLAY_PLACEMENT_COLLISION_AUDIT.md)

- [V2.4 collision-aware XY packaging study (functional layout preserved; enclosure volume may grow)](V2.4_COLLISION_AWARE_XY_PACKAGING_STUDY.md)

- `V2.5_FUNCTIONAL_LAYOUT_INTEGRITY_REVIEW.md` — functional layout constraints, V2.0 source audit, and next component-envelope/Z-stack work; enclosure volume is allowed to grow.

- `V2.6_GLOBAL_Z_STACK_ARITHMETIC_AUDIT.md` — evaluates V2.0 rotor/floor Z equations against the V0.6 LCD glass datum; identifies the 0.3 mm floor overlap and unresolved component measurements.

- [V2.7 parameter provenance and deprecation audit](V2.7_PARAMETER_PROVENANCE_AND_DEPRECATION_AUDIT.md) — traces dimensions and assumptions from V0.6 to V2.0, identifies superseded rotor/encoder geometry, and defines the measurement priorities for V2.8.


- [V2.9 functional layout STEP preview](V2.9_FUNCTIONAL_LAYOUT_STEP_PREVIEW.md) — retained as a historical, rejected preview; its E8H7 axis/wheel plane and TSL2591 Z placement were incorrect. Do not use it as a layout baseline.
- [V3.1 AS5600 exposed upper-right rotor layout correction](V3.1_AS5600_EXPOSED_UPPER_RIGHT_ROTOR_LAYOUT_CORRECTION.md) — records the user-clarified horizontal AS5600-linked rotor disc at the upper-right exterior edge; supersedes the incorrect V3.0 mechanism identification and placement interpretation.\n- [V3.2 local-to-global rotor placement contract](V3.2_LOCAL_TO_GLOBAL_ROTOR_PLACEMENT_CONTRACT.md) — separates the local one-piece rotor mechanism from the enclosure coordinate frame; defines required global placement, edge-overhang and finger-access inputs without inventing coordinates.
- [V2.9 CadQuery STEP generator](generate_v2_9_functional_layout_preview.py) — regenerates the conceptual STEP and STL previews; not a released enclosure or fit-validated CAD.

- [V2.8 physical measurement protocol and datum register](V2.8_PHYSICAL_MEASUREMENT_PROTOCOL_AND_DATUM_REGISTER.md) — provides repeatable measurement procedures, exact reference-face definitions, blank records for LCD/USB-C, E8H7, AS5600/magnet, TSL2591 and rotor interfaces, plus gates for rebuilding the global Z stack.
