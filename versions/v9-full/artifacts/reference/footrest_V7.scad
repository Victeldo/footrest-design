// V7: 240 x 170 mm one-piece ribbed platform, 241 mm nominal height.
// Seated-use prototype. 200 N is a design/check load, NOT a tested rating.
// Print joint coupons first. All printable selectors lie flat on z=0.
part="assembly"; // top, support, socket_coupon, tab_coupon, brace, brace_socket_coupon, brace_tab_coupon, foot_left, foot_right, assembly
$fn=48;
W=150; H=223; T=7; frame=10; brace=8;
tab_w=22; tab_h=7; tab_t=7; tab_centers=[39,111];
top_x=240; top_y=170; skin=2.4; deck_depth=16; rim_depth=10;
slot_t=7.10; slot_w=22.10; engagement=7;
support_x=[22,218]; support_y0=10; slot_y=[49,121];
sole=2; total_height=241;
guide_gap=7.4; guide_depth=8; boss_x=14; boss_y=32;
assert(abs(sole+H+deck_depth-total_height)<0.0001);
assert(slot_t==7.10 && slot_w==22.10 && engagement==7);
module cuboid(a,b){translate(a) cube(b-a);}
module xy_prism(points,z0,z1){translate([0,0,z0]) linear_extrude(z1-z0) polygon(points);}
module yz_prism(points,x0,x1){
 multmatrix([[0,0,1,x0],[1,0,0,0],[0,1,0,0],[0,0,0,1]])
 linear_extrude(x1-x0) polygon(points);
}
module beam2d(x1,y1,x2,y2,w){hull(){translate([x1,y1])circle(d=w);translate([x2,y2])circle(d=w);}}
module frame2d(){union(){
 square([W,frame]);translate([0,H-frame])square([W,frame]);
 translate([0,frame])square([frame,H-2*frame]);translate([W-frame,frame])square([frame,H-2*frame]);
 beam2d(frame-5,frame-5,W-frame+5,H-frame+5,brace);
 beam2d(W-frame+5,frame-5,frame-5,H-frame+5,brace);
 for(p=[[frame,frame],[W-frame,frame],[frame,H-frame],[W-frame,H-frame]])translate(p)circle(d=14);
}}
// V6A catch and foot dimensions remain unchanged after user's successful trial.
module catch_left(){intersection(){
 yz_prism([[3,6.8],[11.25,6.8],[11.25,9.2],[5.2,9.2],[3,7]],9,19);
 xy_prism([[9,3],[19,3],[19,7.25],[15,11.25],[13,11.25],[9,7.25]],6.7,10);
}}
module support_core(){union(){
 linear_extrude(T)frame2d();
 for(c=tab_centers)translate([c-tab_w/2,H,0])cube([tab_w,tab_h,tab_t]);
 catch_left();translate([W,0,0])mirror([1,0,0])catch_left();
}}
// Rear brace sockets are ADDED behind the rear rail (local u=150).
// Socket cross section repeats 7.10 x 22.10, insertion is 7 mm along u.
// Socket roof bridges 22.1 mm: inspect the brace coupon's sliced bridge.
brace_levels=[40,200];
module brace_socket_blocks(){for(h=brace_levels)difference(){
 cuboid([148,h-15,0],[158,h+15,14.1]);
 cuboid([151,h-11.05,3.5],[158.01,h+11.05,10.6]);
}}
module rail_stiffeners(){
 // Raised 6 x 3 mm flanges resist weak-axis bending/buckling of the tall rails.
 // Stop clear of the tested foot and the top shoulder guides; no rail cuts.
 for(u=[2,142])yz_prism([[20,6.8],[H-12,6.8],[H-12,7],[H-18,10],[26,10],[20,7]],u,u+6);
}
module support(){union(){support_core();brace_socket_blocks();rail_stiffeners();}}
module brace_socket_coupon(){translate([-145,-25,0])intersection(){support();cuboid([145,25,0],[158,55,14.1]);}}
// Rear panel prints flat, tab projections up. Assembly tabs point forward.
module rear_brace(){union(){
 linear_extrude(6)union(){
  for(x=[12,208])for(y=[15,175])translate([x-12,y-15])square([24,30]);
  beam2d(12,15,208,175,8);beam2d(12,175,208,15,8);
 }
 for(x=[12,208])for(y=[15,175])cuboid([x-3.5,y-11,5.8],[x+3.5,y+11,13]);
}}
module brace_tab_coupon(){intersection(){rear_brace();cuboid([0,0,0],[24,30,13]);}}
module place_brace(){translate([13.55,174,27])rotate([90,0,0])children();}
module rounded_rect(w,d,r){hull(){for(x=[r,w-r])for(y=[r,d-r])translate([x,y])circle(r=r);}}
module outline(){rounded_rect(top_x,top_y,6);}
module perimeter(){difference(){outline();translate([3,3])rounded_rect(top_x-6,top_y-6,3);}}
module guide(sx,cy){
 // Guides engage the shoulder/body with 0.2 mm per face, NOT extra tab depth.
 // Top frame is 10 mm high; guides extend 8 mm below its bearing shoulder.
 for(sign=[-1,1])translate([sx,cy,0])scale([sign,1,1])
  multmatrix([[1,0,0,0],[0,0,-1,boss_y/2],[0,1,0,0],[0,0,0,1]])
  linear_extrude(boss_y)polygon([[guide_gap/2,deck_depth-.2],[boss_x/2,deck_depth-.2],
   [boss_x/2,deck_depth],[6.5,deck_depth+2],[6.5,deck_depth+guide_depth],
   [guide_gap/2,deck_depth+guide_depth]]);
}
module top(){difference(){union(){
 linear_extrude(skin)outline();
 translate([0,0,skin-.2])linear_extrude(rim_depth-skin+.2)perimeter();
 // Continuous left-right beams; roof/skin acts as their upper flange in service.
 for(y=[49,85,121])cuboid([3,y-2.5,skin-.2],[top_x-3,y+2.5,deck_depth]);
 // Cross-ribs spread heel pressure and connect the beams and perimeter.
 for(x=[22,71,120,169,218])cuboid([x-1.8,3,skin-.2],[x+1.8,top_y-3,rim_depth]);
 for(sx=support_x)for(cy=slot_y){
  cuboid([sx-boss_x/2,cy-boss_y/2,skin-.2],[sx+boss_x/2,cy+boss_y/2,deck_depth]);
  guide(sx,cy);
 }
}
 // Blind sockets OPEN UP in print orientation, roof at z=9 mm.
 // Full 7 mm straight engagement; no pocket cuts through a socket wall.
 for(sx=support_x)for(cy=slot_y)
  cuboid([sx-slot_t/2,cy-slot_w/2,deck_depth-engagement],[sx+slot_t/2,cy+slot_w/2,deck_depth+.01]);
}}
module socket_coupon(){translate([-11,-31,0])intersection(){top();cuboid([11,31,0],[33,67,25]);}}
module tab_coupon(){translate([-23,-(H-frame),0])intersection(){support();cuboid([23,H-frame,0],[55,H+tab_h,T]);}}
module foot_local(){difference(){union(){
 cuboid([-1.8,-2,-2.05],[28,0,9.05]);
 cuboid([-1.8,-.1,-2.05],[28,9,-.25]);
 cuboid([-1.8,-.1,7.25],[28,14,9.05]);
 cuboid([-1.8,-.1,-2.05],[-.25,9,9.05]);
}xy_prism([[8.75,2.75],[19.25,2.75],[19.25,7.25],[15,11.5],[13,11.5],[8.75,7.25]],7,12);}}
module foot_print(){translate([1.8,9.05,2])rotate([90,0,0])foot_local();}
module place_support(sx){translate([sx-T/2,support_y0,sole])rotate([90,0,90])children();}
module place_top(){translate([0,top_y,total_height])rotate([180,0,0])children();}
module assembly(){
 color("silver")place_top()top();
 color("steelblue")place_brace()rear_brace();
 for(sx=support_x)place_support(sx){
  color("slategray")support();
  color("peru"){foot_local();translate([W,0,0])mirror([1,0,0])foot_local();}
 }
}
if(part=="top")top();
else if(part=="support")support();
else if(part=="brace")rear_brace();
else if(part=="brace_socket_coupon")brace_socket_coupon();
else if(part=="brace_tab_coupon")brace_tab_coupon();
else if(part=="socket_coupon")socket_coupon();
else if(part=="tab_coupon")tab_coupon();
else if(part=="foot_left")foot_print();
else if(part=="foot_right")translate([29.8,0,0])mirror([1,0,0])foot_print();
else if(part=="assembly")assembly();
else assert(false,"Unknown part selector");
