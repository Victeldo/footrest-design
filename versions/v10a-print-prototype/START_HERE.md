# V10A — user-requested prototype STLs

Print one LEFT support, one RIGHT support and one BRACE. Reuse the existing V7/V9 top. These supports replace the old T-rail supports; do not mix the two joint systems. Left and right are distinct files, not two copies of the old identical support.

- V10A_left_PLA_PROTOTYPE.stl: 163 x 230 x 23.5 mm.
- V10A_right_PLA_PROTOTYPE.stl: 163 x 230 x 23.5 mm.
- V10A_brace_PLA_PROTOTYPE.stl: 180 x 180 x 8 mm.

All are PLA and already oriented on z=0. Keep the supplied orientations. Each support's sockets open upward in print; the brace lies flat with the tongue/back faces on the bed. Use your established PLA profile; prior baseline was 0.4 mm nozzle, 0.2 mm layers, six walls, six top/bottom layers and 20–30% infill. This new fit/orientation has NOT been physically calibrated. Inspect sliced pockets, roofs and walls, and filament estimate before printing. No slicer/toolpath validation was performed. No support material is intended inside the sockets.

For lowest waste, print one support and the brace first, assess both tongue fits by hand, then print the other support if they seat and release comfortably. The first partial assembly is not a load test. Do not hammer, force or substantially sand the joint to make it fit. Nominal socket clearance is 0.15 mm per face, but the earlier 0p15 C-channel result does not validate these new rectangular sockets.

Assembly: top off; hold brace between supports; move the supports inward over the tongues; then install the top. Both socket pairs face inward. To disassemble, remove the top and move the supports apart. The tongues have 12 mm nominal engagement and 2 mm blind-end gap. The joint does not depend on a wedged friction fit.

Before foot load, gently assess assembled sideways racking and watch for top lifting, support spreading, joints unseating or damage. Stop on any of those observations. The top is still unlatched; coupled top-lift/splay and member flex have not been solved or validated. This is an experimental release requested by the user, not a verified fix or a 200 N rating. Do not stand on it.

The mirrored support arrangement requires checking existing TPU shoe handedness/orientation before reuse. No new TPU shoe is included or declared validated. Keep floor slip distinct from joint racking in observations.

## Change from V10 concept

Socket blocks now extend from x=18.5 instead of x=22 on the left (mirrored on the right), reaching the original flat bed face. This avoids starting the projecting block 3.5 mm above the bed. Socket voids, tongues, top and engagement are unchanged. Added material is external to the original rail; strength is not quantified.

## Checks

World-coordinate assembly checks rerun: no nominal interference in assembled state, side-entry path (0.25 mm steps), or top installation (0.5 mm steps). Fixed-top rigid blocking tests remain conditional on the top staying seated. All print exports reload as single watertight components with consistent winding and positive volume, and fit the A1 object envelope. Reverse transforms match world meshes to STL coordinate rounding: maximum nearest-vertex error 0.0005 mm; volume symmetric differences under 1 mm³ on ~102,000 mm³ supports. See geometry_checks.json. No FEA, physical fit, load, fatigue, creep or TPU-regression claim is made.

Source V10A_prototype.scad uses reference/V7.scad. Select left_print, right_print or brace_print for the printable orientations. Other selectors are world-coordinate reference parts, not print-oriented exports. validation_workspace.py records the checks and depends on work/v10a renders in the original project workspace.
