// V8B TETHER-EYELET COUPON ONLY. V7 rear connection retired after stuck/broken key.
// All PLA. No full support or brace revision is released by this file.
// Nominal values are trial fits, not empirically calibrated.
part="assembly"; // receiver, tongue, keeper, assembly, unlocked, exploded
$fn=64;
// Assembly coordinates: X across brace, Y tongue insertion, Z vertical.
// Receiver Y=0..18; tongue withdraws toward +Y. Keeper axis is Z.
receiver_w=24.6; receiver_l=18; receiver_h=18.6;
tongue_w=18; tongue_h=12; tongue_l=18;
slide_clearance=.3; // EACH FACE, total .6 mm in X and Z
keyhole_x=12.2;keyhole_y=6.6;
shaft_d=6; key_foot_x=11.6; key_foot_y=6;
head_z=19; head_top=23; lift=1.8;
module box(a,b){translate(a)cube(b-a);}
module receiver(){difference(){union(){
 // Added eyelet outside the socket; no cut into tongue bearing walls.
 box([11.8,5,15.6],[20,13,18.6]);
 box([-receiver_w/2,0,0],[receiver_w/2,receiver_l,receiver_h]);
 // Four open indexing posts. LOCKED handle runs along Y between X posts.
 for(sx=[-1,1])for(sy=[-1,1])translate([0,9,0])scale([sx,sy,1])
  box([3.3,3.3,18.4],[5.1,8.5,20.6]);
 // Small seats support the underside of the locked handle at z=19.
 for(sy=[-1,1])translate([0,9,0])scale([1,sy,1])
  box([-3,6.5,18.4],[3,8.5,19]);
}
 translate([16.5,9,15.5])cylinder(d=4,h=3.2);
 // Open through both ends: no blind end to wedge against.
 box([-tongue_w/2-slide_clearance,-.1,3],[tongue_w/2+slide_clearance,18.1,3+tongue_h+2*slide_clearance]);
 box([-keyhole_x/2,9-keyhole_y/2,-.1],[keyhole_x/2,9+keyhole_y/2,24]);
}}
module tongue(){difference(){union(){
 box([-9,0,3.3],[9,18.2,15.3]);
 box([-14,18,.3],[14,24,18.3]); // exposed pad represents rear-brace panel
}
 box([-keyhole_x/2,9-keyhole_y/2,3.2],[keyhole_x/2,9+keyhole_y/2,15.4]);
}}
// Unlocked keeper: foot and handle long axis X. Rotate +90 deg about Z to lock.
// Printed lying flat: all head/foot faces share Y=-3, no elevated grip overhang.
module keeper(){difference(){union(){
 translate([0,9,-2.7])cylinder(d=shaft_d,h=head_z+2.9);
 box([-key_foot_x/2,9-key_foot_y/2,-4.9],[key_foot_x/2,9+key_foot_y/2,-2.5]);
 box([-12,6,head_z],[12,12,head_top]);
}
 // Tether eye in handle tip, away from the load-bearing shaft.
 translate([9,9,18.9])cylinder(d=3,h=4.2);
}}
module turn_key(angle=90,dz=0){translate([0,9,dz])rotate([0,0,angle])translate([0,-9,0])keeper();}
module receiver_print(){multmatrix([[0,1,0,0],[0,0,1,0],[1,0,0,12.3],[0,0,0,1]])receiver();}
module tongue_print(){multmatrix([[1,0,0,14],[0,0,1,-.3],[0,-1,0,24],[0,0,0,1]])tongue();}
module keeper_print(){multmatrix([[0,0,1,4.9],[1,0,0,12],[0,1,0,-6],[0,0,0,1]])keeper();}
if(part=="receiver")receiver_print();
else if(part=="tongue")tongue_print();
else if(part=="keeper")keeper_print();
else if(part=="assembly"){
 color("silver")receiver();color("steelblue")tongue();color("orange")turn_key();
} else if(part=="unlocked"){
 color("silver")receiver();color("steelblue")tongue();color("orange")turn_key(0,lift);
} else if(part=="exploded"){
 color("silver")receiver();color("steelblue")translate([0,30,0])tongue();color("orange")turn_key(0,32);
} else assert(false,"Unknown selector");
