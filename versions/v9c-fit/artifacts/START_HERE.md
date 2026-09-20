# V9C: tighter C-channel fit tests for the EXISTING printed supports

The full V9 assembly racked and its upper C channels slid upward off their T rails. All floor corners contacted the ground. This is a failed assembled-brace test, not a TPU-foot issue. The printed top and supports are retained for this iteration; that does not establish their load capacity.

## Print only the 0p20 channel first

V9C_channel_0p20_PLA.stl reduces nominal axis-aligned clearance from 0.30 to 0.20 mm per face. Head pocket width changes from 14.6 to 14.4 mm, stem opening from 7.6 to 7.4 mm. The corresponding 45-degree shoulder normal gap changes from about 0.42 to 0.28 mm. This is an adjustment to BOTH lateral and fore-aft mating surfaces, not uniform scaling.

Use the same PLA, layer height, line widths, wall settings and supplied orientation as your full V9 brace. Flat back on the bed, channel upward. Do not rotate it upright, scale it, or sand mating surfaces before assessing the result. If the slicer requests mesh repair, stop and report that. The solid-volume estimate is 4.64 g at 1.24 g/cm³; actual slicer consumption may differ.

V9C_channel_0p15_PLA.stl is an optional tighter fallback, not a request to print both immediately. It uses 0.15 mm per face (14.3 mm head pocket, 7.3 mm stem opening, approximately 0.21 mm bevel-normal gap), about 4.69 g solid. Layer quantization and extrusion variation mean a 0.05 mm nominal change may not produce a distinct fit on every surface. Compare sliced layers if the two prints feel identical.

The pieces have no physical size labels. Print individually or label their exterior immediately if printing both. No new T-rail coupon, support or top is needed.

## Test against all four actual rails

Remove the top and rear brace for access, and hold each support securely. Slide the single test channel downward over a T rail to its ledge, then lift it off. Do not snap it on from the rear. Repeat on all four T rails, keeping track of support and upper/lower position.

The goal is easy finger-operated sliding with clearly less sideways/backward movement when seated. Hold close to the channel rather than applying leverage. Compare with the original loose coupon if available. Some upward sliding is unavoidable and intended; this test does not create an upward lock.

Repeat approximately ten cycles on each rail if initial movement is easy. Stop if it jams, needs force, shows whitening/cracks, or scrapes heavily. A fit that is good on three rails but binds on the fourth is not suitable for a four-channel brace. Do not force the tighter 0p15 part if 0p20 is already tight.

If 0p20 is comfortably removable on all four rails and removes most seated play, report that result; there is no need to chase the smallest number. If it is still clearly loose, try 0p15. Report insertion/removal effort, seated play and any difference among the four rails.

## What changed and what did not

Only the C-channel cavity shrinks. Exterior envelope remains 21 x 20 x 13.6 mm in print coordinates; engagement stays 20 mm. Material is added to the inner faces, not removed from structural walls. No latch, taper, extra fastener, support modification or top modification is introduced.

The 0.30 parameter version was Boolean-compared with the original V9 coupon and reproduces it. Both tighter exports are one connected, watertight mesh, with consistent winding and positive volume. Nominal approach and 21 mm vertical travel against the current full support at both joint heights were sampled every 0.25 mm with zero overlap. Intentional sideways/backward/downward overtravel produces blocking contact. Exported STLs were reloaded and checked. See geometry_checks.json.

These checks do not predict printed friction or deformation. No sliced toolpaths, material strength or full revised-brace test is claimed. Because the supports are identical, one nominal support geometry covers both sides; the physical test still needs all four printed rails.

## Next decision

After selecting the loosest variant that gives acceptable play and easy release across all four rails, update the full brace only, recheck its geometry and test the assembled frame again. A local fit test cannot demonstrate that four joints will register without binding or that the frame will resist racking.

Reduced clearance may reduce motion leading to lift-off. It does not physically prevent upward disengagement; continued climbing in the full assembly would mean this approach is insufficient. No replacement full-brace STL is released in this pack yet. Do not resume loading the loose V9 assembly pending the revised-brace test.
