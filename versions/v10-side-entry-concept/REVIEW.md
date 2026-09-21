# V10 side-entry concept — discussion model, not a print release

Parent: V9 bracket V2 and its assembled racking/lift-off failure. New concept created 2026-09-20. No physical tests have been run on V10.

## Agreed design boundary

Preserve the top where practical. Preserve the support frame and TPU interfaces where practical, but allow rear interfaces on both supports and brace to change. Reuse of existing support prints is a preference, not an acceptance criterion. User rejected purchased fasteners and chose investigation of inward-facing horizontal sockets. A stop added to the old drop-in system is not the selected path.

## Observation and hypothesis

V9/V2 upper channels slid upward off their rails during left/right racking. Smaller clearance improved stability but did not prevent the failure. Timing of initial channel lift versus initial racking remains unmeasured.

Hypothesis: restricting vertical movement at the brace attachment points removes a motion that defeats the rear X. Sideways sockets provide roofs and floors without a separate latch. The installed top must then restrain sideways support separation. This is conditional capture, not a positive lock against every combined motion.

## Concept geometry

Four rectangular brace tongues enter inward-facing blind sockets. Nominal tongue section 8 mm fore-aft by 16 mm vertical; 12 mm engaged length, with 2 mm clearance to each blind end. Socket section 8.3 x 16.3 mm. These 0.15 mm clearances are a starting concept value, NOT transferred validation from the differently oriented V9C coupon.

Socket block envelope is 20 x 23 x 24 mm. The roof/floor thickness is 3.85 mm; no strength claim follows from that dimension. Blocks overlap the original rear rail rather than replacing it. Gusseting, fillets, print orientation and material consumption are not finalized. The inward projection moves the X attachment centers closer together (144 mm across by 160 mm vertically); member forces must be re-evaluated rather than inheriting the V9 structural assumptions. X members remain nominally 8 x 6 mm.

Left and right support concepts are mirrored in assembled coordinates. This changes the handedness arrangement from the original identical-support V9 build. A print-orientation and TPU handedness review is still required; do not infer that existing shoes or two identical prints are already reconciled. The top uses the existing V7 geometry through the preserved source module.

## Assembly and force transfer

With the top off, bring supports inward around the brace. Each tongue slides sideways into its socket until its shoulder meets the mouth. Fit the top over the support tabs last. To disassemble, remove top and move supports outward.

Upward/downward tongue motion meets socket roof/floor after nominal clearance is taken up. Sideways withdrawal requires support separation. With the top held seated and rigid, its existing tab/socket walls oppose that separation. This is the reason to investigate the mechanism, not proof of assembled stiffness.

The top is not latched down. The CAD checks hold it seated/fixed when probing support separation and splay. They do not show whether racking can lift the top, rotate or flex supports, crack a roof, or gradually withdraw a lower tongue. That coupled motion is the remaining critical issue. A part with a closed socket can still have excessive angular or elastic compliance.

## Checks actually run

- Four rendered components: one connected, watertight, consistently wound mesh each.
- Assembled nominal overlaps: numerical zero.
- Both supports moving outward/inward 0–16 mm in 0.25 mm steps with brace fixed and top absent: no interference.
- Top installation over 0–40 mm in 0.5 mm steps: no interference.
- Deliberate brace displacement up/down by 0.5 mm: blocking contact at the sockets.
- Deliberate support outward movement of 0.2 mm with top fixed: blocking contact.
- Left-support rotation probes about its top at 0.1, 0.25, 0.5, 1 and 2 degrees also meet the fixed top. These are rigid geometric obstruction probes, not allowable-angle/stiffness predictions.

See concept_checks.json. No FEA, physical test, slicer review, deformable-contact simulation or print-size/orientation qualification is claimed. A clean nominal insertion path does not establish comfortable simultaneous insertion in a printed four-joint assembly.

## Deliverables and next decision

V10_assembly_sequence.png shows the actual mesh assembly stages and a nominal y=165 mm joint section. V10_CONCEPT_ONLY.glb is a reference model, not a printable file. V10_concept.scad defaults to the assembly and exports component geometry in assembled coordinates. No printable STLs have been released.

Before a coupon: examine combined top lift/support splay and finalize the mirrored support/foot arrangement and print orientation. The concept must constrain racking with the real top seated, allow intentional disassembly, and remain simple enough for repeated packing. If that cannot be achieved cleanly, reconsider the capture principle rather than rely on friction.

Rebuild nominal checks with `python build_and_check.py --openscad /path/to/OpenSCAD` after installing requirements.txt. It uses temporary mesh exports, writes the check report, and does not release print files.
