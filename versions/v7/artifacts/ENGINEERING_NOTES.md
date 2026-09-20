# V7 structural reasoning and limits

## Load assumptions

Measured seated load reported by the user: 25.6 lbf ≈ 113.9 N. Agreed vertical check load: 200 N total, about 1.76 times that measurement. This ratio is an allowance on the observed load, not a computed strength safety factor. A separate 20 N horizontal load is an illustrative racking screen chosen for this design pass; it is not a measured user force or a certified requirement.

This remains a seated footrest. No load rating is assigned. PLA brand, print properties, creep and environmental temperature have not been measured for this build.

## Top load path and approximate calculation

The 2.4 mm skin spreads local heel pressure into the grid. Three 5 mm-wide left-right ribs have 16 mm total section depth including the skin. Five 3.6 mm-wide transverse ribs and a 3 mm-wide perimeter reach 10 mm total depth. Bosses are joined directly to the skin and ribs. The 7 mm-deep sockets lie entirely within those bosses; they do not cut through a lightening pocket. Nominal socket side walls are 3.45 mm thick and end walls are 4.95 mm thick.

A small linear beam-grillage model represents skin strips and ribs. At each node it has vertical translation and two rotations. Each member includes Euler–Bernoulli bending and approximate rectangular-section torsion; Poisson ratio is assumed 0.35. Vertical support points are placed at x=22/218 and y=49/85/121, where the actual shoulders/main rib contacts support the deck. Rotations at those points remain free. The solution balances the 200 N load with 200 N of reaction. A separate simply-supported beam check matches the classical center-load deflection to numerical precision.

Calculated deflections for assumed effective E=1500–2500 MPa:

- 200 N over a 40 × 40 mm central patch: approximately **1.11–1.85 mm**.
- Two 100 N, 40 × 40 mm heel patches centered at x=60 and 180 mm, y=85 mm: approximately **0.61–1.02 mm** maximum.
- 200 N at an ideal mathematical center point: approximately **1.29–2.14 mm**; the highest model nominal beam stress is about **13.5 MPa**.
- One offset 200 N patch centered at x=60, y=55 mm: approximately **1.26–2.11 mm**. This case gives very uneven support reactions and needs physical stability testing.

These are screening results, not verified full-assembly predictions. The model has ideal connections and solid sections; it omits local plate deformation between ribs, shear-lag, stress concentrations at pockets/joints, orthotropic print behavior, creep, support deflection and foot compression. Its strip/torsion idealization is approximate and has not been correlated with a printed top. The modulus interval is a sensitivity assumption, not a guaranteed material bound. No allowable stress or material-based safety factor has been established. The numbers justify proceeding to a prototype, not claiming proof of capacity.

For context only, [Bambu's filament guide](https://cdn1.bambulab.com/filament/filament-guide/250123/filament-guide-en.pdf) lists 2750 MPa for PLA XY bending modulus. That is not substituted as the actual modulus of the user's print. Beam equations follow conventional elastic beam theory; see the [US Air Force stress-analysis manual, hosted by Engineering Library](https://engineeringlibrary.org/reference/simple-beam-bending-air-force-stress-manual).

## Why add a rear brace?

The original X lies in each side frame's plane. It is useful against fore-aft racking, but it does not triangulate the space between the two side frames. Tightening the top fit does not remove the tall frames' weak-axis flexibility.

An idealized out-of-plane beam model of a bare V5-style frame, with its bottom corners fully fixed, predicts large lateral compliance at only 10 N per side panel. The resulting displacement is too large for the model's small-deflection assumptions to remain reliable; it is a warning about the load path, not a literal displacement prediction. This model is explicitly for the original unflanged, unbraced frame, not final V7.

V7 adds a rear X in the across-width plane. Its 8 × 6 mm diagonals are about 253 mm between attachment centers and convert much of a sideways push into axial tension/compression. Under an ideal 20 N horizontal load split between both diagonals, each has approximately 12.9 N axial force (0.27 MPa nominal axial stress). An ideal full-length pinned compression-member Euler screen gives roughly 33–56 N for the assumed E range, without crediting the fused crossing as a midspan brace. Imperfections and printing can reduce that value. It is not a buckling proof for the full assembly.

Ideal axial stretch of those two brace members would contribute only about 0.04–0.06 mm displacement. **This is not the assembly's predicted sway.** Socket clearance, end-block deformation, short unbraced frame extensions, foot compliance, possible joint withdrawal and torsion can dominate. Physical lateral testing is still necessary. The brace is retained by press fit; no positive anti-withdrawal latch has been claimed.

Raised 6 × 3 mm flanges along the support rails increase the local solid section's weak-axis second moment from about 286 to 657 mm⁴, roughly 2.3 times. This comparison excludes taper/end effects and does not establish the panel's global buckling capacity. The original 10 × 7 mm rail remains underneath the addition.

## Stability and unverified behavior

The nominal flat-foot contact envelope is x=16.45–223.55 mm and y=8.2–161.8 mm. This defines an outer support polygon, not a guarantee that the resultant load always stays inside it. Heel position, horizontal push, floor friction and TPU deformation affect sliding/tipping. An empty lightweight footrest is particularly easy to move or tip. No friction coefficient or tipping load is asserted.

The 241 mm height is unloaded nominal geometry. TPU compression, print variation and joint seating affect measured height. Bed fit is based on object envelopes; brims and printer exclusions still require slicer inspection.

Full-assembly strength, global buckling, fatigue, long-term creep, accidental impacts and handling retention are unresolved until physical testing. The conservative next step is the two small joint pairs, followed by slicer review and one representative support—not printing all duplicates at once.
