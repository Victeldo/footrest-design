from pathlib import Path
import sys, json, hashlib
import numpy as np
import trimesh as tm
import manifold3d as md
ROOT=Path(__file__).resolve().parent
OUT=ROOT; SRC=ROOT/'reference'
(ROOT/'work').mkdir(exist_ok=True)
import os
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'work/mpl'))
def load(p):
 m=tm.load_mesh(p)
 return md.Manifold(md.Mesh(np.array(m.vertices,dtype=np.float32),np.array(m.faces,dtype=np.uint32)))
def mesh(s):
 m=s.to_mesh();return tm.Trimesh(vertices=m.vert_properties[:,:3],faces=m.tri_verts,process=True)
def box(a,b):return md.Manifold.cube(np.array(b)-a).translate(a)
def yzpoly(points,x0,x1):
 return md.Manifold.hull_points([[x,y,z] for x in [x0,x1] for y,z in points])
def xypoly(points,z0,z1):
 return md.CrossSection([points]).extrude(z1-z0).translate([0,0,z0])
def stats(s):
 m=mesh(s)
 return dict(volume_mm3=float(m.volume),bounds_mm=m.bounds.tolist(),extent_mm=m.extents.tolist(),watertight=bool(m.is_watertight),winding_consistent=bool(m.is_winding_consistent),components=len(m.split(only_watertight=False)),triangles=len(m.faces))
def check(s):
 d=stats(s);assert d['watertight'] and d['winding_consistent'] and d['components']==1 and s.volume()>0,d
 return d
base=load(SRC/'flatpack_footrest_v5_light_support.stl')
# Local coordinates match support: x along rail, y up, z thickness.
# Embedded root (z=6.8) ensures a volumetric union, no touching-only shells.
catch=(yzpoly([(3,6.8),(11.25,6.8),(11.25,9.2),(5.2,9.2),(3,7)],9,19) ^ xypoly([(9,3),(19,3),(19,7.25),(15,11.25),(13,11.25),(9,7.25)],6.7,10))
right=catch.mirror([1,0,0]).translate([150,0,0])
support=base+catch+right
coupon=support ^ box([0,0,0],[32,22,12])
# Roof of latch opening rises at 45 degrees to a 2 mm bridge.
window_pts=[(8.75,2.75),(19.25,2.75),(19.25,7.25),(15,11.5),(13,11.5),(8.75,7.25)]
window=xypoly(window_pts,7,10)
foot=(box([-1.8,-2,-2.05],[28,0,9.05])+
      box([-1.8,-.1,-2.05],[28,9,-.25])+
      box([-1.8,-.1,7.25],[28,14,9.05])+
      box([-1.8,-.1,-2.05],[-.25,9,9.05]))-window
