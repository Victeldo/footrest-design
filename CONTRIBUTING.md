# Future design iterations

Keep source, delivered meshes, checks and physical results traceable. A passing mesh is not a working mechanism.

1. Start from an observed problem in STATUS.md. Record observation separately from proposed cause.
2. State the hypothesis, changed variables, preserved parts and acceptance criteria before making geometry. Prefer the smallest useful experiment.
3. Add a new version directory; do not silently replace a previously printed version. Identify exactly which files and settings are to be printed.
4. Save source, exported meshes, validation scripts/results and relevant images. Record component count, intended contact, interference, assembly/removal paths and printer envelope as appropriate. Call out tests not run and script dependencies.
5. Record physical results separately: coupon or complete assembly, which actual parts, settings if known, observed movement/damage, number of cycles if reported. Never infer that an entire proposed checklist was performed from vague feedback.
6. Update CHANGELOG.md, STATUS.md and that version's REVIEW.md. Include failed experiments and abandoned concepts. Commit the design version with its rationale; add later observations in a clearly named results commit rather than rewriting old commits. Tags identify released design snapshots.
7. Do not reprint large unchanged parts or introduce extra mechanisms without a specific reason. A clearance change must not be described as positive anti-lift retention.

## Review template

- Parent version and observed problem:
- Hypothesis (not established fact):
- Change and reason:
- Preserved interfaces/parts:
- CAD checks actually run and artifact links:
- Physical test proposed and acceptance criteria:
- Physical test actually reported:
- Outcome and limitations:
- Print status and next decision:

No current full footrest load rating exists. The 200 N target is a design/check objective, not a measured safe capacity. The rear joint must constrain racking, not merely stay attached.

Maintain `current/` as the complete selected prototype print set. Update its README and provenance manifest when changing a selected part; include retained parts from older versions so users do not need to hunt through history. Never substitute an older incompatible joint system.
