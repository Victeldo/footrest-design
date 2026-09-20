# Audit script for the original project workspace; requires work/v9c renders and existing V9/V9_full mesh paths.
from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json
W=Path('work/v9c');O=Path('outputs/V9C_fit')
def solid(q):return md.Manifold(md.Mesh(np.asarray(q.vertices,np.float32),np.asarray(q.faces,np.uint32)))
def iv(a,b):return abs((a^b).volume())
def transformed(q,M):q=q.copy();q.apply_transform(M);return q
P=np.array([[1,0,0,10.5],[0,0,1,0],[0,-1,0,14.3],[0,0,0,1]])
old=solid(tm.load_mesh('outputs/V9/PRINT_FIRST_V9_channel_coupon.stl'))
base=solid(tm.load_mesh(W/'C0.30.stl'));assert abs((old-base).volume())+abs((base-old).volume())<.001
support=tm.load_mesh('outputs/V9_full/V9_support_PLA_PROTOTYPE.stl')
support=solid(transformed(support,[[0,0,1,18.5],[1,0,0,10],[0,1,0,2],[0,0,0,1]]))
report={'baseline_0_30_reproduces_original':True,'variants':{}}
for c in ['0.20','0.15']:
 q=tm.load_mesh(W/('C'+c+'.stl'));assert q.is_watertight and q.is_winding_consistent and len(q.split())==1
 assert min(q.bounds[0])>-.001 and max(q.extents)<256
 new=solid(q);assert abs((old-new).volume())<.001
 a=solid(transformed(q,np.linalg.inv(P)))
 travel=max(iv(support,a.translate([25.5,160,z+d])) for z in [30,190] for d in np.linspace(0,21,85));assert travel<.001
 approach=max(iv(support,a.translate([25.5,160+y,z+21])) for z in [30,190] for y in np.linspace(0,25,101));assert approach<.001
 back=iv(support,a.translate([25.5,161,30]));side=iv(support,a.translate([26.5,160,30]));stop=iv(support,a.translate([25.5,160,29.5]));assert min(back,side,stop)>1
 p=O/('V9C_channel_'+c.replace('.','p')+'_PLA.stl');q.export(p);r=tm.load_mesh(p);assert r.is_watertight and len(r.split())==1
 report['variants'][c]={'per_face_clearance_mm':float(c),'bevel_normal_clearance_mm':2**.5*float(c),'components':1,'watertight':True,'size_mm':q.extents.tolist(),'solid_PLA_g':q.volume*.00124,'vertical_path_max_overlap_mm3':travel,'raised_approach_max_overlap_mm3':approach,'deliberate_backward_sideways_downward_collision_mm3':[back,side,stop]}
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
