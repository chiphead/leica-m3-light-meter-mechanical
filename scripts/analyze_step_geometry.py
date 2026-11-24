#!/usr/bin/env python3
"""Validate the source STEP with CadQuery/OpenCascade and write a Markdown report."""
from __future__ import annotations
import hashlib
import json
import math
import sys
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
import cadquery as cq
from OCP.BRepExtrema import BRepExtrema_DistShapeShape

from analysis_cache import load_or_compute

ROOT = Path(__file__).resolve().parents[1]
STEP = ROOT / "source/leica_m3_light_meter.stp"
OUT = ROOT / "working/STEP_GEOMETRY_REPORT.md"

def vec(v):
    return [round(float(v.x), 6), round(float(v.y), 6), round(float(v.z), 6)]

def bbox(shape):
    b = shape.BoundingBox()
    return {
        "min": [round(b.xmin, 6), round(b.ymin, 6), round(b.zmin, 6)],
        "max": [round(b.xmax, 6), round(b.ymax, 6), round(b.zmax, 6)],
        "size": [round(b.xlen, 6), round(b.ylen, 6), round(b.zlen, 6)],
    }

def main():
    if not STEP.is_file():
        raise FileNotFoundError(STEP)
    imported = cq.importers.importStep(str(STEP))
    root_shape = imported.val()
    solids = root_shape.Solids()
    if not solids:
        raise RuntimeError("STEP import produced no solid bodies")
    source_sha256 = hashlib.sha256(STEP.read_bytes()).hexdigest()

    def compute_base_geometry_inventory():
        rows = []
        for index, solid in enumerate(solids, 1):
            rows.append({
                "index": index, "valid": bool(solid.isValid()),
                "volume_mm3": round(float(solid.Volume()), 6),
                "center_of_mass_mm": vec(solid.Center()),
                "bbox_mm": bbox(solid), "faces": len(solid.Faces()),
                "edges": len(solid.Edges()), "vertices": len(solid.Vertices()),
            })
        pairs = []
        for i in range(len(solids)):
            for j in range(i + 1, len(solids)):
                a, b = solids[i], solids[j]
                try:
                    common_volume = float(a.intersect(b).Volume())
                    intersection_error = None
                except Exception as exc:
                    common_volume, intersection_error = None, str(exc)
                try:
                    distance = float(a.distance(b))
                    distance_error = None
                except Exception as exc:
                    distance, distance_error = None, str(exc)
                pairs.append({
                    "a": i + 1, "b": j + 1,
                    "intersection_volume_mm3": round(common_volume, 9) if common_volume is not None else None,
                    "minimum_distance_mm": round(distance, 6) if distance is not None else None,
                    "intersection_error": intersection_error, "distance_error": distance_error,
                })
        return {"rows": rows, "pairs": pairs}

    inventory = load_or_compute(
        stage="base_geometry_inventory",
        version="1",
        inputs={
            "source_sha256": source_sha256,
            "cadquery_version": getattr(cq, "__version__", "unknown"),
            "solid_count": len(solids),
        },
        compute=compute_base_geometry_inventory,
    )
    rows = inventory["rows"]
    pairs = inventory["pairs"]
    all_valid = bool(root_shape.isValid()) and all(x["valid"] for x in rows)
    # First-pass axial sweep for the proposed 1:1, module-0.5 gear pair.
    # Gear blanks use the theoretical 11 mm addendum diameter and 2 mm face width.
    # Solids 2, 3 and 7 are the frozen encoder button, encoder dial and encoder bracket
    # in the currently documented STEP import order. Housing/shutter cover are omitted
    # because those surrounding mechanical structures are explicitly redesignable.
    gear_candidates = []
    frozen_encoder_solids = {"encoder_button": solids[1], "encoder_dial": solids[2], "encoder_bracket": solids[6]}
    gear_centers = {"output": (24.5, 0.0), "input": (34.5, 0.0)}
    z_values = [round(10.5 + i * 0.1, 4) for i in range(45)]
    for z0 in z_values:
        row = {"z_min_mm": z0, "z_max_mm": round(z0 + 2.0, 4), "clear": True, "checks": []}
        for gear_name, (gx, gy) in gear_centers.items():
            blank = cq.Solid.makeCylinder(5.5, 2.0, cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            for frozen_name, frozen_solid in frozen_encoder_solids.items():
                try:
                    overlap = float(blank.intersect(frozen_solid).Volume())
                    distance = float(blank.distance(frozen_solid))
                    error = None
                except Exception as exc:
                    overlap, distance, error = None, None, str(exc)
                row["checks"].append({
                    "gear": gear_name, "frozen_part": frozen_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "minimum_distance_mm": round(distance, 6) if distance is not None else None,
                    "error": error,
                })
                if error or overlap is None or overlap > 1e-6:
                    row["clear"] = False
        gear_candidates.append(row)
    clear_ranges = []
    active = None
    for row in gear_candidates:
        if row["clear"]:
            if active is None:
                active = [row["z_min_mm"], row["z_max_mm"]]
            else:
                active[1] = row["z_max_mm"]
        elif active is not None:
            clear_ranges.append(active)
            active = None
    if active is not None:
        clear_ranges.append(active)
    # Quantify what would need pocketing/reworking around a conservative candidate
    # plane. Z=11.4 leaves 0.5 mm nominal axial clearance above the encoder bracket
    # whose documented STEP extent ends at Z=10.9.
    candidate_z_min = 11.4
    editable_structure_checks = []
    editable_solids = {"old_shutter_dial": solids[3], "cover": solids[4], "main_body": solids[5]}
    # Broad axial feasibility scan against the fixed main body and frozen encoder parts.
    # The cover and old shutter dial are redesignable and intentionally excluded.
    # A cylinder is the full-turn swept radial envelope of a rotating gear.
    axial_body_scan = []
    scan_z_values = [round(i * 0.2, 4) for i in range(101)]  # 0.0 .. 20.0 mm
    for z0 in scan_z_values:
        row = {"z_min_mm": z0, "z_max_mm": round(z0 + 2.0, 4), "clear": True, "checks": []}
        for gear_name, (gx, gy) in gear_centers.items():
            swept = cq.Solid.makeCylinder(5.5, 2.0, cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
            for obstacle_name, obstacle in obstacles:
                try:
                    overlap = float(swept.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                row["checks"].append({
                    "gear": gear_name, "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
                if error or overlap is None or overlap > 1e-6:
                    row["clear"] = False
        axial_body_scan.append(row)
    # Refine the first feasible transition around the coarse 15.8..16.0 mm boundary.
    axial_body_fine_scan = []
    fine_z_values = [round(15.8 + i * 0.02, 4) for i in range(21)]  # 15.80..16.20 mm
    for z0 in fine_z_values:
        row = {"z_min_mm": z0, "z_max_mm": round(z0 + 2.0, 4), "clear": True, "checks": []}
        for gear_name, (gx, gy) in gear_centers.items():
            swept = cq.Solid.makeCylinder(5.5, 2.0, cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
            for obstacle_name, obstacle in obstacles:
                try:
                    overlap = float(swept.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                row["checks"].append({
                    "gear": gear_name, "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
                if error or overlap is None or overlap > 1e-6:
                    row["clear"] = False
        axial_body_fine_scan.append(row)
    # Store feasible lower-face start positions separately from the union envelope.
    # A range [16, 22] in the old field conflated starts 16..20 with blank extents 16..22.
    axial_body_clear_start_z_ranges = []
    axial_body_clear_envelope_ranges = []
    active_starts = None
    for row in axial_body_scan:
        if row["clear"]:
            if active_starts is None:
                active_starts = [row["z_min_mm"], row["z_min_mm"]]
            else:
                active_starts[1] = row["z_min_mm"]
        elif active_starts is not None:
            axial_body_clear_start_z_ranges.append(active_starts)
            active_starts = None
    if active_starts is not None:
        axial_body_clear_start_z_ranges.append(active_starts)
    axial_body_clear_envelope_ranges = [
        [round(start, 4), round(end + 2.0, 4)]
        for start, end in axial_body_clear_start_z_ranges
    ]
    for gear_name, (gx, gy) in gear_centers.items():
        blank = cq.Solid.makeCylinder(5.5, 2.0, cq.Vector(gx, gy, candidate_z_min), cq.Vector(0, 0, 1))
        for editable_name, editable_solid in editable_solids.items():
            try:
                overlap = float(blank.intersect(editable_solid).Volume())
                distance = float(blank.distance(editable_solid))
                error = None
            except Exception as exc:
                overlap, distance, error = None, None, str(exc)
            overlap_bbox = None
            if overlap is not None and overlap > 1e-9:
                try:
                    overlap_bbox = bbox(blank.intersect(editable_solid))
                except Exception:
                    overlap_bbox = None
            editable_structure_checks.append({
                "gear": gear_name, "structure": editable_name,
                "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                "minimum_distance_mm": round(distance, 6) if distance is not None else None,
                "intersection_bbox_mm": overlap_bbox,
                "error": error,
            })
    # Map the input-gear/body overlap onto individual body faces. Locator only.
    input_gear = cq.Solid.makeCylinder(5.5, 2.0, cq.Vector(34.5, 0.0, candidate_z_min), cq.Vector(0, 0, 1))
    body_face_intersections = []
    body = editable_solids["main_body"]
    for face_index, face in enumerate(body.Faces(), 1):
        try:
            common = face.intersect(input_gear)
            area = float(common.Area())
            if area <= 1e-7:
                continue
            body_face_intersections.append({
                "cadquery_face_index": face_index,
                "surface_type": face.geomType(),
                "face_area_mm2": round(float(face.Area()), 6),
                "face_center_mm": vec(face.Center()),
                "face_bbox_mm": bbox(face),
                "intersection_area_mm2": round(area, 9),
                "intersection_bbox_mm": bbox(common),
                "intersection_center_mm": vec(common.Center()),
                "error": None,
            })
        except Exception as exc:
            body_face_intersections.append({
                "cadquery_face_index": face_index,
                "surface_type": face.geomType(),
                "error": str(exc),
            })
    body_face_intersections.sort(
        key=lambda item: item.get("intersection_area_mm2", 0.0), reverse=True
    )
    body_face_topology = []
    # Include the nearest opposing boundary face (currently 101) as well as overlap faces.
    # Its boundary and adjacency reveal whether the candidate relief approaches a shell wall,
    # stepped support, or transition surface; face indices remain import-order dependent.
    target_face_indices = {126, 109, 101}
    body_faces = body.Faces()
    for target_index in sorted(target_face_indices):
        face = body_faces[target_index - 1]
        try:
            normal = vec(face.normalAt())
        except Exception as exc:
            normal = None
            normal_error = str(exc)
        else:
            normal_error = None
        wire_rows = []
        for wire_index, wire in enumerate(face.Wires(), 1):
            wire_edges = wire.Edges()
            wire_rows.append({
                "wire_index": wire_index,
                "edge_count": len(wire_edges),
                "wire_length_mm": round(sum(float(edge.Length()) for edge in wire_edges), 6),
                "edge_types": [edge.geomType() for edge in wire_edges],
                "edge_bboxes_mm": [bbox(edge) for edge in wire_edges],
            })
        adjacent_faces = []
        target_edges = face.Edges()
        for other_index, other_face in enumerate(body_faces, 1):
            if other_index == target_index:
                continue
            shared = []
            for edge_index, target_edge in enumerate(target_edges, 1):
                for other_edge_index, other_edge in enumerate(other_face.Edges(), 1):
                    try:
                        if target_edge.isSame(other_edge):
                            shared.append({
                                "target_edge_index": edge_index,
                                "other_edge_index": other_edge_index,
                                "edge_type": target_edge.geomType(),
                                "edge_length_mm": round(float(target_edge.Length()), 6),
                                "edge_bbox_mm": bbox(target_edge),
                            })
                            break
                    except Exception:
                        continue
            if shared:
                adjacent_faces.append({
                    "face_index": other_index,
                    "surface_type": other_face.geomType(),
                    "face_bbox_mm": bbox(other_face),
                    "shared_edges": shared,
                })
        body_face_topology.append({
            "cadquery_face_index": target_index,
            "surface_type": face.geomType(),
            "face_area_mm2": round(float(face.Area()), 6),
            "face_bbox_mm": bbox(face),
            "normal_at_center": normal,
            "normal_error": normal_error,
            "wires": wire_rows,
            "adjacent_faces": adjacent_faces,
        })
    # Find the nearest non-intersecting main-body boundary faces to the
    # gear/body overlap volume. These are candidate opposite walls, not a
    # certified wall-thickness measurement (edge proximity and face orientation matter).
    gear_body_overlap = input_gear.intersect(body)
    intersecting_face_ids = {
        item["cadquery_face_index"] for item in body_face_intersections
        if item.get("intersection_area_mm2", 0.0) > 1e-7
    }
    nearby_body_faces = []
    for face_index, face in enumerate(body.Faces(), 1):
        if face_index in intersecting_face_ids:
            continue
        try:
            distance = float(face.distance(gear_body_overlap))
            nearby_body_faces.append({
                "cadquery_face_index": face_index,
                "surface_type": face.geomType(),
                "distance_from_gear_body_overlap_mm": round(distance, 6),
                "face_area_mm2": round(float(face.Area()), 6),
                "face_bbox_mm": bbox(face),
            })
        except Exception as exc:
            nearby_body_faces.append({
                "cadquery_face_index": face_index,
                "surface_type": face.geomType(),
                "error": str(exc),
            })
    nearby_body_faces.sort(
        key=lambda item: item.get("distance_from_gear_body_overlap_mm", float("inf"))
    )
    # Refine the nearest candidate boundary (face 101 in the current import order):
    # record exact closest-point pairs for the full overlap and Y-sliced overlap.
    nearest_face_detail = None
    if nearby_body_faces:
        nearest_face_index = nearby_body_faces[0].get("cadquery_face_index")
        if nearest_face_index is not None:
            nearest_face = body.Faces()[nearest_face_index - 1]
            try:
                nearest_normal = vec(nearest_face.normalAt())
            except Exception as exc:
                nearest_normal = None
                nearest_normal_error = str(exc)
            else:
                nearest_normal_error = None
            def closest_pair(shape_a, shape_b):
                extrema = BRepExtrema_DistShapeShape(shape_a.wrapped, shape_b.wrapped)
                extrema.Perform()
                if not extrema.IsDone() or extrema.NbSolution() < 1:
                    raise RuntimeError("OpenCascade did not return a closest-point solution")
                p1 = extrema.PointOnShape1(1)
                p2 = extrema.PointOnShape2(1)
                return {
                    "distance_mm": round(float(extrema.Value()), 9),
                    "point_on_overlap_mm": [round(p1.X(), 6), round(p1.Y(), 6), round(p1.Z(), 6)],
                    "point_on_boundary_mm": [round(p2.X(), 6), round(p2.Y(), 6), round(p2.Z(), 6)],
                }
            try:
                full_pair = closest_pair(gear_body_overlap, nearest_face)
                full_pair_error = None
            except Exception as exc:
                full_pair, full_pair_error = None, str(exc)
            y_slice_pairs = []
            for y_center in [round(-1.0 + i * 0.1, 1) for i in range(21)]:
                y_slab = cq.Solid.makeBox(18.0, 0.05, 10.0, cq.Vector(27.0, y_center - 0.025, 8.0))
                overlap_slice = gear_body_overlap.intersect(y_slab)
                try:
                    if overlap_slice.Volume() <= 1e-9:
                        raise RuntimeError("No overlap material in this Y slice")
                    pair = closest_pair(overlap_slice, nearest_face)
                    pair["y_center_mm"] = y_center
                    pair["overlap_slice_bbox_mm"] = bbox(overlap_slice)
                    pair["error"] = None
                except Exception as exc:
                    pair = {"y_center_mm": y_center, "error": str(exc)}
                y_slice_pairs.append(pair)
            nearest_face_detail = {
                "cadquery_face_index": nearest_face_index,
                "surface_type": nearest_face.geomType(),
                "normal_at_center": nearest_normal,
                "normal_error": nearest_normal_error,
                "full_overlap_closest_pair": full_pair,
                "full_overlap_error": full_pair_error,
                "y_slice_closest_pairs": y_slice_pairs,
            }
    # Local X-Z section sampling through the proposed input gear's 2 mm face width.
    # A 0.05 mm Y-slab is used as a numerical section approximation; volume/thickness
    # estimates cross-sectional area. This is not a true minimum-wall-thickness proof.
    section_samples = []
    section_thickness = 0.05
    section_y_values = [-1.0, -0.5, 0.0, 0.5, 1.0]
    section_roi = cq.Solid.makeBox(
        18.0, section_thickness, 10.0,
        cq.Vector(27.0, -section_thickness / 2.0, 8.0)
    )
    for y_value in section_y_values:
        slab = cq.Solid.makeBox(
            18.0, section_thickness, 10.0,
            cq.Vector(27.0, y_value - section_thickness / 2.0, 8.0)
        )
        try:
            local_material = body.intersect(slab)
            material_solids = local_material.Solids() or ([local_material] if local_material.Volume() > 1e-8 else [])
            local_overlap = body.intersect(input_gear).intersect(slab)
            overlap_solids = local_overlap.Solids() or ([local_overlap] if local_overlap.Volume() > 1e-8 else [])
            section_samples.append({
                "y_mm": y_value,
                "slab_thickness_mm": section_thickness,
                "roi_x_mm": [27.0, 45.0],
                "roi_z_mm": [8.0, 18.0],
                "material_section_area_estimate_mm2": round(float(local_material.Volume()) / section_thickness, 6),
                "material_components": [{
                    "bbox_mm": bbox(component),
                    "section_area_estimate_mm2": round(float(component.Volume()) / section_thickness, 6),
                } for component in material_solids],
                "gear_body_overlap_area_estimate_mm2": round(float(local_overlap.Volume()) / section_thickness, 6),
                "gear_body_overlap_components": [{
                    "bbox_mm": bbox(component),
                    "section_area_estimate_mm2": round(float(component.Volume()) / section_thickness, 6),
                } for component in overlap_solids],
                "error": None,
            })
        except Exception as exc:
            section_samples.append({"y_mm": y_value, "error": str(exc)})
    # Exploratory shaft-corridor scan at the fixed output/input axis projections.
    # Radii are probes only (not selected shaft dimensions); 0.5 mm axial slices
    # map where the immutable body and encoder hardware obstruct each corridor.
    shaft_corridor_scan = []
    shaft_probe_radii_mm = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]
    shaft_slice_z_values = [round(i * 0.5, 4) for i in range(44)]  # 0.0 .. 21.5
    shaft_slice_height_mm = 0.5
    shaft_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
    for axis_name, (axis_x, axis_y) in gear_centers.items():
        for radius in shaft_probe_radii_mm:
            for z0 in shaft_slice_z_values:
                probe = cq.Solid.makeCylinder(radius, shaft_slice_height_mm,
                    cq.Vector(axis_x, axis_y, z0), cq.Vector(0, 0, 1))
                checks = []
                for obstacle_name, obstacle in shaft_obstacles:
                    try:
                        overlap = float(probe.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        overlap, error = None, str(exc)
                    checks.append({
                        "obstacle": obstacle_name,
                        "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                        "error": error,
                    })
                shaft_corridor_scan.append({
                    "axis": axis_name, "center_xy_mm": [axis_x, axis_y],
                    "probe_radius_mm": radius, "z_min_mm": z0,
                    "z_max_mm": round(z0 + shaft_slice_height_mm, 4),
                    "checks": checks,
                    "clear_of_fixed_geometry": all(
                        item["error"] is None and item["intersection_volume_mm3"] is not None
                        and item["intersection_volume_mm3"] <= 1e-6 for item in checks
                    ),
                })
    # Explore alternate input-axis positions on the 10 mm pitch-radius orbit
    # around the immutable magnetic output axis. This is a feasibility map only.
    input_axis_orbit_scan = []
    orbit_probe_radii_mm = [0.5, 1.0, 1.5, 2.0]
    orbit_angles_deg = list(range(0, 360, 10))
    orbit_z_min_mm, orbit_z_max_mm = 8.5, 11.0
    orbit_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
    output_x, output_y = gear_centers["output"]
    for angle_deg in orbit_angles_deg:
        angle_rad = math.radians(angle_deg)
        candidate_x = output_x + 10.0 * math.cos(angle_rad)
        candidate_y = output_y + 10.0 * math.sin(angle_rad)
        for radius in orbit_probe_radii_mm:
            probe = cq.Solid.makeCylinder(radius, orbit_z_max_mm - orbit_z_min_mm,
                cq.Vector(candidate_x, candidate_y, orbit_z_min_mm), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in orbit_obstacles:
                try:
                    overlap = float(probe.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            input_axis_orbit_scan.append({
                "angle_deg_from_positive_x": angle_deg,
                "center_xy_mm": [round(candidate_x, 6), round(candidate_y, 6)],
                "center_distance_from_output_mm": 10.0,
                "probe_radius_mm": radius,
                "z_range_mm": [orbit_z_min_mm, orbit_z_max_mm],
                "checks": checks,
                "clear_of_fixed_geometry": all(
                    item["error"] is None and item["intersection_volume_mm3"] is not None
                    and item["intersection_volume_mm3"] <= 1e-6 for item in checks
                ),
            })
    # Full radial-envelope check for an input gear blank at each orbit candidate.
    # The old shutter dial is redesignable; cover is reported separately.
    input_gear_orbit_envelope_scan = []
    gear_orbit_angles_deg = list(range(0, 360, 5))
    gear_orbit_z_min_mm = 16.0
    gear_orbit_face_width_mm = 2.0
    gear_orbit_radius_mm = 5.5
    gear_orbit_fixed_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
    for angle_deg in gear_orbit_angles_deg:
        angle_rad = math.radians(angle_deg)
        candidate_x = output_x + 10.0 * math.cos(angle_rad)
        candidate_y = output_y + 10.0 * math.sin(angle_rad)
        blank = cq.Solid.makeCylinder(gear_orbit_radius_mm, gear_orbit_face_width_mm,
            cq.Vector(candidate_x, candidate_y, gear_orbit_z_min_mm), cq.Vector(0, 0, 1))
        checks = []
        for obstacle_name, obstacle in gear_orbit_fixed_obstacles:
            try:
                overlap = float(blank.intersect(obstacle).Volume())
                error = None
            except Exception as exc:
                overlap, error = None, str(exc)
            checks.append({"obstacle": obstacle_name,
                "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                "error": error})
        try:
            cover_overlap = float(blank.intersect(editable_solids["cover"]).Volume())
            cover_error = None
        except Exception as exc:
            cover_overlap, cover_error = None, str(exc)
        input_gear_orbit_envelope_scan.append({
            "angle_deg_from_positive_x": angle_deg,
            "center_xy_mm": [round(candidate_x, 6), round(candidate_y, 6)],
            "center_distance_from_output_mm": 10.0,
            "gear_blank_diameter_mm": 11.0,
            "gear_face_width_mm": gear_orbit_face_width_mm,
            "z_range_mm": [gear_orbit_z_min_mm, gear_orbit_z_min_mm + gear_orbit_face_width_mm],
            "fixed_geometry_checks": checks,
            "clear_of_fixed_geometry": all(
                item["error"] is None and item["intersection_volume_mm3"] is not None
                and item["intersection_volume_mm3"] <= 1e-6 for item in checks),
            "cover_intersection_volume_mm3": round(cover_overlap, 9) if cover_overlap is not None else None,
            "cover_error": cover_error,
        })
    # Full-height vertical shaft probes for the two orthogonal candidates that
    # cleared the encoder bracket in the mid-height corridor scan.
    vertical_candidate_shaft_scan = []
    vertical_candidate_angles_deg = [90, 270]
    vertical_candidate_radii_mm = [0.5, 1.0, 1.5, 2.0]
    vertical_candidate_z_values = [round(i * 0.5, 4) for i in range(45)]  # 0 .. 22 mm
    vertical_candidate_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items()) + [("cover", editable_solids["cover"])]
    for angle_deg in vertical_candidate_angles_deg:
        angle_rad = math.radians(angle_deg)
        candidate_x = output_x + 10.0 * math.cos(angle_rad)
        candidate_y = output_y + 10.0 * math.sin(angle_rad)
        for radius in vertical_candidate_radii_mm:
            for z0 in vertical_candidate_z_values:
                probe = cq.Solid.makeCylinder(radius, 0.5,
                    cq.Vector(candidate_x, candidate_y, z0), cq.Vector(0, 0, 1))
                checks = []
                for obstacle_name, obstacle in vertical_candidate_obstacles:
                    try:
                        overlap = float(probe.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        overlap, error = None, str(exc)
                    checks.append({"obstacle": obstacle_name,
                        "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                        "error": error})
                vertical_candidate_shaft_scan.append({
                    "angle_deg_from_positive_x": angle_deg,
                    "center_xy_mm": [round(candidate_x, 6), round(candidate_y, 6)],
                    "probe_radius_mm": radius,
                    "z_min_mm": z0, "z_max_mm": round(z0 + 0.5, 4),
                    "checks": checks,
                    "clear_of_all_checked_solids": all(
                        item["error"] is None and item["intersection_volume_mm3"] is not None
                        and item["intersection_volume_mm3"] <= 1e-6 for item in checks),
                })
    # Map local lateral bypass space around the two candidate input-shaft axes.
    # This is a coarse XY occupancy map at five blocked-height bands, not a proposed cut.
    lateral_bypass_section_scan = []
    lateral_scan_x = [round(14.5 + i, 4) for i in range(21)]  # 14.5 .. 34.5 mm
    lateral_scan_y = [float(i) for i in range(-17, 18)]      # -17 .. +17 mm
    lateral_scan_z = [11.5, 12.5, 13.5, 14.5, 15.5]
    lateral_probe_radius_mm = 0.75
    lateral_probe_height_mm = 0.5
    lateral_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
    for z0 in lateral_scan_z:
        free_nodes = set()
        failed_nodes = []
        for ix, x in enumerate(lateral_scan_x):
            for iy, y in enumerate(lateral_scan_y):
                probe = cq.Solid.makeCylinder(lateral_probe_radius_mm, lateral_probe_height_mm,
                    cq.Vector(x, y, z0), cq.Vector(0, 0, 1))
                blocked = False
                errors = []
                for obstacle_name, obstacle in lateral_obstacles:
                    try:
                        overlap = float(probe.intersect(obstacle).Volume())
                        if overlap > 1e-6:
                            blocked = True
                    except Exception as exc:
                        errors.append({"obstacle": obstacle_name, "error": str(exc)})
                if errors:
                    failed_nodes.append({"x_mm": x, "y_mm": y, "errors": errors})
                elif not blocked:
                    free_nodes.add((ix, iy))
        # 8-connected components identify broad free-space regions in this section.
        components = []
        unseen = set(free_nodes)
        while unseen:
            seed = unseen.pop()
            stack = [seed]
            component = [seed]
            while stack:
                cx, cy = stack.pop()
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nxt = (cx + dx, cy + dy)
                        if nxt in unseen:
                            unseen.remove(nxt)
                            stack.append(nxt)
                            component.append(nxt)
            xs = [lateral_scan_x[ix] for ix, _ in component]
            ys = [lateral_scan_y[iy] for _, iy in component]
            components.append({
                "node_count": len(component),
                "bbox_xy_mm": {"min": [min(xs), min(ys)], "max": [max(xs), max(ys)]},
                "near_90deg_candidate": any(abs(lateral_scan_x[ix] - 24.5) <= 1.0 and abs(lateral_scan_y[iy] - 10.0) <= 1.0 for ix, iy in component),
                "near_270deg_candidate": any(abs(lateral_scan_x[ix] - 24.5) <= 1.0 and abs(lateral_scan_y[iy] + 10.0) <= 1.0 for ix, iy in component),
            })
        components.sort(key=lambda item: item["node_count"], reverse=True)
        lateral_bypass_section_scan.append({
            "z_min_mm": z0, "z_max_mm": round(z0 + lateral_probe_height_mm, 4),
            "probe_radius_mm": lateral_probe_radius_mm,
            "grid_step_mm": 1.0, "grid_size": [len(lateral_scan_x), len(lateral_scan_y)],
            "free_node_count": len(free_nodes), "blocked_or_error_node_count": len(lateral_scan_x) * len(lateral_scan_y) - len(free_nodes),
            "components_8_connected": components[:20],
            "calculation_errors": failed_nodes,
        })
    # Continuous 3D free-space connectivity across the previously blocked shaft band.
    # Each node is a spherical clearance probe; 6-neighbor connectivity only joins
    # overlapping probe spheres, avoiding diagonal corner-touch shortcuts.
    volume_scan_x = [round(14.5 + i, 4) for i in range(21)]
    volume_scan_y = [float(i) for i in range(-17, 18)]
    volume_scan_z = [round(11.5 + 0.5 * i, 4) for i in range(9)]
    volume_probe_radius_mm = 0.75
    volume_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
    free_voxels = set()
    failed_voxels = []
    for iz, z in enumerate(volume_scan_z):
        for ix, x in enumerate(volume_scan_x):
            for iy, y in enumerate(volume_scan_y):
                probe = cq.Solid.makeSphere(volume_probe_radius_mm, cq.Vector(x, y, z))
                blocked = False
                errors = []
                for obstacle_name, obstacle in volume_obstacles:
                    try:
                        overlap = float(probe.intersect(obstacle).Volume())
                        if overlap > 1e-6:
                            blocked = True
                    except Exception as exc:
                        errors.append({"obstacle": obstacle_name, "error": str(exc)})
                if errors:
                    failed_voxels.append({"center_mm": [x, y, z], "errors": errors})
                elif not blocked:
                    free_voxels.add((ix, iy, iz))
    # 6-neighbor adjacency: XY spacing 1 mm and Z spacing 0.5 mm are
    # both below 2*probe radius, so adjacent clearance spheres overlap.
    components_3d = []
    unseen_voxels = set(free_voxels)
    while unseen_voxels:
        seed = unseen_voxels.pop()
        stack = [seed]
        component = [seed]
        while stack:
            cx, cy, cz = stack.pop()
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                nxt = (cx + dx, cy + dy, cz + dz)
                if nxt in unseen_voxels:
                    unseen_voxels.remove(nxt)
                    stack.append(nxt)
                    component.append(nxt)
        xs = [volume_scan_x[ix] for ix, _, _ in component]
        ys = [volume_scan_y[iy] for _, iy, _ in component]
        zs = [volume_scan_z[iz] for _, _, iz in component]
        near_90 = any(abs(volume_scan_x[ix] - 24.5) <= 1.0 and abs(volume_scan_y[iy] - 10.0) <= 1.0 for ix, iy, _ in component)
        near_270 = any(abs(volume_scan_x[ix] - 24.5) <= 1.0 and abs(volume_scan_y[iy] + 10.0) <= 1.0 for ix, iy, _ in component)
        components_3d.append({
            "node_count": len(component),
            "bbox_xyz_mm": {"min": [min(xs), min(ys), min(zs)], "max": [max(xs), max(ys), max(zs)]},
            "near_90deg_candidate": near_90,
            "near_270deg_candidate": near_270,
            "node_centers_mm": [[volume_scan_x[ix], volume_scan_y[iy], volume_scan_z[iz]] for ix, iy, iz in sorted(component, key=lambda p: (p[2], p[1], p[0]))],
        })
    components_3d.sort(key=lambda item: item["node_count"], reverse=True)
    lateral_bypass_3d_scan = {
        "probe_shape": "sphere",
        "probe_radius_mm": volume_probe_radius_mm,
        "grid_step_mm": [1.0, 1.0, 0.5],
        "grid_size": [len(volume_scan_x), len(volume_scan_y), len(volume_scan_z)],
        "x_centers_mm": volume_scan_x,
        "y_centers_mm": volume_scan_y,
        "z_centers_mm": volume_scan_z,
        "free_voxel_count": len(free_voxels),
        "blocked_or_error_voxel_count": len(volume_scan_x) * len(volume_scan_y) * len(volume_scan_z) - len(free_voxels),
        "calculation_errors": failed_voxels,
        "connectivity": "6-neighbor; adjacent spherical probes overlap",
        "components_6_connected": components_3d,
    }

    # Extract shortest 6-connected clearance routes for mirrored candidates.
    # A bent polyline is a spatial corridor, NOT a rigid rotating shaft.
    candidate_centerline_routes = []
    route_probe_radius_mm = 0.75
    index_by_xyz = {
        (x, y, z): (ix, iy, iz)
        for ix, x in enumerate(volume_scan_x)
        for iy, y in enumerate(volume_scan_y)
        for iz, z in enumerate(volume_scan_z)
    }
    for angle_deg, candidate_y in ((90, 10.0), (270, -10.0)):
        start_node = index_by_xyz[(24.5, candidate_y, 11.5)]
        requested_end_node = index_by_xyz[(24.5, candidate_y, 15.5)]
        # The exact nominal endpoint may be blocked even though the same connected
        # free-space component reaches the top layer nearby. Select the nearest
        # free top-layer voxel within 3.1 mm, then let BFS confirm connectivity.
        top_layer = len(volume_scan_z) - 1
        end_candidates = [
            node for node in free_voxels
            if node[2] == top_layer
            and math.hypot(volume_scan_x[node[0]] - 24.5,
                           volume_scan_y[node[1]] - candidate_y) <= 3.1
        ]
        end_candidates.sort(key=lambda node: (
            math.hypot(volume_scan_x[node[0]] - 24.5,
                       volume_scan_y[node[1]] - candidate_y),
            node[1], node[0]
        ))
        if start_node not in free_voxels or not end_candidates:
            candidate_centerline_routes.append({
                "angle_deg": angle_deg, "candidate_xy_mm": [24.5, candidate_y],
                "route_found": False,
                "reason": "No free start node or no free top-layer endpoint within 3.1 mm",
                "requested_endpoint_free": requested_end_node in free_voxels
            })
            continue
        end_set = set(end_candidates)
        queue = deque([start_node])
        previous = {start_node: None}
        reached_end = None
        while queue and reached_end is None:
            current = queue.popleft()
            if current in end_set:
                reached_end = current
                break
            cx, cy, cz = current
            for dx, dy, dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                nxt = (cx + dx, cy + dy, cz + dz)
                if nxt in free_voxels and nxt not in previous:
                    previous[nxt] = current
                    queue.append(nxt)
        end_node = reached_end
        if end_node is None:
            candidate_centerline_routes.append({
                "angle_deg": angle_deg, "candidate_xy_mm": [24.5, candidate_y],
                "route_found": False,
                "reason": "No 6-connected path to any free top-layer endpoint within 3.1 mm",
                "requested_endpoint_free": requested_end_node in free_voxels
            })
            continue
        route_indices = []
        node = end_node
        while node is not None:
            route_indices.append(node)
            node = previous[node]
        route_indices.reverse()
        route_points = [
            [volume_scan_x[ix], volume_scan_y[iy], volume_scan_z[iz]]
            for ix, iy, iz in route_indices
        ]
        full_points = [[24.5, candidate_y, 11.0]] + route_points + [[24.5, candidate_y, 16.0]]
        tube_checks = []
        obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items())
        for segment_index, (a, b) in enumerate(zip(full_points, full_points[1:])):
            av, bv = cq.Vector(*a), cq.Vector(*b)
            direction = bv.sub(av)
            length = float(direction.Length)
            if length <= 1e-8:
                continue
            segment = cq.Solid.makeCylinder(route_probe_radius_mm, length, av, direction.normalized())
            for obstacle_name, obstacle in obstacles:
                try:
                    overlap = float(segment.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                tube_checks.append({
                    "segment_index": segment_index, "from_mm": a, "to_mm": b,
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error
                })
        collisions = [x for x in tube_checks if x["error"] or x["intersection_volume_mm3"] is None or x["intersection_volume_mm3"] > 1e-6]
        route_length = sum(math.dist(a, b) for a, b in zip(full_points, full_points[1:]))
        candidate_centerline_routes.append({
            "angle_deg": angle_deg, "candidate_xy_mm": [24.5, candidate_y],
            "route_found": True, "requested_endpoint_mm": [24.5, candidate_y, 15.5],
            "selected_endpoint_mm": route_points[-1],
            "endpoint_offset_mm": round(math.dist(route_points[-1], [24.5, candidate_y, 15.5]), 4),
            "requested_endpoint_free": requested_end_node in free_voxels,
            "route_node_count": len(route_points),
            "route_length_mm": round(route_length, 4),
            "probe_radius_mm": route_probe_radius_mm,
            "centerline_points_mm": full_points,
            "tube_segment_check_count": len(tube_checks),
            "tube_collision_count": len(collisions),
            "tube_collisions": collisions,
            "tube_clear_of_checked_fixed_geometry": not collisions,
            "limitations": [
                "Polyline is a clearance corridor, not a manufacturable bent rotating shaft",
                "Bends require separate shafts with gears/couplings or a flexible drive",
                "Bearings, supports, gears, fasteners, tolerances and assembly path are not included",
                "Cover is redesignable and intentionally excluded"
            ]
        })
    # Test whether the 1 mm lateral bypass can be replaced by a manufacturable
    # straight vertical shaft at the offset corridor center, rather than a bent shaft.
    straight_bypass_shaft_checks = []
    for angle_deg, candidate_y in ((90, 10.0), (270, -10.0)):
        shaft_y = candidate_y - math.copysign(1.0, candidate_y)
        for shaft_radius_mm in (0.5, 0.75, 1.0, 1.25, 1.5):
            shaft = cq.Solid.makeCylinder(
                shaft_radius_mm, 5.0,
                cq.Vector(24.5, shaft_y, 11.0), cq.Vector(0, 0, 1)
            )
            checks = []
            for obstacle_name, obstacle in (
                ("main_body", editable_solids["main_body"]),
                *list(frozen_encoder_solids.items()),
            ):
                try:
                    overlap = float(shaft.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            collisions = [x for x in checks if x["error"] or x["intersection_volume_mm3"] is None or x["intersection_volume_mm3"] > 1e-6]
            straight_bypass_shaft_checks.append({
                "angle_deg": angle_deg,
                "candidate_input_axis_xy_mm": [24.5, candidate_y],
                "straight_shaft_axis_xy_mm": [24.5, shaft_y],
                "shaft_radius_mm": shaft_radius_mm,
                "shaft_z_range_mm": [11.0, 16.0],
                "obstacle_checks": checks,
                "collision_count": len(collisions),
                "clear_of_checked_fixed_geometry": not collisions,
            })

    # Extend the preferred +/-Y=9 mm straight-shaft candidates through the full STEP height.
    # Check each 0.5 mm axial slice against fixed geometry and the redesignable cover separately.
    bypass_full_height_shaft_scan = []
    bypass_axis_candidates = [(90, 9.0), (270, -9.0)]
    bypass_shaft_radii_mm = [0.5, 0.75, 1.0, 1.25, 1.5]
    bypass_z_starts_mm = [round(i * 0.5, 4) for i in range(44)]  # 0.0 .. 21.5
    bypass_obstacles = [("main_body", editable_solids["main_body"])] + list(frozen_encoder_solids.items()) + [("cover", editable_solids["cover"])]
    for angle_deg, axis_y in bypass_axis_candidates:
        for radius in bypass_shaft_radii_mm:
            for z0 in bypass_z_starts_mm:
                probe = cq.Solid.makeCylinder(radius, 0.5,
                    cq.Vector(24.5, axis_y, z0), cq.Vector(0, 0, 1))
                checks = []
                for obstacle_name, obstacle in bypass_obstacles:
                    try:
                        overlap = float(probe.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        overlap, error = None, str(exc)
                    checks.append({
                        "obstacle": obstacle_name,
                        "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                        "error": error,
                    })
                bypass_full_height_shaft_scan.append({
                    "angle_deg": angle_deg,
                    "shaft_axis_xy_mm": [24.5, axis_y],
                    "shaft_radius_mm": radius,
                    "shaft_diameter_mm": 2.0 * radius,
                    "z_range_mm": [z0, round(z0 + 0.5, 4)],
                    "checks": checks,
                    "clear_of_checked_geometry": all(
                        item["error"] is None and item["intersection_volume_mm3"] is not None
                        and item["intersection_volume_mm3"] <= 1e-6 for item in checks
                    ),
                })
    # Test a matched 1:1 gear-blank pair at 9 mm center distance (module 0.5, 18/18 teeth).
    # The 10 mm pitch diameter / 2 mm face-width blanks are spatial envelopes only;
    # actual involute teeth and meshing clearance are not modeled here.
    bypass_gear_pair_checks = []
    bypass_gear_z_min_mm = 16.0
    bypass_gear_face_width_mm = 2.0
    bypass_gear_radius_mm = 5.0
    for angle_deg, input_y in bypass_axis_candidates:
        gear_rows = []
        for gear_name, gx, gy in (
            ("output", 24.5, 0.0),
            ("input", 24.5, input_y),
        ):
            blank = cq.Solid.makeCylinder(
                bypass_gear_radius_mm, bypass_gear_face_width_mm,
                cq.Vector(gx, gy, bypass_gear_z_min_mm), cq.Vector(0, 0, 1)
            )
            checks = []
            for obstacle_name, obstacle in bypass_obstacles:
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "blank_diameter_mm": 2.0 * bypass_gear_radius_mm,
                "z_range_mm": [bypass_gear_z_min_mm, bypass_gear_z_min_mm + bypass_gear_face_width_mm],
                "obstacle_checks": checks,
                "clear_of_checked_geometry": all(
                    item["error"] is None and item["intersection_volume_mm3"] is not None
                    and item["intersection_volume_mm3"] <= 1e-6 for item in checks
                ),
            })
        bypass_gear_pair_checks.append({
            "angle_deg": angle_deg,
            "center_distance_mm": abs(input_y),
            "candidate_gear_spec": "module 0.5, 18/18 teeth, 1:1, 20 degree pressure angle",
            "gear_face_width_mm": bypass_gear_face_width_mm,
            "z_range_mm": [bypass_gear_z_min_mm, bypass_gear_z_min_mm + bypass_gear_face_width_mm],
            "gears": gear_rows,
            "both_blanks_clear_of_checked_geometry": all(row["clear_of_checked_geometry"] for row in gear_rows),
            "limitations": [
                "Cylindrical blank envelope only; involute tooth geometry and mesh are not modeled",
                "Bearing seats, shoulders, hubs, fasteners and gearbox walls are not included",
                "Cover is redesignable but still checked as the current envelope"
            ]
        })

    # Re-check the confirmed 10 mm +X input-axis layout. The prior +/-Y=9 mm
    # scan is an alternate geometry study and must not replace this design baseline.
    moved_shutter_dial = solids[3].translate((10.0, 0.0, 0.0))
    moved_shutter_dial_checks = []
    moved_dial_obstacles = [("main_body", solids[5]), ("encoder_button", solids[1]),
                            ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                            ("current_cover", solids[4])]
    for obstacle_name, obstacle in moved_dial_obstacles:
        try:
            overlap = float(moved_shutter_dial.intersect(obstacle).Volume())
            distance = float(moved_shutter_dial.distance(obstacle))
            error = None
        except Exception as exc:
            overlap, distance, error = None, None, str(exc)
        moved_shutter_dial_checks.append({
            "obstacle": obstacle_name,
            "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
            "minimum_distance_mm": round(distance, 9) if distance is not None else None,
            "error": error,
        })

    # Full-height shaft corridor for the actual target input axis at (34.5, 0).
    true_input_axis_full_height_scan = []
    true_input_axis_xy = (34.5, 0.0)
    true_input_shaft_radii_mm = [0.5, 0.75, 1.0, 1.25, 1.5]
    true_input_z_starts_mm = [round(i * 0.5, 4) for i in range(44)]
    true_input_obstacles = [("main_body", solids[5]), ("encoder_button", solids[1]),
                            ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                            ("current_cover", solids[4])]
    for radius in true_input_shaft_radii_mm:
        for z0 in true_input_z_starts_mm:
            probe = cq.Solid.makeCylinder(radius, 0.5,
                cq.Vector(true_input_axis_xy[0], true_input_axis_xy[1], z0), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in true_input_obstacles:
                try:
                    overlap = float(probe.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            true_input_axis_full_height_scan.append({
                "axis_xy_mm": list(true_input_axis_xy),
                "shaft_diameter_mm": 2.0 * radius,
                "z_range_mm": [z0, round(z0 + 0.5, 4)],
                "checks": checks,
                "clear_of_checked_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in checks
                ),
            })

    # Compare candidate 10 mm-center-distance gear planes against the actual
    # +X-translated shutter dial. Cylindrical blanks are envelopes, not tooth geometry.
    true_10mm_gear_pair_height_scan = []
    true_gear_centers = {"output": (24.5, 0.0), "input": (34.5, 0.0)}
    true_gear_z_starts_mm = [round(13.0 + i * 0.25, 4) for i in range(21)]  # 13.0..18.0
    true_gear_radius_mm = 5.5
    true_gear_width_mm = 2.0
    true_gear_fixed_obstacles = [("main_body", solids[5]), ("encoder_button", solids[1]),
                                 ("encoder_dial", solids[2]), ("encoder_bracket", solids[6])]
    for z0 in true_gear_z_starts_mm:
        gear_rows = []
        for gear_name, (gx, gy) in true_gear_centers.items():
            blank = cq.Solid.makeCylinder(true_gear_radius_mm, true_gear_width_mm,
                cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            fixed_checks = []
            for obstacle_name, obstacle in true_gear_fixed_obstacles:
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                fixed_checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            redesignable_checks = []
            for obstacle_name, obstacle in (("current_cover", solids[4]),
                                             ("translated_shutter_dial", moved_shutter_dial)):
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                redesignable_checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "blank_diameter_mm": 2.0 * true_gear_radius_mm,
                "z_range_mm": [z0, round(z0 + true_gear_width_mm, 4)],
                "fixed_geometry_checks": fixed_checks,
                "redesignable_geometry_checks": redesignable_checks,
                "clear_of_fixed_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in fixed_checks
                ),
            })
        true_10mm_gear_pair_height_scan.append({
            "center_distance_mm": 10.0,
            "candidate_gear_spec": "module 0.5, 20/20 teeth, 1:1, 20 degree pressure angle",
            "z_range_mm": [z0, round(z0 + true_gear_width_mm, 4)],
            "gears": gear_rows,
            "both_blanks_clear_of_fixed_geometry": all(x["clear_of_fixed_geometry"] for x in gear_rows),
        })

    # Evaluate a thin gear layer immediately below the translated shutter dial's
    # blind-hole floor. The original pin hole is preserved at (28,0), radius 0.9,
    # Z=17.1..20.9; this cylinder is a conservative occupied-pin envelope.
    gear_layer_pin_clearance_scan = []
    pin_envelope = cq.Solid.makeCylinder(0.9, 3.8, cq.Vector(28.0, 0.0, 17.1), cq.Vector(0, 0, 1))
    thin_gear_width_mm = 1.0
    for z0 in [15.9, 16.0, 16.1, 16.2, 16.5, 17.0]:
        gear_rows = []
        for gear_name, (gx, gy) in true_gear_centers.items():
            blank = cq.Solid.makeCylinder(5.5, thin_gear_width_mm,
                cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in (
                ("main_body", solids[5]), ("encoder_button", solids[1]),
                ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                ("current_cover", solids[4]), ("translated_shutter_dial", moved_shutter_dial),
                ("preserved_pin_hole_envelope", pin_envelope)
            ):
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "blank_diameter_mm": 11.0,
                "z_range_mm": [z0, round(z0 + thin_gear_width_mm, 4)],
                "checks": checks,
            })
        gear_layer_pin_clearance_scan.append({
            "center_distance_mm": 10.0,
            "gear_spec_candidate": "module 0.5, 20/20 teeth, 1:1, 20 degree pressure angle",
            "face_width_mm": thin_gear_width_mm,
            "z_range_mm": [z0, round(z0 + thin_gear_width_mm, 4)],
            "pin_envelope": {"center_xy_mm": [28.0, 0.0], "radius_mm": 0.9, "z_range_mm": [17.1, 20.9]},
            "gears": gear_rows,
        })

    # Higher gear layer above the translated shutter dial. The dial occupies
    # the original Z band, so test whether a 10 mm pair can sit above it.
    high_gear_layer_scan = []
    high_gear_z_starts_mm = [round(20.5 + i * 0.25, 4) for i in range(13)]  # 20.5..23.5
    high_gear_centers = {"output": (24.5, 0.0), "input": (34.5, 0.0)}
    for z0 in high_gear_z_starts_mm:
        gear_rows = []
        for gear_name, (gx, gy) in high_gear_centers.items():
            blank = cq.Solid.makeCylinder(5.5, 2.0,
                cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in [
                ("main_body", solids[5]), ("encoder_button", solids[1]),
                ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                ("translated_shutter_dial", moved_shutter_dial),
                ("current_cover", solids[4]),
                ("preserved_pin_hole_envelope", pin_envelope),
            ]:
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "blank_diameter_mm": 11.0,
                "z_range_mm": [z0, round(z0 + 2.0, 4)],
                "checks": checks,
                "clear_of_fixed_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6
                    for x in checks if x["obstacle"] in
                    ("main_body", "encoder_button", "encoder_dial", "encoder_bracket")
                ),
                "clear_of_translated_dial": next(x for x in checks if x["obstacle"] == "translated_shutter_dial")["intersection_volume_mm3"] <= 1e-6,
                "clear_of_current_cover": next(x for x in checks if x["obstacle"] == "current_cover")["intersection_volume_mm3"] <= 1e-6,
            })
        high_gear_layer_scan.append({
            "z_range_mm": [z0, round(z0 + 2.0, 4)],
            "gears": gear_rows,
        })

    # Fine axial window around the body-clear threshold and the preserved pin-hole floor.
    true_gear_axial_window_scan = []
    for z0 in [round(15.5 + i * 0.05, 4) for i in range(15)]:  # 15.50..16.20
        true_window_gear_rows = []
        for gear_name, (gx, gy) in true_gear_centers.items():
            blank = cq.Solid.makeCylinder(5.5, 1.0,
                cq.Vector(gx, gy, z0), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in (
                ("main_body", solids[5]), ("encoder_button", solids[1]),
                ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                ("current_cover", solids[4]), ("translated_shutter_dial", moved_shutter_dial),
                ("preserved_pin_hole_envelope", pin_envelope)
            ):
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            true_window_gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "z_range_mm": [z0, round(z0 + 1.0, 4)],
                "checks": checks,
            })
        true_gear_axial_window_scan.append({
            "face_width_mm": 1.0,
            "center_distance_mm": 10.0,
            "z_range_mm": [z0, round(z0 + 1.0, 4)],
            "gears": true_window_gear_rows,
        })

    # Compare thin gear-face widths at a conservative Z=16.0 mm start.
    # The remaining web to the blind-hole floor is a geometric reserve, not a strength rating.
    thin_gear_width_sweep = []
    thin_gear_start_z_mm = 16.0
    for face_width in [0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
        gear_rows = []
        for gear_name, (gx, gy) in true_gear_centers.items():
            blank = cq.Solid.makeCylinder(5.5, face_width,
                cq.Vector(gx, gy, thin_gear_start_z_mm), cq.Vector(0, 0, 1))
            checks = []
            for obstacle_name, obstacle in (
                ("main_body", solids[5]), ("encoder_button", solids[1]),
                ("encoder_dial", solids[2]), ("encoder_bracket", solids[6]),
                ("current_cover", solids[4]), ("translated_shutter_dial", moved_shutter_dial),
                ("preserved_pin_hole_envelope", pin_envelope)
            ):
                try:
                    overlap = float(blank.intersect(obstacle).Volume())
                    distance = float(blank.distance(obstacle)) if obstacle_name in (
                        "main_body", "preserved_pin_hole_envelope"
                    ) else None
                    error = None
                except Exception as exc:
                    overlap, distance, error = None, None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "minimum_distance_mm": round(distance, 9) if distance is not None else None,
                    "error": error,
                })
            gear_rows.append({
                "gear": gear_name,
                "center_xy_mm": [gx, gy],
                "face_width_mm": face_width,
                "z_range_mm": [thin_gear_start_z_mm, round(thin_gear_start_z_mm + face_width, 4)],
                "remaining_axial_gap_to_pin_floor_mm": round(17.1 - (thin_gear_start_z_mm + face_width), 4),
                "checks": checks,
            })
        thin_gear_width_sweep.append({
            "face_width_mm": face_width,
            "z_range_mm": [thin_gear_start_z_mm, round(thin_gear_start_z_mm + face_width, 4)],
            "remaining_axial_gap_to_pin_floor_mm": round(17.1 - (thin_gear_start_z_mm + face_width), 4),
            "gears": gear_rows,
        })

    # Directly section the translated shutter dial around the two gear footprints
    # and the preserved pin-hole entry. These are exact B-rep intersections with
    # thin slabs; area estimates are volume/slab-thickness approximations.
    shutter_dial_horizontal_sections = []
    shutter_section_z_values = [16.10, 16.15, 16.25, 16.50, 16.75, 17.00, 17.05, 17.10, 17.20, 17.50, 18.00, 20.80]
    shutter_section_xy_roi = {"x_mm": [18.0, 45.0], "y_mm": [-8.0, 8.0]}
    shutter_section_thickness = 0.02
    gear_footprints = {
        "output": cq.Solid.makeCylinder(5.5, 5.5, cq.Vector(24.5, 0.0, 15.5), cq.Vector(0, 0, 1)),
        "input": cq.Solid.makeCylinder(5.5, 5.5, cq.Vector(34.5, 0.0, 15.5), cq.Vector(0, 0, 1)),
    }
    for z_center in shutter_section_z_values:
        slab = cq.Solid.makeBox(
            27.0, 16.0, shutter_section_thickness,
            cq.Vector(18.0, -8.0, z_center - shutter_section_thickness / 2.0)
        )
        try:
            section = moved_shutter_dial.intersect(slab)
            section_solids = section.Solids() or ([section] if section.Volume() > 1e-8 else [])
            gear_rows = {}
            for gear_name, footprint in gear_footprints.items():
                overlap = section.intersect(footprint)
                gear_rows[gear_name] = {
                    "material_area_estimate_mm2": round(float(overlap.Volume()) / shutter_section_thickness, 6),
                    "overlap_volume_mm3": round(float(overlap.Volume()), 9),
                    "components": [{
                        "bbox_mm": bbox(component),
                        "area_estimate_mm2": round(float(component.Volume()) / shutter_section_thickness, 6),
                    } for component in (overlap.Solids() or ([overlap] if overlap.Volume() > 1e-8 else []))],
                }
            pin_overlap = section.intersect(pin_envelope)
            shutter_dial_horizontal_sections.append({
                "z_center_mm": z_center,
                "slab_thickness_mm": shutter_section_thickness,
                "material_area_estimate_mm2": round(float(section.Volume()) / shutter_section_thickness, 6),
                "material_components": [{
                    "bbox_mm": bbox(component),
                    "area_estimate_mm2": round(float(component.Volume()) / shutter_section_thickness, 6),
                } for component in section_solids],
                "gear_footprint_material": gear_rows,
                "pin_envelope_overlap_volume_mm3": round(float(pin_overlap.Volume()), 9),
                "error": None,
            })
        except Exception as exc:
            shutter_dial_horizontal_sections.append({"z_center_mm": z_center, "error": str(exc)})

    shutter_dial_vertical_sections = []
    shutter_section_y_values = [-5.0, -3.0, -1.0, -0.5, 0.0, 0.5, 1.0, 3.0, 5.0]
    vertical_section_thickness = 0.05
    for y_center in shutter_section_y_values:
        slab = cq.Solid.makeBox(
            27.0, vertical_section_thickness, 5.5,
            cq.Vector(18.0, y_center - vertical_section_thickness / 2.0, 15.5)
        )
        try:
            section = moved_shutter_dial.intersect(slab)
            section_solids = section.Solids() or ([section] if section.Volume() > 1e-8 else [])
            gear_rows = {}
            for gear_name, (gx, gy) in {"output": (24.5, 0.0), "input": (34.5, 0.0)}.items():
                gear_probe = cq.Solid.makeCylinder(
                    5.5, 1.1, cq.Vector(gx, gy, 16.0), cq.Vector(0, 0, 1)
                )
                overlap = section.intersect(gear_probe)
                gear_rows[gear_name] = {
                    "material_area_estimate_mm2": round(float(overlap.Volume()) / vertical_section_thickness, 6),
                    "overlap_volume_mm3": round(float(overlap.Volume()), 9),
                    "components": [{
                        "bbox_mm": bbox(component),
                        "area_estimate_mm2": round(float(component.Volume()) / vertical_section_thickness, 6),
                    } for component in (overlap.Solids() or ([overlap] if overlap.Volume() > 1e-8 else []))],
                }
            pin_overlap = section.intersect(pin_envelope)
            shutter_dial_vertical_sections.append({
                "y_center_mm": y_center,
                "slab_thickness_mm": vertical_section_thickness,
                "material_area_estimate_mm2": round(float(section.Volume()) / vertical_section_thickness, 6),
                "material_components": [{
                    "bbox_mm": bbox(component),
                    "area_estimate_mm2": round(float(component.Volume()) / vertical_section_thickness, 6),
                } for component in section_solids],
                "gear_footprint_material": gear_rows,
                "pin_envelope_overlap_volume_mm3": round(float(pin_overlap.Volume()), 9),
                "error": None,
            })
        except Exception as exc:
            shutter_dial_vertical_sections.append({"y_center_mm": y_center, "error": str(exc)})

    # Fine offset sections around Y=0. The previous 0.05 mm slab at exact
    # symmetry produced an isolated zero-area result for the output footprint;
    # use thinner, offset slabs to distinguish a B-rep symmetry artifact.
    shutter_dial_vertical_fine_sections = []
    fine_y_values = [-0.5, -0.25, -0.1, -0.05, 0.05, 0.1, 0.25, 0.5]
    fine_section_thickness = 0.01
    for y_center in fine_y_values:
        slab = cq.Solid.makeBox(
            27.0, fine_section_thickness, 1.1,
            cq.Vector(18.0, y_center - fine_section_thickness / 2.0, 16.0)
        )
        try:
            section = moved_shutter_dial.intersect(slab)
            gear_rows = {}
            for gear_name, (gx, gy) in {"output": (24.5, 0.0), "input": (34.5, 0.0)}.items():
                probe = cq.Solid.makeCylinder(5.5, 1.1, cq.Vector(gx, gy, 16.0), cq.Vector(0, 0, 1))
                overlap = section.intersect(probe)
                parts = overlap.Solids() or ([overlap] if overlap.Volume() > 1e-8 else [])
                gear_rows[gear_name] = {
                    "material_area_estimate_mm2": round(float(overlap.Volume()) / fine_section_thickness, 6),
                    "components": [{"bbox_mm": bbox(part), "area_estimate_mm2": round(float(part.Volume()) / fine_section_thickness, 6)} for part in parts],
                }
            shutter_dial_vertical_fine_sections.append({"y_center_mm": y_center, "slab_thickness_mm": fine_section_thickness, "gear_footprint_material": gear_rows, "error": None})
        except Exception as exc:
            shutter_dial_vertical_fine_sections.append({"y_center_mm": y_center, "error": str(exc)})

    # Radial material sampling around the preserved pin-hole axis. Annuli are
    # probes only: no hole or material is modified. Values are average material
    # cross-sectional areas over the existing pin-envelope Z interval.
    pin_radial_material_scan = []
    pin_center_x, pin_center_y = 28.0, 0.0
    pin_z0, pin_z1 = 17.1, 20.9
    pin_inner_radius = 0.9
    radial_edges = [0.9, 1.1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    for inner_r, outer_r in zip(radial_edges[:-1], radial_edges[1:]):
        outer = cq.Solid.makeCylinder(outer_r, pin_z1 - pin_z0, cq.Vector(pin_center_x, pin_center_y, pin_z0), cq.Vector(0, 0, 1))
        inner = cq.Solid.makeCylinder(inner_r, pin_z1 - pin_z0, cq.Vector(pin_center_x, pin_center_y, pin_z0), cq.Vector(0, 0, 1))
        annulus = outer.cut(inner)
        try:
            overlap = moved_shutter_dial.intersect(annulus)
            pin_radial_material_scan.append({
                "radial_band_mm": [inner_r, outer_r],
                "z_range_mm": [pin_z0, pin_z1],
                "material_volume_mm3": round(float(overlap.Volume()), 6),
                "average_material_area_mm2": round(float(overlap.Volume()) / (pin_z1 - pin_z0), 6),
                "components": [{"bbox_mm": bbox(part), "volume_mm3": round(float(part.Volume()), 6)} for part in (overlap.Solids() or ([overlap] if overlap.Volume() > 1e-8 else []))],
                "error": None,
            })
        except Exception as exc:
            pin_radial_material_scan.append({"radial_band_mm": [inner_r, outer_r], "error": str(exc)})

    # Map the input-gear footprint's existing central gap through the full
    # shutter-dial thickness using thin horizontal slabs.
    input_gap_z_sweep = []
    gap_roi = cq.Solid.makeBox(4.0, 11.0, 0.02, cq.Vector(32.0, -5.5, 16.09))
    gap_z_values = [round(16.1 + 0.1 * i, 2) for i in range(49)]
    for z_center in gap_z_values:
        slab = cq.Solid.makeBox(4.0, 11.0, 0.02, cq.Vector(32.0, -5.5, z_center - 0.01))
        try:
            section = moved_shutter_dial.intersect(slab)
            parts = section.Solids() or ([section] if section.Volume() > 1e-8 else [])
            input_gap_z_sweep.append({
                "z_center_mm": z_center,
                "material_area_estimate_mm2": round(float(section.Volume()) / 0.02, 6),
                "components": [{"bbox_mm": bbox(part), "area_estimate_mm2": round(float(part.Volume()) / 0.02, 6)} for part in parts],
                "error": None,
            })
        except Exception as exc:
            input_gap_z_sweep.append({"z_center_mm": z_center, "error": str(exc)})

    # Localize the known input-footprint gap by measuring missing material,
    # not merely connected material in the wider rectangular ROI above.
    # The ROI encloses the central gap observed in the offset X-Z sections.
    # This is a diagnostic probe only; it does not alter the shutter dial.
    input_gap_local_void_sweep = []
    local_gap_roi = {
        "x_mm": [33.0, 36.0],
        "y_mm": [-1.5, 1.5],
        "z_mm": [16.1, 20.9],
    }
    for z_center in gap_z_values:
        probe = cq.Solid.makeBox(
            3.0, 3.0, 0.02,
            cq.Vector(33.0, -1.5, z_center - 0.01)
        )
        try:
            missing = probe.cut(moved_shutter_dial)
            parts = missing.Solids() or ([missing] if missing.Volume() > 1e-8 else [])
            input_gap_local_void_sweep.append({
                "z_center_mm": z_center,
                "missing_area_estimate_mm2": round(float(missing.Volume()) / 0.02, 6),
                "void_components": [
                    {
                        "bbox_mm": bbox(part),
                        "area_estimate_mm2": round(float(part.Volume()) / 0.02, 6),
                    }
                    for part in parts
                ],
                "error": None,
            })
        except Exception as exc:
            input_gap_local_void_sweep.append({
                "z_center_mm": z_center,
                "error": str(exc),
            })

    # Expand the local void ROI across the full nearby Y span and refine Z
    # sampling around the previously observed gap termination. This measures
    # missing material directly and remains diagnostic-only.
    input_gap_expanded_void_sweep = []
    expanded_gap_roi = {
        "x_mm": [33.0, 36.0],
        "y_mm": [-5.5, 5.5],
        "z_mm": [16.0, 20.3],
    }
    expanded_gap_z_step = 0.05
    expanded_gap_slab_thickness = 0.02
    expanded_gap_z_values = [
        round(16.0 + expanded_gap_z_step * i, 2)
        for i in range(87)
    ]
    for z_center in expanded_gap_z_values:
        probe = cq.Solid.makeBox(
            3.0, 11.0, expanded_gap_slab_thickness,
            cq.Vector(33.0, -5.5, z_center - expanded_gap_slab_thickness / 2.0)
        )
        try:
            missing = probe.cut(moved_shutter_dial)
            parts = missing.Solids() or ([missing] if missing.Volume() > 1e-8 else [])
            input_gap_expanded_void_sweep.append({
                "z_center_mm": z_center,
                "missing_area_estimate_mm2": round(
                    float(missing.Volume()) / expanded_gap_slab_thickness, 6
                ),
                "void_components": [
                    {
                        "bbox_mm": bbox(part),
                        "area_estimate_mm2": round(
                            float(part.Volume()) / expanded_gap_slab_thickness, 6
                        ),
                    }
                    for part in parts
                ],
                "error": None,
            })
        except Exception as exc:
            input_gap_expanded_void_sweep.append({
                "z_center_mm": z_center,
                "error": str(exc),
            })

    # Cross-sections of the material bridge between the fixed output axis and
    # the preserved pin-hole axis. Offset from exact Y=0 to avoid the known
    # symmetry-plane Boolean artifact. These are diagnostics, not cut geometry.
    output_pin_bridge_sections = []
    bridge_roi = cq.Solid.makeBox(7.0, 0.01, 4.8, cq.Vector(22.0, -0.005, 16.1))
    for y_center in [-0.1, -0.05, 0.05, 0.1]:
        slab = cq.Solid.makeBox(7.0, 0.01, 4.8, cq.Vector(22.0, y_center - 0.005, 16.1))
        try:
            section = moved_shutter_dial.intersect(slab)
            parts = section.Solids() or ([section] if section.Volume() > 1e-8 else [])
            output_pin_bridge_sections.append({
                "y_center_mm": y_center,
                "slab_thickness_mm": 0.01,
                "material_area_estimate_mm2": round(float(section.Volume()) / 0.01, 6),
                "components": [{"bbox_mm": bbox(part), "area_estimate_mm2": round(float(part.Volume()) / 0.01, 6)} for part in parts],
                "error": None,
            })
        except Exception as exc:
            output_pin_bridge_sections.append({"y_center_mm": y_center, "error": str(exc)})

    shutter_dial_local_section_analysis = {
        "source_entity": "translated shutter dial #84 analysis copy; source STEP remains unchanged",
        "translation_mm": [10.0, 0.0, 0.0],
        "output_gear_center_xy_mm": [24.5, 0.0],
        "input_gear_center_xy_mm": [34.5, 0.0],
        "gear_blank_radius_mm": 5.5,
        "horizontal_section_roi_mm": shutter_section_xy_roi,
        "horizontal_section_thickness_mm": shutter_section_thickness,
        "horizontal_sections": shutter_dial_horizontal_sections,
        "vertical_section_roi_mm": {"x_mm": [18.0, 45.0], "z_mm": [15.5, 21.0]},
        "vertical_section_thickness_mm": vertical_section_thickness,
        "vertical_sections": shutter_dial_vertical_sections,
        "vertical_fine_sections": shutter_dial_vertical_fine_sections,
        "vertical_fine_section_thickness_mm": fine_section_thickness,
        "pin_radial_material_scan": pin_radial_material_scan,
        "input_gap_z_sweep": input_gap_z_sweep,
        "input_gap_z_sweep_step_mm": 0.1,
        "input_gap_local_void_sweep": input_gap_local_void_sweep,
        "input_gap_local_void_sweep_roi_mm": local_gap_roi,
        "input_gap_expanded_void_sweep": input_gap_expanded_void_sweep,
        "input_gap_expanded_void_sweep_roi_mm": expanded_gap_roi,
        "input_gap_expanded_void_sweep_z_step_mm": expanded_gap_z_step,
        "input_gap_expanded_void_sweep_slab_thickness_mm": expanded_gap_slab_thickness,
        "output_pin_bridge_sections": output_pin_bridge_sections,
        "pin_hole_entry_plane_z_mm": 17.1,
        "pin_hole_envelope": {"center_xy_mm": [28.0, 0.0], "radius_mm": 0.9, "z_range_mm": [17.1, 20.9]},
        "interpretation": [
            "Z=17.1 mm is the lower opening/entry plane of the preserved blind hole, not its closed blind end.",
            "Section area is estimated from exact B-rep slab intersection volume divided by slab thickness; it is not a minimum-wall-thickness or strength measurement.",
            "Gear footprint material is the portion of the translated shutter dial lying inside an 11 mm diameter cylindrical footprint; it is not a proposed cut or final gear geometry.",
            "The pin envelope is a conservative occupied-space check; it does not assert the measured metal rod diameter."
        ]
    }

    # High-layer gear alternative: include the preserved blind-hole / pin envelope,
    # then test whether the fixed output axis can be extended up to the gear plane.
    # The existing cover is redesignable and is intentionally not treated as fixed.
    high_gear_output_shaft_checks = []
    high_gear_output_axis_xy = (24.5, 0.0)
    high_gear_output_shaft_z_range = (0.0, 21.5)
    for shaft_radius in [0.5, 0.75, 1.0, 1.25, 1.5]:
        shaft = cq.Solid.makeCylinder(
            shaft_radius,
            high_gear_output_shaft_z_range[1] - high_gear_output_shaft_z_range[0],
            cq.Vector(high_gear_output_axis_xy[0], high_gear_output_axis_xy[1], high_gear_output_shaft_z_range[0]),
            cq.Vector(0, 0, 1),
        )
        checks = []
        for obstacle_name, obstacle in (
            ("main_body", solids[5]),
            ("encoder_button", solids[1]),
            ("encoder_dial", solids[2]),
            ("encoder_bracket", solids[6]),
            ("translated_shutter_dial", moved_shutter_dial),
        ):
            try:
                overlap = float(shaft.intersect(obstacle).Volume())
                error = None
            except Exception as exc:
                overlap, error = None, str(exc)
            checks.append({
                "obstacle": obstacle_name,
                "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                "error": error,
            })
        high_gear_output_shaft_checks.append({
            "axis_xy_mm": list(high_gear_output_axis_xy),
            "shaft_diameter_mm": round(2.0 * shaft_radius, 3),
            "z_range_mm": list(high_gear_output_shaft_z_range),
            "checks": checks,
            "clear_of_checked_geometry": all(
                x["error"] is None and x["intersection_volume_mm3"] is not None
                and x["intersection_volume_mm3"] <= 1e-6 for x in checks
            ),
        })

    # Segment the output-axis corridor by height so intentional integral
    # material overlap can be distinguished from a genuinely blocked shaft path.
    segmented_output_axis_checks = []
    output_axis_xy = (24.5, 0.0)
    output_axis_diameters = [1.0, 1.5, 2.0, 2.5, 3.0]
    output_axis_z_edges = [round(i * 0.5, 3) for i in range(44)]  # 0.0..21.5
    output_axis_obstacles = (
        ("main_body", solids[5]),
        ("encoder_button", solids[1]),
        ("encoder_dial", solids[2]),
        ("encoder_bracket", solids[6]),
        ("translated_shutter_dial", moved_shutter_dial),
    )
    for z0, z1 in zip(output_axis_z_edges, output_axis_z_edges[1:]):
        for diameter in output_axis_diameters:
            shaft_slice = cq.Solid.makeCylinder(
                diameter / 2.0, z1 - z0,
                cq.Vector(output_axis_xy[0], output_axis_xy[1], z0),
                cq.Vector(0, 0, 1),
            )
            checks = []
            for obstacle_name, obstacle in output_axis_obstacles:
                try:
                    overlap = float(shaft_slice.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
            segmented_output_axis_checks.append({
                "axis_xy_mm": list(output_axis_xy),
                "shaft_diameter_mm": diameter,
                "z_range_mm": [z0, z1],
                "checks": checks,
                "clear_of_all_checked_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in checks
                ),
            })

    high_gear_input_stub_checks = []
    high_gear_input_axis_xy = (34.5, 0.0)
    high_gear_input_stub_z_range = (20.9, 21.5)
    for shaft_radius in [0.5, 0.75, 1.0, 1.25, 1.5]:
        stub = cq.Solid.makeCylinder(
            shaft_radius,
            high_gear_input_stub_z_range[1] - high_gear_input_stub_z_range[0],
            cq.Vector(high_gear_input_axis_xy[0], high_gear_input_axis_xy[1], high_gear_input_stub_z_range[0]),
            cq.Vector(0, 0, 1),
        )
        checks = []
        for obstacle_name, obstacle in (
            ("main_body", solids[5]),
            ("encoder_button", solids[1]),
            ("encoder_dial", solids[2]),
            ("encoder_bracket", solids[6]),
            ("translated_shutter_dial", moved_shutter_dial),
            ("preserved_pin_hole_envelope", pin_envelope),
        ):
            try:
                overlap = float(stub.intersect(obstacle).Volume())
                error = None
            except Exception as exc:
                overlap, error = None, str(exc)
            checks.append({
                "obstacle": obstacle_name,
                "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                "error": error,
            })
        high_gear_input_stub_checks.append({
            "axis_xy_mm": list(high_gear_input_axis_xy),
            "shaft_diameter_mm": round(2.0 * shaft_radius, 3),
            "z_range_mm": list(high_gear_input_stub_z_range),
            "checks": checks,
            "clear_of_checked_geometry": all(
                x["error"] is None and x["intersection_volume_mm3"] is not None
                and x["intersection_volume_mm3"] <= 1e-6 for x in checks
            ),
        })

    # Exploratory input-side bridge hub candidates. The bridge intentionally
    # overlaps the translated shutter dial at the two ends of the measured gap;
    # no source solid is modified. Sweep the dial+bridge at 15-degree increments.
    input_bridge_hub_candidate_scan = []
    input_bridge_sweep_by_bridge_width = {}
    bridge_widths_mm = [0.6, 0.8, 1.0]
    bridge_span_y_mm = 6.0
    bridge_z_min_mm = 18.0
    bridge_thickness_z_mm = 0.6
    bridge_center_x_mm = 34.5
    bridge_center_y_mm = 0.0
    input_hub_shaft_diameters_mm = [1.5, 1.8, 2.0]
    input_hub_shaft_z_min_mm = 18.0
    input_hub_shaft_z_max_mm = 21.2
    input_hub_gear_diameter_mm = 11.0
    input_hub_gear_z_min_mm = 21.0
    input_hub_gear_width_mm = 2.0
    bridge_fixed_obstacles = [
        ("main_body", solids[5]),
        ("encoder_button", solids[1]),
        ("encoder_dial", solids[2]),
        ("encoder_bracket", solids[6]),
    ]
    bridge_redesignable_obstacles = [("current_cover", solids[4])]

    for bridge_width_mm in bridge_widths_mm:
        bridge = cq.Solid.makeBox(
            bridge_width_mm, bridge_span_y_mm, bridge_thickness_z_mm,
            cq.Vector(bridge_center_x_mm - bridge_width_mm / 2.0,
                      bridge_center_y_mm - bridge_span_y_mm / 2.0,
                      bridge_z_min_mm),
        )
        try:
            bridge_dial_overlap = float(bridge.intersect(moved_shutter_dial).Volume())
            moving_dial_bridge = moved_shutter_dial.fuse(bridge)
            moving_fuse_valid = bool(moving_dial_bridge.isValid())
            moving_fuse_solid_count = len(moving_dial_bridge.Solids())
            moving_fuse_error = None
        except Exception as exc:
            bridge_dial_overlap = None
            moving_dial_bridge = None
            moving_fuse_valid = False
            moving_fuse_solid_count = None
            moving_fuse_error = str(exc)

        sweep_rows = []
        bridge_only_cover_sweep = []
        dial_only_cover_baseline_sweep = []
        bridge_dial_engagement = {
            "intersection_volume_mm3": None,
            "intersection_valid": False,
            "intersection_solid_count": None,
            "intersection_components_bbox_mm": [],
            "z_slice_scan": [],
        }
        if moving_dial_bridge is not None:
            try:
                engagement = bridge.intersect(moved_shutter_dial)
                bridge_dial_engagement.update({
                    "intersection_volume_mm3": round(float(engagement.Volume()), 9),
                    "intersection_valid": bool(engagement.isValid()),
                    "intersection_solid_count": len(engagement.Solids()),
                    "intersection_components_bbox_mm": [bbox(x) for x in engagement.Solids()],
                })
                # Thin Z slices localize where the bridge actually engages the
                # existing dial material; these are section samples, not strength data.
                for slice_index in range(7):
                    z0 = round(bridge_z_min_mm + slice_index * 0.1, 4)
                    probe = cq.Solid.makeBox(
                        bridge_width_mm + 0.02, bridge_span_y_mm + 0.02, 0.1,
                        cq.Vector(bridge_center_x_mm - (bridge_width_mm + 0.02) / 2.0,
                                  bridge_center_y_mm - (bridge_span_y_mm + 0.02) / 2.0,
                                  z0),
                    )
                    section = engagement.intersect(probe)
                    bridge_dial_engagement["z_slice_scan"].append({
                        "z_range_mm": [z0, round(z0 + 0.1, 4)],
                        "overlap_volume_mm3": round(float(section.Volume()), 9),
                        "overlap_area_equivalent_mm2": round(float(section.Volume()) / 0.1, 9),
                        "component_count": len(section.Solids()),
                        "components_bbox_mm": [bbox(x) for x in section.Solids()],
                    })
            except Exception as exc:
                bridge_dial_engagement["error"] = str(exc)

            for angle_deg in range(0, 360, 15):
                try:
                    rotated_moving = moving_dial_bridge.rotate(
                        (bridge_center_x_mm, bridge_center_y_mm, 0.0),
                        (bridge_center_x_mm, bridge_center_y_mm, 1.0),
                        float(angle_deg),
                    )
                    rotated_bridge = bridge.rotate(
                        (bridge_center_x_mm, bridge_center_y_mm, 0.0),
                        (bridge_center_x_mm, bridge_center_y_mm, 1.0),
                        float(angle_deg),
                    )
                    rotated_dial = moved_shutter_dial.rotate(
                        (bridge_center_x_mm, bridge_center_y_mm, 0.0),
                        (bridge_center_x_mm, bridge_center_y_mm, 1.0),
                        float(angle_deg),
                    )
                    checks = []
                    for obstacle_name, obstacle in bridge_fixed_obstacles + bridge_redesignable_obstacles:
                        try:
                            overlap = float(rotated_moving.intersect(obstacle).Volume())
                            error = None
                        except Exception as exc:
                            overlap, error = None, str(exc)
                        if error is not None or overlap is None or overlap > 1e-6:
                            checks.append({
                                "obstacle": obstacle_name,
                                "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                                "error": error,
                            })
                    try:
                        bridge_cover_overlap = float(rotated_bridge.intersect(solids[4]).Volume())
                        bridge_cover_error = None
                    except Exception as exc:
                        bridge_cover_overlap, bridge_cover_error = None, str(exc)
                    try:
                        dial_cover_overlap = float(rotated_dial.intersect(solids[4]).Volume())
                        dial_cover_error = None
                    except Exception as exc:
                        dial_cover_overlap, dial_cover_error = None, str(exc)
                    bridge_only_cover_sweep.append({
                        "angle_deg": angle_deg,
                        "intersection_volume_mm3": round(bridge_cover_overlap, 9) if bridge_cover_overlap is not None else None,
                        "error": bridge_cover_error,
                    })
                    dial_only_cover_baseline_sweep.append({
                        "angle_deg": angle_deg,
                        "intersection_volume_mm3": round(dial_cover_overlap, 9) if dial_cover_overlap is not None else None,
                        "error": dial_cover_error,
                    })
                    sweep_rows.append({
                        "angle_deg": angle_deg,
                        "collision_count": len(checks),
                        "collisions": checks,
                        "clear_of_frozen_geometry": not any(
                            x["obstacle"] != "current_cover" for x in checks
                        ),
                        "clear_of_current_cover": not any(
                            x["obstacle"] == "current_cover" for x in checks
                        ),
                    })
                except Exception as exc:
                    sweep_rows.append({
                        "angle_deg": angle_deg,
                        "collision_count": 1,
                        "collisions": [{"obstacle": "rotation_or_boolean",
                                        "intersection_volume_mm3": None, "error": str(exc)}],
                        "clear_of_frozen_geometry": False,
                        "clear_of_current_cover": False,
                    })
                    bridge_only_cover_sweep.append({
                        "angle_deg": angle_deg, "intersection_volume_mm3": None, "error": str(exc)
                    })
                    dial_only_cover_baseline_sweep.append({
                        "angle_deg": angle_deg, "intersection_volume_mm3": None, "error": str(exc)
                    })
        input_bridge_sweep_by_bridge_width[str(bridge_width_mm)] = {
            "bridge_width_x_mm": bridge_width_mm,
            "bridge_span_y_mm": bridge_span_y_mm,
            "bridge_z_range_mm": [bridge_z_min_mm, bridge_z_min_mm + bridge_thickness_z_mm],
            "bridge_dial_overlap_mm3": round(bridge_dial_overlap, 9) if bridge_dial_overlap is not None else None,
            "dial_bridge_fuse_valid": moving_fuse_valid,
            "dial_bridge_fuse_solid_count": moving_fuse_solid_count,
            "fuse_error": moving_fuse_error,
            "rotation_step_deg": 15,
            "rotation_samples": len(sweep_rows),
            "rotation_sweep": sweep_rows,
            "bridge_only_cover_sweep": bridge_only_cover_sweep,
            "dial_only_cover_baseline_sweep": dial_only_cover_baseline_sweep,
            "bridge_dial_engagement": bridge_dial_engagement,
            "clear_of_frozen_geometry_all_angles": len(sweep_rows) == 24 and all(x["clear_of_frozen_geometry"] for x in sweep_rows),
            "clear_of_current_cover_all_angles": len(sweep_rows) == 24 and all(x["clear_of_current_cover"] for x in sweep_rows),
        }

        for shaft_diameter_mm in input_hub_shaft_diameters_mm:
            shaft_radius_mm = shaft_diameter_mm / 2.0
            shaft = cq.Solid.makeCylinder(
                shaft_radius_mm,
                input_hub_shaft_z_max_mm - input_hub_shaft_z_min_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_shaft_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            gear_blank = cq.Solid.makeCylinder(
                input_hub_gear_diameter_mm / 2.0,
                input_hub_gear_width_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_gear_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            try:
                shaft_bridge_overlap = float(shaft.intersect(bridge).Volume())
                gear_shaft_overlap = float(gear_blank.intersect(shaft).Volume())
                shaft_dial_overlap = float(shaft.intersect(moved_shutter_dial).Volume())
                candidate_assembly = moving_dial_bridge.fuse(shaft).fuse(gear_blank)
                assembly_valid = bool(candidate_assembly.isValid())
                assembly_solid_count = len(candidate_assembly.Solids())
                assembly_error = None
            except Exception as exc:
                shaft_bridge_overlap = None
                gear_shaft_overlap = None
                shaft_dial_overlap = None
                assembly_valid = False
                assembly_solid_count = None
                assembly_error = str(exc)

            shaft_checks = []
            for obstacle_name, obstacle in bridge_fixed_obstacles + [
                ("translated_shutter_dial", moved_shutter_dial),
                ("preserved_pin_hole_envelope", pin_envelope),
            ]:
                try:
                    overlap = float(shaft.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                shaft_checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })

            gear_checks = []
            for obstacle_name, obstacle in bridge_fixed_obstacles + bridge_redesignable_obstacles + [
                ("translated_shutter_dial", moved_shutter_dial),
                ("preserved_pin_hole_envelope", pin_envelope),
            ]:
                try:
                    overlap = float(gear_blank.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                gear_checks.append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })

            sweep = input_bridge_sweep_by_bridge_width[str(bridge_width_mm)]
            input_bridge_hub_candidate_scan.append({
                "bridge_width_x_mm": bridge_width_mm,
                "bridge_span_y_mm": bridge_span_y_mm,
                "bridge_z_range_mm": [bridge_z_min_mm, bridge_z_min_mm + bridge_thickness_z_mm],
                "shaft_diameter_mm": shaft_diameter_mm,
                "shaft_z_range_mm": [input_hub_shaft_z_min_mm, input_hub_shaft_z_max_mm],
                "gear_blank_diameter_mm": input_hub_gear_diameter_mm,
                "gear_blank_z_range_mm": [input_hub_gear_z_min_mm, input_hub_gear_z_min_mm + input_hub_gear_width_mm],
                "bridge_dial_intentional_overlap_mm3": round(bridge_dial_overlap, 9) if bridge_dial_overlap is not None else None,
                "shaft_bridge_overlap_mm3": round(shaft_bridge_overlap, 9) if shaft_bridge_overlap is not None else None,
                "gear_shaft_overlap_mm3": round(gear_shaft_overlap, 9) if gear_shaft_overlap is not None else None,
                "shaft_dial_overlap_mm3": round(shaft_dial_overlap, 9) if shaft_dial_overlap is not None else None,
                "assembly_valid": assembly_valid,
                "assembly_solid_count": assembly_solid_count,
                "assembly_fuse_error": assembly_error,
                "shaft_checks": shaft_checks,
                "gear_blank_checks": gear_checks,
                "shaft_clear_of_checked_fixed_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in shaft_checks
                    if x["obstacle"] != "translated_shutter_dial"
                ),
                "gear_blank_clear_of_checked_fixed_geometry": all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in gear_checks
                    if x["obstacle"] not in ("current_cover", "translated_shutter_dial")
                ),
                "rotation_sweep_clear_of_frozen_geometry_all_angles": sweep["clear_of_frozen_geometry_all_angles"],
                "rotation_sweep_clear_of_current_cover_all_angles": sweep["clear_of_current_cover_all_angles"],
                "limitations": [
                    "Exploratory additive bridge and shaft geometry only; not a production design",
                    "Gear is an 11 mm cylindrical blank; involute teeth and mesh are not modeled",
                    "15-degree sweep samples are discrete and do not prove continuous swept clearance",
                    "Strength, fatigue, bearing support, fasteners, tolerances and assembly tooling are not assessed",
                    "The bridge-to-dial overlap is intentional; the preserved source dial is never cut or modified",
                ],
            })

    # Next-stage exploratory geometry: root collar/gusset proxies and a
    # re-cut cover blank using a finer sampled rotational envelope. The source
    # STEP solids remain untouched; the cover result is a diagnostic candidate.
    input_bridge_root_transition_scan = []
    root_transition_bridge_widths_mm = [0.6, 1.0]
    root_transition_shaft_diameter_mm = 1.8
    root_transition_collar_radii_mm = [1.2, 1.5, 1.8]
    for bridge_width_mm in root_transition_bridge_widths_mm:
        bridge = cq.Solid.makeBox(
            bridge_width_mm, bridge_span_y_mm, bridge_thickness_z_mm,
            cq.Vector(bridge_center_x_mm - bridge_width_mm / 2.0,
                      bridge_center_y_mm - bridge_span_y_mm / 2.0,
                      bridge_z_min_mm),
        )
        shaft = cq.Solid.makeCylinder(
            root_transition_shaft_diameter_mm / 2.0,
            input_hub_shaft_z_max_mm - input_hub_shaft_z_min_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_shaft_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        gear_blank = cq.Solid.makeCylinder(
            input_hub_gear_diameter_mm / 2.0, input_hub_gear_width_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_gear_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        for collar_radius_mm in root_transition_collar_radii_mm:
            collar = cq.Solid.makeCylinder(
                collar_radius_mm, bridge_thickness_z_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, bridge_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            try:
                candidate = moved_shutter_dial.fuse(bridge).fuse(collar).fuse(shaft).fuse(gear_blank)
                valid = bool(candidate.isValid())
                solid_count = len(candidate.Solids())
                fuse_error = None
            except Exception as exc:
                candidate = None
                valid = False
                solid_count = None
                fuse_error = str(exc)
            checks = []
            if candidate is not None:
                for obstacle_name, obstacle in bridge_fixed_obstacles + [("preserved_pin_hole_envelope", pin_envelope)]:
                    try:
                        volume = float(candidate.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        volume, error = None, str(exc)
                    checks.append({"obstacle": obstacle_name,
                                   "intersection_volume_mm3": round(volume, 9) if volume is not None else None,
                                   "error": error})
            input_bridge_root_transition_scan.append({
                "bridge_width_x_mm": bridge_width_mm,
                "shaft_diameter_mm": root_transition_shaft_diameter_mm,
                "collar_radius_mm": collar_radius_mm,
                "collar_z_range_mm": [bridge_z_min_mm, bridge_z_min_mm + bridge_thickness_z_mm],
                "assembly_valid": valid,
                "assembly_solid_count": solid_count,
                "fuse_error": fuse_error,
                "fixed_geometry_checks": checks,
                "clear_of_checked_frozen_geometry": bool(candidate is not None) and all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in checks
                ),
                "collar_volume_mm3": round(float(collar.Volume()), 9),
                "limitations": ["Cylindrical collar is a reinforcement proxy, not a true tangent fillet",
                                "No stress, fatigue, print anisotropy or torque capacity analysis"],
            })

    input_cover_relief_candidate_scan = []
    cover_relief_rotation_step_deg = 10
    cover_relief_bridge_widths_mm = [0.6, 0.8, 1.0]
    cover_relief_shaft_diameter_mm = 1.8
    for bridge_width_mm in cover_relief_bridge_widths_mm:
        bridge = cq.Solid.makeBox(
            bridge_width_mm, bridge_span_y_mm, bridge_thickness_z_mm,
            cq.Vector(bridge_center_x_mm - bridge_width_mm / 2.0,
                      bridge_center_y_mm - bridge_span_y_mm / 2.0,
                      bridge_z_min_mm),
        )
        shaft = cq.Solid.makeCylinder(
            cover_relief_shaft_diameter_mm / 2.0,
            input_hub_shaft_z_max_mm - input_hub_shaft_z_min_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_shaft_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        gear_blank = cq.Solid.makeCylinder(
            input_hub_gear_diameter_mm / 2.0, input_hub_gear_width_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_gear_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        try:
            moving_candidate = moved_shutter_dial.fuse(bridge).fuse(shaft).fuse(gear_blank)
            moving_candidate_valid = bool(moving_candidate.isValid())
            moving_candidate_solids = len(moving_candidate.Solids())
            cover_candidate = solids[4]
            cut_errors = []
            cut_samples = 0
            for angle_deg in range(0, 360, cover_relief_rotation_step_deg):
                rotated = moving_candidate.rotate(
                    (bridge_center_x_mm, bridge_center_y_mm, 0.0),
                    (bridge_center_x_mm, bridge_center_y_mm, 1.0), float(angle_deg))
                cover_candidate = cover_candidate.cut(rotated)
                cut_samples += 1
                if not cover_candidate.isValid():
                    cut_errors.append({"angle_deg": angle_deg, "error": "cover candidate invalid after cut"})
                    break
            cover_valid = bool(cover_candidate.isValid())
            cover_solids = len(cover_candidate.Solids())
            cover_remaining_volume = float(cover_candidate.Volume())
            cover_cut_volume = float(solids[4].Volume()) - cover_remaining_volume
            cover_error = None
        except Exception as exc:
            moving_candidate_valid = False
            moving_candidate_solids = None
            cut_samples = 0
            cut_errors = [{"error": str(exc)}]
            cover_valid = False
            cover_solids = None
            cover_remaining_volume = None
            cover_cut_volume = None
            cover_error = str(exc)
        input_cover_relief_candidate_scan.append({
            "bridge_width_x_mm": bridge_width_mm,
            "shaft_diameter_mm": cover_relief_shaft_diameter_mm,
            "gear_blank_diameter_mm": input_hub_gear_diameter_mm,
            "rotation_step_deg": cover_relief_rotation_step_deg,
            "rotation_samples_applied": cut_samples,
            "moving_assembly_valid": moving_candidate_valid,
            "moving_assembly_solid_count": moving_candidate_solids,
            "cover_candidate_valid": cover_valid,
            "cover_candidate_solid_count": cover_solids,
            "original_cover_volume_mm3": round(float(solids[4].Volume()), 9),
            "remaining_cover_volume_mm3": round(cover_remaining_volume, 9) if cover_remaining_volume is not None else None,
            "removed_cover_volume_mm3": round(cover_cut_volume, 9) if cover_cut_volume is not None else None,
            "cut_errors": cut_errors,
            "error": cover_error,
            "limitations": ["Cover is only a subtractive relief diagnostic from the old cover blank",
                            "10-degree discrete samples do not prove continuous swept clearance",
                            "No wall-thickness, fastening, sealing, machining access or assembly validation"],
        })

    # True edge-fillet candidates at the upper bridge/shaft junction. Unlike the
    # previous cylindrical collar proxy, these use OpenCascade's actual edge fillet.
    input_bridge_true_fillet_scan = []
    true_fillet_bridge_widths_mm = [0.6, 1.0]
    true_fillet_radii_mm = [0.10, 0.15, 0.20]
    true_fillet_shaft_diameter_mm = 1.8
    target_bridge_top_z_mm = bridge_z_min_mm + bridge_thickness_z_mm
    for bridge_width_mm in true_fillet_bridge_widths_mm:
        bridge = cq.Solid.makeBox(
            bridge_width_mm, bridge_span_y_mm, bridge_thickness_z_mm,
            cq.Vector(bridge_center_x_mm - bridge_width_mm / 2.0,
                      bridge_center_y_mm - bridge_span_y_mm / 2.0,
                      bridge_z_min_mm),
        )
        shaft = cq.Solid.makeCylinder(
            true_fillet_shaft_diameter_mm / 2.0,
            input_hub_shaft_z_max_mm - input_hub_shaft_z_min_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_shaft_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        gear_blank = cq.Solid.makeCylinder(
            input_hub_gear_diameter_mm / 2.0, input_hub_gear_width_mm,
            cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_gear_z_min_mm),
            cq.Vector(0, 0, 1),
        )
        try:
            unfilleted = moved_shutter_dial.fuse(bridge).fuse(shaft).fuse(gear_blank)
            base_valid = bool(unfilleted.isValid())
            base_solids = len(unfilleted.Solids())
            base_error = None
        except Exception as exc:
            unfilleted = None
            base_valid = False
            base_solids = None
            base_error = str(exc)
        target_edges = []
        target_edge_diagnostics = []
        if unfilleted is not None:
            target_radius_mm = true_fillet_shaft_diameter_mm / 2.0
            for edge in unfilleted.Edges():
                try:
                    edge_type = edge.geomType()
                    eb = edge.BoundingBox()
                    radius = float(edge.radius()) if edge_type == "CIRCLE" else None
                    near_top_plane = (
                        abs(float(eb.zmin) - target_bridge_top_z_mm) <= 1e-4
                        and abs(float(eb.zmax) - target_bridge_top_z_mm) <= 1e-4
                    )
                    within_shaft_circle = (
                        eb.xmin >= bridge_center_x_mm - target_radius_mm - 1e-4
                        and eb.xmax <= bridge_center_x_mm + target_radius_mm + 1e-4
                        and eb.ymin >= bridge_center_y_mm - target_radius_mm - 1e-4
                        and eb.ymax <= bridge_center_y_mm + target_radius_mm + 1e-4
                    )
                    if near_top_plane and within_shaft_circle:
                        target_edge_diagnostics.append({
                            "edge_type": edge_type,
                            "radius_mm": round(radius, 6) if radius is not None else None,
                            "bbox_mm": bbox(edge),
                        })
                    if (edge_type == "CIRCLE" and radius is not None
                        and abs(radius - target_radius_mm) <= 1e-4
                        and near_top_plane and within_shaft_circle):
                        target_edges.append(edge)
                except Exception:
                    continue
        for fillet_radius_mm in true_fillet_radii_mm:
            try:
                if unfilleted is None:
                    raise RuntimeError(base_error or "Base bridge assembly unavailable")
                if not target_edges:
                    raise RuntimeError("No bridge/shaft junction arc edges were found")
                # The bridge intersects the shaft and splits the nominal circular
                # junction into two arc edges. Fillet both arcs as one edge set.
                filleted = unfilleted.fillet(fillet_radius_mm, target_edges)
                valid = bool(filleted.isValid())
                solid_count = len(filleted.Solids())
                fillet_error = None
            except Exception as exc:
                filleted = None
                valid = False
                solid_count = None
                fillet_error = str(exc)
            checks = []
            if filleted is not None:
                for obstacle_name, obstacle in bridge_fixed_obstacles + [("preserved_pin_hole_envelope", pin_envelope)]:
                    try:
                        overlap = float(filleted.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        overlap, error = None, str(exc)
                    checks.append({
                        "obstacle": obstacle_name,
                        "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                        "error": error,
                    })
            input_bridge_true_fillet_scan.append({
                "bridge_width_x_mm": bridge_width_mm,
                "shaft_diameter_mm": true_fillet_shaft_diameter_mm,
                "fillet_radius_mm": fillet_radius_mm,
                "target_edge_count": len(target_edges),
                "target_edge_diagnostics": target_edge_diagnostics,
                "base_assembly_valid": base_valid,
                "base_assembly_solid_count": base_solids,
                "filleted_assembly_valid": valid,
                "filleted_assembly_solid_count": solid_count,
                "fillet_error": fillet_error,
                "fixed_geometry_checks": checks,
                "clear_of_checked_frozen_geometry": bool(filleted is not None) and all(
                    x["error"] is None and x["intersection_volume_mm3"] is not None
                    and x["intersection_volume_mm3"] <= 1e-6 for x in checks
                ),
                "limitations": [
                    "OpenCascade edge fillet is applied only to the upper circular bridge/shaft junction",
                    "A successful fillet is local geometric validity, not stress or fatigue validation",
                    "No print anisotropy, torque, bearing support, fastener or assembly analysis",
                ],
            })

    # Reconstruct a clean annular perimeter-frame concept around the full-turn
    # radial envelope. This is deliberately independent of the old cover topology.
    # The radial envelope is conservatively derived from all vertices and circular
    # edge center/radius pairs of the moving input assembly.
    input_new_cover_ring_candidate_scan = []
    cover_ring_bridge_width_mm = 1.0
    cover_ring_shaft_diameter_mm = 1.8
    cover_ring_clearances_mm = [0.5, 0.75, 1.0]
    cover_ring_radial_width_mm = 1.5
    cover_ring_moving_bridge = cq.Solid.makeBox(
        cover_ring_bridge_width_mm, bridge_span_y_mm, bridge_thickness_z_mm,
        cq.Vector(bridge_center_x_mm - cover_ring_bridge_width_mm / 2.0,
                  bridge_center_y_mm - bridge_span_y_mm / 2.0, bridge_z_min_mm),
    )
    cover_ring_moving_shaft = cq.Solid.makeCylinder(
        cover_ring_shaft_diameter_mm / 2.0,
        input_hub_shaft_z_max_mm - input_hub_shaft_z_min_mm,
        cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_shaft_z_min_mm),
        cq.Vector(0, 0, 1),
    )
    cover_ring_moving_gear = cq.Solid.makeCylinder(
        input_hub_gear_diameter_mm / 2.0, input_hub_gear_width_mm,
        cq.Vector(bridge_center_x_mm, bridge_center_y_mm, input_hub_gear_z_min_mm),
        cq.Vector(0, 0, 1),
    )
    cover_ring_moving_assembly = moved_shutter_dial.fuse(cover_ring_moving_bridge).fuse(
        cover_ring_moving_shaft).fuse(cover_ring_moving_gear)
    radial_extent_candidates = []
    for vertex in cover_ring_moving_assembly.Vertices():
        point = vertex.Center()
        radial_extent_candidates.append(math.hypot(point.x - bridge_center_x_mm, point.y - bridge_center_y_mm))
    for edge in cover_ring_moving_assembly.Edges():
        try:
            if edge.geomType() == "CIRCLE":
                center = edge.Center()
                radial_extent_candidates.append(
                    math.hypot(center.x - bridge_center_x_mm, center.y - bridge_center_y_mm)
                    + float(edge.radius())
                )
        except Exception:
            pass
    moving_sweep_radius_mm = max(radial_extent_candidates) if radial_extent_candidates else None
    old_cover_bbox = solids[4].BoundingBox()
    cover_ring_z_min_mm = float(old_cover_bbox.zmin)
    cover_ring_height_mm = float(old_cover_bbox.zlen)
    for radial_clearance_mm in cover_ring_clearances_mm:
        row = {
            "radial_clearance_mm": radial_clearance_mm,
            "radial_frame_width_mm": cover_ring_radial_width_mm,
            "moving_sweep_radius_mm": round(moving_sweep_radius_mm, 6) if moving_sweep_radius_mm is not None else None,
            "inner_radius_mm": None,
            "outer_radius_mm": None,
            "z_range_mm": [round(cover_ring_z_min_mm, 6), round(cover_ring_z_min_mm + cover_ring_height_mm, 6)],
            "candidate_valid": False,
            "candidate_solid_count": None,
            "moving_assembly_intersection_mm3": None,
            "fixed_geometry_checks": [],
            "error": None,
            "limitations": [
                "New annular perimeter frame is a topology/layout prototype, not a complete cover",
                "Z span is borrowed from the old cover bounding box only as an exploratory envelope",
                "No mounting tabs, screw holes, locating features, sealing, wall thickness optimization or tool access",
                "The circular radial envelope is conservative and does not establish a final cover outline",
            ],
        }
        try:
            if moving_sweep_radius_mm is None:
                raise RuntimeError("Could not derive moving assembly radial envelope")
            inner_radius_mm = moving_sweep_radius_mm + radial_clearance_mm
            outer_radius_mm = inner_radius_mm + cover_ring_radial_width_mm
            outer = cq.Solid.makeCylinder(
                outer_radius_mm, cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            inner = cq.Solid.makeCylinder(
                inner_radius_mm, cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            ring = outer.cut(inner)
            row.update({
                "inner_radius_mm": round(inner_radius_mm, 6),
                "outer_radius_mm": round(outer_radius_mm, 6),
                "candidate_valid": bool(ring.isValid()),
                "candidate_solid_count": len(ring.Solids()),
                "moving_assembly_intersection_mm3": round(float(ring.intersect(cover_ring_moving_assembly).Volume()), 9),
            })
            for obstacle_name, obstacle in bridge_fixed_obstacles:
                try:
                    overlap = float(ring.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                row["fixed_geometry_checks"].append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
        except Exception as exc:
            row["error"] = str(exc)
        input_new_cover_ring_candidate_scan.append(row)

    # Diagnose which angular portions of the conservative annular frame can
    # coexist with the immutable main body. Each 10-degree sector is checked
    # independently; this is a layout diagnostic, not a final cover design.
    input_new_cover_ring_sector_scan = []
    cover_ring_sector_step_deg = 5
    for sector_start_deg in range(0, 360, cover_ring_sector_step_deg):
        try:
            outer_sector = cq.Solid.makeCylinder(
                moving_sweep_radius_mm + 0.5 + cover_ring_radial_width_mm,
                cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1), cover_ring_sector_step_deg,
            )
            inner_sector = cq.Solid.makeCylinder(
                moving_sweep_radius_mm + 0.5,
                cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1), cover_ring_sector_step_deg,
            )
            sector = outer_sector.cut(inner_sector).rotate(
                (bridge_center_x_mm, bridge_center_y_mm, 0),
                (bridge_center_x_mm, bridge_center_y_mm, 1),
                float(sector_start_deg),
            )
            body_overlap = float(sector.intersect(solids[5]).Volume())
            input_new_cover_ring_sector_scan.append({
                "angle_range_deg": [sector_start_deg, sector_start_deg + cover_ring_sector_step_deg],
                "candidate_valid": bool(sector.isValid()),
                "candidate_solid_count": len(sector.Solids()),
                "main_body_intersection_mm3": round(body_overlap, 9),
                "clear_of_main_body": body_overlap <= 1e-6,
                "error": None,
            })
        except Exception as exc:
            input_new_cover_ring_sector_scan.append({
                "angle_range_deg": [sector_start_deg, sector_start_deg + cover_ring_sector_step_deg],
                "candidate_valid": False,
                "candidate_solid_count": None,
                "main_body_intersection_mm3": None,
                "clear_of_main_body": False,
                "error": str(exc),
            })

    # Test whether trimming only the new cover (never the immutable body) by
    # the exact body intersection can preserve a single connected B-rep.
    # This is a topology feasibility test; it does not add manufacturing clearance.
    input_new_cover_ring_body_relief_scan = []
    for radial_clearance_mm in cover_ring_clearances_mm:
        row = {
            "radial_clearance_mm": radial_clearance_mm,
            "radial_frame_width_mm": cover_ring_radial_width_mm,
            "moving_sweep_radius_mm": round(moving_sweep_radius_mm, 6),
            "body_relief_method": "subtract exact main-body B-rep intersection from cover ring",
            "candidate_valid": False,
            "candidate_solid_count": None,
            "candidate_volume_mm3": None,
            "removed_volume_mm3": None,
            "moving_assembly_intersection_mm3": None,
            "fixed_geometry_checks": [],
            "error": None,
            "limitations": [
                "Only the cover candidate is trimmed; source STEP and main body remain unchanged",
                "Exact body subtraction provides zero-clearance contact at the trimmed interface, not manufacturing clearance",
                "Single-solid topology does not prove adequate stiffness, mounting, sealing, tool access or printability",
            ],
        }
        try:
            inner_radius_mm = moving_sweep_radius_mm + radial_clearance_mm
            outer_radius_mm = inner_radius_mm + cover_ring_radial_width_mm
            outer = cq.Solid.makeCylinder(
                outer_radius_mm, cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            inner = cq.Solid.makeCylinder(
                inner_radius_mm, cover_ring_height_mm,
                cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                cq.Vector(0, 0, 1),
            )
            raw_ring = outer.cut(inner)
            relieved_ring = raw_ring.cut(solids[5])
            body_removed = float(raw_ring.Volume()) - float(relieved_ring.Volume())
            row.update({
                "candidate_valid": bool(relieved_ring.isValid()),
                "candidate_solid_count": len(relieved_ring.Solids()),
                "candidate_volume_mm3": round(float(relieved_ring.Volume()), 9),
                "removed_volume_mm3": round(body_removed, 9),
                "moving_assembly_intersection_mm3": round(float(relieved_ring.intersect(cover_ring_moving_assembly).Volume()), 9),
            })
            for obstacle_name, obstacle in bridge_fixed_obstacles:
                try:
                    overlap = float(relieved_ring.intersect(obstacle).Volume())
                    error = None
                except Exception as exc:
                    overlap, error = None, str(exc)
                row["fixed_geometry_checks"].append({
                    "obstacle": obstacle_name,
                    "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                    "error": error,
                })
        except Exception as exc:
            row["error"] = str(exc)
        input_new_cover_ring_body_relief_scan.append(row)

    # Build a single-piece open annular frame with two body-clearance gaps.
    # Each gap is bridged outside the nominal ring radius; the bridge overlaps
    # the ring by 0.5 mm to give the Boolean fuse a positive-volume connection.
    # This is a topology/layout experiment, not a production cover.
    input_new_cover_open_ring_bridge_scan = []
    open_ring_gap_margins_deg = [2.5, 5.0]
    open_ring_bridge_offsets_mm = [1.0, 2.0]
    open_ring_inner_radius_mm = moving_sweep_radius_mm + 0.5
    open_ring_outer_radius_mm = open_ring_inner_radius_mm + cover_ring_radial_width_mm
    for gap_margin_deg in open_ring_gap_margins_deg:
        gap_ranges = [
            [150.0 - gap_margin_deg, 160.0 + gap_margin_deg],
            [200.0 - gap_margin_deg, 210.0 + gap_margin_deg],
        ]
        for bridge_offset_mm in open_ring_bridge_offsets_mm:
            row = {
                "gap_margin_deg": gap_margin_deg,
                "gap_ranges_deg": gap_ranges,
                "bridge_outer_offset_mm": bridge_offset_mm,
                "bridge_overlap_into_ring_mm": 0.5,
                "candidate_valid": False,
                "candidate_solid_count": None,
                "candidate_volume_mm3": None,
                "main_body_intersection_mm3": None,
                "moving_assembly_intersection_mm3": None,
                "fixed_geometry_checks": [],
                "error": None,
                "limitations": [
                    "Exploratory annular frame with two local gaps and external polygonal bridges",
                    "Bridge overlap is a Boolean-fuse aid, not a specified manufacturing joint",
                    "No mounting tabs, fasteners, wall-thickness, stiffness, sealing or tool-access validation",
                ],
            }
            try:
                outer = cq.Solid.makeCylinder(
                    open_ring_outer_radius_mm, cover_ring_height_mm,
                    cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                    cq.Vector(0, 0, 1),
                )
                inner = cq.Solid.makeCylinder(
                    open_ring_inner_radius_mm, cover_ring_height_mm,
                    cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm),
                    cq.Vector(0, 0, 1),
                )
                frame = outer.cut(inner)
                bridge_solids = []
                for gap_start_deg, gap_end_deg in gap_ranges:
                    gap_outer = cq.Solid.makeCylinder(
                        open_ring_outer_radius_mm + 0.01, cover_ring_height_mm + 0.02,
                        cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm - 0.01),
                        cq.Vector(0, 0, 1), gap_end_deg - gap_start_deg,
                    ).rotate(
                        (bridge_center_x_mm, bridge_center_y_mm, 0),
                        (bridge_center_x_mm, bridge_center_y_mm, 1), gap_start_deg,
                    )
                    gap_inner = cq.Solid.makeCylinder(
                        max(0.0, open_ring_inner_radius_mm - 0.01), cover_ring_height_mm + 0.02,
                        cq.Vector(bridge_center_x_mm, bridge_center_y_mm, cover_ring_z_min_mm - 0.01),
                        cq.Vector(0, 0, 1), gap_end_deg - gap_start_deg,
                    ).rotate(
                        (bridge_center_x_mm, bridge_center_y_mm, 0),
                        (bridge_center_x_mm, bridge_center_y_mm, 1), gap_start_deg,
                    )
                    frame = frame.cut(gap_outer.cut(gap_inner))
                    r_inner_bridge = open_ring_outer_radius_mm - 0.5
                    r_outer_bridge = open_ring_outer_radius_mm + bridge_offset_mm
                    points = []
                    for radius, angle_deg in [
                        (r_inner_bridge, gap_start_deg),
                        (r_outer_bridge, gap_start_deg),
                        (r_outer_bridge, gap_end_deg),
                        (r_inner_bridge, gap_end_deg),
                    ]:
                        angle_rad = math.radians(angle_deg)
                        points.append(cq.Vector(
                            bridge_center_x_mm + radius * math.cos(angle_rad),
                            bridge_center_y_mm + radius * math.sin(angle_rad),
                            cover_ring_z_min_mm,
                        ))
                    wire = cq.Wire.makePolygon(points + [points[0]])
                    face = cq.Face.makeFromWires(wire)
                    bridge_solids.append(cq.Solid.extrudeLinear(
                        face.outerWire(), [], cq.Vector(0, 0, cover_ring_height_mm)
                    ))
                for bridge in bridge_solids:
                    frame = frame.fuse(bridge)
                frame = frame.clean()
                body_overlap = float(frame.intersect(solids[5]).Volume())
                moving_overlap = float(frame.intersect(cover_ring_moving_assembly).Volume())
                row.update({
                    "candidate_valid": bool(frame.isValid()),
                    "candidate_solid_count": len(frame.Solids()),
                    "candidate_volume_mm3": round(float(frame.Volume()), 9),
                    "main_body_intersection_mm3": round(body_overlap, 9),
                    "moving_assembly_intersection_mm3": round(moving_overlap, 9),
                })
                for obstacle_name, obstacle in bridge_fixed_obstacles:
                    try:
                        overlap = float(frame.intersect(obstacle).Volume())
                        error = None
                    except Exception as exc:
                        overlap, error = None, str(exc)
                    row["fixed_geometry_checks"].append({
                        "obstacle": obstacle_name,
                        "intersection_volume_mm3": round(overlap, 9) if overlap is not None else None,
                        "error": error,
                    })
            except Exception as exc:
                row["error"] = str(exc)
            input_new_cover_open_ring_bridge_scan.append(row)

    gear_axial_analysis = {
        "gear_blank_diameter_mm": 11.0,
        "gear_face_width_mm": 2.0,
        "gear_centers_xy_mm": gear_centers,
        "frozen_encoder_solids_checked": list(frozen_encoder_solids),
        "z_scan_min_mm": z_values[0], "z_scan_max_start_mm": z_values[-1],
        "scan_step_mm": 0.1,
        "clear_start_z_ranges_mm": clear_ranges,
        "samples": gear_candidates,
        "candidate_z_min_mm": candidate_z_min,
        "axial_body_clear_start_z_ranges_mm": axial_body_clear_start_z_ranges,
        "axial_body_clear_envelope_ranges_mm": axial_body_clear_envelope_ranges,
        "axial_body_scan_step_mm": 0.2,
        "axial_body_scan_samples": axial_body_scan,
        "axial_body_fine_scan_step_mm": 0.02,
        "axial_body_fine_scan_samples": axial_body_fine_scan,
        "shaft_corridor_probe_radii_mm": shaft_probe_radii_mm,
        "shaft_corridor_slice_height_mm": shaft_slice_height_mm,
        "shaft_corridor_scan_samples": shaft_corridor_scan,
        "input_axis_orbit_probe_radii_mm": orbit_probe_radii_mm,
        "input_axis_orbit_z_range_mm": [orbit_z_min_mm, orbit_z_max_mm],
        "input_axis_orbit_scan_samples": input_axis_orbit_scan,
        "input_gear_orbit_envelope_scan_samples": input_gear_orbit_envelope_scan,
        "vertical_candidate_shaft_angles_deg": vertical_candidate_angles_deg,
        "vertical_candidate_shaft_probe_radii_mm": vertical_candidate_radii_mm,
        "vertical_candidate_shaft_slice_height_mm": 0.5,
        "vertical_candidate_shaft_scan_samples": vertical_candidate_shaft_scan,
        "lateral_bypass_section_scan": lateral_bypass_section_scan,
        "lateral_bypass_3d_scan": lateral_bypass_3d_scan,
        "candidate_centerline_routes": candidate_centerline_routes,
        "straight_bypass_shaft_checks": straight_bypass_shaft_checks,
        "bypass_full_height_shaft_scan": bypass_full_height_shaft_scan,
        "bypass_full_height_shaft_scan_slice_height_mm": 0.5,
        "bypass_full_height_shaft_scan_parameters": {
            "axis_candidates_xy_mm": [[24.5, 9.0], [24.5, -9.0]],
            "shaft_diameters_mm": [1.0, 1.5, 2.0, 2.5, 3.0],
            "z_range_mm": [0.0, 22.0],
            "obstacles": ["main_body", "encoder_button", "encoder_dial", "encoder_bracket", "cover"],
        },
        "bypass_gear_pair_parameters": {
            "center_distance_mm": 9.0,
            "module_mm": 0.5,
            "tooth_counts": [18, 18],
            "pressure_angle_deg": 20.0,
            "blank_diameter_mm": 10.0,
            "face_width_mm": 2.0,
            "z_range_mm": [16.0, 18.0],
        },
        "bypass_gear_pair_checks": bypass_gear_pair_checks,
        "confirmed_plus_x_layout": {
            "output_axis_xy_mm": [24.5, 0.0],
            "input_axis_xy_mm": [34.5, 0.0],
            "center_distance_mm": 10.0,
            "shutter_dial_translation_mm": [10.0, 0.0, 0.0],
            "preserved_pin_hole_center_xy_mm": [28.0, 0.0],
            "gear_candidate": "module 0.5, 20/20 teeth, 1:1, 20 degree pressure angle"
        },
        "translated_shutter_dial_checks": moved_shutter_dial_checks,
        "true_input_axis_full_height_scan": true_input_axis_full_height_scan,
        "true_input_axis_full_height_scan_parameters": {
            "axis_xy_mm": [34.5, 0.0],
            "shaft_diameters_mm": [1.0, 1.5, 2.0, 2.5, 3.0],
            "z_range_mm": [0.0, 22.0],
            "slice_height_mm": 0.5,
            "obstacles": ["main_body", "encoder_button", "encoder_dial", "encoder_bracket", "current_cover"]
        },
        "true_10mm_gear_pair_height_scan": true_10mm_gear_pair_height_scan,
        "high_gear_layer_scan": high_gear_layer_scan,
        "high_gear_output_shaft_checks": high_gear_output_shaft_checks,
        "segmented_output_axis_checks": segmented_output_axis_checks,
        "high_gear_input_stub_checks": high_gear_input_stub_checks,
        "input_bridge_hub_candidate_scan": input_bridge_hub_candidate_scan,
        "input_bridge_sweep_by_bridge_width": input_bridge_sweep_by_bridge_width,
        "input_bridge_root_transition_scan": input_bridge_root_transition_scan,
        "input_cover_relief_candidate_scan": input_cover_relief_candidate_scan,
        "input_cover_relief_candidate_scan_parameters": {"rotation_step_deg": cover_relief_rotation_step_deg, "bridge_widths_mm": cover_relief_bridge_widths_mm, "shaft_diameter_mm": cover_relief_shaft_diameter_mm, "method": "subtract sampled rotating dial+bridge+shaft+gear blank from current cover as diagnostic only"},
        "input_bridge_true_fillet_scan": input_bridge_true_fillet_scan,
        "input_bridge_true_fillet_scan_parameters": {"bridge_widths_mm": true_fillet_bridge_widths_mm, "fillet_radii_mm": true_fillet_radii_mm, "shaft_diameter_mm": true_fillet_shaft_diameter_mm, "filleted_edge": "upper circular bridge/shaft junction at bridge top Z"},
        "input_new_cover_ring_candidate_scan": input_new_cover_ring_candidate_scan,
        "input_new_cover_ring_sector_scan": input_new_cover_ring_sector_scan,
        "input_new_cover_ring_body_relief_scan": input_new_cover_ring_body_relief_scan,
        "input_new_cover_open_ring_bridge_scan": input_new_cover_open_ring_bridge_scan,
        "input_new_cover_ring_sector_scan_parameters": {
            "sector_step_deg": cover_ring_sector_step_deg,
            "radial_clearance_mm": 0.5,
            "radial_frame_width_mm": cover_ring_radial_width_mm,
            "z_range_mm": [cover_ring_z_min_mm, cover_ring_z_min_mm + cover_ring_height_mm],
            "checked_obstacle": "main_body",
            "scope": "independent annular sector screening; not a complete cover"
        },
        "input_new_cover_ring_candidate_scan_parameters": {"bridge_width_mm": cover_ring_bridge_width_mm, "shaft_diameter_mm": cover_ring_shaft_diameter_mm, "radial_clearances_mm": cover_ring_clearances_mm, "radial_frame_width_mm": cover_ring_radial_width_mm, "z_height_source": "current cover bounding-box height and lower Z only; exploratory"},
        "input_bridge_cover_and_engagement_scan_parameters": {
            "rotation_step_deg": 15,
            "bridge_only_cover_checked_separately": True,
            "dial_only_cover_baseline_checked_separately": True,
            "engagement_z_slice_step_mm": 0.1,
            "engagement_section_scope": "bridge intersect translated shutter dial",
        },
        "high_gear_layer_scan_parameters": {"z_starts_mm": [20.5, 23.5], "step_mm": 0.25, "blank_diameter_mm": 11.0, "face_width_mm": 2.0, "centers_xy_mm": [[24.5, 0.0], [34.5, 0.0]]},
        "gear_layer_pin_clearance_scan": gear_layer_pin_clearance_scan,
        "true_gear_axial_window_scan": true_gear_axial_window_scan,
        "thin_gear_width_sweep": thin_gear_width_sweep,
        "shutter_dial_local_section_analysis": shutter_dial_local_section_analysis,
        "candidate_editable_structure_checks": editable_structure_checks,
        "input_main_body_face_intersections": body_face_intersections,
        "input_main_body_face_topology": body_face_topology,
        "input_gear_local_xz_sections": section_samples,
        "nearby_main_body_faces_from_gear_overlap": nearby_body_faces,
        "nearest_main_body_boundary_detail": nearest_face_detail,
    }
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": "source/leica_m3_light_meter.stp",
        "source_bytes": STEP.stat().st_size,
        "cadquery_version": getattr(cq, "__version__", "unknown"),
        "overall_valid": all_valid, "solid_count": len(solids),
        "overall_bbox_mm": bbox(root_shape), "solids": rows, "pairs": pairs,
        "gear_axial_analysis": gear_axial_analysis,
    }
    lines = [
        "# STEP 几何内核检查报告", "",
        f"- 生成时间（UTC）：{report['generated_utc']}",
        f"- 输入文件：{report['source']}",
        f"- 文件大小：{report['source_bytes']} bytes",
        f"- CadQuery：{report['cadquery_version']}",
        f"- 实体数量：{len(solids)}",
        f"- 整体 B-rep 有效性：{'通过' if all_valid else '未通过'}", "",
        "> 本报告来自 CadQuery/OpenCascade 实际导入后的 B-rep 计算。实体编号是 STEP 导入顺序，不能仅凭编号推断零件名称。相交体积和最小距离是几何内核计算结果；零距离也可能表示接触，不能单独等同于装配干涉。", "",
        "## 整体包围盒", "",
        f"- Min (mm)：{report['overall_bbox_mm']['min']}",
        f"- Max (mm)：{report['overall_bbox_mm']['max']}",
        f"- Size (mm)：{report['overall_bbox_mm']['size']}", "",
        "## 各实体", "",
        "|实体|有效|体积 (mm³)|质心 (mm)|尺寸 X×Y×Z (mm)|面/边/顶点|",
        "|---:|:---:|---:|---|---|---:|",
    ]
    for x in rows:
        lines.append(f"|{x['index']}|{'是' if x['valid'] else '否'}|{x['volume_mm3']}|{x['center_of_mass_mm']}|{x['bbox_mm']['size']}|{x['faces']}/{x['edges']}/{x['vertices']}|")
    lines += ["", "## 双齿轮轴向空间扫描（冻结编码器机构避让）", "",
              f"- 齿轮包络：直径 11.0 mm，齿宽 2.0 mm；中心：(24.5,0) 与 (34.5,0) mm。",
              f"- 检查对象：{', '.join(gear_axial_analysis['frozen_encoder_solids_checked'])}。",
              f"- 通过扫描的齿轮起始 Z 区间（mm）：{gear_axial_analysis['clear_start_z_ranges_mm']}（仅扫描起始 Z=10.5…14.9 mm，步长 0.1 mm）",
              f"- 选定用于结构交叠评估的候选齿轮下表面 Z：{gear_axial_analysis['candidate_z_min_mm']} mm；上表面 Z：{gear_axial_analysis['candidate_z_min_mm'] + 2.0} mm。",
              "- 候选高度下与可重构旧快门盘、盖子、主体的交叠体积（mm³）：",
              *[f"  - {x['gear']} × {x['structure']}: {x['intersection_volume_mm3']}，最小距离 {x['minimum_distance_mm']} mm" for x in gear_axial_analysis['candidate_editable_structure_checks']],
              "- 冻结编码器实体的无相交结论只适用于直径 11 mm、宽 2 mm 的圆柱毛坯；尚不包含轴、齿轮轮毂、齿形、磁铁/AS5600未建模保留体积或装配路径。",
              "",
              "### 输入/输出齿轮全轴向高度可行区间扫描",
              "",
              "- 对Z起始位置0.0…20.0 mm按0.2 mm步长扫描；每个候选均为Ø11×2 mm旋转扫掠包络。",
              "- 同时检查主体及冻结编码器按键、转盘、支架；旧快门盘和盖子不纳入障碍物，因为它们属于可重构结构。",
              f"- 两齿轮同时无正体积相交的毛坯下表面起始Z区间（mm）：{axial_body_clear_start_z_ranges}。",
              f"- 对应毛坯整体扫掠Z覆盖区间（mm）：{axial_body_clear_envelope_ranges}。",
              "- 在15.80…16.20 mm范围内另以0.02 mm步长复核两齿轮与主体及冻结编码器组件的交叠，详细数据见JSON字段 axial_body_fine_scan_samples。",
              "- 此扫描仅筛选轴向高度候选，不验证齿轮轴、轮毂、轴承、支架、齿轮匣、装配路径、强度或实际可用轴向空间。",
              "", "## 高层齿轮毛坯扫描（平移快门盘上方）", "",
              "- 对正式轴心(24.5,0)/(34.5,0)的Ø11×2 mm圆柱毛坯，从Z=20.5至23.5 mm按0.25 mm步长扫描；逐项检查主体、冻结编码器组件、+X平移快门盘及当前盖子。",
              *[f"### Z={x['z_range_mm'][0]}…{x['z_range_mm'][1]} mm" for x in gear_axial_analysis["high_gear_layer_scan"]],
              *[f"- {g['gear']}齿轮中心{g['center_xy_mm']}：固定几何净空={'是' if g['clear_of_fixed_geometry'] else '否'}；平移快门盘净空={'是' if g['clear_of_translated_dial'] else '否'}；当前盖子净空={'是' if g['clear_of_current_cover'] else '否'}；交叠详情：" + json.dumps([{'obstacle': q['obstacle'], 'intersection_volume_mm3': q['intersection_volume_mm3'], 'error': q['error']} for q in g['checks'] if q['error'] is not None or (q['intersection_volume_mm3'] or 0) > 1e-6], ensure_ascii=False) for x in gear_axial_analysis["high_gear_layer_scan"] for g in x["gears"]],
              "- 本扫描仅验证圆柱毛坯与列明实体的正体积交叠，不代表真实齿形啮合、轴系支撑、轴肩、装配路径、强度或盖子重构后的空间已经验证。",
              "", "## 输入齿轮与主体的面级交叠定位", "",
              "|CadQuery 面序号|曲面类型|面交叠面积 (mm²)|交叠包围盒 Min (mm)|Max (mm)|",
              "|---:|---|---:|---|---|",
              *[f"|{x['cadquery_face_index']}|{x['surface_type']}|{x.get('intersection_area_mm2', '错误')}|{x.get('intersection_bbox_mm', {}).get('min', '')}|{x.get('intersection_bbox_mm', {}).get('max', x.get('error', ''))}|" for x in body_face_intersections],
              "", "### 齿轮交叠体到其他主体边界面的距离", "",
              "- 下表排除与齿轮毛坯直接交叠的面，仅列出距离交叠体最近的主体边界面。距离是候选反侧边界线索，不等于最小壁厚；需结合面法线、局部曲率和最近点位置复核。",
              *[f"- 面 {x['cadquery_face_index']}（{x['surface_type']}）：距离 {x.get('distance_from_gear_body_overlap_mm')} mm；面积 {x.get('face_area_mm2')} mm²；包围盒 {json.dumps(x.get('face_bbox_mm'), ensure_ascii=False)}；错误 {x.get('error')}" for x in nearby_body_faces[:12]],
              "", "### 输入齿轮局部 X-Z 截面采样", "",
              "- 在候选齿轮宽度范围 Y=-1…+1 mm 内，按 0.5 mm 间隔取样；每个截面用厚度 0.05 mm 的薄片近似，截面面积由局部体积除以薄片厚度估算。",
              "- ROI：X=27…45 mm、Z=8…18 mm。组件包围盒仅用于定位，不代表真实最小壁厚。",
              *[f"- Y={x['y_mm']} mm：材料截面积估算 {x.get('material_section_area_estimate_mm2')} mm²；材料组件 {json.dumps(x.get('material_components', []), ensure_ascii=False)}；齿轮毛坯与主体交叠截面积估算 {x.get('gear_body_overlap_area_estimate_mm2')} mm²；交叠组件 {json.dumps(x.get('gear_body_overlap_components', []), ensure_ascii=False)}；错误 {x.get('error')}" for x in section_samples],
              "", "## 平移快门盘局部截面与齿轮投影材料分布", "",
              "- 本节直接对+X平移10 mm后的快门盘实体做OpenCascade B-rep薄片相交；不修改原始STEP。",
              "- 水平截面：Z=16.10…20.80 mm的12个高度，XY ROI为X=18…45、Y=-8…8 mm，薄片厚0.02 mm。",
              "- 纵向截面：Y=-5…+5 mm的9个位置，XZ ROI为X=18…45、Z=15.5…21 mm，薄片厚0.05 mm。",
              "- 每个截面分别统计快门盘材料面积、连通材料块，以及落在输出/输入齿轮Ø11 mm投影范围内的材料面积；同时检查与保留盲孔占位的交叠。",
              "- 注意：Z=17.1 mm是盲孔下端开口/金属杆进入平面，不是盲孔封闭端；此处只作为保留接口边界。",
              *[f"- 水平 Z={x['z_center_mm']} mm：总材料截面积估算 {x.get('material_area_estimate_mm2')} mm²；输出齿轮投影材料 {x.get('gear_footprint_material', {}).get('output', {}).get('material_area_estimate_mm2')} mm²；输入齿轮投影材料 {x.get('gear_footprint_material', {}).get('input', {}).get('material_area_estimate_mm2')} mm²；盲孔占位交叠 {x.get('pin_envelope_overlap_volume_mm3')} mm³；错误 {x.get('error')}" for x in shutter_dial_horizontal_sections],
              *[f"- 纵向 Y={x['y_center_mm']} mm：总材料截面积估算 {x.get('material_area_estimate_mm2')} mm²；输出齿轮投影材料 {x.get('gear_footprint_material', {}).get('output', {}).get('material_area_estimate_mm2')} mm²；输入齿轮投影材料 {x.get('gear_footprint_material', {}).get('input', {}).get('material_area_estimate_mm2')} mm²；盲孔占位交叠 {x.get('pin_envelope_overlap_volume_mm3')} mm³；错误 {x.get('error')}" for x in shutter_dial_vertical_sections],
              "- 这些截面用于识别可重构材料区域和几何瓶颈，不等于最小壁厚、疲劳寿命、承载能力或切削许可；是否减料必须在保留盲孔和联动杆接口后另做真实B-rep候选验证。",
              "", "### 截面组件包围盒原始数据", "",
              json.dumps(shutter_dial_local_section_analysis, ensure_ascii=False, indent=2),
              "", "### 最近主体边界面的法线与最近点复核", "",
              f"- 目标面与最近点数据：{json.dumps(gear_axial_analysis['nearest_main_body_boundary_detail'], ensure_ascii=False)}",
              "- 最近点由 OpenCascade BRepExtrema_DistShapeShape 计算；Y 切片仍是 0.05 mm 薄片近似。面法线方向需结合实体内外侧语义判断，不能仅凭法线正负确定可切除方向。",
              "", "### 交叠面法线、边界环与邻接面", "",
              *[line for x in body_face_topology for line in (
                  f"#### 主体面 {x['cadquery_face_index']}（{x['surface_type']}）",
                  f"- 中心法线：{x['normal_at_center']}；法线计算错误：{x['normal_error']}",
                  f"- 边界环：{json.dumps(x['wires'], ensure_ascii=False)}",
                  f"- 邻接面：{json.dumps(x['adjacent_faces'], ensure_ascii=False)}", ""
              )],
              "", "> 面序号为 CadQuery 导入后主体实体的面枚举序号，不等同于 STEP 文件中的 ADVANCED_FACE 编号。此表只用于定位冲突表面，不代表这些面可直接切除。",
              "", "## 实体两两关系", "",
              "|实体 A|实体 B|相交体积 (mm³)|最小距离 (mm)|备注|",
              "|---:|---:|---:|---:|---|"]
    for p in pairs:
        notes = []
        if p["intersection_error"]:
            notes.append("相交计算失败：" + p["intersection_error"])
        if p["distance_error"]:
            notes.append("距离计算失败：" + p["distance_error"])
        if p["intersection_volume_mm3"] is not None and p["intersection_volume_mm3"] > 1e-6:
            notes.append("存在正相交体积，需结合装配意图复核")
        lines.append(f"|{p['a']}|{p['b']}|{p['intersection_volume_mm3']}|{p['minimum_distance_mm']}|{'；'.join(notes) or '计算完成'}|")
    lines += ["", "## 主体阻挡高度的三维空腔连通性扫描", "",
              f"- 球形净空探针半径：{volume_probe_radius_mm} mm；XY步长1.0 mm，Z步长0.5 mm；网格规模 {len(volume_scan_x)}×{len(volume_scan_y)}×{len(volume_scan_z)}。",
              f"- 检查对象：主体及冻结编码器实体；旧盖子未纳入障碍物，因为属于可重构件。",
              f"- 可用节点：{len(free_voxels)}；计算错误节点：{len(failed_voxels)}。",
              "- 仅使用6邻接连通，且相邻球形探针中心距小于探针直径；连通分量同时保存全部节点坐标，便于后续提取连续候选中心线。",
              "- 该扫描只覆盖Z=11.5…15.5 mm阻挡带，不代表从快门盘到齿轮层的完整轴系路径；球形净空探针是几何筛查，不是最终轴径或强度验证。",
              *[f"- 连通分量 {i + 1}：{x['node_count']}节点；包围盒 {json.dumps(x['bbox_xyz_mm'], ensure_ascii=False)}；邻近90°候选={x['near_90deg_candidate']}，270°候选={x['near_270deg_candidate']}。" for i, x in enumerate(components_3d[:12])],
              "", "## 原始数据", "", json.dumps(report, ensure_ascii=False, indent=2),
              "", "## 限制", "",
              "- STEP 不包含未建模的 PCB、传感器、电池等实际零件；本报告不能证明这些零件的保留空间充足。",
              "- STEP 实体编号和装配语义需结合原始 CAD 视图人工映射。",
              "- 本报告不自动修改或覆盖 source/ 中的原始 STEP。",
              "- 接触、嵌套、重叠的设计意图必须结合机构关系判断；不能仅凭 AABB 或单一距离指标判定故障。", ""]
    lines += [
        "", "## 桥根真实圆角与独立上盖环框候选扫描", "",
        "- 桥根圆角使用 OpenCascade 对桥接条上表面与中心轴交界处的圆形边执行真实 edge fillet；结果字段为 input_bridge_true_fillet_scan。",
        "- 新上盖初筛不再修剪旧盖，而是围绕运动总成完整旋转半径构造独立环形边框；结果字段为 input_new_cover_ring_candidate_scan。",
        "- 环框仅用于验证单件拓扑、运动净空及冻结结构避让，不包含安装耳、螺钉孔、密封和最终外形。",
        "", "### 桥根圆角候选", "", json.dumps(input_bridge_true_fillet_scan, ensure_ascii=False, indent=2),
        "", "### 独立上盖环框候选", "", json.dumps(input_new_cover_ring_candidate_scan, ensure_ascii=False, indent=2),
        "", "### 双开口环框与外侧桥接候选", "", json.dumps(input_new_cover_open_ring_bridge_scan, ensure_ascii=False, indent=2),
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"valid={all_valid} solids={len(solids)} pairs={len(pairs)}")
    return 0 if all_valid else 2

if __name__ == "__main__":
    sys.exit(main())
