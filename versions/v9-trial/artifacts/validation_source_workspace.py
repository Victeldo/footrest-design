# Reproduction script for original project workspace; requires work/v9 context meshes, work/v7 top mesh and renderer plus numpy/trimesh/manifold3d/Pillow.
from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json
W=Path('work/v9');O=Path('outputs/V9');ms={};report={}
def solid(q):return md.Manifold(md.Mesh(np.asarray(q.vertices,np.float32),np.asarray(q.faces,np.uint32)))
def move(q,M):q=q.copy();q.apply_transform(M);return q
def overlap(a,b):return abs((a^b).volume())
for n in ['rail_coupon','channel_coupon','support_context','brace_context']:
 q=tm.load_mesh(W/(n+'.stl'));ms[n]=q
 assert q.is_watertight and q.is_winding_consistent and len(q.split())==1 and q.volume>0
 assert min(q.bounds[0])>-.001 and max(q.extents)<256
 report[n]={'connected_components':len(q.split()),'watertight':bool(q.is_watertight),'volume_mm3':q.volume,'print_size_mm':q.extents.tolist()}
rail=move(ms['rail_coupon'],np.linalg.inv([[0,1,0,10],[0,0,1,6],[1,0,0,7],[0,0,0,1]]))
channel=move(ms['channel_coupon'],np.linalg.inv([[1,0,0,10.5],[0,0,1,0],[0,-1,0,14.3],[0,0,0,1]]))
r,c=solid(rail),solid(channel)
checks={'coupon_vertical_path':max(overlap(r,c.translate([0,0,z])) for z in np.linspace(0,21,85)), 'coupon_rear_approach_raised':max(overlap(r,c.translate([0,y,21])) for y in np.linspace(0,25,101))}
brace=move(ms['brace_context'],np.linalg.inv([[1,0,0,-15],[0,0,1,-30],[0,-1,0,174.3],[0,0,0,1]]));b=solid(brace)
supports=[move(ms['support_context'],[[0,0,1,x-3.5],[1,0,0,10],[0,1,0,2],[0,0,0,1]]) for x in [22,218]]
top=move(tm.load_mesh('work/v7/top.stl'),[[1,0,0,0],[0,-1,0,170],[0,0,-1,241],[0,0,0,1]])
s=solid(supports[0])+solid(supports[1]);t=solid(top)
checks['full_vertical_path_top_removed']=max(overlap(s,b.translate([0,0,z])) for z in np.linspace(0,21,85))
checks['full_rear_approach_top_removed']=max(overlap(s,b.translate([0,y,21])) for y in np.linspace(0,30,121))
checks['assembled_top_interference']=overlap(t,s+b)
checks['top_install_path']=max(overlap(t.translate([0,0,z]),s+b) for z in np.linspace(0,30,61))
print(checks)
for z in np.linspace(0,21,85):
 hit=s^b.translate([0,0,z])
 if abs(hit.volume())>.001:print(z,hit.volume(),hit.bounding_box())
assert max(checks.values())<.001
checks['down_stop_0_5mm_overlap']=overlap(r,c.translate([0,0,-.5]));checks['pull_back_1mm_overlap']=overlap(r,c.translate([0,1,0]));checks['sideways_1mm_overlap']=overlap(r,c.translate([1,0,0]));assert min(list(checks.values())[-3:])>1
# No unproven claim that the existing top locks the brace.
checks['lift_21mm_with_top_overlap']=overlap(t,b.translate([0,0,21]))
report['checks_mm3']=checks;report['coupon_solid_PLA_g']=sum(ms[n].volume for n in ['rail_coupon','channel_coupon'])*.00124
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2))
for n in ['rail_coupon','channel_coupon']:ms[n].export(O/('PRINT_FIRST_V9_'+n+'.stl'))
src=Path('work/v7/render_views.py').read_text();exec(src[src.index('def render('):src.index('fig,axes=')])
from PIL import Image,ImageDraw
im=Image.new('RGB',(1500,650),'white');d=ImageDraw.Draw(im)
for i,(items,title) in enumerate([([(rail,np.array([160,175,188])),(channel,np.array([67,140,185]))],'Seated: C channel wraps the T rail'), ([(rail,np.array([160,175,188])),(move(channel,tm.transformations.translation_matrix([0,0,21])),np.array([67,140,185]))],'Lift 21 mm to disengage'), ([(q,np.array([160,175,188])) for q in supports]+[(top,np.array([190,195,200])),(brace,np.array([67,140,185]))],'Full concept: four joints, no separate fasteners')]):
 im.paste(Image.fromarray(render(items,55,28,500,570)),(i*500,50));d.text((i*500+10,20),title,fill='black')
d.text((15,625),'V9 concept - only the two small fit coupons are released for printing. Full assembly is not load validated.',fill='black');im.save(O/'V9_design.png')
print(json.dumps(report,indent=2))
