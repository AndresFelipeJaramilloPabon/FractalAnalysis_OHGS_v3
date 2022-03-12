# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:01:22 2021

@author: Andrés Jaramillo
"""

import matplotlib.pyplot as plt 
from matplotlib.ticker import FormatStrFormatter
from matplotlib.pyplot import figure
from matplotlib import cm
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import math
from scipy.spatial import ConvexHull
from PIL import Image
import matplotlib.patches as mpatches

fig, axs = plt.subplots(7,4)
fig.set_size_inches(10, 15)
fig.set_dpi(600)

x=[1.15,1.12,1.09,1.06,1.03,1,0.97,0.94,0.91,0.88,0.85]

N1=[2.0333,1.9676,1.9947,1.9410,2.0290,1.9655,1.9578,2.0022,1.9595,1.9697,1.9895]
N2=[2.1029,2.0441,2.0282,2.0629,2.0492,2.0569,2.0569,2.0574,2.0524,2.0148,2.0974]
N3=[2.0723,2.0224,2.0322,2.0536,2.0353,2.0376,1.9637,2.0073,1.9975,2.0093,2.0012]
N4=[2.1343,2.1358,2.1087,2.0542,2.0756,1.9787,1.9723,1.9667,1.9727,1.9775,1.9385]
N5=[2.0214,2.0007,2.0232,2.0056,2.0045,1.9933,1.9967,2.0027,2.0022,1.9621,1.9713]
N6=[2.3388,2.3165,2.2692,2.2581,2.2385,2.0044,2.3380,2.2035,2.1271,2.2319,1.9296]
N7=[2.0381,2.0942,2.0847,2.0273,1.9581,2.1622,2.1598,2.0370,2.0772,2.0828,2.1289]
N8=[2.0894,2.0891,2.0869,2.0872,2.0680,2.1332,2.1093,2.1136,2.1294,2.1312,2.0971]
N9=[2.2121,2.2118,2.3674,2.0036,2.0877,2.0582,1.9762,2.0721,2.0324,2.0186,2.1720]
N10=[2.0647,1.9869,2.0112,1.9725,2.0483,2.0404,2.1061,1.9947,1.9129,1.9290,1.9816]
N11=[2.3125,2.3207,2.3426,2.2354,2.2641,2.2650,2.3186,2.2697,2.1792,2.2856,2.1773]
N12=[2.3204,2.2662,2.3093,2.2883,2.2155,2.2014,2.2746,2.2003,2.2053,2.1965,2.2065]
N13=[2.2982,2.2802,2.2563,2.2763,2.2917,2.2967,2.2945,2.3016,2.3058,2.3028,2.3024]
N14=[2.0064,2.0060,2.0042,2.0054,1.9548,1.9290,1.9289,2.0638,2.0767,1.9490,2.1055]
N15=[2.2110,2.2108,2.2111,2.2171,2.1860,2.2061,2.1618,2.1725,2.1076,2.1586,2.2162]
N16=[1.9386,1.8812,1.9224,1.8420,1.8463,1.9101,1.9316,1.9885,2.0426,1.9040,1.9151]
N17=[2.1754,2.1602,2.1594,2.1570,2.1577,2.1083,2.1626,2.1992,2.2078,2.1546,2.1551]
N18=[2.0338,2.0536,2.0409,2.0603,2.0298,2.0593,2.0669,2.0786,2.0713,2.0839,1.9979]
N19=[2.0703,2.0798,2.0613,2.0500,2.0512,2.0700,2.1532,2.1996,2.0266,2.0816,2.2853]
N20=[2.1971,2.2001,2.2054,2.1974,2.1835,2.2384,2.2221,2.0891,2.2326,2.2047,2.1476]
N21=[2.0617,2.0616,2.0628,2.1000,2.0708,2.0817,2.0510,2.0639,2.0550,2.1161,2.0831]
N22=[2.1202,2.1171,2.1203,2.1342,2.1421,2.1057,2.0958,2.1129,2.1007,2.0885,2.0892]
N23=[1.9283,1.9233,1.9462,1.9673,1.9454,1.9327,1.8858,1.6737,1.8206,1.8411,1.5216]
N24=[2.1394,2.1307,2.1260,2.1350,2.1147,2.1250,2.1019,2.1322,2.0711,2.1126,2.1557]
N25=[2.0852,2.0834,2.0690,2.0699,2.0706,2.0900,2.0705,2.0797,2.0854,2.0953,2.0877]
N26=[2.0583,2.0606,2.0584,2.0418,2.0367,2.0365,2.0843,1.9789,2.0492,2.0215,1.9782]
N27=[1.8622,1.8621,1.8469,1.9611,1.8006,2.0430,1.9929,1.8864,1.8876,2.0795,2.1691]
N28=[2.0834,2.0821,2.0844,2.0820,2.0800,2.0803,2.0831,2.0829,2.0833,2.0829,2.0841]

axs[0,0].boxplot(N1,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""], widths=0.4)
axs[0,0].tick_params(axis="x",length=0)
y=N1
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[0,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[0,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[0,0].set_yticks(np.arange(math.floor(min(N1)*100)/100,math.ceil(max(N1)*100)/100, 0.02))
axs[0,0].set_ylabel("D")
axs[0,0].set_title("Two Loops",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[0,0].text(0.625, 0.13, textstr, transform=axs[0,0].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[0,1].boxplot(N2,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[0,1].tick_params(axis="x",length=0)
y=N2
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[0,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[0,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[0,1].set_yticks(np.arange(math.floor(min(N2)*100)/100,math.ceil(max(N2)*100)/100, 0.02))
axs[0,1].set_ylabel("D")
axs[0,1].set_title("Two Reservoirs",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[0,1].text(0.45, 0.13, textstr, transform=axs[0,1].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[0,2].boxplot(N3,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[0,2].tick_params(axis="x",length=0)
y=N3
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[0,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[0,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[0,2].set_yticks(np.arange(math.floor(min(N3)*100)/100,math.ceil(max(N3)*100)/100, 0.02))
axs[0,2].set_ylabel("D")
axs[0,2].set_title("Taichung",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[0,2].text(0.625, 0.13, textstr, transform=axs[0,2].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[0,3].boxplot(N4,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[0,3].tick_params(axis="x",length=0)
y=N4
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[0,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[0,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[0,3].set_yticks(np.arange(math.floor(min(N4)*100)/100,math.ceil(max(N4)*100)/100, 0.04))
axs[0,3].set_ylabel("D")
axs[0,3].set_title("Jilin",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[0,3].text(0.625, 0.13, textstr, transform=axs[0,3].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[1,0].boxplot(N5,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[1,0].tick_params(axis="x",length=0)
y=N5
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[1,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[1,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[1,0].set_yticks(np.arange(math.floor(min(N5)*100)/100,math.ceil(max(N5)*100)/100, 0.01))
axs[1,0].set_ylabel("D")
axs[1,0].set_title("Hanoi",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[1,0].text(0.625, 0.13, textstr, transform=axs[1,0].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[1,1].boxplot(N6,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[1,1].tick_params(axis="x",length=0)
y=N6
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[1,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[1,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[1,1].set_yticks(np.arange(math.floor(min(N6)*100)/100,math.ceil(max(N6)*100)/100, 0.08))
axs[1,1].set_ylabel("D")
axs[1,1].set_title("Blacksburg",fontsize=10)

textstr = r"0.96 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[1,1].text(0.45, 0.13, textstr, transform=axs[1,1].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[1,2].boxplot(N7,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[1,2].tick_params(axis="x",length=0)
y=N7
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[1,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[1,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[1,2].set_yticks(np.arange(math.floor(min(N7)*100)/100,math.ceil(max(N7)*100)/100, 0.04))
axs[1,2].set_ylabel("D")
axs[1,2].set_title("New York Tunnels",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[1,2].text(0.625, 0.13, textstr, transform=axs[1,2].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[1,3].boxplot(N8,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[1,3].tick_params(axis="x",length=0)
y=N8
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[1,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[1,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[1,3].set_yticks(np.arange(math.floor(min(N8)*100)/100,math.ceil(max(N8)*100)/100, 0.02))
axs[1,3].set_ylabel("D")
axs[1,3].set_title("BakRyan",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[1,3].text(0.55, 0.18, textstr, transform=axs[1,3].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[2,0].boxplot(N9,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[2,0].tick_params(axis="x",length=0)
y=N9
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[2,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[2,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[2,0].set_yticks(np.arange(math.floor(min(N9)*100)/100,math.ceil(max(N9)*100)/100, 0.08))
axs[2,0].set_ylabel("D")
axs[2,0].set_title("Fossolo",fontsize=10)

textstr = r"0.95 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[2,0].text(0.05, 0.90, textstr, transform=axs[2,0].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[2,1].boxplot(N10,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[2,1].tick_params(axis="x",length=0)
y=N10
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[2,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[2,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[2,1].set_yticks(np.arange(math.floor(min(N10)*100)/100,math.ceil(max(N10)*100)/100, 0.03))
axs[2,1].set_ylabel("D")
axs[2,1].set_title("R28",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[2,1].text(0.05, 0.90, textstr, transform=axs[2,1].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[2,2].boxplot(N11,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[2,2].tick_params(axis="x",length=0)
y=N11
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[2,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[2,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[2,2].set_yticks(np.arange(math.floor(min(N11)*100)/100,math.ceil(max(N11)*100)/100, 0.03))
axs[2,2].set_ylabel("D")
axs[2,2].set_title("Pescara",fontsize=10)

textstr = r"0.95 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[2,2].text(0.05, 0.90, textstr, transform=axs[2,2].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[2,3].boxplot(N12,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[2,3].tick_params(axis="x",length=0)
y=N12
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[2,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[2,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[2,3].set_yticks(np.arange(math.floor(min(N12)*100)/100,math.ceil(max(N12)*100)/100, 0.03))
axs[2,3].set_ylabel("D")
axs[2,3].set_title("Modena",fontsize=10)

textstr = r"0.96 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[2,3].text(0.05, 0.90, textstr, transform=axs[2,3].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[3,0].boxplot(N13,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[3,0].tick_params(axis="x",length=0)
y=N13
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[3,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[3,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[3,0].set_yticks(np.arange(math.floor(min(N13)*100)/100,math.ceil(max(N13)*100)/100, 0.01))
axs[3,0].set_ylabel("D")
axs[3,0].set_title("Balerma",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 0.99"
props = dict(boxstyle='round', facecolor='white')
axs[3,0].text(0.625, 0.13, textstr, transform=axs[3,0].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[3,1].boxplot(N14,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[3,1].tick_params(axis="x",length=0)
y=N14
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[3,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[3,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[3,1].set_yticks(np.arange(math.floor(min(N14)*100)/100,math.ceil(max(N14)*100)/100, 0.03))
axs[3,1].set_ylabel("D")
axs[3,1].set_title("La Uribe",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[3,1].text(0.55, 0.13, textstr, transform=axs[3,1].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[3,2].boxplot(N15,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[3,2].tick_params(axis="x",length=0)
y=N15
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[3,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[3,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[3,2].set_yticks(np.arange(math.floor(min(N15)*100)/100,math.ceil(max(N15)*100)/100, 0.02))
axs[3,2].set_ylabel("D")
axs[3,2].set_title("El Overo",fontsize=10)

textstr = r"0.96 ≤ "+'$R$'+chr(0x00b2)+" ≤ 0.98"
props = dict(boxstyle='round', facecolor='white')
axs[3,2].text(0.55, 0.13, textstr, transform=axs[3,2].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[3,3].boxplot(N16,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[3,3].tick_params(axis="x",length=0)
y=N16
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[3,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[3,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[3,3].set_yticks(np.arange(math.floor(min(N16)*100)/100,math.ceil(max(N16)*100)/100, 0.04))
axs[3,3].set_ylabel("D")
axs[3,3].set_title("San Vicente",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[3,3].text(0.625, 0.13, textstr, transform=axs[3,3].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[4,0].boxplot(N17,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[4,0].tick_params(axis="x",length=0)
y=N17
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[4,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[4,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[4,0].set_yticks(np.arange(math.floor(min(N17)*100)/100,math.ceil(max(N17)*100)/100, 0.02))
axs[4,0].set_ylabel("D")
axs[4,0].set_title("Cazucá",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[4,0].text(0.05, 0.90, textstr, transform=axs[4,0].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[4,1].boxplot(N18,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[4,1].tick_params(axis="x",length=0)
y=N18
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[4,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[4,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[4,1].set_yticks(np.arange(math.floor(min(N18)*100)/100,math.ceil(max(N18)*100)/100, 0.02))
axs[4,1].set_ylabel("D")
axs[4,1].set_title("Elevada",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[4,1].text(0.05, 0.90, textstr, transform=axs[4,1].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[4,2].boxplot(N19,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[4,2].tick_params(axis="x",length=0)
y=N19
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[4,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[4,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[4,2].set_yticks(np.arange(math.floor(min(N19)*100)/100,math.ceil(max(N19)*100)/100, 0.04))
axs[4,2].set_ylabel("D")
axs[4,2].set_title("Andalucía Alta",fontsize=10)

textstr = r"0.98 ≤ "+'$R$'+chr(0x00b2)+" ≤ 0.99"
props = dict(boxstyle='round', facecolor='white')
axs[4,2].text(0.05, 0.90, textstr, transform=axs[4,2].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[4,3].boxplot(N20,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[4,3].tick_params(axis="x",length=0)
y=N20
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[4,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[4,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[4,3].set_yticks(np.arange(math.floor(min(N20)*100)/100,math.ceil(max(N20)*100)/100, 0.03))
axs[4,3].set_ylabel("D")
axs[4,3].set_title("La Cumbre",fontsize=10)

textstr = r"0.96 ≤ "+'$R$'+chr(0x00b2)+" ≤ 0.99"
props = dict(boxstyle='round', facecolor='white')
axs[4,3].text(0.05, 0.90, textstr, transform=axs[4,3].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[5,0].boxplot(N21,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[5,0].tick_params(axis="x",length=0)
y=N21
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[5,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[5,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[5,0].set_yticks(np.arange(math.floor(min(N21)*100)/100,math.ceil(max(N21)*100)/100, 0.01))
axs[5,0].set_ylabel("D")
axs[5,0].set_title("Andalucía Baja",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[5,0].text(0.625, 0.13, textstr, transform=axs[5,0].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

axs[5,1].boxplot(N22,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[5,1].tick_params(axis="x",length=0)
y=N22
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[5,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[5,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[5,1].set_yticks(np.arange(math.floor(min(N22)*100)/100,math.ceil(max(N22)*100)/100, 0.01))
axs[5,1].set_ylabel("D")
axs[5,1].set_title("Toro",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[5,1].text(0.55, 0.10, textstr, transform=axs[5,1].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[5,2].boxplot(N23,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[5,2].tick_params(axis="x",length=0)
y=N23
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[5,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[5,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[5,2].set_yticks(np.arange(math.floor(min(N23)*100)/100,math.ceil(max(N23)*100)/100, 0.06))
axs[5,2].set_ylabel("D")
axs[5,2].set_title("Candelaria",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[5,2].text(0.475, 0.13, textstr, transform=axs[5,2].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[5,3].boxplot(N24,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[5,3].tick_params(axis="x",length=0)
y=N24
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[5,3].plot(x, y, 'r.', zorder=10,markersize=4)
axs[5,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[5,3].set_yticks(np.arange(math.floor(min(N24)*100)/100,math.ceil(max(N24)*100)/100, 0.02))
axs[5,3].set_ylabel("D")
axs[5,3].set_title("Bugalagrande",fontsize=10)

textstr = r"0.97 ≤ "+'$R$'+chr(0x00b2)+" ≤ 0.98"
props = dict(boxstyle='round', facecolor='white')
axs[5,3].text(0.475, 0.13, textstr, transform=axs[5,3].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[6,0].boxplot(N25,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[6,0].tick_params(axis="x",length=0)
y=N25
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[6,0].plot(x, y, 'r.', zorder=10,markersize=4)
axs[6,0].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[6,0].set_yticks(np.arange(math.floor(min(N25)*100)/100,math.ceil(max(N25)*100)/100, 0.005))
axs[6,0].set_ylabel("D")
axs[6,0].set_title("Carmen del Viboral",fontsize=10)

textstr = r"0.96 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[6,0].text(0.55, 0.10, textstr, transform=axs[6,0].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[6,1].boxplot(N26,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[6,1].tick_params(axis="x",length=0)
y=N26
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[6,1].plot(x, y, 'r.', zorder=10,markersize=4)
axs[6,1].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[6,1].set_yticks(np.arange(math.floor(min(N26)*100)/100,math.ceil(max(N26)*100)/100, 0.02))
axs[6,1].set_ylabel("D")
axs[6,1].set_title("Morrorico Bajo",fontsize=10)

textstr = r"0.83 ≤ "+'$R$'+chr(0x00b2)+" ≤ 0.94"
props = dict(boxstyle='round', facecolor='white')
axs[6,1].text(0.45, 0.13, textstr, transform=axs[6,1].transAxes, fontsize=6,
        verticalalignment='top', bbox=props)

axs[6,2].boxplot(N27,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[6,2].tick_params(axis="x",length=0)
y=N27
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
axs[6,2].plot(x, y, 'r.', zorder=10,markersize=4)
axs[6,2].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[6,2].set_yticks(np.arange(math.floor(min(N27)*100)/100,math.ceil(max(N27)*100)/100, 0.06))
axs[6,2].set_ylabel("D")
axs[6,2].set_title("Chinú",fontsize=10)

textstr = r"0.99 ≤ "+'$R$'+chr(0x00b2)+" ≤ 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[6,2].text(0.55, 0.13, textstr, transform=axs[6,2].transAxes, fontsize=5,
        verticalalignment='top', bbox=props)

axs[6,3].boxplot(N28,patch_artist=True,
               boxprops=dict(color="black",facecolor="lightskyblue"),
               medianprops=dict(color="darkred"), zorder=0,
               showfliers=False,labels=[""],widths=0.4)
axs[6,3].tick_params(axis="x",length=0)
y=N28
Dopt=y[0]
y.sort(reverse=True)
Dind=y.index(Dopt)
sc1,=axs[6,3].plot(x, y, 'r.', zorder=10,markersize=4)
sc2,=axs[6,3].plot(x[Dind], Dopt, 'r.', zorder=10,markersize=6,marker="*",color="darkolivegreen")
axs[6,3].set_yticks(np.arange(math.floor(min(N28)*100)/100,math.ceil(max(N28)*100)/100, 0.002))
axs[6,3].set_ylabel("D")
axs[6,3].set_title("La Enea",fontsize=10)

textstr = r'$R$'+chr(0x00b2)+" = 1.00"
props = dict(boxstyle='round', facecolor='white')
axs[6,3].text(0.625, 0.15, textstr, transform=axs[6,3].transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

leg=fig.legend([sc1,sc2],["NO","LC"], loc="center right")
leg.get_frame().set_edgecolor('black')

plt.tight_layout(rect=[0,0,.925,1])
plt.savefig("Fig_12.pdf",dpi=600)