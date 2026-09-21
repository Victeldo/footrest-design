# Changelog — retrospective, chronological

Design sequence is reconstructed from artifacts and conversation. Outcomes include later observations; no claim that they were known at original release. Dates of individual prints were not consistently recorded.

## v3-inherited — Inherited V3 top and assembly concept

**Change / why:** Imported the older top/assembly reference supplied with the handoff. Approximate 230 x 170 mm top; not reconciled to the latest support.

**CAD:** Later V6A inspection reported five disconnected top bodies (platform plus four socket bosses), despite watertightness. That finding belongs to the later inspection, not an original V3 test.

**Physical:** No full V3 top test result is available in this conversation.

**Outcome:** Reference only. Required connected socket bosses, support reconciliation and height review. Handoff also mentions unavailable V4 and earlier disconnected-brace failures.

[Artifacts and review](versions/v3-inherited/REVIEW.md)

## v5-inherited — Inherited V5 lightweight support and friction shoe

**Change / why:** Inherited 10 mm perimeter rails, 8 mm X members, 7 mm thickness and local junction pads. Handoff describes reduction from unavailable V4 (12 mm rails/10 mm braces). Existing TPU shoe relied on friction only.

**CAD:** Handoff reports a connected support and roughly 80.17 cm³ volume. Later V6A checks preserved the full bottom rail. No structural rating was established.

**Physical:** No standalone V5 structural load result is available. User requested proper replaceable TPU retention.

**Outcome:** Use as structural starting point; replace friction-only foot interface without cutting the rail.

[Artifacts and review](versions/v5-inherited/REVIEW.md)

## v6-calibration-inherited — Inherited V6 top-joint tolerance calibration

**Change / why:** Preserved historical calibration artifact. This is a tolerance coupon, not a V6 full assembly. Selected 7 x 22 mm tab into 7.10 x 22.10 mm socket with 7 mm engagement.

**CAD:** Later parser inspection reported non-watertight geometry and 24 components; this does not negate the historical physical fit observation.

**Physical:** Handoff: +0.30 mm total still wobbly; +0.10 and +0.20 had similar low true play; +0.10 slightly harder to dislodge and selected. +0.50 previously too loose.

**Outcome:** Preserve calibrated top interface. Do not assume it transfers to differently oriented rear joints or TPU interfaces.

[Artifacts and review](versions/v6-calibration-inherited/REVIEW.md)

## v6a — V6A mechanically retained TPU foot

**Change / why:** Added external PLA corner catches and mating TPU window shoes, keeping the bottom rail intact. Replaced friction-only retention with an intentional peel-to-release interface.

**CAD:** Recorded component/watertightness checks, material-preservation booleans, nominal contacts, rigid blocking checks and independent SCAD export comparison. Found inherited disconnected top bosses and 243 mm provisional height with sole.

**Physical:** User printed shoe and PLA key/coupon, reported it fit and passed the tests. Small internal gap opposite the key slot was reported. Exact forces and per-test cycle counts were not supplied.

**Outcome:** Local TPU interface accepted for reuse; not full-structure validation. Next reconcile top/height and across-width bracing.

[Artifacts and review](versions/v6a/REVIEW.md)

## v7 — V7 ribbed 240 mm top and rear X brace

**Change / why:** Chose 240 x 170 mm one-piece top for A1 bed rather than wider split platform. Added connected rib/boss top, shortened support for nominal 241 mm height, rail stiffeners and rear X brace. Rear joint repeated a tight 7 x 22 x 7 interface. User measured heel spread about 12 inches and seated load about 25.6 lb; 200 N remained an unproven check target.

**CAD:** Recorded topology, exact tab/socket and rail checks, assembly/insertion booleans, orientation review, rebuild checks and idealized structural screens. These screens were not measured full-frame stiffness or strength.

**Physical:** Top and rear coupons fit with effort. Full rear brace/support slid in then tightened/snapped; could not be removed by hand. Pulling later broke the rear key/tab inside support; user discarded both. Photo/orientation review did not identify reversed assembly as the cause. Reported slicer masses: rear 26 g, supports 54 g each, top 161.41 g.

**Outcome:** Rear connection failed packability/removal. Top and TPU interfaces subsequently retained. Do not reuse tight rear fit; geometry validity did not establish removability.

[Artifacts and review](versions/v7/REVIEW.md)

## v8 — V8 sliding tongue and loose quarter-turn keeper

**Change / why:** Separated structural sliding tongue (0.30 mm per face) from quarter-turn withdrawal keeper. Added lift-to-turn locating posts and exposed grip to avoid forceful disassembly.

**CAD:** Recorded connected watertight meshes, sampled insertion/lift/rotation/extraction paths and deliberate blocking collisions. No load validation.

**Physical:** No successful printed V8 trial reported. User flagged four loose keys as a loss/usability issue; print was canceled as the design changed.

**Outcome:** Abandoned before physical validation. Added operations/loose parts were unacceptable for packing.

[Artifacts and review](versions/v8/REVIEW.md)

## v8b — V8B tether-eyelet keeper trial

**Change / why:** Added receiver/keeper eyelets for cord retention. Initially considered TPU tether, but actual deliverable assumed cord; no TPU tether attachment was validated. Provisional rearward locations studied for key access.

**CAD:** Recorded joint mesh/path checks and four provisional key-clearance paths against top/support core. Attachment webs, full brace integration, tether motion and human access were not complete.

**Physical:** No physical V8B pass reported. User questioned increasing complexity; assistant agreed keys/posts/tethers were overcomplicating the problem.

**Outcome:** Abandoned. Return to whole-assembly sequence and simpler connections rather than iterating an elaborate lock.

