# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:56:43 2020

@author: Andrés Jaramillo
"""
# Andrés Felipe Jaramillo Pabón - 201713473

# Libraries


import itertools
import matplotlib.pyplot as plt 
from matplotlib import cm
from scipy.interpolate import griddata
from scipy.stats import linregress
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math
from scipy.spatial import ConvexHull
from PIL import Image
import matplotlib.patches as mpatches

NumNodes=19
NumReservoirs=1
NumPipes=42

NodesID=[2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20]

NodesX=[1407.77,
873.79,
809.06,
792.88,
987.05,
1197.41,
1747.57,
2702.27,
2038.83,
3673.14,
3996.76,
4110.03,
3867.31,
3042.07,
4255.66,
1132.69,
5906.15,
7944.98,
5339.81]

NodesY=[8608.41,
7702.27,
6893.2,
6019.42,
5210.36,
4207.12,
3559.87,
2718.45,
1779.94,
3721.68,
5000,
6569.58,
7847.9,
8883.5,
1731.39,
663.43,
5048.54,
5113.27,
3220.06]

NodesZ=[0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0]

NodesHGL=[89.0418,
85.8067,
84.8956,
84.1277,
83.0636,
81.5456,
80.7367,
79.5327,
79.043,
80.3074,
82.1133,
83.3355,
86.3364,
89.4054,
77.7777,
77.7382,
79.26,
77.7763,
79.1516]

Nodes=list()

for i in range(NumNodes):
    Var=dict()
    Var['ID']=NodesID[i]
    Var['X']=NodesX[i]
    Var['Y']=NodesY[i]
    Var['Z']=NodesZ[i]
    Var['HGL']=NodesHGL[i]
    Nodes.append(Var)

ReservoirsID=[1]
ReservoirsX=[1957.93]
ReservoirsY=[9449.84]
ReservoirsZ=[91.44]
ReservoirsHGL=[91.44]

Reservoirs=list()

for i in range(NumReservoirs):
    Var=dict()
    Var['ID']=ReservoirsID[i]
    Var['X']=ReservoirsX[i]
    Var['Y']=ReservoirsY[i]
    Var['Z']=ReservoirsZ[i]
    Var['HGL']=ReservoirsHGL[i]
    Reservoirs.append(Var)

PipesID=[1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42]

PipesNI=[1,
2,
3,
4,
5,
6,
7,
8,
9,
11,
12,
13,
14,
15,
1,
10,
12,
18,
11,
20,
9,
1,
2,
3,
4,
5,
6,
7,
8,
9,
11,
12,
13,
14,
15,
1,
10,
12,
18,
11,
20,
9]

PipesNF=[2,
3,
4,
5,
6,
7,
8,
9,
10,
9,
11,
12,
13,
14,
15,
17,
18,
19,
20,
16,
16,
2,
3,
4,
5,
6,
7,
8,
9,
10,
9,
11,
12,
13,
14,
15,
17,
18,
19,
20,
16,
16]

Pipes=list()

for i in range(NumPipes):
    Var=dict()
    Var['ID']=PipesID[i]
    Var['NI']=PipesNI[i]
    Var['NF']=PipesNF[i]
    Pipes.append(Var)

    
NodesX=list()
NodesY=list()
NodesZ=list()

for i in range(len(Reservoirs)):
    NodesX.append(Reservoirs[i]['X'])
    NodesY.append(Reservoirs[i]['Y'])
    NodesZ.append(Reservoirs[i]['Z'])
    
for i in range(len(Nodes)):
    NodesX.append(Nodes[i]['X'])
    NodesY.append(Nodes[i]['Y'])
    NodesZ.append(Nodes[i]['Z'])
    
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax1 = fig.add_subplot(1, 2, 2, projection='3d')
fig.set_size_inches(15, 8)
ax.scatter(NodesX, NodesY, NodesZ, c='black', marker='o', alpha=1)
ax1.scatter(NodesX, NodesY, NodesZ, c='black', marker='o', alpha=1)

for i in range(len(Pipes)):
    NI=Pipes[i]['NI']
    NF=Pipes[i]['NF']
    X=list()
    Y=list()
    Z=list()
    v=None
    for i in range(len(Reservoirs)):
        v=Reservoirs[i]['ID']
        if v==NI:
            X.append(Reservoirs[i]['X'])
            Y.append(Reservoirs[i]['Y'])
            Z.append(Reservoirs[i]['Z'])
            break
    for i in range(len(Nodes)):
        v=Nodes[i]['ID']
        if v==NI:
            X.append(Nodes[i]['X'])
            Y.append(Nodes[i]['Y'])
            Z.append(Nodes[i]['Z'])
            break
    for i in range(len(Reservoirs)):
        v=Reservoirs[i]['ID']
        if v==NF:
            X.append(Reservoirs[i]['X'])
            Y.append(Reservoirs[i]['Y'])
            Z.append(Reservoirs[i]['Z'])
            break
    for i in range(len(Nodes)):
        v=Nodes[i]['ID']
        if v==NF:
            X.append(Nodes[i]['X'])
            Y.append(Nodes[i]['Y'])
            Z.append(Nodes[i]['Z'])
            break
    ax.plot(X,Y,Z,color='darkblue') 
    ax1.plot(X,Y,Z,color='darkblue')
    
# 3. Hydraulic Gradient Surface

HGLX=list()
HGLY=list()
HGLZ=list()

for i in range(len(Pipes)):
    NI=Pipes[i]['NI']
    NF=Pipes[i]['NF']
    for i in range(len(Reservoirs)):
        v=Reservoirs[i]['ID']
        if v==NI:
            Xo=Reservoirs[i]['X']
            Yo=Reservoirs[i]['Y']
            Zo=Reservoirs[i]['HGL']
            HGLX.append(Xo)
            HGLY.append(Yo)
            HGLZ.append(Zo)
            break
    for i in range(len(Nodes)):
        v=Nodes[i]['ID']
        if v==NI:
            Xo=Nodes[i]['X']
            Yo=Nodes[i]['Y']
            Zo=Nodes[i]['HGL']
            HGLX.append(Xo)
            HGLY.append(Yo)
            HGLZ.append(Zo)
            break
    for i in range(len(Reservoirs)):
        v=Reservoirs[i]['ID']
        if v==NF:
            Xf=Reservoirs[i]['X']
            Yf=Reservoirs[i]['Y']
            Zf=Reservoirs[i]['HGL']
            HGLX.append(Xf)
            HGLY.append(Yf)
            HGLZ.append(Zf)
            break
    for i in range(len(Nodes)):
        v=Nodes[i]['ID']
        if v==NF:
            Xf=Nodes[i]['X']
            Yf=Nodes[i]['Y']
            Zf=Nodes[i]['HGL']
            HGLX.append(Xf)
            HGLY.append(Yf)
            HGLZ.append(Zf)
            break 
    for i in range(10):
        HGLX.append(Xo+(i/10)*(Xf-Xo))
        HGLY.append(Yo+(i/10)*(Yf-Yo))
        HGLZ.append(Zo+(i/10)*(Zf-Zo))

Xmax=max(HGLX)
Ymax=max(HGLY)
Xmin=min(HGLX)
Ymin=min(HGLY)


grid_x , grid_y=np.mgrid[Xmin:Xmax:50,Ymin:Ymax:50]

HGLInt1=griddata((HGLX,HGLY),HGLZ,(grid_x,grid_y),method='linear')
HGLInt2=np.nan_to_num(HGLInt1, copy=True, nan=0.0, posinf=None, neginf=None)
surf=ax.plot_surface(grid_x,grid_y,HGLInt1,cmap=cm.YlOrRd,vmin=np.nanmin(HGLInt1), vmax=np.nanmax(HGLInt1),rcount=200, ccount=200)

Nodes1ID=[2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20]

Nodes1X=[1407.77,
873.79,
809.06,
792.88,
987.05,
1197.41,
1747.57,
2702.27,
2038.83,
3673.14,
3996.76,
4110.03,
3867.31,
3042.07,
4255.66,
1132.69,
5906.15,
7944.98,
5339.81]

Nodes1Y=[8608.41,
7702.27,
6893.2,
6019.42,
5210.36,
4207.12,
3559.87,
2718.45,
1779.94,
3721.68,
5000,
6569.58,
7847.9,
8883.5,
1731.39,
663.43,
5048.54,
5113.27,
3220.06]

Nodes1Z=[0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0]

Nodes1HGL=[90.5255,
90.1349,
89.8995,
89.0117,
88.9633,
87.3874,
87.278,
80.3987,
80.3949,
80.3999,
83.1882,
83.3577,
88.2375,
88.6895,
80.3074,
80.3899,
83.0884,
82.9443,
80.3355]

Nodes1=list()

for i in range(NumNodes):
    Var=dict()
    Var['ID']=Nodes1ID[i]
    Var['X']=Nodes1X[i]
    Var['Y']=Nodes1Y[i]
    Var['Z']=Nodes1Z[i]
    Var['HGL']=Nodes1HGL[i]
    Nodes1.append(Var)

Reservoirs1ID=[1]
Reservoirs1X=[1957.93]
Reservoirs1Y=[9449.84]
Reservoirs1Z=[91.44]
Reservoirs1HGL=[91.44]

Reservoirs1=list()

for i in range(NumReservoirs):
    Var=dict()
    Var['ID']=Reservoirs1ID[i]
    Var['X']=Reservoirs1X[i]
    Var['Y']=Reservoirs1Y[i]
    Var['Z']=Reservoirs1Z[i]
    Var['HGL']=Reservoirs1HGL[i]
    Reservoirs1.append(Var)

HGLX1=list()
HGLY1=list()
HGLZ1=list()

for i in range(len(Pipes)):
    NI=Pipes[i]['NI']
    NF=Pipes[i]['NF']
    for i in range(len(Reservoirs1)):
        v=Reservoirs1[i]['ID']
        if v==NI:
            Xo=Reservoirs1[i]['X']
            Yo=Reservoirs1[i]['Y']
            Zo=Reservoirs1[i]['HGL']
            HGLX1.append(Xo)
            HGLY1.append(Yo)
            HGLZ1.append(Zo)
            break
    for i in range(len(Nodes1)):
        v=Nodes1[i]['ID']
        if v==NI:
            Xo=Nodes1[i]['X']
            Yo=Nodes1[i]['Y']
            Zo=Nodes1[i]['HGL']
            HGLX1.append(Xo)
            HGLY1.append(Yo)
            HGLZ1.append(Zo)
            break
    for i in range(len(Reservoirs1)):
        v=Reservoirs[i]['ID']
        if v==NF:
            Xf=Reservoirs1[i]['X']
            Yf=Reservoirs1[i]['Y']
            Zf=Reservoirs1[i]['HGL']
            HGLX1.append(Xf)
            HGLY1.append(Yf)
            HGLZ1.append(Zf)
            break
    for i in range(len(Nodes1)):
        v=Nodes[i]['ID']
        if v==NF:
            Xf=Nodes1[i]['X']
            Yf=Nodes1[i]['Y']
            Zf=Nodes1[i]['HGL']
            HGLX1.append(Xf)
            HGLY1.append(Yf)
            HGLZ1.append(Zf)
            break 
    for i in range(10):
        HGLX1.append(Xo+(i/10)*(Xf-Xo))
        HGLY1.append(Yo+(i/10)*(Yf-Yo))
        HGLZ1.append(Zo+(i/10)*(Zf-Zo))

Xmax1=max(HGLX1)
Ymax1=max(HGLY1)
Xmin1=min(HGLX1)
Ymin1=min(HGLY1)

# Please specify desired step size
# Step size must be equal in both sides

grid_x1 , grid_y1=np.mgrid[Xmin1:Xmax1:50,Ymin1:Ymax1:50]

HGLInt11=griddata((HGLX1,HGLY1),HGLZ1,(grid_x1,grid_y1),method='linear')
HGLInt21=np.nan_to_num(HGLInt11, copy=True, nan=0.0, posinf=None, neginf=None)
surf1=ax1.plot_surface(grid_x1,grid_y1,HGLInt11,cmap=cm.YlOrRd,vmin=np.nanmin(HGLInt11), vmax=np.nanmax(HGLInt11),rcount=200, ccount=200)

#cbaxes = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cbar=plt.colorbar(surf,ax=ax,shrink=0.5)
cbar.set_label('HGS [m]', labelpad=-40, y=1.05, rotation=0,fontsize=12)
cbar.ax.tick_params(labelsize=12)
cbar1=plt.colorbar(surf1,ax=ax1,shrink=0.5)
cbar1.set_label('HGS [m]', labelpad=-40, y=1.05, rotation=0,fontsize=12)
cbar1.ax.tick_params(labelsize=12)

#fig.tight_layout()


# Please specify rotation (elevation angle, azimuth angle)
# Delete # symbol before ax.view_init to allow Python to run the instruction

ax.view_init(30,325)
ax1.view_init(30,325)

ax.set_xlim(Xmin,Xmax)
ax.set_ylim(Ymin,Ymax)
ax.set_xlabel('X [m]',fontsize=12,labelpad=20)
ax.set_ylabel('Y [m]',fontsize=12,labelpad=20)
ax.set_zlabel('Z [m]',fontsize=12,labelpad=20)

ax.tick_params(axis='both', which='major', labelsize=12,direction='out')

ax1.set_xlim(Xmin1,Xmax1)
ax1.set_ylim(Ymin1,Ymax1)
ax1.set_xlabel('X [m]',fontsize=12,labelpad=20)
ax1.set_ylabel('Y [m]',fontsize=12,labelpad=20)
ax1.set_zlabel('Z [m]',fontsize=12,labelpad=20)

ax1.tick_params(axis='both', which='major', labelsize=12,direction='out')

ax.set_title('(a)')
ax1.set_title('(b)')
#fig.subplots_adjust(top=0.95)
plt.tight_layout()
plt.savefig('Fig_10.pdf', dpi=600,bbox_inches='tight')



