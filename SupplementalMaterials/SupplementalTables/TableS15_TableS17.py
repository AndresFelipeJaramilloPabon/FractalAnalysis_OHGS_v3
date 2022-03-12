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

def cost_calculation(k,n,length,diameters):
    cost=np.sum([k*length[i]*diameters[i]**n for i in range(len(diameters))])
    return cost


Diameters=[[1,2,3,4,6,8,10,12,14,16,18,20,22,24],[152,203,254,305,356,407,458,509],
           [100,150,200,250,300,350,400,450,500,600,700,800,900],[150,200,250,300,350,400,450,500,600,700,750,800,900,1000],
           [12,16,20,24,30,40],[25.4,50.8,76.2,101.6,152.4,203.2,254.0,304.8,355.6,406.4,457.2,508.0,558.8,609.6],
           [36,48,60,72,84,96,108,120,132,144,156,168,180,192,204],[300,350,400,450,500,600,700,800,900,1000,1100],
           [16.0,20.4,26.0,32.6,40.8,51.4,61.4,73.6,90.0,102.2,114.6,130.8,147.2,163.6,184.0,204.6,229.2,257.8,290.6,327.4,368.2,409.2],
           [50,75,100,150,200,250,300,350,400,450,500,600,750,800,1000,1200,1400,1500,1800],
           [100,125,150,200,250,300,350,400,450,500,600,700,800],[100,125,150,200,250,300,350,400,450,500,600,700,800],
           [113.0,126.6,144.6,162.8,180.8,226.2,285.0,361.8,452.2,581.8],
           [76.2,101.6,152.4,203.2,254.0,304.8,355.6,406.4,457.2,508.0,609.6,762.0,914.4]]


UnitCosts=[[2,5,8,11,16,23,32,50,60,90,130,170,300,550],[49.54,63.32,94.82,132.87,170.93,194.88,232.94,264.10],
           [860,1160,1470,1700,2080,2640,3240,3810,4400,5580,8360,10400,12800],[24.5,35.2,47.4,61.2,76.5,93.6,113.8,134.0,180.2,234.7,261.2,291.7,355.3,426.7],
           [45.70,70.40,98.40,129.30,180.70,278.30],[0.52,2.10,4.72,8.40,18.90,33.60,52.50,75.59,102.89,134.39,170.09,209.98,254.08,302.37],
           [93.59,133.70,176.32,221.05,267.61,315.80,365.46,416.46,468.71,522.11,576.59,632.09,688.54,745.91,804.14],
           [118,129,145,160,181,214,242,285,325,370,434],[0.38,0.56,0.88,1.35,2.02,3.21,4.44,6.45,9.59,11.98,14.93,19.61,24.78,30.55,38.71,47.63,59.70,75.61,99.58,126.48,160.29,197.71],
           [436.11,785.11,1191.49,2144.98,3255.25,4498.88,5860.26,7328.08,8893.61,10549.93,12291.30,16010.71,22127.38,24298.07,33580.82,43742.55,54698.69,60453.80,78747.43],
           [27.7,38.0,40.5,55.4,75.0,92.4,123.1,141.9,169.3,191.5,246.0,319.6,391.1],[27.7,38.0,40.5,55.4,75.0,92.4,123.1,141.9,169.3,191.5,246.0,319.6,391.1],
           [7.22,9.10,11.92,14.84,18.38,28.60,45.39,76.32,124.64,215.85],
           [22398.500000000,36956.166666667,80694.500000000,136687.000000000,215172.833333333,301068.000000000,373361.166666667,490042.000000000,628960.666666667,783442.000000000,1071610.410841820,1625537.494995020,2284820.739405680]]

K=list()
n=list()

t=28

for i in range(t): 
    if i<=13:
        LND=[np.log(j) for j in Diameters[i]]
        LNU=[np.log(j) for j in UnitCosts[i]]
    else:
        LND=[np.log(j) for j in Diameters[13]]
        LNU=[np.log(j) for j in UnitCosts[13]]
    
    m,b,r,p,std=linregress(LND,LNU)
    k=np.exp(b)
    exp=m
    K.append(round(k,4))
    n.append(round(exp,4))

Networks=["TwoLoops.txt","TwoReservoirs.txt","Taichung.txt","Jilin.txt","Hanoi.txt","Blacksburg.txt",
          "NewYorkTunnels.txt","BakRyan.txt","Fossolo.txt","R28.txt","Pescara.txt","Modena.txt","Balerma.txt",
          "LaUribe.txt","ElOvero.txt","SanVicente.txt","Cazuca.txt","Elevada.txt","AndaluciaAlta.txt","LaCumbre.txt",
          "AndaluciaBaja.txt","Toro.txt","Candelaria.txt","Bugalagrande.txt","CarmendelViboral.txt","MorroBajo.txt",
          "Chinu.txt","LaEnea.txt"]
