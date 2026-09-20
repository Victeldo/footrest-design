"""Linear beam-grillage screening, NOT a solid FEA or validated load rating.
N, mm, MPa. Solid sections, perfect joints, small deflections, no creep.
"""
import numpy as np,json
from pathlib import Path
OUT=Path(__file__).resolve().parent
def rectJ(a,b):
 a,b=max(a,b),min(a,b)
 return a*b**3*(1/3-.21*(b/a)*(1-b**4/(12*a**4)))
def section(width,web,depth,skin=2.4):
 areas=np.array([width*skin,web*(depth-skin)])
 z=np.array([skin/2,(skin+depth)/2]); c=np.dot(areas,z)/sum(areas)
 I=width*skin**3/12+web*(depth-skin)**3/12+sum(areas*(z-c)**2)
 J=rectJ(width,skin)+rectJ(web,depth-skin)
 return I,J,c,max(c,depth-c)
def addbeam(K,xy,i,j,E,I,J,nu=.35):
 d=xy[j]-xy[i];L=np.linalg.norm(d);dx,dy=d/L
 # w along global z; slope along beam = dy*theta_x - dx*theta_y.
 T=np.zeros((6,6));T[0,0]=1;T[1,1:3]=[dy,-dx];T[2,1:3]=[dx,dy]
 T[3,3]=1;T[4,4:6]=[dy,-dx];T[5,4:6]=[dx,dy]
 kb=E*I/L**3*np.array([[12,6*L,-12,6*L],[6*L,4*L*L,-6*L,2*L*L],[-12,-6*L,12,-6*L],[6*L,2*L*L,-6*L,4*L*L]])
 kl=np.zeros((6,6));idx=[0,1,3,4];kl[np.ix_(idx,idx)]=kb
 kl[np.ix_([2,5],[2,5])]=E/(2*(1+nu))*J/L*np.array([[1,-1],[-1,1]])
 kg=T.T@kl@T; dofs=[3*i,3*i+1,3*i+2,3*j,3*j+1,3*j+2]
 K[np.ix_(dofs,dofs)]+=kg
 return dict(dofs=dofs,T=T,kb=kb,idx=idx,L=L,I=I)
def solve(K,F,fixed):
 free=np.setdiff1d(np.arange(len(F)),fixed); u=np.zeros(len(F));u[free]=np.linalg.solve(K[np.ix_(free,free)],F[free]);return u,K@u-F
xs=np.array([1.5,22,71,120,169,218,238.5]);ys=np.array([1.5,49,85,121,168.5]);xy=np.array([[x,y] for y in ys for x in xs]); nx=len(xs)
xb=np.r_[0,(xs[:-1]+xs[1:])/2,240];yb=np.r_[0,(ys[:-1]+ys[1:])/2,170]
def loadpoint(F,x,y,P):
 ix=max(0,min(len(xs)-2,np.searchsorted(xs,x)-1));iy=max(0,min(len(ys)-2,np.searchsorted(ys,y)-1))
 a=(x-xs[ix])/(xs[ix+1]-xs[ix]);b=(y-ys[iy])/(ys[iy+1]-ys[iy])
 for i,j,w in [(ix,iy,(1-a)*(1-b)),(ix+1,iy,a*(1-b)),(ix,iy+1,(1-a)*b),(ix+1,iy+1,a*b)]: F[3*(j*nx+i)]-=P*w

def toppass(E):
 K=np.zeros((3*len(xy),)*2);members=[]
 for j,y in enumerate(ys):
  I,J,c,ext=section(yb[j+1]-yb[j],3 if j in [0,4] else 5,10 if j in [0,4] else 16)
  for i in range(nx-1):
   m=addbeam(K,xy,j*nx+i,j*nx+i+1,E,I,J);m['ext']=ext;members.append(m)
 for i,x in enumerate(xs):
  I,J,c,ext=section(xb[i+1]-xb[i],3 if i in [0,6] else 3.6,10)
  for j in range(len(ys)-1):
   m=addbeam(K,xy,j*nx+i,(j+1)*nx+i,E,I,J);m['ext']=ext;members.append(m)
 fixed=[3*(j*nx+i) for i in [1,5] for j in [1,2,3]]
 cases={}
 for case in ['center_point_200N','center_patch_200N','two_heel_patches_total_200N','single_offset_patch_200N']:
  F=np.zeros(len(K))
  if case=='center_point_200N':loadpoint(F,120,85,200)
  else:
   patches={'center_patch_200N':[(120,85,200)],'two_heel_patches_total_200N':[(60,85,100),(180,85,100)],'single_offset_patch_200N':[(60,55,200)]}[case]
   for cx,cy,P in patches:
    for x in np.linspace(cx-20,cx+20,9):
     for y in np.linspace(cy-20,cy+20,9):loadpoint(F,x,y,P/81)
  u,R=solve(K,F,fixed);stress=[]
  for m in members:
   q=(m['T']@u[m['dofs']])[m['idx']];f=m['kb']@q
   stress.append(max(abs(f[1]),abs(f[3]))*m['ext']/m['I'])
  assert abs(sum(R[::3])-200)<1e-6
  cases[case]={'max_deflection_mm':float(-min(u[::3])),'peak_nominal_beam_stress_MPa':float(max(stress)),
   'vertical_reactions_N':[float(R[i]) for i in fixed],'min_reaction_N':float(min(R[fixed]))}
 return cases
