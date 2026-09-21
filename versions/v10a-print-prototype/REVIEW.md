# V10A prototype STL release

Parent: V10 side-entry concept. User explicitly requested STLs after discussion of unresolved fit/top restraint. Created 2026-09-20.

Change: export distinct left/right supports and brace in print orientations. Extend rear socket block bases to the original flat support faces to eliminate elevated block starts. Mating geometry and existing top unchanged.

Checks run: source rendered with OpenSCAD; single watertight consistently wound components; print-bed bounds; assembly, support insertion and top installation paths; fixed-top obstruction probes; print/world inverse-transform regression with measured sub-micron STL rounding. Full results in geometry_checks.json.

Physical evidence: none for this new design. Prior V9C clearance success is not a new socket fit pass. Top-lift and racking remain unresolved. No claim of structural acceptance. TPU handedness is pending.

Release: full STLs supplied on user's request as a prototype; recommend one support plus brace first to limit wasted material. Next test is local seating/removal, then assembled racking and top lift. See START_HERE.md.

## Physical update — 2026-09-21

User reports: “v10 seems to have solved racking for the most part” and “it feels way more stable.” Recorded against the supplied V10A print release, called V10 by the user; exact file hashes of printed parts were not reconfirmed.

This is qualitative assembled stability improvement relative to V9/V2. It supports continuing with the side-entry mechanism rather than another redesign. It is consistent with improved vertical restraint at brace joints, but does not isolate the effects of changed fit, socket geometry or support stiffness.

Not reported: applied force, residual displacement, whether the top lifts, measured loading, sustained load duration, assembly/removal cycling, TPU installation or damage inspection. Do not infer these passed. Next check: comfortable intentional disassembly/reassembly and retention of the improved seating/stability. No geometry changed for this result.

## Physical update — 2026-09-21, fully seated top removal

User reports that after fully pushing the top in, pulling it straight out feels locked; angling it somewhat helps removal. The top has no intentional latch. Record this as difficult removal/binding, not a successful positive lock. Which connection binds, applied force and any damage are not established. Possible four-joint alignment, friction or guide contact are hypotheses, not diagnoses. Do not recommend forceful prying. Packability remains unresolved despite the improved racking feedback. No geometry changed.
