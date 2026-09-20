# V9: drop-in T-and-C joint — print these two coupons only

V8 and V8B keys/tethers are superseded. V9 uses four short rails, four integral brace channels and fixed seating ledges. No loose fasteners, flexing latch or wedge fit. The existing top does NOT trap the brace: it can lift off. This is a gravity-seated concept, not positive anti-lift retention.

## Print

Print one PRINT_FIRST_V9_rail_coupon.stl and one PRINT_FIRST_V9_channel_coupon.stl. Both PLA, same plate, normal by-layer printing; retain supplied orientations. Start with your existing PLA profile, 0.4 mm nozzle, 0.2 mm layers, 6 walls, 5 top/bottom layers. Supports are not intended. Review the slicer: the 45-degree internal shoulders replace unsupported square lips. The rail has separate initial bed-contact regions that merge as printing progresses; check bed adhesion. No slicer/toolpath verification has been performed here.

Together the coupons contain 8.48 cm³, about 10.5 g if solid PLA at 1.24 g/cm³. Actual slicer consumption depends on settings. Do not print the full support/brace context selectors yet.

## Test

1. Hold the rail upright: its long 20 mm engagement runs vertically, and the seating ledge is at the bottom.
2. Put the channel above the rail, with its narrow opening facing the rail stem. Lower it straight down until its solid back lands on the ledge. Do not push it on from the rear at the seated height.
3. Lift roughly 21 mm to clear the rail completely, then separate. It should be finger-easy in both directions. No hammering, prying or forceful snap is intended.
4. Repeat ten cycles, checking for rough sliding, binding, whitening or wear. Report whether it falls into place under its own weight or requires light hand pressure, plus side-to-side/backward play.
5. Gently pull straight backward while seated: the shoulders should prevent separation. Gently push downward: the ledge should stop travel. This is only a fit/handling test; do not load it with body weight.

Do not sand extensively to make it pass without reporting that: the goal is to assess the printed clearance. A single joint passing does not prove four simultaneous joints will align or remain seated under racking.

## Mechanics and dimensions

T head: 14 mm across, 4 mm rear portion; stem: 7 mm. Vertical engagement: 20 mm. C outer width: 21 mm. Side wall thickness beside the head: 3.2 mm; rear wall: 6 mm. Axis-aligned mating faces have 0.3 mm clearance per face; matching 45-degree shoulders have approximately 0.42 mm normal clearance. These are uncalibrated trial values. The joint is constant-section along its travel, not tapered to wedge tight.

The angled shoulders preserve wraparound retention while improving flat-print overhangs. They can also spread the C walls when loaded backward; wall/root strength requires physical assessment. Fillets and local reinforcement remain candidates before final structural release.

The T attachments add material behind the existing rail rather than cutting into it. Their offset still creates bending at the attachment root: unchanged rail material does not prove unchanged strength. The top interface and V6A foot geometry remain unchanged. Both supports use the same orientation, matching the existing design.

## Geometry validation

Both coupons, the full support concept and full X-brace concept are each single connected, watertight meshes with consistent winding and positive volume. Print envelopes fit the A1: support 164.3 x 230 x 14 mm; brace 217 x 180 x 13.6 mm. See geometry_checks.json.

Boolean checks sampled 0.25 mm steps over the 21 mm vertical engagement/release path and raised rear approach, for the coupon and all four full-assembly connections together. No interference remained. Top installation was checked at 0.5 mm increments over 30 mm; the assembled top/support/brace do not interfere. Deliberate 0.5 mm downward, 1 mm backward and 1 mm sideways motions produce contact/interference as expected, establishing the ledge and wraparound geometry. These checks are nominal rigid CAD checks, not print-tolerance, strength or fatigue proofs.

An initial upper-stop/diagonal clash was corrected by narrowing the stop to 11 mm. The rear wall has a nominal 11 x 6 mm seating patch. The stop is not a latch.

## Full assembly sequence and remaining work

With the top removed, hold the brace 21 mm above its seated location, approach the supports from behind, align the four channels and lower onto the stops. Install the top. Reverse to pack. The current geometry also permits upward brace removal with the top present; no anti-lift benefit is claimed from the top.

After coupon fit succeeds, check simultaneous four-joint alignment and seating, then assembled racking and corner lift. Vertical seated-foot loading alone does not establish rear-brace stability. The 200 N target is not a tested rating. Full-size release is withheld pending fit feedback and further root/shoulder/load review.
