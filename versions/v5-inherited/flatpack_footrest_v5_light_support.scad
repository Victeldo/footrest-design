
$fn=48;

// V5 lightweight support
// Same calibrated top interface as earlier version.
// 150 mm wide x 234 mm body + 7 mm tabs = 241 mm total part height.
// Intended as a seated footrest support, not a step stool.

W = 150;
H = 234;
T = 7;

frame = 10;     // reduced from 12 mm
brace = 8;      // reduced from 10 mm

tab_w = 22;
tab_h = 7;
tab_t = 7;
tab_centers = [39,111];

// Small local "gusset" radius at brace/frame junctions.
module beam2d(x1,y1,x2,y2,w){
    hull(){
        translate([x1,y1]) circle(d=w);
        translate([x2,y2]) circle(d=w);
    }
}

module frame2d(){
    union(){
        // perimeter
        square([W,frame]);
        translate([0,H-frame]) square([W,frame]);
        translate([0,frame]) square([frame,H-2*frame]);
        translate([W-frame,frame]) square([frame,H-2*frame]);

        // X bracing, deliberately overlapping the perimeter
        beam2d(frame-5, frame-5, W-frame+5, H-frame+5, brace);
        beam2d(W-frame+5, frame-5, frame-5, H-frame+5, brace);

        // modest junction pads where braces cross perimeter:
        // these smooth stress flow without thickening every member.
        for (p=[[frame,frame],[W-frame,frame],[frame,H-frame],[W-frame,H-frame]])
            translate(p) circle(d=14);
    }
}

module support(){
    union(){
        linear_extrude(T) frame2d();

        // calibrated 7 x 22 x 7 mm tabs
        for (c=tab_centers)
            translate([c-tab_w/2,H,0])
                cube([tab_w,tab_h,tab_t]);
    }
}

support();
