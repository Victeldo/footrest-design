from pathlib import Path
import json,numpy as np,trimesh as tm,manifold3d as md
W=Path(__file__).resolve().parent;O=W
matrices=[[[0,1,0,0],[0,0,1,0],[1,0,0,12.3],[0,0,0,1]],[[1,0,0,14],[0,0,1,-.3],[0,-1,0,24],[0,0,0,1]],[[0,0,1,4.9],[1,0,0,12],[0,1,0,-6],[0,0,0,1]]]
meshes={};solids={};report={}
for n,M in zip(['receiver','tongue','keeper'],matrices):
 m=tm.load_mesh(W/('V8_trial_'+n+'.stl'));report[n]={'watertight':bool(m.is_watertight),'winding':bool(m.is_winding_consistent),'components':len(m.split(only_watertight=False)),'volume_mm3':float(m.volume),'print_bounds_mm':m.bounds.tolist()}
 assert m.is_watertight and m.is_winding_consistent and len(m.split())==1 and m.volume>0
 assert min(m.bounds[0])>=-1e-4 and max(m.extents)<256
 m.apply_transform(np.linalg.inv(M));meshes[n]=m
 solids[n]=md.Manifold(md.Mesh(np.asarray(m.vertices,np.float32),np.asarray(m.faces,np.uint32)))
r,t,k=[solids[n] for n in ['receiver','tongue','keeper']]
def key(a=90,z=0):return k.translate([0,-9,0]).rotate([0,0,a]).translate([0,9,z])
def vol(a,b):return abs((a^b).volume())
checks={}
checks['tongue_insertion_max_overlap_mm3']=max(vol(r,t.translate([0,y,0])) for y in np.linspace(0,30,121))
checks['locked_pair_overlap_mm3']=max(vol(r,t),vol(r,key()),vol(t,key()))
checks['lift_max_overlap_mm3']=max(vol(r+t,key(z=z)) for z in np.linspace(0,1.8,37))
checks['turn_max_overlap_mm3']=max(vol(r+t,key(a,1.8)) for a in np.linspace(0,90,181))
checks['keeper_withdrawal_max_overlap_mm3']=max(vol(r+t,key(0,z)) for z in np.linspace(1.8,30,283))
print(checks)
assert max(checks.values())<.001
checks['withdrawal_block_at_1mm_mm3']=vol(t.translate([0,1,0]),key())
checks['locked_lift_block_at_3mm_mm3']=vol(r,key(z=3))
checks['seated_turn_block_at_15deg_mm3']=vol(r,key(75))
assert min(list(checks.values())[-3:])>.01
report['path_checks']=checks
report['solid_PLA_mass_g_at_1_24']=sum(report[n]['volume_mm3'] for n in meshes)*.00124
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2))
for n in meshes:
 q=tm.load_mesh(W/('V8_trial_'+n+'.stl'));q.export(O/('V8_trial_'+n+'.stl'))
print(json.dumps(report,indent=2))
