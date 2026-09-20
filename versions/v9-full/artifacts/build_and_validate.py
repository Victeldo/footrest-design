from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json,hashlib
import argparse,subprocess,tempfile
p=argparse.ArgumentParser();p.add_argument('--openscad',default='openscad');args=p.parse_args()
O=Path(__file__).resolve().parent
tmp=tempfile.TemporaryDirectory();W=Path(tmp.name)
for part in ['support','brace','top','foot_left','foot_right']:
 subprocess.run([args.openscad,'-D','part=\"'+part+'\"','-o',str(W/(part+'.stl')),str(O/'V9_full_prototype.scad')],check=True)
meshes={};report={}
def solid(q):return md.Manifold(md.Mesh(np.asarray(q.vertices,np.float32),np.asarray(q.faces,np.uint32)))
def moved(q,M):q=q.copy();q.apply_transform(M);return q
def iv(a,b):return abs((a^b).volume())
for n in ['support','brace','top','foot_left','foot_right']:
 q=tm.load_mesh(W/(n+'.stl'));meshes[n]=q
 assert q.is_watertight and q.is_winding_consistent and len(q.split())==1 and q.volume>0
 assert min(q.bounds[0])>=-.001 and max(q.extents)<256
 report[n]={'watertight':True,'components':1,'print_size_mm':q.extents.tolist(),'volume_mm3':q.volume}
sm=[np.array([[0,0,1,x-3.5],[1,0,0,10],[0,1,0,2],[0,0,0,1]]) for x in [22,218]]
supports=[moved(meshes['support'],M) for M in sm]
brace=moved(meshes['brace'],np.linalg.inv([[1,0,0,-15],[0,0,1,-30],[0,-1,0,174.3],[0,0,0,1]]))
top=moved(meshes['top'],[[1,0,0,0],[0,-1,0,170],[0,0,-1,241],[0,0,0,1]])
s=solid(supports[0])+solid(supports[1]);b=solid(brace);t=solid(top)
checks={'seated_support_brace':iv(s,b),'top_seated':iv(t,s+b),'vertical_release_0_25mm':max(iv(s,b.translate([0,0,z])) for z in np.linspace(0,21,85)), 'rear_approach_raised_0_25mm':max(iv(s,b.translate([0,y,21])) for y in np.linspace(0,30,121)), 'top_install_0_5mm':max(iv(t.translate([0,0,z]),s+b) for z in np.linspace(0,30,61))}
fm=np.array([[1,0,0,-1.8],[0,0,1,-2],[0,-1,0,9.05],[0,0,0,1]])
flip=np.array([[-1,0,0,150],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
feet=[moved(meshes['foot_left'],M@F) for M in sm for F in [fm,flip@fm]]
checks['feet_structural_interference']=max(iv(s+b+t,solid(f)) for f in feet)
# Check full solid equality for parts that should not change.
checks['brace_symmetric_difference_vs_tested_context']=(solid(meshes['brace'])-solid(tm.load_mesh(O/'reference/tested_brace_context.stl'))).volume()+(solid(tm.load_mesh(O/'reference/tested_brace_context.stl'))-solid(meshes['brace'])).volume()
checks['top_symmetric_difference_vs_V7']=(solid(meshes['top'])-solid(tm.load_mesh(O/'reference/unchanged_top.stl'))).volume()+(solid(tm.load_mesh(O/'reference/unchanged_top.stl'))-solid(meshes['top'])).volume()
print(checks);assert max(abs(v) for v in checks.values())<.001
# Added root backing occupies y<=160; sliding C surfaces start y=160.7.
report['zero_overlap_checks_mm3']=checks
report['nominal_root_backing_to_channel_front_gap_mm']=.7
report['notes']='No FEA or load rating. Gravity seated; top does not prevent lift-off. Sampled rigid paths, not tolerance stack or deformable TPU simulation.'
for n,q in meshes.items():
 name='V9_'+n+('_TPU95A' if n.startswith('foot') else '_PLA_PROTOTYPE')+'.stl';p=O/name;q.export(p)
 re=tm.load_mesh(p);assert re.is_watertight and len(re.split())==1
 report[n]['file']=name;report[n]['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
