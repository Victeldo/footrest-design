from pathlib import Path
import json,hashlib,itertools
import numpy as np
import trimesh as tm
import manifold3d as md
import argparse,subprocess,sys,shutil
ROOT=Path(__file__).resolve().parent;W=ROOT/'work';OUT=ROOT
W.mkdir(exist_ok=True)
parser=argparse.ArgumentParser(description='Compile and validate the default V7 prototype.')
parser.add_argument('--openscad',default=shutil.which('openscad'))
args=parser.parse_args()
if not args.openscad:parser.error('Supply --openscad /path/to/OpenSCAD')
for part in ['top','support','brace','socket_coupon','tab_coupon','brace_socket_coupon','brace_tab_coupon','foot_left','foot_right']:
 result=subprocess.run([args.openscad,'-D','part="'+part+'"','-o',str(W/(part+'.stl')),str(ROOT/'footrest_V7.scad')],capture_output=True,text=True)
 (W/(part+'.log')).write_text(result.stdout+result.stderr)
 if result.returncode:raise RuntimeError(part+': '+result.stderr)

def load(p):
 m=tm.load_mesh(p);return md.Manifold(md.Mesh(np.asarray(m.vertices,dtype=np.float32),np.asarray(m.faces,dtype=np.uint32)))
def mesh(s):
 m=s.to_mesh();return tm.Trimesh(vertices=m.vert_properties[:,:3],faces=m.tri_verts,process=True)
def box(a,b):return md.Manifold.cube(np.array(b)-a).translate(a)
def stats(s):
 m=mesh(s)
 return {'watertight':bool(m.is_watertight),'winding_consistent':bool(m.is_winding_consistent),'components':len(m.split(only_watertight=False)),'bounds_mm':m.bounds.tolist(),'extents_mm':m.extents.tolist(),'volume_cm3':float(m.volume/1000),'solid_mass_g':float(m.volume/1000*1.24)}
def volume(s):return max(0,float(s.volume()))
def sym(a,b):return volume(a-b)+volume(b-a)
parts={p.stem:load(p) for p in W.glob('*.stl') if p.stem in ['top','support','brace','socket_coupon','tab_coupon','brace_socket_coupon','brace_tab_coupon','foot_left','foot_right']}
assert len(parts)==9,parts.keys()
report={'parts':{n:stats(s) for n,s in parts.items()},'checks':{}}
for n,s in parts.items():
 d=report['parts'][n]; assert d['watertight'] and d['winding_consistent'] and d['components']==1,(n,d)
 assert max(d['extents_mm'])<256 and min(d['bounds_mm'][0])>=-.001,(n,d)
 if n.startswith('foot_'):d['solid_mass_g']=d['volume_cm3']*1.20
S=parts['support'];T=parts['top']; B=parts['brace']
# Axis transforms from print coordinates to assembled global coordinates.
mt=np.array([[1,0,0,0],[0,-1,0,170],[0,0,-1,241]],float)
mb=np.array([[1,0,0,13.55],[0,0,-1,174],[0,1,0,27]],float)
ml=np.array([[0,0,1,18.5],[1,0,0,10],[0,1,0,2]],float);mr=ml.copy();mr[0,3]=214.5
# Undo the foot print transform: (x,y,z)->(x-1.8,z-2,9.05-y).
mf=np.array([[1,0,0,-1.8],[0,0,1,-2],[0,-1,0,9.05]],float)
f=parts['foot_left'].transform(mf);fr=f.mirror([1,0,0]).translate([150,0,0])
assembly={'top':T.transform(mt),'support_L':S.transform(ml),'support_R':S.transform(mr),'rear_brace':B.transform(mb),
 'foot_L_front':f.transform(ml),'foot_L_rear':fr.transform(ml),'foot_R_front':f.transform(mr),'foot_R_rear':fr.transform(mr)}
c=report['checks'];c['pairwise_intersections_mm3']={}
for (na,a),(nb,b) in itertools.combinations(assembly.items(),2):
 v=volume(a^b);c['pairwise_intersections_mm3'][na+' / '+nb]=v;assert v<.02,(na,nb,v)
mins=np.min([mesh(s).bounds[0] for s in assembly.values()],axis=0);maxs=np.max([mesh(s).bounds[1] for s in assembly.values()],axis=0)
c['assembled_bounds_mm']=[mins.tolist(),maxs.tolist()];c['assembled_extents_mm']=(maxs-mins).tolist();assert abs(maxs[2]-mins[2]-241)<.001
# Actual support tabs: expected boxes at 7 x22 x7, not just asserted variables.
expected=box([28,223,0],[50,230,7])+box([100,223,0],[122,230,7]);actual=S^box([-1,223,-1],[160,231,16])
c['tab_symmetric_difference_mm3']=sym(actual,expected);assert c['tab_symmetric_difference_mm3']<.01
# Four exact socket prisms; void within; 9 mm cap above, continuous 3.45 mm side walls.
c['socket_dimensions_mm']=[7.1,22.1,7];c['socket_void_intersections_mm3']=[];c['socket_wall_missing_mm3']=[]
for sx in [22,218]:
 for cy in [49,121]:
  slot=box([sx-3.55,cy-11.05,9],[sx+3.55,cy+11.05,16]);c['socket_void_intersections_mm3'].append(volume(T^slot))
  for a,b in [([sx-7,cy-16,2.4],[sx-3.55,cy+16,16]),([sx+3.55,cy-16,2.4],[sx+7,cy+16,16]),([sx-3.55,cy-16,2.4],[sx+3.55,cy-11.05,16]),([sx-3.55,cy+11.05,2.4],[sx+3.55,cy+16,16]),([sx-3.55,cy-11.05,2.4],[sx+3.55,cy+11.05,9])]:c['socket_wall_missing_mm3'].append(volume(box(a,b)-T))
