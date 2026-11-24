# Optical reference and design review — TSL2591

Status: research and prototype guidance. No dimensions here are released for manufacturing.

## Primary reference: Curious Scientist photographic light meter

Project: https://www.pcbway.com/project/shareproject/Light_meter_for_analog_cameras_%5BCH32V006F8P6_TSL2591%5D_7560e041.html  
Author article: https://curiousscientist.tech/blog/light-meter-for-analogue-cameras  
License shown on the project page: CC BY-SA.

The project uses the same TSL2591 sensor in a photographic light meter and publishes FrontBody.3mf, RearBody.3mf and RearBody_BuiltInMount.3mf. Its description states that the front shell seats the PCB, a recessed hole is in front of the TSL2591, the rear shell closes with screws into heat-set inserts, and the sensor is centered and aligned with the optics.

This is the strongest direct mechanical reference found so far. The published description does not specify a calibrated field-of-view angle or a long internal baffle. Treat the recessed opening as the primary reference concept; do not claim the project validates a deep tunnel. The original 3MF geometry has not yet been imported and measured, so no dimensions here should be represented as copied from it.

## Secondary references

### FreeDSM / SQMeter
FreeDSM project: https://gitlab.citic.udc.es/lia2-publico/g4s  
SQMeter enclosure notes: https://sqmeter.dev/hardware/enclosure/

These are TSL2591 sky-photometer projects. They are useful for sensor protection, cleaning access and weather-resistant packaging. Their sky-facing angular response is not necessarily suitable for a camera reflective meter.

### addrummond/mlm
Repository: https://github.com/addrummond/mlm

A photographic reflective meter using a different ambient-light sensor. Useful construction observations include light-tight printed walls, attention to internal finish and a separate sensor window. Its acrylic window must not be assumed suitable for TSL2591 visible/IR spectral response.

## Sensor-specific optical caution

The TSL2591 has full-spectrum and IR channels. Their angular responses are not identical. A baffle or recess can therefore change not only total signal but also the channel ratio used by the metering algorithm. Validate raw channel readings independently.

A black-looking printed surface is not automatically low-reflectance in near-IR. A visually clear window is not automatically transparent across both sensor response bands. Prefer an open aperture for the first prototype unless physical protection is necessary. If a window is added, obtain spectral transmission data and calibrate with that exact window installed.

## V0.8 test coupons

build_v08_optical_test_coupons.FCMacro creates three independent comparison coupons:
- **A — flush aperture:** 4 x 4 mm through-hole, no recess or rear sleeve.
- **B — front counterbore:** 7 x 7 mm recess, 1.5 mm deep from the incident-light face, stepping down to the common 4 x 4 mm through-hole.
- **C — rear baffle:** hollow sleeve extending 4 mm from the sensor side of the plate toward the sensor.

The coordinate convention is incident light from -Y to +Y, front face Y=0, plate Y=0..2 mm, and sensor active-plane reference Y=8 mm. The actual sensor holder/test jig is not modeled and must locate the active plane consistently. Coupon dimensions are provisional experimental values, not inferred from the reference 3MF.

## Measurement plan

1. Inspect and validate each solid in FreeCAD; confirm coupon orientation before printing.
2. Mount the actual TSL2591 module in a rigid jig and keep its active plane at the same datum for each coupon.
3. Use a stable source and fixed spectrum, distance, integration time and gain.
4. Record raw full-spectrum and IR channels separately at 0, 10, 20, 30 and 45 degrees incidence.
5. Repeat with a bright source just outside the intended field to test stray-light pickup.
6. Rotate the sensor/coupon assembly around its optical axis to detect asymmetric response.
7. Compare channel ratio as well as total counts and computed EV.
8. Select the shallowest profile that meets off-axis rejection requirements without unacceptable loss or angular instability.

## Attribution and reuse

The Curious Scientist project page identifies CC BY-SA. This workspace links to that work and records design observations; the V0.8 coupons are independently authored and do not copy its CAD geometry. If original 3MF geometry is imported or adapted, retain author attribution and comply with the applicable CC BY-SA version and share-alike terms.
