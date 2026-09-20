# Orthographic depth-buffer renderer for actual STL triangles; no painter-order artifacts.
from pathlib import Path
import numpy as np,trimesh as tm
from PIL import Image
import os;os.environ['MPLCONFIGDIR']=str(Path(__file__).resolve().parent/'work/mpl')
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent;W=OUT/'work'
def m(n,M=None):
 q=tm.load_mesh(W/(n+'.stl'))
 if M is not None:q.apply_transform(M)
 return q
mt=np.array([[1,0,0,0],[0,-1,0,170],[0,0,-1,241],[0,0,0,1]],float)
mb=np.array([[1,0,0,13.55],[0,0,-1,174],[0,1,0,27],[0,0,0,1]],float)
ml=np.array([[0,0,1,18.5],[1,0,0,10],[0,1,0,2],[0,0,0,1]],float);mr=ml.copy();mr[0,3]=214.5
mf=np.array([[1,0,0,-1.8],[0,0,1,-2],[0,-1,0,9.05],[0,0,0,1]],float)
flip=np.array([[-1,0,0,150],[0,1,0,0],[0,0,1,0],[0,0,0,1]],float)
colors={'top':np.array([185,195,205]),'support':np.array([112,128,145]),'brace':np.array([84,143,181]),'foot':np.array([211,141,94])}
assembly=[(m('top',mt),colors['top']),(m('support',ml),colors['support']),(m('support',mr),colors['support']),(m('brace',mb),colors['brace'])]
for M in [ml,mr]:
 for F in [mf,flip@mf]:assembly.append((m('foot_left',M@F),colors['foot']))
def render(items,az,el,width=950,height=680):
 az,el=np.deg2rad([az,el]);d=np.array([np.cos(el)*np.cos(az),np.cos(el)*np.sin(az),np.sin(el)])
 right=np.cross([0,0,1],d);right/=np.linalg.norm(right);up=np.cross(d,right);R=np.array([right,up,d]).T
 allv=np.concatenate([q.vertices@R for q,c in items]);lo=allv[:,:2].min(0);hi=allv[:,:2].max(0)
 scale=min((width-40)/(hi[0]-lo[0]),(height-40)/(hi[1]-lo[1]));center=(hi+lo)/2
 zbuf=np.full((height,width),-np.inf);pix=np.full((height,width,3),255,dtype=np.uint8)
 light=d+np.array([-.3,-.1,.8]);light/=np.linalg.norm(light)
 for q,col in items:
  v=q.vertices@R;v[:,0]=(v[:,0]-center[0])*scale+width/2;v[:,1]=height/2-(v[:,1]-center[1])*scale
  for idx,f in enumerate(q.faces):
   a,b,c=v[f];den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
   if abs(den)<1e-8:continue
   x0=max(0,int(np.floor(min(a[0],b[0],c[0]))));x1=min(width-1,int(np.ceil(max(a[0],b[0],c[0]))))
   y0=max(0,int(np.floor(min(a[1],b[1],c[1]))));y1=min(height-1,int(np.ceil(max(a[1],b[1],c[1]))))
   if x1<x0 or y1<y0:continue
   yy,xx=np.mgrid[y0:y1+1,x0:x1+1];xx=xx+.5;yy=yy+.5
   wa=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/den
   wb=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/den;wc=1-wa-wb
   depth=wa*a[2]+wb*b[2]+wc*c[2];old=zbuf[y0:y1+1,x0:x1+1]
   take=(wa>=-1e-7)&(wb>=-1e-7)&(wc>=-1e-7)&(depth>old)
   old[take]=depth[take];shade=.55+.45*max(0,float(q.face_normals[idx]@light))
   pix[y0:y1+1,x0:x1+1][take]=np.clip(col*shade,0,255).astype(np.uint8)
 return pix
fig,axes=plt.subplots(2,2,figsize=(13,9),facecolor='white')
views=[(assembly,55,24,'Assembled • 240 × 174 × 241 mm'),([(m('top'),colors['top'])],-60,55,'Underside • ribs and connected socket bosses'),([(m('support'),colors['support'])],-65,68,'Support • raised rail flanges and brace sockets'),([(m('brace'),colors['brace'])],-65,68,'Removable rear X-brace • flat printable part')]
for ax,(items,az,el,title) in zip(axes.flat,views):ax.imshow(render(items,az,el));ax.axis('off');ax.set_title(title,loc='left',fontsize=12)
fig.suptitle('V7 • geometry-checked prototype / test the two new joints first',x=.04,ha='left',fontsize=17);fig.tight_layout(rect=[0,0,1,.95]);fig.savefig(OUT/'V7_design_review.png',dpi=180)
# Clear two coupon assembly images with matching coordinate transforms.
mc=np.array([[0,0,1,7.5],[-1,0,0,34],[0,-1,0,26],[0,0,0,1]],float)
mbc=np.array([[0,0,-1,19],[0,1,0,0],[1,0,0,-4.95],[0,0,0,1]],float)
fig,axes=plt.subplots(1,2,figsize=(11,5),facecolor='white')
for ax,items,title in [(axes[0],[(m('socket_coupon'),colors['top']),(m('tab_coupon',mc),colors['support'])],'Top joint • tab + shoulder guides'),(axes[1],[(m('brace_socket_coupon'),colors['support']),(m('brace_tab_coupon',mbc),colors['brace'])],'Rear-brace joint • insertion from the rear')]:
 ax.imshow(render(items,-50,30));ax.axis('off');ax.set_title(title,loc='left',fontsize=12)
fig.tight_layout();fig.savefig(OUT/'V7_coupon_assemblies.png',dpi=160)
