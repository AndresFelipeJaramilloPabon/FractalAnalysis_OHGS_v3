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


NumNodes=39
NumReservoirs=1
NumPipes=67

NodesID=[1,
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
39]

NodesX=[0,
0,
0,
0,
0,
100,
100,
100,
100,
100,
300,
300,
300,
300,
300,
480,
480,
480,
480,
480,
700,
700,
700,
700,
900,
900,
900,
900,
900,
1080,
1080,
1080,
1080,
1080,
1230,
1230,
1230,
1230,
1230]

NodesY=[0,
80,
230,
330,
450,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
450,
330,
230,
80,
0]

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
0,
0,
0,
0]

NodesHGL=[20.18713,
20.12976,
20.15113,
20.33414,
20.36742,
22.50031,
26.10804,
25.38205,
23.88703,
21.8102,
20.00159,
20.33775,
21.47659,
28.97863,
22.67911,
35.05286,
33.17194,
27.78337,
24.92695,
21.07314,
27.58988,
28.71969,
33.02515,
35.21624,
34.53811,
32.95787,
25.04035,
20.52469,
20.44678,
22.9626,
25.22489,
26.96626,
30.05166,
23.24804,
21.95694,
23.59581,
21.25581,
21.67803,
21.50141]

Nodes=list()

for i in range(NumNodes):
    Var=dict()
    Var['ID']=NodesID[i]
    Var['X']=NodesX[i]
    Var['Y']=NodesY[i]
    Var['Z']=NodesZ[i]
    Var['HGL']=NodesHGL[i]
    Nodes.append(Var)

ReservoirsID=[40]
ReservoirsX=[700]
ReservoirsY=[450]
ReservoirsZ=[40]
ReservoirsHGL=[40]

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
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67]

PipesNI=[2,
3,
4,
5,
6,
6,
7,
8,
9,
15,
15,
14,
13,
12,
16,
16,
17,
18,
19,
40,
40,
24,
23,
22,
40,
25,
26,
27,
28,
25,
34,
33,
32,
31,
34,
35,
36,
37,
38,
30,
21,
20,
11,
1,
10,
29,
2,
31,
9,
28,
12,
22,
19,
3,
32,
8,
27,
13,
23,
18,
4,
33,
7,
26,
14,
24,
17]

PipesNF=[1,
2,
3,
4,
5,
7,
8,
9,
10,
6,
14,
13,
12,
11,
15,
17,
18,
19,
20,
16,
24,
23,
22,
21,
25,
26,
27,
28,
29,
34,
33,
32,
31,
30,
35,
36,
37,
38,
39,
39,
29,
21,
20,
10,
11,
30,
9,
38,
12,
31,
19,
28,
22,
8,
37,
13,
32,
18,
27,
23,
7,
36,
14,
33,
17,
26,
24]

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

grid_x , grid_y=np.mgrid[Xmin:Xmax:10,Ymin:Ymax:10]

HGLInt1=griddata((HGLX,HGLY),HGLZ,(grid_x,grid_y),method='linear')
HGLInt2=np.nan_to_num(HGLInt1, copy=True, nan=0.0, posinf=None, neginf=None)
surf=ax.plot_surface(grid_x,grid_y,HGLInt1,cmap=cm.YlOrRd,vmin=np.nanmin(HGLInt1), vmax=np.nanmax(HGLInt1),rcount=200, ccount=200)

Nodes1ID=[1,
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
39]

Nodes1X=[0,
0,
0,
0,
0,
100,
100,
100,
100,
100,
300,
300,
300,
300,
300,
480,
480,
480,
480,
480,
700,
700,
700,
700,
900,
900,
900,
900,
900,
1080,
1080,
1080,
1080,
1080,
1230,
1230,
1230,
1230,
1230]

Nodes1Y=[0,
80,
230,
330,
450,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
330,
230,
80,
0,
0,
80,
230,
330,
450,
450,
330,
230,
80,
0]

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
0,
0,
0,
0]

Nodes1HGL=[39.7075,
39.7062,
39.32376,
39.32254,
39.30339,
39.30334,
39.31514,
39.32664,
39.7062,
39.7075,
39.7075,
39.70646,
39.77822,
39.31514,
39.3152,
39.31717,
39.88933,
39.88914,
39.7909,
39.7909,
39.88978,
39.89011,
39.89115,
39.89136,
39.89198,
39.89129,
39.89116,
39.89109,
39.89046,
39.8843,
39.88507,
39.88418,
39.89096,
39.89098,
39.89077,
39.89008,
39.89008,
39.88317,
39.88317]

Nodes1=list()

for i in range(NumNodes):
    Var=dict()
    Var['ID']=Nodes1ID[i]
    Var['X']=Nodes1X[i]
    Var['Y']=Nodes1Y[i]
    Var['Z']=Nodes1Z[i]
    Var['HGL']=Nodes1HGL[i]
    Nodes1.append(Var)

Reservoirs1=Reservoirs

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

grid_x1 , grid_y1=np.mgrid[Xmin1:Xmax1:10,Ymin1:Ymax1:10]

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
plt.savefig('Fig_8.pdf', dpi=600,bbox_inches='tight')



