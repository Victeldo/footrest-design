
// Flat-pack Footrest V3 — calibrated from physical fit tests
// Overall height: 241 mm
// Nominal tab: 7.00 x 22.00 mm
// Tested winning socket: 7.10 x 22.10 mm (+0.10 mm total)
// Intended use: seated footrest, not a step stool.

$fn=48;
part = "assembly"; // "top", "support", "assembly"

top_x = 230;
top_y = 170;
top_skin_t = 5;       // visible platform thickness
boss_extra = 2;       // bosses extend 2 mm below platform
engagement = 7;       // total socket depth = 5 + 2
overall_h = 241;
support_body_h = overall_h - engagement; // 234 mm

support_span_y = 150;
support_t = 7;

tab_t = 7;
tab_w = 22;
tab_h = 7;

slot_t = 7.10;
slot_w = 22.10;

support_x1 = 26;
support_x2 = top_x - 26;
support_y0 = 10;

// Slot centers along Y. Support tabs are placed to match these exactly.
slot_cy1 = 49;
slot_cy2 = 121;
local_tab_c1 = slot_cy1 - support_y0; // 39
local_tab_c2 = slot_cy2 - support_y0; // 111

module rr2d(x,y,r){
    offset(r=r) offset(delta=-r) square([x,y]);
}

module beam2d(x1,y1,x2,y2,w){
    hull(){
        translate([x1,y1]) circle(d=w);
        translate([x2,y2]) circle(d=w);
    }
}

module support_2d(){
    union(){
        // 12 mm perimeter frame
        difference(){
            rr2d(support_span_y, support_body_h, 7);
            translate([12,15])
                rr2d(support_span_y-24, support_body_h-30, 6);
        }
        // One diagonal brace to resist in-plane racking without much material.
        beam2d(18,22,support_span_y-18,support_body_h-22,8);
    }
}

module side_support(){
    union(){
        linear_extrude(support_t) support_2d();

        // Two calibrated tabs.
        translate([local_tab_c1-tab_w/2, support_body_h, 0])
            cube([tab_w, tab_h, tab_t]);
        translate([local_tab_c2-tab_w/2, support_body_h, 0])
            cube([tab_w, tab_h, tab_t]);
    }
}

module top_raw(){
    // 5 mm platform.
    linear_extrude(top_skin_t) rr2d(top_x,top_y,8);

    // Local 2 mm bosses around each socket give 7 mm total engagement
    // without making the whole platform 7 mm thick.
    for (sx=[support_x1,support_x2])
        for (cy=[slot_cy1,slot_cy2])
            translate([sx-8.5, cy-16, -boss_extra])
                cube([17,32,boss_extra]);
}

module top_panel(){
    difference(){
        top_raw();

        // Underside lightening pockets: leave 2 mm top skin, 12 mm perimeter,
        // and ~10 mm ribs between six pockets.
        for (ix=[0:2])
            for (iy=[0:1])
                translate([12 + ix*72, 12 + iy*78, -0.01])
                    cube([62,68,3.01]);

        // Four sockets through boss + top: exactly 7 mm deep.
        for (sx=[support_x1,support_x2])
            for (cy=[slot_cy1,slot_cy2])
                translate([sx-slot_t/2, cy-slot_w/2, -boss_extra-0.01])
                    cube([slot_t,slot_w,engagement+0.02]);
    }
}

module assembly(){
    // Supports: local width -> global Y, local height -> global Z,
    // local thickness -> global X.
    translate([support_x1-support_t/2, support_y0, 0])
        rotate([90,0,90]) side_support();

    translate([support_x2-support_t/2, support_y0, 0])
        rotate([90,0,90]) side_support();

    // Bottom of bosses sits at z = 234; top surface at z = 241.
    translate([0,0,support_body_h+boss_extra])
        top_panel();
}

if (part=="top") top_panel();
else if (part=="support") side_support();
else assembly();
