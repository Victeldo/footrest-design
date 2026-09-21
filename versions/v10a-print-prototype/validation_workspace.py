from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json
W=Path('work/v10a');O=Path('footrest-design/versions/v10a-print-prototype')
ms={n:tm.load_mesh(W/(n+'.stl')) for n in ['left','right','brace','top']}
def solid(q):return md.Manifold(md.Mesh(np.asarray(q.vertices,np.float32),np.asarray(q.faces,np.uint32)))
def iv(a,b):return abs((a^b).volume())
for q in ms.values():assert q.is_watertight and q.is_winding_consistent and len(q.split())==1
l,r,b,t=[solid(ms[n]) for n in ms]
checks={'assembled':max(iv(l,b),iv(r,b),iv(t,l+r+b)),'sideways_assembly_0_25mm':max(iv(l.translate([-d,0,0])+r.translate([d,0,0]),b) for d in np.linspace(0,16,65)),'top_install_0_5mm':max(iv(t.translate([0,0,d]),l+r+b) for d in np.linspace(0,40,81))}
print(checks);assert max(checks.values())<.001
blocks={'brace_up_0_5mm':iv(l+r,b.translate([0,0,.5])),'brace_down_0_5mm':iv(l+r,b.translate([0,0,-.5])),'support_outward_0_2mm_top_fixed':iv(t,l.translate([-.2,0,0])+r.translate([.2,0,0]))}
assert min(blocks.values())>0.01
# Rigid splay probes with top held fixed/seated. Not a coupled elastic simulation.
splay={}
for a in [.1,.25,.5,1,2]:
 splay[str(a)]=iv(t,l.translate([-22,0,-225]).rotate([0,a,0]).translate([22,0,225]))
report={'stage':'user-requested prototype STL release; no load rating','zero_overlap_checks_mm3':checks,'intentional_blocking_mm3':blocks,'left_splay_deg_top_fixed_overlap_mm3':splay,'tongue_engagement_mm':12,'blind_end_gap_mm':2,'nominal_vertical_and_depth_clearance_per_face_mm':.15,'top_tab_clearance_total_mm':.10,'limitations':['No deformable-contact or coupled top-lift analysis','No measured stiffness/strength','New socket fit and print directions untested','Top can lift off; capture is conditional on top remaining seated','No TPU handedness/assembly regression yet']}
(O/'concept_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))

import hashlib
transforms={
 'left_print':('left',[[0,1,0,-10],[0,0,1,-2],[1,0,0,-18.5],[0,0,0,1]]),
 'right_print':('right',[[0,1,0,-10],[0,0,-1,232],[-1,0,0,221.5],[0,0,0,1]]),
 'brace_print':('brace',[[1,0,0,-30],[0,0,1,-30],[0,-1,0,169],[0,0,0,1]])}
report['print_parts']={}
for name,(world,M) in transforms.items():
 q=tm.load_mesh(W/(name+'.stl'))
 assert q.is_watertight and q.is_winding_consistent and len(q.split())==1 and q.volume>0
 assert min(q.bounds[0])>=-.001 and max(q.extents)<256
 w=q.copy();w.apply_transform(np.linalg.inv(M));a=solid(w);b=solid(ms[world])
 delta=abs((a-b).volume())+abs((b-a).volume());from scipy.spatial import cKDTree
 max_vertex_error=max(cKDTree(w.vertices).query(ms[world].vertices)[0].max(),cKDTree(ms[world].vertices).query(w.vertices)[0].max())
 assert max_vertex_error<.001 and delta<1.0
 fn='V10A_'+name.replace('_print','')+'_PLA_PROTOTYPE.stl';q.export(O/fn)
 re=tm.load_mesh(O/fn);assert re.is_watertight and len(re.split())==1
 report['print_parts'][name]={'file':fn,'bounds_mm':q.bounds.tolist(),'size_mm':q.extents.tolist(),'volume_mm3':q.volume,'solid_PLA_g':q.volume*.00124,'one_watertight_component':True,'inverse_transform_regression_mm3':delta,'max_vertex_rounding_error_mm':float(max_vertex_error),'sha256':hashlib.sha256((O/fn).read_bytes()).hexdigest()}
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report['print_parts'],indent=2))
