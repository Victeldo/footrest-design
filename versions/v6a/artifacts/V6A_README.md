# V6A retained TPU corner foot — first physical trial

This is a coupon-stage design, not a validated final foot or full footrest. Print **one PLA coupon and one TPU foot**, inspect the fit, and return the observations below before printing full supports or duplicate feet. The supplied handoff was read before source and mesh inspection; its historical decisions were treated as design context. Original files are unchanged.

## Files and current status

- `V6A_PLA_corner_coupon.stl`: 32 × 22 × 9.2 mm representative bottom-left corner. PLA, flat original support face on bed, catch facing up.
- `V6A_TPU95A_test_foot.stl`: 29.8 × 11.1 × 16 mm in supplied print orientation. TPU 95A, sole on bed. No rotation or scaling needed.
- `V6A_retained_foot.scad`: editable native geometry. Default `part="coupon"`; use `"foot"`, `"coupon_assembly"`, `"support_reference"`, or `"support_assembly"`. The full support selectors are previews, not instructions to print a complete support yet.
- `V6A_interface_review.png`: mesh-derived views and cross-section.
- `geometry_checks.json`: baseline and new-part measurements and exact-solid intersection tests.
- `source_export_checks.json`: independent OpenSCAD 2021.01 export checks against the generated meshes.
- `reference/`: unchanged input files, for provenance only. Do not print the obsolete V5 foot or V3 top from this folder.
- `validate_and_build.py`: reproducible Manifold/Trimesh generator and geometry checks using the reference STLs. Dependencies are listed in `requirements.txt`. Run in a virtual environment with `python validate_and_build.py`; intermediate outputs go in `work/`. This validates default dimensions. Parameter edits in SCAD must be exported and checked anew; they do not automatically change the Python construction.

## Why this connector

The full 10 mm-high × 7 mm-thick V5 bottom rail, braces, gussets and top tabs are retained. Two small catches are added on the support's upper printing face, one near each lower corner. The catch root overlaps the existing material by 0.2 mm, so this is a solid union, not touching shells. No hole, slot, notch or rail thinning is introduced.

A groove cut into a thin rail can remove material from an important bending section and create a stress concentration. An external catch avoids that section loss. It still needs a physical test for catch-root damage and layer adhesion; preserving the rail section is not a load-rating calculation.

Each TPU shoe has a 2 mm sole, side walls, an outer-end stop and a through-window. The PLA bottom bears directly on the TPU sole. The catch is unloaded by ideal downward compression and primarily retains the shoe during lifting or dragging. In-plane handling forces meet the end stop or catch/window edges. The opposite side wall restrains motion across the 7 mm rail thickness.

The catch has a 45° entry ramp and a roof-shaped retaining edge. The window follows that retaining edge with nominal 0.25 mm vertical clearance, distributing capture across its width. Pull-off requires the window wall to flex outward over the catch, rather than merely overcoming surface friction. For replacement, deliberately peel that wall outward and withdraw the shoe toward the floor. This is positive geometric retention, but release force and fatigue are not yet established.

The roof-shaped window narrows to a 2 mm bridge at its top. This avoids asking TPU to bridge the full 10.5 mm window width. The PLA catch grows from the upward face during printing and needs no underside support. Slicer inspection is still needed to confirm the roof and ramp toolpaths with your profile.

## Nominal fit dimensions

- Rail remains 7.00 mm thick. Shoe channel is 7.50 mm wide: 0.25 mm clearance per face.
- Catch spans x = 9–19 mm from the outer corner; it rises 2.2 mm beyond the PLA face.
- TPU window wall is 1.8 mm thick; its inner face is at z = 7.25 mm.
- Passing the catch therefore requires up to 9.2 − 7.25 = **1.95 mm local outward displacement**. This is displacement, not a measured strain or installation-force prediction. The constrained TPU wall bends and stretches nonlinearly.
- Sole nominal contact with PLA is 28 × 7 = 196 mm² at each foot; actual floor pressure depends on load, sole deformation and the printed surface.
- Existing top tabs remain **7 × 22 mm, 7 mm engagement**, centers 39 and 111 mm. The historical **7.10 × 22.10 mm socket decision is preserved**. Its PLA/PLA fit does not calibrate TPU clearances.

## Geometry evidence

Checks use Manifold3D solid booleans plus Trimesh STL topology checks; the native SCAD was also compiled independently in OpenSCAD 2021.01 and compared with the generated solids. STL exports were reloaded and checked.

