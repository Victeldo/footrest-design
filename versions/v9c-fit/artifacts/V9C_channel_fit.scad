// Replacement C-channel FIT TEST ONLY. Existing V9 supports/top unchanged.
// clearance is per axis-aligned face; diagonal normal gap = sqrt(2)*clearance.
clearance=0.20;
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
// SAME orientation as full brace: flat back on bed, channel facing upward.
multmatrix([[1,0,0,10.5],[0,0,1,0],[0,-1,0,14.3],[0,0,0,1]])channel();
