# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:33:17 2021

@author: Andrés Jaramillo
"""

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

Diameter_Units='mm'
UnitCost_Units='COP/m'

Diameters=[76.2,101.6,152.4,203.2,254.0,304.8,355.6,406.4,457.2,508.0,609.6,762.0,914.4]
UnitCosts=[22398.50,36956.17,80694.50,136687.00,215172.83,301068.00,373361.17,490042.00,628960.67,783442.00,1071610.41,1625537.49,2284820.74]
    
# Power Regression
    
LND=[np.log(i) for i in Diameters]
LNU=[np.log(i) for i in UnitCosts]

m,b,r,p,std=linregress(LND,LNU)
K=np.exp(b)
n=m
CD=r**2

Y=[K*i**n for i in Diameters]

fig=plt.figure(dpi=600)
ax = fig.add_subplot()
fig.set_size_inches(2,2)
ax.scatter(Diameters,UnitCosts, c='blue',s=10, marker='o', alpha=1)
ax.plot(Diameters,Y,c='maroon',linestyle='dotted')
ax.set_xlabel('Diameter ('+Diameter_Units+')', fontsize=6)
ax.set_ylabel('Unit Cost ('+UnitCost_Units+')', fontsize=6)
textstr = '\n'.join((
    r'$K=%.4f$' % (K, ),
    r'$n=%.4f$' % (n, ),
    r'$R$'+chr(0x00b2)+'$=%.2f$' % (CD, )))
props = dict(boxstyle='round', facecolor='None', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=6,
        verticalalignment='top', bbox=props)
ax.set_yticklabels(['${:,}'.format(int(x)) for x in ax.get_yticks().tolist()], fontsize=6)
ax.set_xticks([200,400,600,800])
plt.xticks(fontsize=6)
plt.savefig('Fig_1.tiff', dpi=500,bbox_inches = 'tight')