- V5 support: one watertight connected body, 80.1749 cm³.
- Modified reference support: one watertight connected body, 80.4191 cm³, 150 × 241 × 9.2 mm envelope. Original V5 material removed: **0 mm³**. Two catches add 244.2 mm³ (0.2442 cm³), about 0.30 g PLA at an assumed 1.24 g/cm³, or 0.30% added solid volume.
- PLA coupon: one watertight connected body, 3.8213 cm³, about 4.74 g fully solid PLA at 1.24 g/cm³.
- TPU foot: one watertight connected body, 1.8670 cm³, about 2.24 g fully solid TPU at an assumed 1.20 g/cm³. Use your spool density for a better estimate.
- Zero seated solid overlap for the coupon/foot, full support/left foot, full support/reflected right foot, and foot/foot pairs. The rail underside and sole touch intentionally; lateral assembly gaps are 0.25 mm nominal.
- Translating the seated shoe down 1 mm produces 13.5 mm³ collision with the catch. Translations of ±1 mm along the rail and ±1 mm across it also collide with the support. These checks demonstrate obstructions to straight rigid translation, **not** a measured retention force or proof against every combined rotation/peeling path.
- A rigid insertion sweep intentionally intersects the catch. The wall must flex during assembly; this is not a collision-free rigid sliding joint.
- Both support positions were transformed into the original V3 assembly coordinates. Their tab locations align with the nominal sockets, and solid top/support overlap is zero. This does not establish functional socket walls or validate the top structure.
- Both coupons fit easily inside the stated 256 × 256 mm bed. The reference support's 150 × 241 mm flat footprint fits the nominal bed, leaving only 15 mm total in its long direction before brims and printer exclusions.

No FEA, strength certification, fatigue test, floor-grip test or printer-specific slicing was performed. Filament masses above are solid-volume estimates, not slicer predictions.

## Inherited issues found during inspection

**Height:** V5 reaches 241 mm from bare rail bottom to tab top. The V3 platform is positioned with its top at the same height. Adding this sole yields **243 mm uncompressed overall height**, not 241 mm. This trial deliberately leaves V5's structural height and calibrated engagement unchanged. After foot fit succeeds, reconcile nominal overall height with the top. One possible later revision is reducing support body height by the sole allowance while retaining 7 mm engagement; that would require new brace/junction and assembly validation. Actual loaded height also depends on TPU compression.

**V3 top:** the supplied STL is watertight but has **five disconnected bodies: the platform and four separate socket bosses**. Each boss ends at about z = −0.01 mm; none is joined to the platform. Its lightening cuts and boss/socket region need inspection and repair before a full top print. Watertightness alone is insufficient. This inherited top is not modified or endorsed by the present connector trial.

**Historical tolerance coupon:** the supplied mesh reports non-watertight geometry and 24 components under the current parser. This does not negate the reported physical fit experiment. The selected tab/socket fit is retained; re-export/repair that mesh if it is needed again.

**Handedness:** the delivered test foot is for the illustrated corner. The opposite corner uses a reflected shoe. Reflection was included in the assembly checks, but a duplicate production batch has not been released. Do not assume four identical end-stop shoes fit all corners.

## Low-waste print and test sequence

1. Import each test STL separately into Bambu Studio with the correct material profile. Confirm millimetres and the dimensions above. For an assumed 0.4 mm nozzle, a 0.20 mm layer height and about four walls are a reasonable first coupon setup. Use your already-working PLA and TPU 95A profiles; no unverified temperature or speed is prescribed here. A solid TPU foot makes this small retention trial repeatable; confirm gap fill produces continuous 1.8 mm walls. Keep settings consistent for future comparisons.
2. Inspect sliced catch layers for continuous attachment, and the window roof for a clean 2 mm final bridge. Check the sole is solid and the end stop remains present. Print supports are not intended. Report predicted grams/time before scaling up; do not print a full support yet.
3. Print one PLA coupon and one TPU foot. Check for elephant-foot bulges, strings in the window, and cracks/delamination at the catch. Remove strings, but do not sand away the catch or window to force a fit: that would hide the tolerance result.
4. Align the corner with the end stop, the window with the raised catch, and the sole under the rail. Flex the window wall outward with a finger and seat the rail against the sole. The catch should appear in the window and the wall should return toward its relaxed position. Do not force the PLA if the shoe will not seat by hand.
5. Hold the PLA coupon and gently tug the TPU toward the floor and in both directions along the rail. It should remain captured without deliberate peeling. Inspect seating and end play; the designed clearance means some small free movement is expected.
6. Peel the window wall outward until it clears the catch, then remove the foot. Repeat 10 installation/removal cycles. Inspect window edges for tearing, permanent stretch and the PLA catch for whitening or cracking. Note whether retention weakens.
7. Apply hand compression through the coupon on the intended floor, then do 20 short back-and-forth strokes. Check for migration, rolling of the shoe, exposed PLA touching the floor and visible marks. This is a screening test, not a substitute for full-assembly testing.

Return: whether it seated by hand; tightness/looseness; whether it stayed captured during gentle tugging and dragging; whether intentional peeling worked; any damage after cycling; slicer grams/time; and your TPU brand/profile. If possible, include a close photo of the seated window. The first adjustment should change one fit variable at a time—for example clearance—with the PLA corner and print settings held constant. Do not print multiple tolerance variants up front.

Manufacturer background: TPU print preparation and adhesion vary with the material and surface; consult the filament maker's instructions. The [Prusament TPU 95A material guide](https://help.prusa3d.com/article/prusament-tpu-95a-material-guide_899653) is a useful example, not evidence that your particular TPU will have the same snap response.
