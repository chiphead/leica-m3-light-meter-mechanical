# Mechanical design

This directory is the active home for the user-maintained mechanical design of the Leica M3 light meter.

## Source of truth

The current mechanical baseline is the STEP/native CAD model supplied by the user and stored in `source/`. Until that model is uploaded, this directory intentionally contains no active enclosure geometry.

**Do not use files in `archive/legacy_generated/` as the current design baseline.** They are retained only for historical traceability and may describe superseded concepts, dimensions, component placements, or mechanisms.

## Directory layout

- `source/` — immutable copies of user-supplied source models and reference files. Do not edit originals in place.
- `working/` — in-progress revisions derived from the current source model.
- `releases/` — user-approved, versioned deliverables (STEP and, where useful, STL/native CAD).
- `drawings/` — dimensioned drawings, screenshots, assembly views, and manufacturing notes.
- `archive/legacy_generated/` — previous repository-generated conceptual models, scripts, parameter studies, and their historical documentation.

## File workflow

1. Upload the current STEP/STP model (and native CAD project if available) into `source/`.
2. Record its origin, units, coordinate orientation, and revision in a short accompanying note.
3. Inspect the model before changing it. Keep the uploaded original unchanged.
4. Put proposed modifications in `working/`, preserving a clear revision history.
5. Move/copy only user-approved results into `releases/`.
6. Keep a concise change note with each release, including what changed and what was not validated.

## CAD conventions

- Use millimetres unless the source model explicitly declares otherwise; verify units on import.
- Preserve the user's coordinate system and datum choices unless a change is explicitly agreed.
- Do not infer missing dimensions from archived conceptual models.
- Distinguish measured dimensions, manufacturer specifications, and provisional estimates.
- Check clearances, interference, wall thickness, fastener access, cable/USB access, assembly sequence, and manufacturing constraints before calling a model release-ready.
- A STEP export is geometry, not proof of parametric editability. Keep the native CAD file when available.

## Scope boundary

This workspace is for mechanical CAD and its supporting engineering records. Firmware, UI assets, and unrelated project documentation remain in their existing locations.
