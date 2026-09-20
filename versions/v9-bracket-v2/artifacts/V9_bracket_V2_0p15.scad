// Full rear bracket V2: tested 0p15 channels. Existing supports/top unchanged.
// clearance is per axis-aligned face; diagonal normal gap = sqrt(2)*clearance.
clearance=0.15;
assert(clearance>=.1 && clearance<=.3);
module box(a,b){translate(a)cube(b-a);}
module channel(){difference(){
 box([-10.5,.7,0],[10.5,14.3,20]);
 translate([0,0,-.1])linear_extrude(20.2)polygon([
 [-7-clearance,8+clearance],[7+clearance,8+clearance],
 [7+clearance,4-clearance],[3.5+clearance,.5-clearance],
 [-3.5-clearance,.5-clearance],[-7-clearance,4-clearance]]);
 box([-3.5-clearance,.6,-.1],[3.5+clearance,4-clearance+.1,20.1]);
}}

$fn=48;
module brace_world(){union(){
 for(x=[25.5,221.5])for(z=[30,190])translate([x,160,z])channel();
 for(pair=[[[25.5,40],[221.5,200]],[[25.5,200],[221.5,40]]])
 hull()for(p=pair)translate([p[0],168.3,p[1]])rotate([-90,0,0])cylinder(d=8,h=6);
}}
// Flat rear face on bed, channels upward. Millimetres.
multmatrix([[1,0,0,-15],[0,0,1,-30],[0,-1,0,174.3],[0,0,0,1]])brace_world();
