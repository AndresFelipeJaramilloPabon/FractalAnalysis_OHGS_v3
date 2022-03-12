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


Figures=["Fig_S1.tiff","Fig_S2.tiff","Fig_S3.tiff","Fig_S4.tiff","Fig_S5.tiff",
         "Fig_S6.tiff","Fig_S7.tiff","Fig_S8.tiff","Fig_S9.tiff","Fig_S10.tiff",
         "Fig_S11.tiff","Fig_S12.tiff","Fig_S13.tiff"]
Diameter_Units=["in","mm","mm","mm","in","mm","in",
                "mm","mm","mm","mm","mm","mm"]
UnitCost_Units=["USD/m","$/m","$/m","$/m","USD/m","$/m","$/ft",
                "$/m","€/m","$/m","€/m","€/m","€/m"]

Diameters=[[1,2,3,4,6,8,10,12,14,16,18,20,22,24],[152,203,254,305,356,407,458,509],
           [100,150,200,250,300,350,400,450,500,600,700,800,900],[150,200,250,300,350,400,450,500,600,700,750,800,900,1000],
           [12,16,20,24,30,40],[25.4,50.8,76.2,101.6,152.4,203.2,254.0,304.8,355.6,406.4,457.2,508.0,558.8,609.6],
           [36,48,60,72,84,96,108,120,132,144,156,168,180,192,204],[300,350,400,450,500,600,700,800,900,1000,1100],
           [16.0,20.4,26.0,32.6,40.8,51.4,61.4,73.6,90.0,102.2,114.6,130.8,147.2,163.6,184.0,204.6,229.2,257.8,290.6,327.4,368.2,409.2],
           [50,75,100,150,200,250,300,350,400,450,500,600,750,800,1000,1200,1400,1500,1800],
           [100,125,150,200,250,300,350,400,450,500,600,700,800],[100,125,150,200,250,300,350,400,450,500,600,700,800],
           [113.0,126.6,144.6,162.8,180.8,226.2,285.0,361.8,452.2,581.8]]


UnitCosts=[[2,5,8,11,16,23,32,50,60,90,130,170,300,550],[49.54,63.32,94.82,132.87,170.93,194.88,232.94,264.10],
           [860,1160,1470,1700,2080,2640,3240,3810,4400,5580,8360,10400,12800],[24.5,35.2,47.4,61.2,76.5,93.6,113.8,134.0,180.2,234.7,261.2,291.7,355.3,426.7],
           [45.70,70.40,98.40,129.30,180.70,278.30],[0.52,2.10,4.72,8.40,18.90,33.60,52.50,75.59,102.89,134.39,170.09,209.98,254.08,302.37],
           [93.59,133.70,176.32,221.05,267.61,315.80,365.46,416.46,468.71,522.11,576.59,632.09,688.54,745.91,804.14],
           [118,129,145,160,181,214,242,285,325,370,434],[0.38,0.56,0.88,1.35,2.02,3.21,4.44,6.45,9.59,11.98,14.93,19.61,24.78,30.55,38.71,47.63,59.70,75.61,99.58,126.48,160.29,197.71],
           [436.11,785.11,1191.49,2144.98,3255.25,4498.88,5860.26,7328.08,8893.61,10549.93,12291.30,16010.71,22127.38,24298.07,33580.82,43742.55,54698.69,60453.80,78747.43],
           [27.7,38.0,40.5,55.4,75.0,92.4,123.1,141.9,169.3,191.5,246.0,319.6,391.1],[27.7,38.0,40.5,55.4,75.0,92.4,123.1,141.9,169.3,191.5,246.0,319.6,391.1],
           [7.22,9.10,11.92,14.84,18.38,28.60,45.39,76.32,124.64,215.85]]

Networks=list()
for i in range(13):
    Var=dict()
    Var["Name"]=Figures[i]
    Var["DU"]=Diameter_Units[i]
    Var["UCU"]=UnitCost_Units[i]
    Var["D"]=Diameters[i]
    Var["UC"]=UnitCosts[i]
    Networks.append(Var)

for i in Networks: 
    LND=[np.log(j) for j in i["D"]]
    LNU=[np.log(j) for j in i["UC"]]
    
    m,b,r,p,std=linregress(LND,LNU)
    K=np.exp(b)
    n=m
    CD=r**2
    
    Y=[K*j**n for j in i["D"]]
    
    fig=plt.figure(dpi=600)
    ax = fig.add_subplot()
    fig.set_size_inches(2,2)
    ax.scatter(i["D"],i["UC"], c='blue',s=10, marker='o', alpha=1)
    ax.plot(i["D"],Y,c='maroon',linestyle='dotted')
    ax.set_xlabel('Diameter ('+i["DU"]+')',fontsize=6)
    ax.set_ylabel('Unit Cost ('+i["UCU"]+')',fontsize=6)
    textstr = '\n'.join((
        r'$K=%.4f$' % (K, ),
        r'$n=%.4f$' % (n, ),
        r'$R$'+chr(0x00b2)+'$=%.2f$' % (CD, )))
    props = dict(boxstyle='round', facecolor='None', alpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=6,
            verticalalignment='top', bbox=props)
    ax.set_yticklabels(['${:,}'.format(int(x)) for x in ax.get_yticks().tolist()],fontsize=6)
    ax.tick_params(axis="x",labelsize=6)
    plt.savefig(i["Name"], dpi=500,bbox_inches = 'tight')
