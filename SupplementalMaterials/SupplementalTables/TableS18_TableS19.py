# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:20:12 2021

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
import statistics as stats


Networks=["TwoLoops.txt","TwoReservoirs.txt","Taichung.txt","Jilin.txt","Hanoi.txt","Blacksburg.txt",
          "NewYorkTunnels.txt","BakRyan.txt","Fossolo.txt","R28.txt","Pescara.txt","Modena.txt","Balerma.txt",
          "LaUribe.txt","ElOvero.txt","SanVicente.txt","Cazuca.txt","Elevada.txt","AndaluciaAlta.txt","LaCumbre.txt",
          "AndaluciaBaja.txt","Toro.txt","Candelaria.txt","Bugalagrande.txt","CarmendelViboral.txt","MorroBajo.txt",
          "Chinu.txt","LaEnea.txt"]

Units=[1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

LCMean=list()
NO1Mean=list()
NO2Mean=list()
NO3Mean=list()
NO4Mean=list()
NO5Mean=list()
NO6Mean=list()
NO7Mean=list()
NO8Mean=list()
NO9Mean=list()
NO10Mean=list()

LCStd=list()
NO1Std=list()
NO2Std=list()
NO3Std=list()
NO4Std=list()
NO5Std=list()
NO6Std=list()
NO7Std=list()
NO8Std=list()
NO9Std=list()
NO10Std=list()

for i in range(28):
    File=open(Networks[i],"r")
    Lines=File.readlines()
    NumPipes=int(Lines[0])
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
        if Units[i]==1:
            LC.append(25.4*float(Lines[1+j+NumPipes]))
            NO1.append(25.4*float(Lines[1+j+2*NumPipes]))
            NO2.append(25.4*float(Lines[1+j+3*NumPipes]))
            NO3.append(25.4*float(Lines[1+j+4*NumPipes]))
            NO4.append(25.4*float(Lines[1+j+5*NumPipes]))
            NO5.append(25.4*float(Lines[1+j+6*NumPipes]))
            NO6.append(25.4*float(Lines[1+j+7*NumPipes]))
            NO7.append(25.4*float(Lines[1+j+8*NumPipes]))
            NO8.append(25.4*float(Lines[1+j+9*NumPipes]))
            NO9.append(25.4*float(Lines[1+j+10*NumPipes]))
            NO10.append(25.4*float(Lines[1+j+11*NumPipes]))
        else:
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
            
    LCMean.append(round(sum(LC)/len(LC),2))
    NO1Mean.append(round(sum(NO1)/len(NO1),2))
    NO2Mean.append(round(sum(NO2)/len(NO2),2))
    NO3Mean.append(round(sum(NO3)/len(NO3),2))
    NO4Mean.append(round(sum(NO4)/len(NO4),2))
    NO5Mean.append(round(sum(NO5)/len(NO5),2))
    NO6Mean.append(round(sum(NO6)/len(NO6),2))
    NO7Mean.append(round(sum(NO7)/len(NO7),2))
    NO8Mean.append(round(sum(NO8)/len(NO8),2))
    NO9Mean.append(round(sum(NO9)/len(NO9),2))
    NO10Mean.append(round(sum(NO10)/len(NO10),2))
    
    LCStd.append(round(stats.stdev(LC),2))
    NO1Std.append(round(stats.stdev(NO1),2))
    NO2Std.append(round(stats.stdev(NO2),2))
    NO3Std.append(round(stats.stdev(NO3),2))
    NO4Std.append(round(stats.stdev(NO4),2))
    NO5Std.append(round(stats.stdev(NO5),2))
    NO6Std.append(round(stats.stdev(NO6),2))
    NO7Std.append(round(stats.stdev(NO7),2))
    NO8Std.append(round(stats.stdev(NO8),2))
    NO9Std.append(round(stats.stdev(NO9),2))
    NO10Std.append(round(stats.stdev(NO10),2))

TableS18=open("TableS18.txt","w")

TableS18.write("LC")
TableS18.write("\n")

t=28

for i in range(t):
    TableS18.write(str(LCMean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO1")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO1Mean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO2")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO2Mean[i]))
    TableS18.write("\n")

TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO3")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO3Mean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO4")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO4Mean[i]))
    TableS18.write("\n")

TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO5")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO5Mean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO6")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO6Mean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO7")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO7Mean[i]))
    TableS18.write("\n")

TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO8")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO8Mean[i]))
    TableS18.write("\n")
    
TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO9")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO9Mean[i]))
    TableS18.write("\n")

TableS18.write("-------------------------------")
TableS18.write("\n")

TableS18.write("NO10")
TableS18.write("\n")

for i in range(t):
    TableS18.write(str(NO10Mean[i]))
    TableS18.write("\n")

TableS18.close()

TableS19=open("TableS19.txt","w")

TableS19.write("LC")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(LCStd[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO1")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO1Std[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO2")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO2Std[i]))
    TableS19.write("\n")

TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO3")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO3Std[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO4")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO4Std[i]))
    TableS19.write("\n")

TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO5")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO5Std[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO6")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO6Std[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO7")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO7Std[i]))
    TableS19.write("\n")

TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO8")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO8Std[i]))
    TableS19.write("\n")
    
TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO9")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO9Std[i]))
    TableS19.write("\n")

TableS19.write("-------------------------------")
TableS19.write("\n")

TableS19.write("NO10")
TableS19.write("\n")

for i in range(t):
    TableS19.write(str(NO10Std[i]))
    TableS19.write("\n")

TableS19.close()

