# V7 — one-piece top and braced flat-pack footrest

**Status: geometry-checked prototype. Print the two PLA joint pairs first.**
200 N is the agreed provisional vertical design/check load, not a tested working-load rating. The user's measured seated load was approximately 25.6 lb = 113.9 N. No standing/step-stool use is intended.

## What changed

The one-piece top is 240 × 170 mm, with a 2.4 mm skin, three 5 mm-wide main ribs reaching 16 mm below the top, smaller cross-ribs, a 10 mm-deep perimeter and 6 mm corner radii. Four blind socket bosses are part of that same solid body. No lightening cut crosses their walls. The calibrated top connection stays 7.00 × 22.00 mm into 7.10 × 22.10 mm, with 7.00 mm straight engagement.

Support centerlines are 22 and 218 mm across the top: 196 mm apart, with 22 mm centerline-to-edge overhangs. The top sits on support shoulders, not on a disconnected boss. New guides extend 8 mm alongside the 10 mm-high upper rail with a 7.4 mm gap (0.2 mm per face). They spread joint bearing over a longer region without changing the tab engagement. Guide fit is provisional.

The support body is shortened from 234 to 223 mm, and brace endpoints follow the new height. The height stack is 2 mm sole + 223 mm body + 16 mm deck = **241 mm nominal, before TPU compression**. Tabs extend 7 mm into the 16 mm deck, leaving 9 mm above their ends. Printed support height including tabs is 230 mm.

The V5 10 mm perimeter rails and 8 mm diagonal widths are retained. Added 6 × 3 mm flanges along the tall rails help resist bending across their thickness. The flanges taper out before the foot and top guide regions. No bottom-rail material is removed.

The out-of-plane frame screen exposed a weakness that top guides alone cannot solve. A removable rear X-brace now ties the supports together. It has 8 × 6 mm diagonal members, four 7 × 22 × 7 mm tabs and no glue or hardware. Added blocks behind each rear support rail receive those tabs; their socket cuts lie outside the original rail. The brace is retained by the trial press fit, not a positive latch. Its handling retention and four-point registration must be checked in the physical assembly.

The rear panel makes overall assembled depth **174 mm**, although the top remains 170 mm. All parts remain flat-packable.

**V6A foot geometry and catches are unchanged.** The user has already passed its seating, retention, cycling and dragging tests. Do not reprint another foot coupon.

## Print first: four small PLA pieces, two tests

All STLs are in millimetres and already in their intended print orientations. Keep those orientations: rotating a coupon can change the fit/bridge behavior it is supposed to test.

1. `PRINT_FIRST_top_socket_coupon.stl` — approximately 11.2 g solid PLA.
2. `PRINT_FIRST_top_tab_coupon.stl` — approximately 4.1 g solid PLA.
3. `PRINT_FIRST_brace_socket_coupon.stl` — approximately 5.0 g solid PLA.
4. `PRINT_FIRST_brace_tab_coupon.stl` — approximately 6.7 g solid PLA.

The four pieces can share one PLA plate, without material changes or a prime tower. For the lowest commitment, print the top pair first (about 15.3 g), then the brace pair (about 11.7 g). These are solid-volume estimates at 1.24 g/cm³, not slicer predictions; purge, brim and actual infill change usage.

For an assumed 0.4 mm nozzle, start with your proven PLA profile, 0.20 mm layers, six walls, six top and six bottom layers, and 20–30% infill. Use the same settings/material for the eventual matching parts. Six walls are intended to make the narrow ribs and brace members largely solid; inspect the actual toolpaths because line width changes that result. These settings are a starting point, not a validated print recipe.

Supports are not intended. The **brace socket has a 22.1 mm roof bridge**; inspect that bridge in the slicer and the printed coupon. Layer quantization also affects its 7.1 mm opening because that dimension lies through the support's print thickness. Do not enlarge or sand the opening before reporting whether it fits. Remove loose strings only. If the roof sags and obstructs insertion, stop and report it; that is precisely why this coupon comes before a full support.

### Top joint test

Insert the male tab into the socket between the two guide cheeks, as shown in `V7_coupon_assemblies.png`. The tab should enter fully by hand and the shoulder should seat against the boss underside. The guide cheeks should straddle the 7 mm-thick body without jamming; slight guide clearance is intended. Check for obvious side-to-side rocking, then assemble/disassemble 10 times. Report tightness, full seating, rocking and any whitening/cracking. This checks fit and local handling, not the top's bending capacity.

### Rear-brace joint test

