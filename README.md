# Flat-pack footrest — design and experiment history

Local engineering repository reconstructed on 2026-09-20 from supplied files, workspace artifacts and the user messages in this conversation. Each available design stage has its own chronological commit and tag. Commits use their actual creation time; they are not the original design timestamps.

Read [STATUS.md](STATUS.md) before using any print files, then [CHANGELOG.md](CHANGELOG.md). Each directory under `versions/` contains preserved artifacts and a `REVIEW.md` explaining the change, reason, evidence, outcome and next question. [CONTRIBUTING.md](CONTRIBUTING.md) sets the process for future iterations.

## Evidence and provenance

- `provenance/files.json` maps copied files to workspace paths and SHA-256 hashes. Paths are relative to the original project workspace, not this repository.
- Original files are copied without rewriting their contents. Some README files were annotated later in the project; they are preserved as found, not represented as exact release-day snapshots. Their print instructions can be obsolete.
- `archives/` retains original ZIP exports, which may contain earlier documentation than the unpacked artifacts. Historical print instructions are not current recommendations.
- Test observations in REVIEW files are retrospective summaries of user messages, not instrumented measurements. They distinguish local fit from assembled performance. Source reports preserve the recorded CAD evidence; this repository import does not rerun CAD, FEA or printer tests.
- V4 and earlier failed disconnected-brace versions have historical mentions but no standalone supplied geometry. No missing geometry or measured result has been invented.
- No GitHub remote, publication, license grant or external upload is implied. Existing local Git identity is used for the reconstruction, not claimed as authorship of all inherited geometry.

## Browse

`git log --oneline --reverse` shows the sequence. `git show <tag>` shows a stage's import and review. `git diff <old-tag> <new-tag> -- CHANGELOG.md` shows the recorded transition. Geometry snapshots have different paths: use `git diff --no-index <old-source.scad> <new-source.scad>` for a direct source comparison (exit 1 means differences).

Archived scripts vary in portability. Scripts named `validation_workspace.py` rely on original workspace paths. Do not assume relocating them makes them runnable. Preserved reference meshes and raw validation outputs are evidence, not additional parts to print.

Import audit: `provenance/output_coverage.json` accounts for every original output file by hash, including duplicate download folders. Original handoff files were also hash-verified. Large tool runtimes/caches and unrelated workspace scratch are intentionally excluded.
