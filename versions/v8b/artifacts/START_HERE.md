# V8B: tethered-key usability trial

V8's loose-key trial is superseded. This is one small joint coupon, not a full footrest release. The current working assumption is a short cord tether; no TPU tether attachment has been validated or released.

## What changed

A 4 mm eyelet was added outside the receiver socket wall. A 3 mm eyelet was added through the keeper handle tip, away from its central shaft. A cord tied between these eyes keeps the key attached after removal, including when the parts are turned upside down. The tether carries only the loose key, not structural brace loads. It is replaceable by untying/cutting the cord. It does not prevent the unlocked key from dangling and does not make the lock vibration-proof.

The sliding tongue, 0.3 mm clearance per face, quarter-turn crossbar and lift-to-turn locating posts are unchanged. No support rail, top connection or TPU foot interface has been cut or revised.

## Print one joint

Print one each: V8B_trial_receiver.stl, V8B_trial_tongue.stl, V8B_trial_keeper.stl. All PLA, same plate, normal by-layer printing. Keep supplied orientations. Starting profile: 0.4 mm nozzle, 0.2 mm layers, 6 walls, 5 top/bottom layers, your previous PLA settings. No supports intended; inspect the 12.6 mm receiver cavity bridge, 12.2 mm tongue opening bridge, and smaller keeper/eyelet openings in the slicer. Geometric printability has been reviewed, but no slicer/toolpath or physical print validation was performed here.

Total solid-volume estimate: 13.7 g PLA at 1.24 g/cm³; use the slicer for actual consumption. Do not print full-size replacements yet.

## Fit and tether test

1. Check that the tongue slides freely in and out of the receiver with the keeper absent. Stop if it wedges; do not hammer it.
2. Insert the keeper across the elongated hole, leaving the handle about 1.8 mm above its seated position. Turn 90 degrees and lower between the posts. A gentle withdrawal tug should be blocked.
3. Lift about 2 mm, turn back, and remove the keeper; then slide the tongue out. Repeat a few times before fitting a tether.
4. Use flexible cord around 0.8–1 mm diameter. Tie one end through each eyelet, leaving approximately 60 mm of free cord between attachments plus sufficient knot tails. This length is a starting trial value, not a tested optimum. Tie around the eyelet material rather than relying on a small stopper knot being larger than the hole. Tug-check each attachment. Keep knots outside the locking surfaces.
5. Repeat ten lock/release cycles with the cord attached. The keeper must lift and turn without pulling the tether taut, and the cord must not enter the tongue socket or locating posts. The released keeper should stay attached when the coupon is inverted and gently shaken. Check the knots and eyelets afterwards.
6. Report finger effort, whether two hands feel awkward, any cord snagging, and whether locked/unlocked is easy to identify. Stop for whitening, cracking, wedging, or a loosening tether. These are usability trials, not body-weight tests.

When locked, the handle runs along the tongue's sliding direction and sits down between the posts. When released, it turns across that direction. This orientation is the current visual/tactile cue; printed LOCK labels and a stow position are not yet implemented.

## Validation completed

All three meshes are watertight, consistently wound, one connected component each, with positive volume. Largest part dimension is 32.3 mm. Sampled joint insertion, lift, rotation and extraction have no significant Boolean overlap (numerical residue under 1e-12 mm³). Deliberate wrong-direction tests confirm geometric blocking of tongue withdrawal, excessive locked lifting and seated rotation. See geometry_checks.json.

Four provisional receiver origins are [25.55 or 221.55, 168, 33 or 193] mm in assembled coordinates. At all four, the sampled keeper release paths clear the existing top and unchanged support cores/rail stiffeners. Retired V7 rear sockets are omitted from that context. See layout_checks.json and V8B_access_study.png. The illustration omits the new brace and attachment webs; the receivers are not integrated structural parts.

This is NOT a completed four-joint assembly validation: new connecting webs and brace, tether motion, human finger access, and strength are still outstanding. Moving receivers rearward creates a larger offset from the rail, so the attachment must resist the corresponding bending moment. Their supports must be designed before full-size export. The upper connector path clearing the top does not alone prove comfortable hand access.

The tether does not improve tongue/keeper strength. The 2.9 mm tongue ligaments beside the opening remain a structural trial detail. Neither V8 nor V8B establishes the provisional 200 N footrest capacity. Once usability is acceptable, the full assembly needs reinforcement, geometry checks, print review and physical loading checks.
