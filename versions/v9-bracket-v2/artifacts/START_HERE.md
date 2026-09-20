# Rear bracket V2 — tested 0p15 fit

Print ONE PRINT_V9_bracket_V2_0p15_PLA.stl. It replaces the loose original V9 rear bracket. Keep your existing printed top and both supports.

All four channels now use the successful 0p15 coupon geometry: 0.15 mm nominal clearance per axis-aligned face, approximately 0.21 mm normal to the angled shoulders. Engagement remains 20 mm. X members, outside dimensions, joint spacing and assembly orientation are unchanged. No latch or anti-lift stop has been added.

## Print

Use the same PLA and slicer settings as your successful 0p15 coupon. Preserve the supplied orientation: flat X/back face on the bed, channels facing up. Size: 217 x 180 x 13.6 mm, within the A1 envelope. Inspect the sliced shoulder overhangs and channel openings. No new sliced toolpaths were generated or verified here. Solid-volume estimate is approximately 45.4 g; actual filament use comes from your slicer. The change adds about 0.53 g solid PLA over the previous bracket.

If you have not already done so, try the successful 0p15 coupon on all four actual rails before starting this larger print. Do not force it onto a rail that differs from the one originally tested.

## Assemble and evaluate

Remove the old rear bracket. With the top removed, align all four channels about 21 mm above their seated positions, approach from behind and lower straight down onto the stops. Guide at the joint blocks; do not bend the X to force four-point alignment. Install the existing top. All four channel backs should rest on their ledges.

Before applying foot load, gently alternate sideways pressure with the assembly on a flat floor. Compare racking against the original bracket and watch the upper AND lower connections for upward movement. Stop for climbing, binding, cracking, whitening or a floating corner. Confirm hand removal remains practical, supporting the side frames while lifting the bracket.

A closer local fit does not prove full-frame stiffness or anti-lift behavior. If V2 still climbs, reduced clearance alone has not solved retention. No 200 N capacity or normal-use qualification is claimed. Report seated play, racking, corner lift and removal effort before further load testing.

## Geometry validation

The exported and reloaded bracket is one connected watertight solid with consistent winding. All four nominal channels clear the current supports in the assembled position and sampled 21 mm vertical release/raised rear approach paths (0.25 mm increments). The existing top's installation path was sampled at 0.5 mm increments. All collision checks returned zero volume.

The full mesh was compared against the old brace unioned with four copies of the tested 0p15 coupon. Symmetric difference was 0.00994 mm³ over roughly 36,600 mm³, within a 0.02 mm³ numerical tolerance for STL/float coordinate rounding. This verifies the intended channel-only revision to mesh precision. See geometry_checks.json for dimensions, checks and hash.

Source: V9_bracket_V2_0p15.scad is self-contained and exports the full bracket directly. validation_workspace.py records the validation using the existing project reference meshes; it is not a standalone rebuild tool.
