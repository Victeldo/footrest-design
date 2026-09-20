
$fn=48;

// TPU 95A slip-on foot for V5 support.
// Print 4 total. Test one first.
// Designed to flex around a 7 mm thick PLA support edge.

L = 30;          // along support bottom rail
inner_w = 7.0;   // support thickness
inner_h = 8.0;   // captures 8 mm of the 10 mm-tall bottom rail
side = 1.5;
sole = 2.5;
lip = 1.0;

// Coordinates: X = length along rail, Y = across support thickness, Z = vertical.
module foot(){
    union(){
        // sole
        cube([L, inner_w + 2*side, sole]);

        // flexible side walls
        translate([0,0,sole]) cube([L,side,inner_h]);
        translate([0,inner_w+side,sole]) cube([L,side,inner_h]);

        // tiny inward lips at top; TPU flexes over the PLA edge
        translate([0,side,sole+inner_h-lip])
            cube([L,0.8,lip]);
        translate([0,side+inner_w-0.8,sole+inner_h-lip])
            cube([L,0.8,lip]);
    }
}

foot();
