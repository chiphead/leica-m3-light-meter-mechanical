#!/usr/bin/env python3
"""Generate a provisional, colored STEP assembly for the Leica M3 meter.

This is a visual packaging preview, NOT a released enclosure or validated CAD.
All dimensions except the explicitly noted LCD envelope are placeholders.
Coordinate convention: LCD glass outer face Z=0; +Z toward top cover;
+X right across landscape display; +Y toward meter front; USB-C on left.
Requires: cadquery >= 2.4
"""
from pathlib import Path
import cadquery as cq
from cadquery import Vector

OUT = Path(__file__).resolve().parent

# ---- provisional module envelopes (mm) ----
LCD_X, LCD_Y, LCD_Z = 37.0, 21.0, 8.0
LCD_CX, LCD_CY = -33.0, -6.0
USB_W, USB_H, USB_PROJ = 9.0, 3.2, 3.5

AS_X, AS_Y, AS_T = 23.0, 23.0, 1.6
AS_PKG_XY, AS_PKG_DROP = 2.0, 1.5
MAG_D, MAG_T, MAG_GAP = 6.0, 2.0, 1.0
ROTOR_CARRIER_D, ROTOR_CARRIER_T = 20.0, 2.0
ROTOR_FLANGE_D, ROTOR_FLANGE_T = 24.0, 2.0
ROTOR_JOURNAL_D, ROTOR_JOURNAL_L = 6.0, 2.4
ROTOR_OUTER_D, ROTOR_OUTER_T = 20.0, 2.0

TSL_X, TSL_Z, TSL_T = 16.0, 19.0, 5.0
TSL_CX, TSL_FRONT_Y, TSL_CZ = -31.0, 27.0, 0.0

ENC_BODY_X, ENC_BODY_Y, ENC_BODY_Z = 7.8, 6.9, 6.5
ENC_SHAFT_D, ENC_SHAFT_PROJ = 3.0, 2.5
WHEEL_D, WHEEL_T = 20.0, 1.5
ENC_CX, ENC_CY, ENC_CZ = 34.0, 22.0, 8.0
HOUSING_FRONT_EDGE_Y = 27.0

def box(dx, dy, dz, x0, y0, z0):
    return cq.Solid.makeBox(dx, dy, dz, Vector(x0, y0, z0))

def cyl_z(d, h, x, y, z):
    return cq.Solid.makeCylinder(d/2, h, Vector(x, y, z), Vector(0, 0, 1))

def cyl_x(d, h, x, y, z):
    return cq.Solid.makeCylinder(d/2, h, Vector(x, y, z), Vector(1, 0, 0))

parts = []
def add(name, shape, color):
    parts.append((name, shape, color))

# LCD glass outer face is the global Z=0 datum; module lies below it.
lcd = box(LCD_X, LCD_Y, LCD_Z, LCD_CX-LCD_X/2, LCD_CY-LCD_Y/2, -8.6)
add("Waveshare ESP32-S3-LCD-1.47B PCB envelope (provisional)", lcd, (0.25,0.43,0.70))
glass = box(32.0, 18.0, 0.6, LCD_CX-16.0, LCD_CY-9.0, -0.6)
add("LCD glass / active face datum (outline placeholder)", glass, (0.12,0.16,0.20))
# USB-C shell faces outward toward -X.
usb = box(USB_PROJ, USB_W, USB_H, LCD_CX-LCD_X/2-USB_PROJ, LCD_CY-USB_W/2, -7.55)
add("USB-C metal shell envelope (left-facing; provisional)", usb, (0.72,0.72,0.75))

# AS5600 PCB is horizontal; sensor package faces down toward the magnet.
as_board = box(AS_X, AS_Y, AS_T, -AS_X/2, -AS_Y/2, 0.0)
add("AS5600 horizontal PCB; package faces down", as_board, (0.22,0.58,0.34))
pkg = box(AS_PKG_XY, AS_PKG_XY, AS_PKG_DROP, -AS_PKG_XY/2, -AS_PKG_XY/2, -AS_PKG_DROP)
add("AS5600 package envelope (placeholder)", pkg, (0.12,0.75,0.30))
mag_top = -AS_PKG_DROP-MAG_GAP
mag = cyl_z(MAG_D, MAG_T, 0, 0, mag_top-MAG_T)
add("Magnet centered on AS5600 axis (placeholder)", mag, (0.82,0.25,0.18))