assert max(c['socket_void_intersections_mm3'])<.01 and max(c['socket_wall_missing_mm3'])<.01
# No collision along vertical support insertion or horizontal rear-brace insertion.
c['support_insertion_intersections_mm3']={str(d):volume((assembly['support_L'].translate([0,0,-d])+assembly['support_R'].translate([0,0,-d]))^assembly['top']) for d in [0,.25,1,3,7,10,15,25]}
c['brace_insertion_intersections_mm3']={str(d):volume(assembly['rear_brace'].translate([0,d,0])^(assembly['support_L']+assembly['support_R']+assembly['top'])) for d in [0,.25,1,3,7,10,15]}
assert max(c['support_insertion_intersections_mm3'].values())<.02;assert max(c['brace_insertion_intersections_mm3'].values())<.02
# Shoulder gap/engagement evaluated on actual solids by small deliberate displacement.
c['shoulder_contact_overlap_at_0p1mm_overinsertion_mm3']=volume(assembly['top']^(assembly['support_L'].translate([0,0,.1])+assembly['support_R'].translate([0,0,.1])))
assert c['shoulder_contact_overlap_at_0p1mm_overinsertion_mm3']>1
# Coupon fit in its actual assembly coordinate system.
key=parts['tab_coupon'].transform(np.array([[0,0,1,7.5],[-1,0,0,34],[0,-1,0,26]],float))
bracekey=parts['brace_tab_coupon'].transform(np.array([[0,0,-1,19],[0,1,0,0],[1,0,0,-4.95]],float))
c['top_coupon_fit_intersection_mm3']=volume(key^parts['socket_coupon']);c['brace_coupon_fit_intersection_mm3']=volume(bracekey^parts['brace_socket_coupon'])
assert c['top_coupon_fit_intersection_mm3']<.02 and c['brace_coupon_fit_intersection_mm3']<.02
legacy=load(ROOT/'reference/V6A_tested_foot.stl');c['tested_foot_symmetric_difference_mm3']=sym(parts['foot_left'],legacy);assert c['tested_foot_symmetric_difference_mm3']<.01
old=load(ROOT/'reference/V6A_support_reference_NOT_FOR_PRINT.stl')
# Compare catch projection beyond z=7: should be exact even though support height changed.
catchbox=box([-1,-1,7.001],[151,20,10]);c['tested_catch_symmetric_difference_mm3']=sym(S^catchbox,old^catchbox);assert c['tested_catch_symmetric_difference_mm3']<.01
# The full bottom rail rectangular region remains present, excluding no material.
c['bottom_rail_missing_mm3']=volume(box([0,0,0],[150,10,7])-S);assert c['bottom_rail_missing_mm3']<.01
# Thin surface-slab volume measures actual contact footprint on flat floor.
feet=[s for n,s in assembly.items() if n.startswith('foot')]
bottoms=[mesh(s^box([-10,-10,-.01],[250,180,.01])).bounds for s in feet]
c['floor_contact_envelope_mm']=[np.min([b[0][:2] for b in bottoms],axis=0).tolist(),np.max([b[1][:2] for b in bottoms],axis=0).tolist()]
# Export released printable meshes only after validation; reload each.
filenames={'top':'V7_top_PROTOTYPE.stl','support':'V7_support_PROTOTYPE.stl','brace':'V7_rear_brace_PROTOTYPE.stl',
 'socket_coupon':'PRINT_FIRST_top_socket_coupon.stl','tab_coupon':'PRINT_FIRST_top_tab_coupon.stl',
 'brace_socket_coupon':'PRINT_FIRST_brace_socket_coupon.stl','brace_tab_coupon':'PRINT_FIRST_brace_tab_coupon.stl',
 'foot_left':'V6A_unchanged_foot_left.stl','foot_right':'V6A_mirrored_foot_right.stl'}
for n,s in parts.items():
 p=OUT/filenames[n];mesh(s).export(p);d=stats(load(p));assert d['watertight'] and d['components']==1
 report['parts'][n]['filename']=p.name;report['parts'][n]['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
report['total_solid_mass_g']=report['parts']['top']['solid_mass_g']+2*report['parts']['support']['solid_mass_g']+report['parts']['brace']['solid_mass_g']+4*report['parts']['foot_left']['solid_mass_g']
(OUT/'geometry_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
# Export multipart visual reference as GLB, with materials per component; not a print file.
scene=tm.Scene()
colors={'top':[181,192,204,255],'support_L':[99,116,136,255],'support_R':[99,116,136,255],'rear_brace':[74,127,167,255]}
for n,s in assembly.items():
 m=mesh(s);m.visual.face_colors=colors.get(n,[205,134,87,255]);scene.add_geometry(m,node_name=n,geom_name=n)
scene.export(OUT/'V7_assembly_REFERENCE.glb')

subprocess.run([sys.executable,str(ROOT/"structural_screen.py")],check=True)
subprocess.run([sys.executable,str(ROOT/"render_views.py")],check=True)
print("V7 default geometry checks passed; physical joint and load tests remain required.")