Insert the projecting tab into the side opening of the socket block until its pad seats against the block's mouth. It should engage 7 mm by hand, have little transverse play, resist falling out during ordinary handling and be removable without tools. Repeat 10 cycles. Report any bridge sag, scraping, looseness or damage. The nominal cross-section matches the earlier calibrated joint, but its print orientation is different; it is not assumed calibrated merely because the numbers match.

No test here establishes a full 200 N capacity. Report these results and slicer grams/time before committing the large parts.

## Full prototype files — after coupon results and slicer review

- `V7_top_PROTOTYPE.stl`: print 1, 240 × 170 × 24 mm. Smooth foot-contact surface faces the bed; ribs and guides grow upward. About 252 g solid PLA.
- `V7_support_PROTOTYPE.stl`: eventually 2 identical parts, 158 × 230 × 14.1 mm. Flat original face on bed; catches, stiffeners and socket blocks upward. About 111.5 g solid PLA each. Print one representative support first to inspect rail continuity, upper tabs, brace sockets and the existing TPU foot fit.
- `V7_rear_brace_PROTOTYPE.stl`: eventually 1, 220 × 190 × 13 mm. Flat X on bed, tabs upward. About 52.7 g solid PLA.
- `V6A_unchanged_foot_left.stl`: 2 total for the complete assembly; your successful test shoe can count as one.
- `V6A_mirrored_foot_right.stl`: 2 total for opposite corners. About 2.24 g solid TPU each at assumed density 1.20 g/cm³. Print separately from PLA, sole down, with your tested TPU settings.

The theoretical fully solid total is about **537 g**, excluding coupons, brims and purge. This is not weight-optimized further: the extra rear brace and local rail stiffeners address a structural weakness. Actual slicer usage must be reviewed before deciding whether and where to reduce material.

The top leaves only 8 mm nominal bed margin per side along its 240 mm direction; center it and check any brim and printer exclusion areas. Do not scale parts to make a brim fit. Other pieces have more margin.

## Assembly order

1. Attach the tested TPU shoes to the support corners. Each support takes one left and one mirrored right shoe.
2. Place the top upside down on a protected surface. Insert both supports into the top. Their added rear socket blocks must face the same rear edge, and their raised printing faces must point toward the same global side, as in the reference model. Do not mirror one support: the brace block thickness is intentionally asymmetric.
3. With both supports fully seated, align all four rear-brace tabs and slide the brace forward into their rear-facing sockets. Support the joint areas while seating; do not flex a diagonal to force a misaligned tab.
4. Turn upright and check that all soles contact the floor, all shoulders/pads remain seated, and there is no obvious rocking or loose brace. Refer to the assembly image or open `V7_assembly_REFERENCE.glb` in a compatible 3D viewer. This GLB is not a print file.

The coupons cannot establish four-socket registration, whole-frame stability or brace retention during handling. Those checks occur on the real assembly. Full assembly must still undergo a staged measured load/deflection check, lateral/handling check and sustained seated-use observation before treating the prototype as accepted. The next load-test details should be selected after the coupon results and actual slicer settings are known.

## Validation performed

OpenSCAD 2021.01 rendered the native source; Manifold3D and Trimesh then checked the exported solids. Every individual STL is watertight, has consistent winding and exactly one connected component. All fit within a 256 mm cube in their supplied orientation.

All 28 pairs in the eight-component assembly (top, two supports, rear brace, four feet) were checked for unintended intersection. Maximum overlap was numerical zero. Sampled insertion paths for the supports and rear brace also have no interference. Small deliberate over-insertion produces shoulder contact, confirming the intended stops exist.

The actual tab solids were compared with exact 7 × 22 × 7 mm boxes. All four top socket voids and their complete walls/roofs were checked with solid booleans. The top and brace coupon assemblies have zero unintended overlap. Foot geometry and catch projections were compared with V6A; their differences are numerical zero. The complete 150 × 10 × 7 mm bottom rail remains present.

See `geometry_checks.json` for measurements, checks and STL hashes, and `ENGINEERING_NOTES.md` for the structural model and its limitations. Geometry validity is not a strength certification.

## Source and reproducibility

`footrest_V7.scad` defaults to a colored assembly preview. Its `part` selector can export each part or coupon. The default dimensions are checked; editing dimensions requires rerunning validation and possibly updating the assembly transforms/model assumptions.

`build_and_validate.py` renders all individual parts using an installed OpenSCAD executable, validates them, and regenerates STL/GLB files. Install the packages in `requirements.txt` in a Python virtual environment, then run `python build_and_validate.py --openscad /path/to/OpenSCAD`. `structural_screen.py` reproduces the approximate beam calculations. `render_views.py` creates the mesh-derived pictures. Reference V6A meshes are supplied only for regression checks.
