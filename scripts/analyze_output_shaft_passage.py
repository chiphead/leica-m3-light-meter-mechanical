#!/usr/bin/env python3
"""Screen candidate output-shaft passages through the translated shutter dial.
The original STEP remains read-only; every bore is cut only into a translated copy.
"""
from __future__ import annotations
import math, sys
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_transmission_candidate import gear, check, clear, INPUT, OUTPUT_AXIS, FROZEN

SOURCE = ROOT / "source/leica_m3_light_meter.stp"
REPORT = ROOT / "working/OUTPUT_SHAFT_PASSAGE_SCREEN.md"
OUTPUT = ROOT / "working/OUTPUT_SHAFT_PASSAGE_CANDIDATES.step"
BORE_DIAMETERS = (2.2, 2.7, 3.2)  # candidate clearance bores, not measured shaft sizes
SHAFT_DIAMETER = 1.8             # provisional screening value only
SHAFT_Z0, SHAFT_Z1 = 15.6, 21.0
GEAR_Z, GEAR_WIDTH = 21.0, 2.0
BLIND_HOLE_CENTER = (28.0, 0.0)  # source offset blind hole after rigid +10 X translation
BLIND_HOLE_RADIUS = 0.9
TOL = 1e-6

def cylinder(center, radius, z0, z1):
    return cq.Solid.makeCylinder(radius, z1-z0, cq.Vector(center[0],center[1],z0), cq.Vector(0,0,1))

def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7:
        raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    shutter = solids[3].translate((10,0,0))
    body = solids[5]
    frozen = {k: solids[i] for k,i in FROZEN.items()}
    input_gear = gear(INPUT, 0.0)
    output_gear = gear(OUTPUT_AXIS, math.pi + math.pi/20)
    shaft = cylinder(OUTPUT_AXIS, SHAFT_DIAMETER/2, SHAFT_Z0, SHAFT_Z1)
    output_unit = shaft.fuse(output_gear).clean()
    rows, variants = [], []
    center_spacing = math.dist(OUTPUT_AXIS, BLIND_HOLE_CENTER)
    for bore_d in BORE_DIAMETERS:
        cutter = cylinder(OUTPUT_AXIS, bore_d/2, 16.0, 21.0)
        try:
            bored = shutter.cut(cutter).clean()
            valid = bored.isValid() and len(bored.Solids()) == 1
            shaft_fit = check(shaft, bored)
            body_check = check(output_unit, body)
            frozen_checks = {k: check(output_unit,v) for k,v in frozen.items()}
            shutter_check = check(output_unit, bored)
            gear_check = check(input_gear, output_gear)
            web = center_spacing - BLIND_HOLE_RADIUS - bore_d/2
            passed = (valid and shaft_fit["error"] is None and shaft_fit["overlap"] is not None
                      and shaft_fit["overlap"] <= TOL
                      and clear({"body":body_check}) and clear(frozen_checks)
                      and clear({"shutter":shutter_check}) and gear_check["error"] is None
                      and gear_check["overlap"] is not None and gear_check["overlap"] <= TOL)
            rows.append({"bore":bore_d,"valid":valid,"shaft_fit":shaft_fit,
                         "body":body_check,"frozen":frozen_checks,"shutter":shutter_check,
                         "gear":gear_check,"web":web,"pass":passed})
            if valid:
                variants.append(cq.Compound.makeCompound([body,*frozen.values(),bored,input_gear,output_unit]))
        except Exception as exc:
            rows.append({"bore":bore_d,"valid":False,"error":repr(exc),"pass":False})
    if not variants:
        raise RuntimeError("No valid bored-shutter variant was produced")
    cq.exporters.export(cq.Compound.makeCompound(variants),str(OUTPUT),exportType="STEP")
    lines = [
      "# Output shaft passage candidate screen","",
      f"- Generated UTC: {datetime.now(timezone.utc).isoformat()}",
      "- Source STEP is read-only; bores are applied only to a translated copy of shutter solid #84.",
      "- Translation used for this candidate: STEP +X 10 mm; input axis (34.5, 0), fixed output axis (24.5, 0).",
      f"- Existing offset blind-hole center after translation: {BLIND_HOLE_CENTER}; radius {BLIND_HOLE_RADIUS:.2f} mm.",
      f"- Candidate shaft diameter: {SHAFT_DIAMETER:.2f} mm (PROVISIONAL, not inferred from the blind hole).",
      f"- Shaft screening span: Z={SHAFT_Z0:.2f}..{SHAFT_Z1:.2f} mm; gear plane Z={GEAR_Z:.2f}..{GEAR_Z+GEAR_WIDTH:.2f} mm.",
      "- Bore diameters are clearance-bore variants, not approved manufacturing dimensions.","",
      "| Bore Ø mm | Remaining web to blind-hole cavity mm | B-rep valid | Shaft fits | Body clear | Frozen encoder clear | Shutter clear | Gear pair clear | Pass |",
      "|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"
    ]
    for r in rows:
        if "error" in r:
            lines.append(f"| {r['bore']:.2f} | — | no | — | — | — | — | — | no |")
            continue
        yes = lambda x: "yes" if x else "no"
        lines.append(f"| {r['bore']:.2f} | {r['web']:.2f} | {yes(r['valid'])} | {yes(r['shaft_fit']['overlap'] is not None and r['shaft_fit']['overlap'] <= TOL)} | {yes(clear({'body':r['body']}))} | {yes(clear(r['frozen']))} | {yes(clear({'shutter':r['shutter']}))} | {yes(r['gear']['overlap'] is not None and r['gear']['overlap'] <= TOL)} | {yes(r['pass'])} |")
    lines += [
      "","## Interpretation","",
      "- The web value is a 2D center-distance estimate between the new through-bore and the existing blind-hole cavity; it is not a strength result.",
      "- Shaft Ø1.8 mm is only a geometric probe. Its value is independent of the existing Ø1.8 mm offset blind hole.",
      "- The STEP export is a compound of alternative bored-shutter variants, not one simultaneously assembled part.",
      "- No variant is production-approved. Bearing support, axial retention, actual magnet/AS5600 Z datum and magnetic air gap remain unverified.",
      "- If every candidate fails, do not force the shaft through the shutter; redesign the transmission path instead.",""
    ]
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\n".join(lines),encoding="utf-8")

if __name__ == "__main__":
    main()