[Artifacts and review](versions/v8b/REVIEW.md)

## v9-trial — V9 drop-in T/C coupon and full-layout concept

**Change / why:** Adopted four short T rails with C channels, fixed lower seating ledges and 20 mm vertical engagement. No latch. Beveled 45-degree shoulders for flat-print geometry; 0.30 mm per axis face. Narrowed ledge after detecting diagonal interference.

**CAD:** Recorded connected coupon/support/brace meshes, full approach/vertical paths and top install checks. Existing top explicitly did not block lift-off. Strength, uplift and four-point physical fit remained unknown.

**Physical:** Coupon slid easily and remained wrapped during X/Y motion, with some rocking. User highlighted looseness. This was a local fit test only.

**Outcome:** Advanced to full prototype without proof of racking restraint. Later failures showed that easy fit and wraparound engagement were insufficient.

[Artifacts and review](versions/v9-trial/REVIEW.md)

## v9-full — V9 full assembly with backed rail roots

**Change / why:** Kept coupon contact geometry; added backing at each T root, with roughly 183 mm³ net added per support. Released full support/brace and unchanged top/TPU parts.

**CAD:** Recorded full topology/bed checks, four-joint assembly/removal and top installation, TPU nominal intersections, plus top/brace regressions. Root review was qualitative, not strength qualification.

**Physical:** One support plus brace slid smoothly but swayed; user flagged this before printing second. Assistant expected the second support to constrain it. Complete assembly without TPU feet racked with all floor corners touching. Upper C channels slid upward off T rails; they did not spread/pop backward. User described the frame becoming a parallelogram.

**Outcome:** FAILED assembled racking/retention. Earlier confidence in the second support was unsupported. Floor grip was not the identified cause. Keep top/supports for experiments, not as a rated structure.

[Artifacts and review](versions/v9-full/REVIEW.md)

## v9c-fit — V9C brace-side clearance coupons

**Change / why:** Reduced only channel clearance to 0.20 and optional 0.15 mm per face, maintaining engagement, exterior, supports and top. No anti-lift stop added. Goal: distinguish excess clearance from the unrestricted release direction.

**CAD:** Recorded original-0.30 reproduction, single-solid tighter exports, added-material-only check, and nominal approach/vertical paths against support rail positions. No revised full-frame test at this stage.

**Physical:** User reported 0p15 felt pretty good and authorized full bracket V2. Separate 0p20 result and explicit all-four-rail/cycle confirmation were not supplied.

**Outcome:** Local 0p15 fit selected. This did not prove racking or lift-off solved.

[Artifacts and review](versions/v9c-fit/REVIEW.md)

## v9-bracket-v2 — V9 bracket V2 with four 0p15 channels

**Change / why:** Applied tested 0.15 mm fit to all four brace channels; X, spacing, top and supports unchanged. No anti-lift feature. About 0.53 g solid PLA added over prior brace.

**CAD:** Recorded one watertight component, A1 envelope, nominal assembly/removal/top-install checks. Regression against old brace plus four tighter coupons differed 0.00994 mm³ within documented 0.02 mm³ numerical tolerance.

**Physical:** User printed V2: more stable, but during left/right racking the upper channels again slid up off the T rails. User emphasized that the brace still does not prevent racking.

**Outcome:** FAILED full-frame racking/retention despite improved local fit. Further tightening is not the established fix. Open question: when does vertical channel motion begin relative to frame racking? A proposed anti-lift feature must carry load and constrain racking, not merely catch a detached brace.

[Artifacts and review](versions/v9-bracket-v2/REVIEW.md)

## v10-side-entry-concept — horizontal sockets captured by support spacing

**Change / why:** Following V2 racking/lift-off, move the brace release direction sideways. Inward-facing support sockets have closed roofs/floors; the top is intended to constrain support separation. Top geometry retained, support rear interfaces open to redesign, no purchased fasteners. No further V9 clearance adjustment.

**CAD:** New concept model, assembly sequence and joint section. Connected watertight components; sampled sideways assembly and top installation clear. Deliberate upward/downward brace motion and outward support motion with the top fixed meet geometry. Reports do not establish coupled top-lift restraint, strength or real stiffness.

**Physical:** Not printed or tested. No new print files released.

**Outcome:** Candidate for discussion. Capture depends on the top remaining seated; flexing, combined lift/splay, new fit, print orientation and mirrored support/TPU arrangement remain open. [Concept review](versions/v10-side-entry-concept/REVIEW.md).

## v10a-print-prototype — requested full STLs

**Change / why:** User requested V10 STLs. Added flat-face backing to socket blocks for printing, retained mating geometry, and exported separate left/right supports and rear brace. Existing top retained.

**CAD:** Reran rigid assembly/path checks; verified print exports, orientation regression and A1 envelopes. No sliced toolpaths or structural qualification.

**Physical:** Untested. New rectangular socket fit, combined top lift/racking and TPU handedness remain unresolved. This prototype release does not supersede V9/V2 failure evidence with a claimed pass.

[Files and instructions](versions/v10a-print-prototype/START_HERE.md).

## 2026-09-21 — V10/V10A assembled feedback

User reports racking mostly resolved and assembly feels much more stable. Qualitative full-assembly improvement; no measured force/displacement, load-capacity or durability result. Preserve geometry for further evaluation. Added physical result to V10A review; no new design version.

## 2026-09-21 — fully seated top binds during removal

V10A user feedback: fully seated top resists straight extraction; angling helps. No designed latch exists. Stability improvement remains reported, but easy disassembly is not established. Record binding/alignment/friction as possible causes, pending localization; no design change made.