foot_r=foot.mirror([1,0,0]).translate([150,0,0])
# Proper rotation: sole on bed, local x unchanged, z thickness -> -print y.
print_transform=np.array([[1,0,0,1.8],[0,0,-1,9.05],[0,1,0,2]])
foot_print=foot.transform(print_transform)
# Foot reflection is done only for full-assembly checking. Coupon tests same connector.
report={'baseline':{},'new':{},'checks':{}}
for p in SRC.glob('*.stl'):
 m=tm.load_mesh(p)
 report['baseline'][p.name]={'watertight':bool(m.is_watertight),'components':len(m.split(only_watertight=False)),'volume_mm3':float(m.volume),'bounds_mm':m.bounds.tolist(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
for n,s in [('support',support),('coupon',coupon),('foot',foot),('foot_print',foot_print)]:report['new'][n]=check(s)
c=report['checks']
c['original_material_removed_mm3']=(base-support).volume()
c['added_material_mm3']=(support-base).volume()
c['foot_support_intersection_mm3']=(foot^support).volume()
c['right_foot_support_intersection_mm3']=(foot_r^support).volume()
c['feet_intersection_mm3']=(foot^foot_r).volume()
c['coupon_foot_intersection_mm3']=(coupon^foot).volume()
c['tab_symmetric_difference_mm3']=((support^box([0,234,-1],[150,242,12]))-(base^box([0,234,-1],[150,242,12]))).volume()
# Zero-fit overlap; then collision when trying each removal direction as rigid objects.
c['rigid_motion_collision_mm3']={}
for label,delta in [('down_1mm',[0,-1,0]),('along_rail_plus_1mm',[1,0,0]),('along_rail_minus_1mm',[-1,0,0]),('across_plus_1mm',[0,0,1]),('across_minus_1mm',[0,0,-1])]:
 c['rigid_motion_collision_mm3'][label]=(foot.translate(delta)^support).volume()
# Nominal insertion path: report intentional elastic interference, not a clash-free claim.
c['insertion_rigid_overlap_mm3']={str(d):(foot.translate([0,-d,0])^support).volume() for d in [0,1,2,4,6,8,10,12,14]}
# Assembly with original V3 placement, no redesign. Exact transformation R: (x,y,z)->(z,x,y).
M=np.array([[0,0,1,22.5],[1,0,0,10],[0,1,0,0]],float)
left=support.transform(M); M2=M.copy();M2[0,3]=200.5;right_support=support.transform(M2)
top=load(SRC/'flatpack_footrest_v3_top.stl').translate([0,0,236])
c['top_support_intersection_mm3']=(top^left).volume()+(top^right_support).volume()
c['support_to_support_intersection_mm3']=(left^right_support).volume()
c['assembled_uncompressed_height_mm']=243
c['sole_thickness_mm']=2
assert c['original_material_removed_mm3']<1e-5
for k in ['foot_support_intersection_mm3','right_foot_support_intersection_mm3','feet_intersection_mm3','coupon_foot_intersection_mm3','top_support_intersection_mm3','support_to_support_intersection_mm3']:assert abs(c[k])<1e-5,(k,c[k])
assert all(v>0 for v in c['rigid_motion_collision_mm3'].values())
# Exports only after all solid-level validations pass; then reload STL for a second check.
for filename,s in [('V6A_PLA_corner_coupon.stl',coupon),('V6A_TPU95A_test_foot.stl',foot_print)]:
 p=OUT/filename;mesh(s).export(p); reloaded=load(p);check(reloaded)
 assert abs(reloaded.volume()-s.volume())<.01
# Full support is retained as a working validation mesh, not released for full printing.
mesh(support).export(ROOT/'work/support_reference.stl')
report['new']['coupon']['solid_PLA_mass_g_at_1p24']=coupon.volume()/1000*1.24
report['new']['foot']['solid_TPU_mass_g_at_assumed_1p20']=foot.volume()/1000*1.20
(OUT/'geometry_checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report['new'],indent=2));print(json.dumps(c,indent=2))
# Diagnostic figure in true geometric coordinates, not an AI illustration.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig=plt.figure(figsize=(13,8),facecolor='white')
def draw(ax,s,color,alpha=1):
 m=mesh(s); from matplotlib.colors import to_rgb; light=np.array([.2,-.5,1.0]);light=light/np.linalg.norm(light); shade=.65+.35*np.maximum(0,m.face_normals@light); colors=np.array(to_rgb(color))[None,:]*shade[:,None]; pc=Poly3DCollection(m.triangles,facecolor=colors,edgecolor='none',alpha=alpha);ax.add_collection3d(pc)
def setup(ax,bounds,title):
 a,b=np.array(bounds);ax.set_xlim(a[0],b[0]);ax.set_ylim(a[1],b[1]);ax.set_zlim(a[2],b[2]);ax.set_box_aspect(b-a);ax.view_init(elev=24,azim=-58);ax.set_title(title,loc='left',fontsize=12);ax.set_xlabel('Along rail');ax.set_ylabel('Height');ax.set_zlabel('Thickness')
a=fig.add_subplot(221,projection='3d');draw(a,coupon,'#b3bcc4');setup(a,[[0,-2,-2.05],[32,22,12]],'PLA corner: added ramp catch, intact rail')
a=fig.add_subplot(222,projection='3d');draw(a,foot,'#cf8758');setup(a,[[-2,-2,-2.05],[32,22,12]],'TPU shoe: end stop and roofed capture window')
a=fig.add_subplot(223,projection='3d');draw(a,coupon,'#b3bcc4');draw(a,foot,'#cf8758',.8);setup(a,[[-2,-2,-2.05],[32,22,12]],'Seated pair: zero solid overlap')
a=fig.add_subplot(224)
# section at x=9.1, near edge where roof catches shoulder
for s,col in [(coupon,'#b3bcc4'),(foot,'#cf8758')]:
 section=mesh(s).section(plane_origin=[9.1,0,0],plane_normal=[1,0,0])
 for line in section.discrete:a.fill(line[:,2],line[:,1],color=col,alpha=.9)
a.set_aspect('equal');a.set_xlim(-3,11);a.set_ylim(-3,16);a.set_xlabel('Support thickness direction (mm)');a.set_ylabel('Height above PLA bottom (mm)');a.set_title('Section near catch edge (x = 9.1 mm)',loc='left',fontsize=12);a.grid(alpha=.15)
a.annotate('2 mm sole',xy=(3.5,-1),xytext=(-2,2),arrowprops={'arrowstyle':'->'},fontsize=9)
a.annotate('Retaining shoulder',xy=(8.3,7),xytext=(-2,12),arrowprops={'arrowstyle':'->'},fontsize=9)
fig.suptitle('V6A / coupon-stage retained foot — dimensions in mm',fontsize=17,x=.04,ha='left');fig.tight_layout(rect=[0,0,1,.95]);fig.savefig(OUT/'V6A_interface_review.png',dpi=180)
