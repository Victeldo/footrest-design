from pathlib import Path
import numpy as np,trimesh as tm,manifold3d as md,json,hashlib
O=Path('outputs/V9_bracket_V2')
def solid(q):return md.Manifold(md.Mesh(np.asarray(q.vertices,np.float32),np.asarray(q.faces,np.uint32)))
def move(q,M):q=q.copy();q.apply_transform(M);return q
def iv(a,b):return abs((a^b).volume())
q=tm.load_mesh('work/v9_v2/brace.stl');assert q.is_watertight and q.is_winding_consistent and len(q.split())==1 and q.volume>0
assert min(q.bounds[0])>-.001 and max(q.extents)<256
P=np.array([[1,0,0,-15],[0,0,1,-30],[0,-1,0,174.3],[0,0,0,1]])
b=solid(move(q,np.linalg.inv(P)))
old=solid(move(tm.load_mesh('outputs/V9_full/V9_brace_PLA_PROTOTYPE.stl'),np.linalg.inv(P)))
c=solid(move(tm.load_mesh('outputs/V9C_fit/V9C_channel_0p15_PLA.stl'),np.linalg.inv([[1,0,0,10.5],[0,0,1,0],[0,-1,0,14.3],[0,0,0,1]])))
expected=old
for x in [25.5,221.5]:
 for z in [30,190]:expected=expected+c.translate([x,160,z])
support=tm.load_mesh('outputs/V9_full/V9_support_PLA_PROTOTYPE.stl');s=None
for x in [22,218]:
 a=solid(move(support,[[0,0,1,x-3.5],[1,0,0,10],[0,1,0,2],[0,0,0,1]]));s=a if s is None else s+a
t=solid(move(tm.load_mesh('outputs/V9_full/V9_top_PLA_PROTOTYPE.stl'),[[1,0,0,0],[0,-1,0,170],[0,0,-1,241],[0,0,0,1]]))
checks={'exact_tested_channels_plus_unchanged_brace_difference':abs((expected-b).volume())+abs((b-expected).volume()),'assembled':iv(b,s+t),'vertical_release':max(iv(s,b.translate([0,0,z])) for z in np.linspace(0,21,85)),'raised_rear_approach':max(iv(s,b.translate([0,y,21])) for y in np.linspace(0,30,121)),'top_install':max(iv(b,t.translate([0,0,z])) for z in np.linspace(0,30,61))}
print(checks)
regression=checks.pop('exact_tested_channels_plus_unchanged_brace_difference')
assert regression<.02 # accumulated float32/STL coordinate rounding across full-width model
assert max(checks.values())<.001
p=O/'PRINT_V9_bracket_V2_0p15_PLA.stl';q.export(p);r=tm.load_mesh(p);assert r.is_watertight and r.is_winding_consistent and len(r.split())==1
report={'watertight':True,'consistent_winding':True,'components':1,'size_mm':q.extents.tolist(),'volume_mm3':q.volume,'solid_PLA_g':q.volume*.00124,'added_solid_PLA_g_vs_V1':(b.volume()-old.volume())*.00124,'zero_overlap_checks_mm3':checks,'regression_symmetric_difference_mm3':regression,'regression_tolerance_mm3':.02,'sampling_mm':{'brace':.25,'top':.5},'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'limits':'Rigid nominal geometry only; no anti-lift feature or load rating. Full-frame racking retest required.'}
(O/'geometry_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