# One-piece bottom rotor concept. Thrust hardware is intentionally omitted.
carrier_z = mag_top-MAG_T-ROTOR_CARRIER_T
carrier = cyl_z(ROTOR_CARRIER_D, ROTOR_CARRIER_T, 0, 0, carrier_z)
flange_z = carrier_z-ROTOR_FLANGE_T
flange = cyl_z(ROTOR_FLANGE_D, ROTOR_FLANGE_T, 0, 0, flange_z)
journal_z = flange_z-ROTOR_JOURNAL_L
journal = cyl_z(ROTOR_JOURNAL_D, ROTOR_JOURNAL_L, 0, 0, journal_z)
outer_z = journal_z-ROTOR_OUTER_T
outer = cyl_z(ROTOR_OUTER_D, ROTOR_OUTER_T, 0, 0, outer_z)
rod = cyl_z(1.0, 10.0, 8.5, 0, outer_z-9.8)
rotor = carrier.fuse(flange).fuse(journal).fuse(outer).fuse(rod)
add("One-piece bottom rotor concept (dimensions provisional)", rotor, (0.72,0.43,0.18))

# TSL2591 is vertical, with its sensing face toward +Y.
tsl = box(TSL_X, TSL_T, TSL_Z, TSL_CX-TSL_X/2, TSL_FRONT_Y-TSL_T, TSL_CZ-TSL_Z/2)
add("TSL2591 vertical PCB; sensing face points +Y and sensor center is below E8H7 shaft axis", tsl, (0.20,0.55,0.72))
tsl_pkg = box(3.0, 1.0, 2.0, TSL_CX-1.5, TSL_FRONT_Y, TSL_CZ-1.0)
add("TSL2591 optical package envelope", tsl_pkg, (0.10,0.72,0.82))

# E8H7 is an independent side control; shaft axis is horizontal (+Y),\n# with its thin wheel in a vertical XZ plane. The wheel sits beyond the\n# front housing-edge datum so its rim is finger-accessible from outside.
enc = box(ENC_BODY_X, ENC_BODY_Y, ENC_BODY_Z, ENC_CX-ENC_BODY_X/2, ENC_CY-ENC_BODY_Y/2, ENC_CZ-ENC_BODY_Z/2)
add("F-SWITCH E8H7-6.5J30-9B15-F200 body envelope", enc, (0.27,0.38,0.72))
shaft = cyl_y(ENC_SHAFT_D, ENC_SHAFT_PROJ, ENC_CX, ENC_CY+ENC_BODY_Y/2, ENC_CZ)
add("E8H7 horizontal +Y shaft (projection placeholder)", shaft, (0.18,0.20,0.24))
wheel_center_y = ENC_CY+ENC_BODY_Y/2+ENC_SHAFT_PROJ+WHEEL_T/2
wheel = cyl_y(WHEEL_D, WHEEL_T, ENC_CX, wheel_center_y-WHEEL_T/2, ENC_CZ)
add("Vertical XZ-plane E8H7 wheel outside front housing edge", wheel, (0.68,0.34,0.14))
# Thin reference wall marks the front housing boundary; it is not a designed shell.
edge_ref = box(22.0, 0.8, 0.5, ENC_CX-11.0, HOUSING_FRONT_EDGE_Y-0.8, -1.0)
add("Front housing edge reference only", edge_ref, (0.48,0.50,0.54))

assy = cq.Assembly(name="Leica M3 light meter - V2.9 functional layout preview")
for idx, (name, shape, color) in enumerate(parts):
    assy.add(shape, name=f"P{idx:02d}", color=cq.Color(*color), loc=cq.Location())
step_path = OUT / "V2.9_FUNCTIONAL_LAYOUT_PREVIEW.step"
assy.save(str(step_path), exportType="STEP")
stl_path = OUT / "V2.9_FUNCTIONAL_LAYOUT_PREVIEW.stl"
cq.exporters.export(cq.Compound.makeCompound([p[1] for p in parts]), str(stl_path), tolerance=0.15, angularTolerance=0.15)
print(f"STEP: {step_path}")
print(f"STL: {stl_path}")
print(f"Components: {len(parts)}")
print(f"E8H7 shaft axis: +Y; wheel center Y={wheel_center_y:.2f}; front edge Y={HOUSING_FRONT_EDGE_Y:.2f}; wheel is outside edge.")
print(f"TSL2591 center Z={TSL_CZ:.2f}; E8H7 shaft axis Z={ENC_CZ:.2f}; sensor is below dial axis.")
print("Preview only: provisional dimensions; no interference or fit validation claimed.")