# Bare side frame out-of-plane screen: frame centerlines and X crossing.
# Both bottom corners fully fixed (optimistic). A rigid top distributes total
# 20 N lateral force as 10 N per panel. Does NOT include actual compliant feet.
H=223.;nodes=np.array([[5,5],[145,5],[145,H-5],[5,H-5],[75,H/2]])
def framesway(E):
 K=np.zeros((15,15));F=np.zeros(15)
 for i,j,b in [(0,1,10),(1,2,10),(2,3,10),(3,0,10),(0,4,8),(4,2,8),(1,4,8),(4,3,8)]:
  addbeam(K,nodes,i,j,E,b*7**3/12,rectJ(b,7))
 F[6]=F[9]=5
 u,R=solve(K,F,list(range(6)))
 return {'top_sway_mm_at_10N_per_panel_fixed_feet':float((u[6]+u[9])/2)}
# Verify beam element with classical center-load simply-supported beam.
a=np.array([[0.,0.],[98.,0.],[196.,0.]]);K=np.zeros((9,9));F=np.zeros(9);E=1500.;I=1000.
addbeam(K,a,0,1,E,I,500);addbeam(K,a,1,2,E,I,500);F[3]=-200
u,R=solve(K,F,[0,6,1,4,7]);expected=200*196**3/(48*E*I)
assert abs(-u[3]-expected)<1e-8
report={'scope':'Approximate linear beam grillage, not solid FEA. Solid skins/webs, ideal joints and fixed vertical support points; ignores creep, local stress concentrations, layer defects, and foot compliance.',
 'assumed_E_MPa':[1500,2500], 'load_N':200,'measured_user_load_lbf':25.6,'measured_user_load_N':25.6*4.4482216152605,
 'top':{str(E):toppass(E) for E in [1500,2500]},'lateral_frame_screen':{str(E):framesway(E) for E in [1500,2500]},
 'solver_check':{'calculated_mm':float(-u[3]),'classical_mm':expected}}
(OUT/'structural_screen.json').write_text(json.dumps(report,indent=2))
# Rear X-brace screen. Both diagonals engaged, ideal end joints, no clearance.
L=float(np.hypot(196,160));cosine=196/L;A=8*6;Iweak=8*6**3/12;Hforce=20
report['rear_brace_screen']={}
for E in [1500,2500]:
 k=2*E*A/L*cosine**2
 report['rear_brace_screen'][str(E)]={'horizontal_check_load_N':Hforce,'ideal_diagonal_extension_sway_mm':Hforce/k,
  'diagonal_axial_force_N':Hforce/(2*cosine),'nominal_axial_stress_MPa':Hforce/(2*cosine)/A,
  'pinned_full_length_Euler_buckling_N':np.pi**2*E*Iweak/L**2,
  'limitations':'Assumes solid 8x6 members, straight columns, pinned ends, both diagonals engaged. Does not credit fused X crossing as a brace. Joint clearance, upper/lower frame extensions, contact slip, and foot compliance omitted. Not full assembly sway.'}
# Bare rail and local flanged-section comparisons; no global buckling claim.
a=np.array([10*7,6*3]);z=np.array([3.5,8.5]);zc=float(a@z/sum(a));Ifc=10*7**3/12+6*3**3/12+float(np.sum(a*(z-zc)**2))
report['rail_section_screen']={'original_weak_axis_I_mm4':10*7**3/12,'flanged_weak_axis_I_mm4':Ifc,'ratio':Ifc/(10*7**3/12),
 'limitations':'Local solid section only. Tapers, corner restraint and load sharing affect actual panel buckling. No global buckling rating.'}
report['lateral_frame_screen']['note']='This is the unbraced V5-style frame, BEFORE rail flanges or rear X-brace. Large predicted motion is a warning, not a valid large-deflection prediction.'
(OUT/'structural_screen.json').write_text(json.dumps(report,indent=2))
