#!/usr/bin/env python3
"""Build an integrated high-level transmission candidate; source STEP is immutable."""
from __future__ import annotations
import math
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/leica_m3_light_meter.stp"
REPORT = ROOT / "working/TRANSMISSION_INTEGRATED_CANDIDATE.md"
OUTPUT = ROOT / "working/TRANSMISSION_INTEGRATED_CANDIDATE.step"
INPUT = (34.5, 0.0)
OUTPUT_AXIS = (24.5, 0.0)
MODULE, TEETH, PRESSURE = 0.5, 20, 20.0
GEAR_Z, GEAR_WIDTH = 21.0, 2.0
BRIDGE_Z0, BRIDGE_Z1 = 18.0, 18.6
SHAFT_Z0, SHAFT_Z1, SHAFT_DIA = 18.0, 21.2, 1.8
BRIDGE_SPAN_Y = 6.0
BRIDGE_WIDTHS = (0.6, 1.0)
TOL = 1e-6
FROZEN = {"encoder_body": 1, "encoder_dial": 2, "encoder_bracket": 6}

def inv(a):
    return math.tan(a) - a

def outline(phase, samples=16):
    alpha = math.radians(PRESSURE)
    rp, rb = MODULE * TEETH / 2, MODULE * TEETH / 2 * math.cos(alpha)
    ra, rf = rp + MODULE, rp - 1.25 * MODULE
    base = math.pi / (2 * TEETH) + inv(alpha)
    root = base + math.radians(1.4)
    def hw(r):
        p = math.acos(max(-1.0, min(1.0, rb / r)))
        return math.pi / (2 * TEETH) + inv(alpha) - inv(p)
    pts, pitch = [], 2 * math.pi / TEETH
    for n in range(TEETH):
        c = phase + n * pitch
        pts.append((rf*math.cos(c-root), rf*math.sin(c-root)))
        radii = [rb + (ra-rb)*i/samples for i in range(samples+1)]
        for r in radii:
            a = c - hw(r); pts.append((r*math.cos(a), r*math.sin(a)))
        tip = hw(ra)
        for i in range(1,4):
            a = c-tip+2*tip*i/4; pts.append((ra*math.cos(a), ra*math.sin(a)))
        for r in reversed(radii):
            a = c + hw(r); pts.append((r*math.cos(a), r*math.sin(a)))
        pts.append((rf*math.cos(c+root), rf*math.sin(c+root)))
        end = c + pitch - root
        for i in range(1,4):
            a = c+root+(end-(c+root))*i/4
            pts.append((rf*math.cos(a), rf*math.sin(a)))
    return pts

def gear(center, phase):
    return cq.Workplane("XY").polyline(outline(phase)).close().extrude(GEAR_WIDTH).val().translate((center[0], center[1], GEAR_Z))

def cyl(center, radius, z0, z1):
    return cq.Solid.makeCylinder(radius, z1-z0, cq.Vector(center[0],center[1],z0), cq.Vector(0,0,1))

def check(a,b):
    try: return {"overlap": float(a.intersect(b).Volume()), "distance": float(a.distance(b)), "error": None}
    except Exception as e: return {"overlap": None, "distance": None, "error": repr(e)}

def clear(items):
    return all(v["error"] is None and v["overlap"] is not None and v["overlap"] <= TOL for v in items.values())

