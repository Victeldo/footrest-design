// V9 full-size PROTOTYPE. User-tested sliding surfaces preserved. Not load-rated.
use <reference/footrest_V7.scad>
part="assembly";
$fn=48;
module box(a,b){translate(a)cube(b-a);}
// Joint local frame: x across width, y rearwards from rear rail face, z up.
// T head 14 x 4, stem 7, engagement 20. Straight 0.3 mm/axis-face trial clearance; bevel normal clearance approx 0.42 mm.
module t_joint(){union(){
 // Root backing extends into the rear rail; remains ahead of C channel.
 box([-7,-6,-3],[3.5,0,23]);
 linear_extrude(20)polygon([[-3.5,-2],[3.5,-2],[3.5,.5],[7,4],[7,8],[-7,8],[-7,4],[-3.5,.5]]);
 // A bearing ledge, NOT a latch. C back wall lands on this ledge.
 box([-5.5,-2,-3],[5.5,14.3,0]);
}}
module c_joint(){difference(){
 box([-10.5,.7,0],[10.5,14.3,20]);
 translate([0,0,-.1])linear_extrude(20.2)polygon([[-7.3,8.3],[7.3,8.3],[7.3,3.7],[3.8,.2],[-3.8,.2],[-7.3,3.7]]);
 box([-3.8,.6,-.1],[3.8,3.8,20.1]);
}}
module support_new(){union(){support_core();rail_stiffeners();
 for(h=[28,188]) // assembled bases z=30,190
  multmatrix([[0,1,0,150],[0,0,1,h],[1,0,0,7],[0,0,0,1]])t_joint();
}}
module brace_world(){union(){
 for(x=[25.5,221.5])for(z=[30,190])translate([x,160,z])c_joint();
 // Existing X principle, connected to the solid backs of four C shoes.
 for(pair=[[[25.5,40],[221.5,200]],[[25.5,200],[221.5,40]]])
 hull()for(p=pair)translate([p[0],168.3,p[1]])rotate([-90,0,0])cylinder(d=8,h=6);
}}
module rail_coupon(){union(){
 // Representative rear rail: local x=-7..0 is original 7 mm support thickness.
 box([-7,-10,-6],[0,0,26]);t_joint();
}}
module rail_print(){multmatrix([[0,1,0,10],[0,0,1,6],[1,0,0,7],[0,0,0,1]])rail_coupon();}
module channel_print(){multmatrix([[1,0,0,10.5],[0,0,1,0],[0,-1,0,14.3],[0,0,0,1]])c_joint();}
module brace_print(){multmatrix([[1,0,0,-15],[0,0,1,-30],[0,-1,0,174.3],[0,0,0,1]])brace_world();}
if(part=="rail_coupon")rail_print();
else if(part=="channel_coupon")channel_print();
else if(part=="support" || part=="support_context")support_new();
else if(part=="brace" || part=="brace_context")brace_print();
else if(part=="top")top();
else if(part=="foot_left")foot_print();
else if(part=="foot_right")translate([29.8,0,0])mirror([1,0,0])foot_print();
else if(part=="assembly"){
 color("silver")place_top()top();
 for(x=[22,218])color("slategray")place_support(x)support_new();
 color("steelblue")brace_world();
}
