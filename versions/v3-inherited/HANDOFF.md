# Modular Backpack Footrest — Codex Handoff

## Goal
Design a compact, flat-pack, tool-less 3D-printed office footrest inspired by an IKEA kids bathroom stool, but optimized to fit in a backpack and assemble at the office.

Target use: seated footrest only. Not intended to be stood on or used as a step stool.

## User / Printer Constraints
- Printer: Bambu Lab A1, 256 x 256 mm bed.
- Main structural material: PLA.
- TPU 95A is now available for replaceable non-slip feet.
- User strongly prefers low filament waste and wants engineering decisions explained as the design evolves.
- Design should look intentional/product-like, not like a bulky hobby print.
- Tool-less assembly; avoid screws/nuts/bolts/glue where practical.

## Target Dimensions
- Finished height: 9.5 in = 241 mm.
- Current top target: about 230 x 170 mm.
- Flat-pack parts must fit A1 bed individually.

## Physically Calibrated Tab/Slot Fit
This is the most important validated parameter.

Existing support tab nominal cross-section:
- 7.00 mm thick
- 22.00 mm wide
- 7.00 mm insertion depth

Physical clearance test used 7 mm-deep sockets:
- I = 7.10 x 22.10 mm (+0.10 mm total clearance)
- II = 7.20 x 22.20 mm (+0.20 mm total clearance)
- III = 7.30 x 22.30 mm (+0.30 mm total clearance)
- Earlier 7.50 x 22.50 mm (+0.50 total) was visibly too loose.

User test result:
- III still too wobbly.
- I and II had similarly little true joint wobble.
- I was slightly harder to dislodge and felt slightly more stable.

DECISION: use 7.00 x 22.00 mm tabs into 7.10 x 22.10 mm sockets.
Keep 7 mm engagement. Do NOT increase depth unless future full-scale geometry reveals actual angular play. The previous idea of 12-15 mm engagement was abandoned because the observed coupon movement was mostly the tiny coupon tipping off its edge, not the joint rocking inside the socket.

## Current Structural Direction
The side support should be a lightweight truss/frame rather than a solid panel or honeycomb-filled slab.

Engineering reasoning:
- Main deformation mode is racking/shear of a tall rectangular support.
- Triangulation is more material-efficient than generic honeycomb for this specific load path.
- Keep material around the perimeter and at joints; remove material from low-value interior regions.
- Avoid long skinny members that become buckling-prone.
- Local gussets/junction reinforcement are preferable to making every member thick.

Current V5 support geometry:
- Overall support part envelope: 150 x 241 x 7 mm.
- Structural body height: about 234 mm + 7 mm tabs.
- Perimeter frame width: 10 mm.
- X-braces: 8 mm.
- Small local junction pads/gussets at brace/frame intersections.
- Two top tabs: 22 x 7 x 7 mm, centered approximately at 39 mm and 111 mm across the support width.
- Mesh was validated as one connected, watertight body.
- Raw solid geometry volume: ~80.17 cm^3, roughly 99 g PLA-equivalent if fully solid. Actual slicer usage will depend on walls/infill.

Previous V4 was 12 mm perimeter / 10 mm X-braces and was ~95 cm^3. V5 reduced raw geometry volume by ~16%.

DO NOT blindly shrink rails further. If optimizing weight, reason about buckling, member slenderness, joint loads, and print orientation.

## Top Platform
Current top concept/source is from V3 and is not yet final relative to the latest V5 support.

V3 concept:
- ~230 x 170 mm top.
- Lightweight underside pockets/ribs rather than a thick solid plate.
- Four calibrated sockets for the two side supports.
- Local bosses around socket locations so the full 7 mm engagement is available without making the whole top 7 mm thick.

Important: before printing a full top, reconcile the top socket positions with the final V5/V6 support geometry and validate assembly computationally.

## TPU Feet — Current State
Decision: use small replaceable TPU 95A feet for grip and floor protection.

Engineering philosophy:
- PLA carries structural load.
- TPU handles friction/compliance.
- TPU should be a replaceable wear item, not a structural requirement.

A V5 TPU slip-on shoe exists in the attached files, but DO NOT treat it as final.
Issue discovered: the V5 PLA support has no dedicated connector/retention geometry; the TPU shoe only friction-grips the bottom rail.

NEXT DESIGN CHANGE REQUIRED:
Add an intentional mechanical retention feature to the bottom corners of the PLA support and redesign the TPU foot to mate with it. Preferred concepts:
- shallow dovetail,
- T-slot / mushroom-style slide feature,
- small captured snap geometry suitable for TPU 95A.

Requirements for TPU foot connector:
- should not materially weaken the 10 mm bottom rail,
- localized near each bottom corner,
- easy to replace,
- no glue,
- mechanically retained so it does not walk off when the footrest is moved,
- keep each TPU foot only a few grams.

Do NOT print the existing TPU foot before redesigning this interface.

## Validation Workflow — Important
The user wants a disciplined, low-waste engineering workflow.

For every major revision:
1. Validate dimensions against A1 bed and 241 mm assembled height.
2. Validate tab/slot dimensions use the physically tested fit: 7.00 x 22.00 tab, 7.10 x 22.10 slot, 7 mm engagement.
3. Assemble parts computationally and check positions/alignment.
4. Check meshes are watertight.
5. Check connected-component count: a structural part should be one connected body. This matters because an earlier diagonal brace only appeared connected but exported as a separate shell.
6. Check for unintended intersections or gaps at brace/frame/tab junctions.
7. Calculate raw mesh volume and approximate material mass.
8. Prefer small coupons for any new joint/TPU retention feature before committing a large print.
9. Slice before printing large structural parts and inspect predicted grams/time.
10. User prefers printing one representative part first before committing to duplicates.

## Known Failure / Lessons Learned
- Earlier support brace visually approached the perimeter but was actually a disconnected mesh. Always check component count after STL export.
- Earlier clearance of +0.50 mm total was too loose.
- Do not change two experimental variables at once; e.g. clearance and engagement depth should not be altered together when calibrating.
- The user is actively checking geometry and will notice questionable interfaces. Explain why each change is mechanically justified.

## Suggested Next Steps
1. Modify the V5 support bottom corners to include a shallow, structurally safe TPU-foot retention feature.
2. Design one tiny TPU 95A test foot/coupon around that connector.
3. Validate the connector mechanically/geometrically before changing anything else.
4. Reconcile/update the top platform against the finalized support/tab layout.
5. Build an assembled reference model and run component/interference checks.
6. Compute actual volume/material estimates.
7. Ask user to slice one support in Bambu Studio and report grams/time before printing it.
8. Only then decide whether the 10 mm perimeter / 8 mm brace can be reduced further.

## Files Included
- flatpack_footrest_v5_light_support.scad — current support source, best structural starting point.
- flatpack_footrest_v5_light_support.stl — current support export.
- flatpack_footrest_v3.scad — older full design source containing top/assembly concepts; use carefully because support has evolved since then.
- flatpack_footrest_v3_top.stl — current top reference, not final.
- footrest_tolerance_coupon_v6_7mm_sockets_only.stl — physical calibration coupon used to choose +0.10 mm clearance.
- flatpack_footrest_v5_tpu_foot.scad / .stl — obsolete friction-fit TPU foot concept; reference only, needs connector redesign.
