> ASSEMBLY TEST FAILED: user reported racking and upper channels lifting off. Do not reprint the unchanged brace as a fix. Current next step: ../V9C_fit/START_HERE.md. Existing top/supports are retained for the fit revision.

# V9 full-size assembly-test prototype

The user-tested drop-in fit is retained. The channel and full brace are geometrically identical to the V9 concept. Each T rail now has a backing pad extending 6 mm into the rear rail region and 3 mm above/below its engagement, without entering the sliding channel. No separate key, cord or latch is required. No original rail material was removed.

## What to print

- V9_support_PLA_PROTOTYPE.stl: TWO identical copies, 164.3 x 230 x 14 mm. Print the first support and brace before committing the duplicate.
- V9_brace_PLA_PROTOTYPE.stl: ONE, 217 x 180 x 13.6 mm.
- V9_top_PLA_PROTOTYPE.stl: ONE, 240 x 170 x 24 mm. This is unchanged from V7; reuse an intact V7 top if already printed.
- V9_foot_left_TPU95A.stl and V9_foot_right_TPU95A.stl: TWO of each for four feet total. Reuse matching successful V6A/V7 feet. These interfaces are unchanged.

All STLs are in millimetres and oriented for printing. Do not mirror one support: both supports have their raised printing faces pointing in the same global direction in the assembled model. The brace is asymmetric through its thickness and aligns with these identical supports.

Use the material/profile that produced the successful V9 coupons, preserving their orientation-dependent fit. If using the previous baseline: 0.4 mm nozzle, 0.20 mm layers, 6 walls, 6 top/bottom layers, 20–30% infill. These are starting settings, not a strength qualification. Print TPU separately with your successful settings. No multi-material purge tower is needed.

The top prints smooth face on the bed. Supports print original flat face down. The brace prints its flat X/back faces on the bed, channels facing up. Inspect the channel shoulders, stop ledges and root additions in sliced preview. The coupon established the local fit/print approach, but the new backing pads and whole parts have not been physically printed. The short ledges include local overhangs; no automatic support generation or slicer validation was performed. Do not add supports inside the sliding surfaces without checking their effect on fit.

Center the 240 mm top: it leaves only 8 mm nominal margin on each side of the 256 mm plate. Check brim and exclusion areas. Do not scale any part. Each large part should have its own plate unless the slicer verifies another arrangement; printing two supports together is not assumed feasible.

Actual filament consumption must come from the slicer. The earlier reported V7 masses are historical, not V9 predictions. The root backing adds only about 0.23 g solid PLA per support over the V9 concept.

## Low-waste print order

1. Print one support and the rear brace. Engage both joints on that one support, then lift the brace off. Check simultaneous seating, easy removal and no root whitening. Do not use the cantilevered brace as a lever or load this partial assembly.
2. If both joints slide and seat as expected, print the second identical support. Reuse or print the unchanged top and TPU feet.
3. Assemble the complete prototype and assess whole-frame behavior below. No further isolated coupon is requested.

## Assembly

Fit one left and one right TPU shoe to each support. Place both supports upright with their rear T rails at the same rear edge, and both raised printing faces pointing the same global direction; use the assembly image as the orientation reference. Hold them about 196 mm apart at their center planes.

With the top off, align the brace channels roughly 21 mm above their seated positions. Approach from the rear and lower all four channels together onto their stops. Guide at the joint blocks rather than bending an X member to force alignment. Install the top over the four calibrated tabs; the support shoulders should seat against the top.

The four C backs should sit on their ledges. Print variation may prevent perfect four-point seating; if one corner floats, report it instead of forcing or sanding the assembly immediately. Reverse the sequence for packing: remove the top, support the side frames, lift the brace about 21 mm and separate.

The top does NOT positively block brace lift-off. Lift-off is the intended release mechanism. Carry disassembled or support the components together; do not assume lifting by the top or brace retains the rest.

## Full-assembly evaluation

First check all four feet touch a flat floor and all top shoulders and brace stops seat. With hands at the top, gently alternate lateral pressure in both directions while watching each C channel. Distinguish a small initial clearance take-up from continuing flex, clunking or a corner rising off its stop. Record a short view of the rear if the motion is difficult to describe.

Stop for joint climbing, increasing movement, whitening, cracks or an unseated top. If the assembly remains stable, introduce seated heel pressure gradually while keeping your weight on the chair and inspect again. Do not stand on it. This initial check does not certify the provisional 200 N target, cyclic durability or long-term creep. An agreed measured-load test can follow the seating/racking results; normal use is not yet validated by CAD.

## Completed checks

Each exported mesh was reloaded and verified as one connected, watertight component with consistent winding and positive volume. All object envelopes fit the A1 bed. Nominal full-assembly interference is numerical zero, including all four TPU feet. Vertical brace travel and raised rear approach were sampled every 0.25 mm; top installation every 0.5 mm. No collision was found. The brace and top were Boolean-compared against their previous versions and are identical.

These checks do not simulate printed tolerances, human assembly force, elastic deformation or layer strength. See geometry_checks.json for measurements and hashes, ENGINEERING_REVIEW.md for joint reasoning, and V9_full_assembly.png for orientation.

## Rebuild

Install OpenSCAD and the Python packages in requirements.txt, then run `python build_and_validate.py --openscad /path/to/OpenSCAD`. This rerenders the five parts, repeats validation and writes the STLs/report next to the source. The reference meshes are regression inputs, not additional print parts.
