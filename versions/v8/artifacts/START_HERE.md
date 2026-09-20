> SUPERSEDED: loose-key print canceled. See ../V8B/START_HERE.md for tethered-key trial status.

# V8 rear joint: print one small trial set

The V7 rear joint is retired after the printed brace key broke during removal and remained stuck in the support. Both prints are discarded. This release tests a new mechanism; it does not contain replacement full-size supports or a brace.

Print one each of V8_trial_receiver.stl, V8_trial_tongue.stl, and V8_trial_keeper.stl. All three are PLA and can share one plate with normal by-layer printing. No material changes or purge tower are needed. Keep the supplied orientations so the trial represents the intended structural parts. Use the same PLA/profile used previously, a 0.4 mm nozzle, 0.2 mm layers, 6 walls, and 5 top/bottom layers. Supports are not intended; inspect the small bridges in the slicer and after printing. Total solid-volume PLA estimate is 13.5 g at 1.24 g/cm³; use the slicer for actual consumption including brim/purge.

## Why this mechanism

The rectangular tongue has 0.3 mm clearance on each mating face (0.6 mm total). Its broad faces transfer brace loads through bearing contact. A separate quarter-turn keeper prevents withdrawal. This avoids requiring a structural tongue to be both an extremely tight fit and a hand-removable fastening.

The receiver is open-ended for inspection. The keeper's head seats between four posts, which obstruct rotation until the head is lifted. Its lower crossbar catches beneath the receiver when locked. This is a gravity-seated keeper, not a spring-latched or vibration-secured fastener: inverted transport retention is not established. For flat packing, remove and store the keeper separately.

## Trial sequence

1. Inspect bridges and remove only loose strings or brim. Record any sanding needed; extensive fitting would defeat this clearance test.
2. With the keeper removed, slide the blue tongue into the grey receiver until its broad pad meets the end. It must slide in AND out using fingers. If it wedges, stop; do not hammer or force it.
3. Align the keeper's long head and lower crossbar across the receiver's width, matching the elongated through-hole. Insert from above until the head remains about 1.8 mm above its seated height. The lower crossbar must have passed below the receiver.
4. Turn 90 degrees so the head runs along the tongue's sliding direction, then lower it between the indexing posts. A gentle withdrawal tug should be stopped by the keeper. Some clearance/play is intentional.
5. Lift the head about 1.8 mm (roughly 2 mm), turn 90 degrees back, and pull the keeper up and out. Then slide the tongue out. If the head will not rotate, inspect whether it clears the posts; do not twist forcefully.
6. Repeat 10 cycles. Report sliding effort without keeper, ease of lifting/turning/removing the keeper, play when locked, and any whitening, cracks, or wear. No body-weight test on this coupon.

See V8_release_sequence.png. Colors identify components only; one PLA spool is sufficient.

## Completed validation and limits

All three exported STL meshes have one connected component, consistent winding, positive volume, and are watertight. Largest dimension is 28 mm. Boolean overlap checks found zero collision at the assembled position and along sampled straight insertion (0.25 mm), lifting (0.05 mm), turning (0.5 degree), and keeper extraction (0.1 mm) paths. Deliberate out-of-path checks confirm tongue withdrawal by 1 mm hits the locked keeper, lifting the locked keeper by 3 mm catches the underside, and turning the seated handle by 15 degrees hits the indexing posts. These positive collision checks establish nominal geometric blocking, not strength.

The supplied receiver orientation includes a 12.6 mm tongue-cavity bridge and a 6.6 mm keeper-hole bridge. The tongue has a 12.2 mm keeper-hole bridge. These surfaces can reduce real printed clearance: inspection and the physical trial remain necessary.

The 18 mm tongue retains 2.9 mm of material on each side of its 12.2 mm-wide keeper opening. This is an intentionally small mechanism trial; neither those ligaments nor the receiver's attachment to a full support have passed a structural load test. Geometry checks do not establish fatigue life, impact strength, or the project's provisional 200 N vertical capacity.

If the trial passes, integrate the receiver into new full-size supports and the tongue into a rear brace, then validate the complete assembly, reinforcement, print orientation, release access, bed fit, and load path. The previously tested top connection and V6A TPU interface remain unchanged. Do not print another V7 rear connection.
