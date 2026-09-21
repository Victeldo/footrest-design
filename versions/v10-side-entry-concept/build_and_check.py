from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json
import argparse,subprocess,tempfile
p=argparse.ArgumentParser();p.add_argument('--openscad',default='openscad');args=p.parse_args()
O=Path(__file__).resolve().parent
tmp=tempfile.TemporaryDirectory();W=Path(tmp.name)
for name in ['left','right','brace','top']:
 subprocess.run([args.openscad,'-D','part="'+name+'"','-o',str(W/(name+'.stl')),str(O/'V10_concept.scad')],check=True)

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
report={'stage':'concept only; no print release','zero_overlap_checks_mm3':checks,'intentional_blocking_mm3':blocks,'left_splay_deg_top_fixed_overlap_mm3':splay,'tongue_engagement_mm':12,'blind_end_gap_mm':2,'nominal_vertical_and_depth_clearance_per_face_mm':.15,'top_tab_clearance_total_mm':.10,'limitations':['No deformable-contact or coupled top-lift analysis','No measured stiffness/strength','New socket fit and print directions untested','Top can lift off; capture is conditional on top remaining seated','No TPU handedness/assembly regression yet']}
(O/'concept_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
