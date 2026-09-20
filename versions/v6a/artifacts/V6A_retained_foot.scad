// V6A experimental retained TPU foot. Units: mm.
// Default is ONE PLA coupon. Read V6A_README.md before printing.
// Full support preserves V5 height: with 2 mm sole assembled height is 243 mm.
// Full support is reference-only pending foot test and top/height reconciliation.
part = "coupon"; // coupon, foot, coupon_assembly, support_reference, support_assembly
$fn=48;

// Unchanged V5 geometry from original source.
W=150; H=234; T=7; frame=10; brace=8;
tab_w=22; tab_h=7; tab_t=7; tab_centers=[39,111];
module beam2d(x1,y1,x2,y2,w) {
 hull() { translate([x1,y1]) circle(d=w); translate([x2,y2]) circle(d=w); }
}
module frame2d() {
 union() {
  square([W,frame]); translate([0,H-frame]) square([W,frame]);
  translate([0,frame]) square([frame,H-2*frame]);
  translate([W-frame,frame]) square([frame,H-2*frame]);
  beam2d(frame-5,frame-5,W-frame+5,H-frame+5,brace);
  beam2d(W-frame+5,frame-5,frame-5,H-frame+5,brace);
  for(p=[[frame,frame],[W-frame,frame],[frame,H-frame],[W-frame,H-frame]])
   translate(p) circle(d=14);
 }
}
module base_support() {
 union() {
  linear_extrude(T) frame2d();
  for(c=tab_centers) translate([c-tab_w/2,H,0]) cube([tab_w,tab_h,tab_t]);
 }
}
// x along rail, y upward, z through rail thickness. Underside of rail: y=0.
sole=2;
wall=1.8;
clearance=0.25; // per face, UNCALIBRATED TPU trial; independent of PLA socket fit
catch_projection=2.2;
foot_length=28;
module cuboid(a,b) {translate(a) cube(b-a);}
module xy_prism(points,z0,z1) {translate([0,0,z0]) linear_extrude(z1-z0) polygon(points);}
module yz_prism(points,x0,x1) {
 multmatrix([[0,0,1,x0],[1,0,0,0],[0,1,0,0],[0,0,0,1]])
 linear_extrude(x1-x0) polygon(points);
}
module catch_left() {
 // 0.2 mm root overlap guarantees a volumetric connection.
 // 45 degree insertion ramp; roof follows TPU window for distributed retention.
 intersection() {
  yz_prism([[3,6.8],[11.25,6.8],[11.25,7+catch_projection],
            [3+catch_projection,7+catch_projection],[3,7]],9,19);
  xy_prism([[9,3],[19,3],[19,7.25],[15,11.25],[13,11.25],[9,7.25]],6.7,10);
 }
}
module support_new() {
 union() {
  base_support(); catch_left();
  translate([W,0,0]) mirror([1,0,0]) catch_left();
 }
}
module coupon() {intersection() {support_new();cuboid([0,0,0],[32,22,12]);}}
module foot_local() {
 difference() {
  union() {
   cuboid([-wall,-sole,-clearance-wall],[foot_length,0,7+clearance+wall]);
   cuboid([-wall,-.1,-clearance-wall],[foot_length,9,-clearance]);
   cuboid([-wall,-.1,7+clearance],[foot_length,14,7+clearance+wall]);
   cuboid([-wall,-.1,-clearance-wall],[-clearance,9,7+clearance+wall]);
  }
  // 45 degree roof narrows final bridge to 2 mm for sole-down printing.
  xy_prism([[9-clearance,3-clearance],[19+clearance,3-clearance],
            [19+clearance,7.25],[15,11.25+clearance],
            [13,11.25+clearance],[9-clearance,7.25]],7,12);
 }
}
module foot_print() {
 translate([wall,7+clearance+wall,sole]) rotate([90,0,0]) foot_local();
}
if(part=="coupon") coupon();
else if(part=="foot") foot_print();
else if(part=="coupon_assembly") {
 color("lightgray") coupon(); color("peru") foot_local();
} else if(part=="support_reference") support_new();
else if(part=="support_assembly") {
 color("lightgray") support_new();
 color("peru") {foot_local();translate([W,0,0]) mirror([1,0,0]) foot_local();}
} else assert(false,"Unknown part selector");