def main():
    solids = cq.importers.importStep(str(SOURCE)).val().Solids()
    if len(solids) != 7: raise RuntimeError(f"Expected 7 source solids, got {len(solids)}")
    shutter = solids[3].translate((10,0,0))
    body, cover = solids[5], solids[4]
    frozen = {k: solids[i] for k,i in FROZEN.items()}
    gi = gear(INPUT, 0.0)
    go = gear(OUTPUT_AXIS, math.pi + math.pi/TEETH)
    pair = check(gi,go)
    rows, passing = [], []
    for bw in BRIDGE_WIDTHS:
        bridge = cq.Workplane("XY").box(bw, BRIDGE_SPAN_Y, BRIDGE_Z1-BRIDGE_Z0, centered=(True,True,False)).val().translate((INPUT[0],INPUT[1],BRIDGE_Z0))
        shaft = cyl(INPUT, SHAFT_DIA/2, SHAFT_Z0, SHAFT_Z1)
        try:
            input_unit = shutter.fuse(bridge).fuse(shaft).fuse(gi).clean()
            fuse_error = None
        except Exception as e:
            input_unit, fuse_error = None, repr(e)
        row = {
            "bridge_width": bw, "valid": bool(input_unit and input_unit.isValid()),
            "solid_count": len(input_unit.Solids()) if input_unit else None, "fuse_error": fuse_error,
            "input_body": check(input_unit,body) if input_unit else {},
            "input_frozen": {k:check(input_unit,v) for k,v in frozen.items()} if input_unit else {},
            "gear_pair": pair,
            "output_body": check(go,body),
            "output_frozen": {k:check(go,v) for k,v in frozen.items()},
            "output_cover_reference": check(go,cover),
            "output_moved_shutter": check(go,shutter),
        }
        row["pass"] = (row["valid"] and row["solid_count"] == 1 and
                       clear({"body":row["input_body"]}) and clear(row["input_frozen"]) and
                       clear({"body":row["output_body"]}) and clear(row["output_frozen"]) and
                       clear({"cover":row["output_cover_reference"],"shutter":row["output_moved_shutter"]}) and
                       pair["error"] is None and pair["overlap"] is not None and pair["overlap"] <= TOL)
        rows.append(row)
        if row["pass"]: passing.append((bw,input_unit))
    if not passing: raise RuntimeError("No integrated input assembly passed declared geometric checks")
    selected_bw, selected_input = passing[0]
    # Keep the original body and encoder parts; omit the old cover for redesign.
    result = cq.Compound.makeCompound([body,*frozen.values(),selected_input,go])
    cq.exporters.export(result,str(OUTPUT),exportType="STEP")
    lines = [
      "# Integrated high-level transmission candidate","",
      f"- Generated UTC: {datetime.now(timezone.utc).isoformat()}",
      "- Source STEP imported read-only; no source geometry modified.",
      f"- Axes: input {INPUT}, fixed output {OUTPUT_AXIS}; center distance 10.0 mm.",
      f"- True sampled involute gears: m{MODULE}, {TEETH}/{TEETH} teeth, {PRESSURE} degree pressure angle, Z={GEAR_Z:.2f}..{GEAR_Z+GEAR_WIDTH:.2f} mm, face width {GEAR_WIDTH:.2f} mm.",
      f"- Input bridge: width X={selected_bw:.2f} mm, Y span={BRIDGE_SPAN_Y:.2f} mm, Z={BRIDGE_Z0:.2f}..{BRIDGE_Z1:.2f} mm; center shaft Ø{SHAFT_DIA:.2f} mm, Z={SHAFT_Z0:.2f}..{SHAFT_Z1:.2f} mm.",
      "- The translated shutter dial, bridge, input shaft and input gear are fused as one input unit. The offset blind-hole interface is preserved by rigidly translating the source shutter solid.",
      "- The output gear remains a separate unsupported solid. No shaft is routed through the moved shutter dial volume; that output-side routing is still unresolved.",
      "- The old cover is omitted from the candidate because it is a redesign item; it is checked only as a reference obstacle.","",
      "## Candidate check matrix","",
      "| Bridge width X | Input unit valid | Solids | Input/body clear | Input/frozen clear | Output/body clear | Output/frozen clear | Gear-pair overlap | Pass |",
      "|---:|:---:|---:|:---:|:---:|:---:|:---:|---:|:---:|"
    ]
    for r in rows:
        lines.append(f"| {r['bridge_width']:.2f} | {'yes' if r['valid'] else 'no'} | {r['solid_count']} | {'yes' if clear({'body':r['input_body']}) else 'no'} | {'yes' if clear(r['input_frozen']) else 'no'} | {'yes' if clear({'body':r['output_body']}) else 'no'} | {'yes' if clear(r['output_frozen']) else 'no'} | {r['gear_pair']['overlap']} | {'yes' if r['pass'] else 'no'} |")
    lines += [
      "","## Export","",
      f"- Selected first passing bridge-width candidate: {selected_bw:.2f} mm. This is a geometry-screening choice, not a strength-based selection.",
      "- STEP contains the immutable body and encoder solids, the translated shutter/input bridge/shaft/input gear fused as one solid, and the separate output gear.",
      "- STEP intentionally excludes the old cover and does not claim a complete supported transmission.","",
      "## Unresolved before mechanical release","",
      "1. Output gear shaft route from the fixed magnet/AS5600 axis to the high gear plane. A straight shaft crossing the moved shutter-dial volume is not assumed feasible.",
      "2. Independent double-ended bearing support, thrust retention, transmission cassette base/bridge, fasteners, tool access and assembly sequence.",
      "3. AS5600 PCB, magnet, magnetic axis and air gap are absent from the source STEP; their measured positions and gap remain frozen and are not validated by this model.",
      "4. Gear backlash, root fillets, tip relief, manufacturing compensation, full-cycle tooth contact, torque capacity, wear, material and print anisotropy.",
      "5. New cover/enclosure, wall thickness, CNC tool access, sealing and manufacturing tolerances.",
      "6. Continuous swept-volume checks; this is a static nominal B-rep candidate, not motion or strength certification.","",
      "## Frozen constraints preserved","",
      "- Original STEP remains unchanged.",
      "- Encoder solids remain at their source coordinates.",
      "- Shutter offset blind-hole position, diameter, depth, opening direction and linkage insertion geometry remain unchanged on the translated shutter copy.",
      "- ESP32/display/USB, TSL2591 optical slot/aperture/alignment, AS5600/magnet working center and gap remain frozen.",""
    ]
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\\n".join(lines),encoding="utf-8")

if __name__ == "__main__":
    main()
