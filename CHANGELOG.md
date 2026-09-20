# Changelog — retrospective, chronological

Design sequence is reconstructed from artifacts and conversation. Outcomes include later observations; no claim that they were known at original release. Dates of individual prints were not consistently recorded.

## v3-inherited — Inherited V3 top and assembly concept

**Change / why:** Imported the older top/assembly reference supplied with the handoff. Approximate 230 x 170 mm top; not reconciled to the latest support.

**CAD:** Later V6A inspection reported five disconnected top bodies (platform plus four socket bosses), despite watertightness. That finding belongs to the later inspection, not an original V3 test.

**Physical:** No full V3 top test result is available in this conversation.

**Outcome:** Reference only. Required connected socket bosses, support reconciliation and height review. Handoff also mentions unavailable V4 and earlier disconnected-brace failures.

[Artifacts and review](versions/v3-inherited/REVIEW.md)

## v5-inherited — Inherited V5 lightweight support and friction shoe

**Change / why:** Inherited 10 mm perimeter rails, 8 mm X members, 7 mm thickness and local junction pads. Handoff describes reduction from unavailable V4 (12 mm rails/10 mm braces). Existing TPU shoe relied on friction only.

**CAD:** Handoff reports a connected support and roughly 80.17 cm³ volume. Later V6A checks preserved the full bottom rail. No structural rating was established.

**Physical:** No standalone V5 structural load result is available. User requested proper replaceable TPU retention.

**Outcome:** Use as structural starting point; replace friction-only foot interface without cutting the rail.

[Artifacts and review](versions/v5-inherited/REVIEW.md)

## v6-calibration-inherited — Inherited V6 top-joint tolerance calibration

**Change / why:** Preserved historical calibration artifact. This is a tolerance coupon, not a V6 full assembly. Selected 7 x 22 mm tab into 7.10 x 22.10 mm socket with 7 mm engagement.

**CAD:** Later parser inspection reported non-watertight geometry and 24 components; this does not negate the historical physical fit observation.

**Physical:** Handoff: +0.30 mm total still wobbly; +0.10 and +0.20 had similar low true play; +0.10 slightly harder to dislodge and selected. +0.50 previously too loose.

**Outcome:** Preserve calibrated top interface. Do not assume it transfers to differently oriented rear joints or TPU interfaces.

[Artifacts and review](versions/v6-calibration-inherited/REVIEW.md)

## v6a — V6A mechanically retained TPU foot

**Change / why:** Added external PLA corner catches and mating TPU window shoes, keeping the bottom rail intact. Replaced friction-only retention with an intentional peel-to-release interface.

**CAD:** Recorded component/watertightness checks, material-preservation booleans, nominal contacts, rigid blocking checks and independent SCAD export comparison. Found inherited disconnected top bosses and 243 mm provisional height with sole.

**Physical:** User printed shoe and PLA key/coupon, reported it fit and passed the tests. Small internal gap opposite the key slot was reported. Exact forces and per-test cycle counts were not supplied.

**Outcome:** Local TPU interface accepted for reuse; not full-structure validation. Next reconcile top/height and across-width bracing.

[Artifacts and review](versions/v6a/REVIEW.md)