length=list()
LC=list()
NO1=list()
NO2=list()
NO3=list()
NO4=list()
NO5=list()
NO6=list()
NO7=list()
NO8=list()
NO9=list()
NO10=list()

CLC=list()
CNO1=list()
CNO2=list()
CNO3=list()
CNO4=list()
CNO5=list()
CNO6=list()
CNO7=list()
CNO8=list()
CNO9=list()
CNO10=list()

for i in range(t):
    File=open(Networks[i],"r")
    Lines=File.readlines()
    NumPipes=int(Lines[0])
    length=list()
    LC=list()
    NO1=list()
    NO2=list()
    NO3=list()
    NO4=list()
    NO5=list()
    NO6=list()
    NO7=list()
    NO8=list()
    NO9=list()
    NO10=list()
    for j in range(NumPipes):
        length.append(float(Lines[1+j]))
        LC.append(float(Lines[1+j+NumPipes]))
        NO1.append(float(Lines[1+j+2*NumPipes]))
        NO2.append(float(Lines[1+j+3*NumPipes]))
        NO3.append(float(Lines[1+j+4*NumPipes]))
        NO4.append(float(Lines[1+j+5*NumPipes]))
        NO5.append(float(Lines[1+j+6*NumPipes]))
        NO6.append(float(Lines[1+j+7*NumPipes]))
        NO7.append(float(Lines[1+j+8*NumPipes]))
        NO8.append(float(Lines[1+j+9*NumPipes]))
        NO9.append(float(Lines[1+j+10*NumPipes]))
        NO10.append(float(Lines[1+j+11*NumPipes]))
    CLC.append(round(cost_calculation(K[i],n[i],length,LC),0))
    CNO1.append(round(cost_calculation(K[i],n[i],length,NO1),0))
    CNO2.append(round(cost_calculation(K[i],n[i],length,NO2),0))
    CNO3.append(round(cost_calculation(K[i],n[i],length,NO3),0))
    CNO4.append(round(cost_calculation(K[i],n[i],length,NO4),0))
    CNO5.append(round(cost_calculation(K[i],n[i],length,NO5),0))
    CNO6.append(round(cost_calculation(K[i],n[i],length,NO6),0))
    CNO7.append(round(cost_calculation(K[i],n[i],length,NO7),0))
    CNO8.append(round(cost_calculation(K[i],n[i],length,NO8),0))
    CNO9.append(round(cost_calculation(K[i],n[i],length,NO9),0))
    CNO10.append(round(cost_calculation(K[i],n[i],length,NO10),0))
    
TableS15=open("TableS15.txt","w")
TableS16=open("TableS16.txt","w")
TableS17=open("TableS17.txt","w")

TableS15.write("LC")
TableS15.write("\n")

for i in range(t):
    TableS15.write(str(CLC[i]))
    TableS15.write("\n")
    
TableS15.write("-------------------------------")
TableS15.write("\n")

TableS15.write("NO1")
TableS15.write("\n")


for i in range(t):
    TableS15.write(str(CNO1[i]))
    TableS15.write("\n")

TableS15.write("-------------------------------")
TableS15.write("\n")

TableS15.write("NO2")
TableS15.write("\n")

for i in range(t):
    TableS15.write(str(CNO2[i]))
    TableS15.write("\n")
    
TableS15.write("-------------------------------")
TableS15.write("\n")

TableS15.write("NO3")
TableS15.write("\n")


for i in range(t):
    TableS15.write(str(CNO3[i]))
    TableS15.write("\n")
    
TableS15.close()

TableS16.write("NO4")
TableS16.write("\n")

for i in range(t):
    TableS16.write(str(CNO4[i]))
    TableS16.write("\n")
    
TableS16.write("-------------------------------")
TableS16.write("\n")

TableS16.write("NO5")
TableS16.write("\n")

for i in range(t):
    TableS16.write(str(CNO5[i]))
    TableS16.write("\n")

TableS16.write("-------------------------------")
TableS16.write("\n")

TableS16.write("NO6")
TableS16.write("\n")

for i in range(t):
    TableS16.write(str(CNO6[i]))
    TableS16.write("\n")
    
TableS16.write("-------------------------------")
TableS16.write("\n")

TableS16.write("NO7")
TableS16.write("\n")

for i in range(t):
    TableS16.write(str(CNO7[i]))
    TableS16.write("\n")

TableS16.close()

TableS17.write("NO8")
TableS17.write("\n")

for i in range(t):
    TableS17.write(str(CNO8[i]))
    TableS17.write("\n")
    
TableS17.write("-------------------------------")
TableS17.write("\n")

TableS17.write("NO9")
TableS17.write("\n")

for i in range(t):
    TableS17.write(str(CNO9[i]))
    TableS17.write("\n")

TableS17.write("-------------------------------")
TableS17.write("\n")

TableS17.write("NO10")
TableS17.write("\n")

for i in range(t):
    TableS17.write(str(CNO10[i]))
    TableS17.write("\n")
    
TableS17.close()