# Current iteration — complete V10A print set

Start here instead of searching historical version folders. This folder collects the current assembly's parts; it is not a new geometry revision. Existing printed parts do not need reprinting.

## Print quantities

PLA:
- `PLA/01_top_PRINT_1.stl` — ONE top. Unchanged V7/V9 top; reuse yours.
- `PLA/02_left_support_PRINT_1.stl` — ONE V10A left support.
- `PLA/03_right_support_PRINT_1.stl` — ONE V10A right support. Do not print two lefts.
- `PLA/04_rear_brace_PRINT_1.stl` — ONE V10A side-entry rear brace.

TPU 95A:
- `TPU95A/05_foot_A_PRINT_2.stl` — TWO feet of variant A.
- `TPU95A/06_foot_B_PRINT_2.stl` — TWO feet of variant B.

Complete assembly: eight printed pieces. If your PLA assembly is already printed, only the four TPU feet are needed. Print TPU separately from PLA, with the orientations supplied and the settings that worked for your V6A shoe. A and B can share a TPU plate. Do not mirror or scale them in the slicer.

## Where the feet go

“Left/right” means viewed from the front of the footrest, facing toward the rear X-brace:

- Left support, front corner: A.
- Left support, rear corner: B.
- Right support, front corner: B.
- Right support, rear corner: A.

Thus A occupies one diagonal and B the other. Each support uses one of each. The window in the taller shoe wall aligns with the support's raised catch; on V10A these catches face inward. The closed shoe end goes at the outer end of the bottom rail. Seat the shoe and check the catch appears in the window; peel the window wall away deliberately for removal rather than forcing the PLA catch.

These are the original V6A-derived shoe geometries, preserved byte-for-byte from the V9 full pack. The mirrored V10A arrangement was checked on 2026-10-07: all four shoes can be positioned using ordinary rotations/translations (no new reflected print required), with zero nominal interference against the assembled structural parts. Physical fit on your actual V10A prints remains to be confirmed. This check is not a grip or fatigue test.

## Current experimental status

V10A reportedly substantially improved racking stability. The fully seated top reportedly binds during straight removal; packability remains unresolved. No load rating or measured 200 N qualification exists. Feet are for grip/floor protection, not a cure for structural racking. See [latest status](../STATUS.md).

## Provenance and updates

`manifest.json` records quantities, exact versioned sources and SHA-256 hashes. `foot_compatibility_checks.json` records the four rigid placement transforms and interference results. All six STLs are unchanged copies of their source version; only filenames and organization changed.

When a future iteration is accepted for testing, refresh this folder and quantities/manifest in the same commit. Preserve historical artifacts under `versions/`. Current means latest selected prototype assembly, not certified/final.
