// V10A user-requested full prototype. New fit/top-lift behavior untested; no load rating.
use <reference/V7.scad>
part="assembly";
$fn=48;
module box(a,b){translate(a)cube(b-a);}
module left_world(){union(){
 place_support(22){support_core();rail_stiffeners();}
 for(z=[40,200])difference(){
  box([18.5,150,z-12],[42,173,z+12]);
  // Inward-facing blind pocket. Closed above and below, open toward center.
  box([28,160.85,z-8.15],[42.1,169.15,z+8.15]);
 }
}}
module right_world(){translate([240,0,0])mirror([1,0,0])left_world();}
module brace_world(){union(){
 for(z=[40,200]){
  box([30,161,z-8],[42.2,169,z+8]);
  box([42,161,z-10],[54,169,z+10]);
  box([197.8,161,z-8],[210,169,z+8]);
  box([186,161,z-10],[198,169,z+10]);
 }
 for(pair=[[[48,40],[192,200]],[[48,200],[192,40]]])
 hull()for(p=pair)translate([p[0],163,p[1]])rotate([-90,0,0])cylinder(d=8,h=6);
}}
// Rear blocks extend to the original flat face so they start on the bed.
if(part=="left_print")multmatrix([[0,1,0,-10],[0,0,1,-2],[1,0,0,-18.5],[0,0,0,1]])left_world();
else if(part=="right_print")multmatrix([[0,1,0,-10],[0,0,-1,232],[-1,0,0,221.5],[0,0,0,1]])right_world();
else if(part=="brace_print")multmatrix([[1,0,0,-30],[0,0,1,-30],[0,-1,0,169],[0,0,0,1]])brace_world();
else if(part=="left")left_world();
else if(part=="right")right_world();
else if(part=="brace")brace_world();
else if(part=="top")place_top()top();
else {color("silver")place_top()top();color("slategray"){left_world();right_world();}color("steelblue")brace_world();}
