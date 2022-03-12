# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:08:57 2021

@author: Andrés Jaramillo
"""

from scipy.interpolate import griddata
from scipy.stats import linregress
import numpy as np
import math
from scipy.sparse.csgraph import shortest_path


StepSizeL=[25]
Networks=["MorroricoBajo.txt"]

WCriterion=[1,2,3,4]

DOHGS=list()
R2OHGS=list()
DTopology=list()
R2Topology=list()
DFlow=list()
R2Flow=list()
DEnergy=list()
R2Energy=list()
DInfrastructural=list()
R2Infrastructural=list()

def cal_var(HGLInt2,L,X,Y):
        mtx=HGLInt2[Y:Y+L,X:X+L]
        max_val=np.max(mtx)
        if max_val==0:
            VR=math.nan
        else:
            min_val=np.min(mtx[np.nonzero(mtx)])
            VR=max_val-min_val
        return VR

def indweight_calculator(i,w):
    W=0
    if w==1:
        W=1
    elif w==2:
        pipes=[k for k in Pipes if i in k['NIyNF']]
        for k in pipes:
            if k['Q']>0 and i==k['NIyNF'][1]:
                W=W+k['Q']
            elif k['Q']<0 and i==k['NIyNF'][0]:
                W=W-k['Q']
    elif w==3:
        for k in NyE:
            if i==k['ID']:
                W=k['HGL']
    elif w==4:
        for k in graph[i]:
            for m in Pipes:
                if i in m['NIyNF'] and k in m['NIyNF']:
                    W=W+m['D']
    return W

def box_builder(node,step):
    box=list()
    nd=np.where(SD[int(node)-1]<=step)[0]+1
    w=[i for i in NyE if i['ID']==node][0]['W']
    for i in nd:
        f=[item for item in NyE if item['ID']==i]
        if f[0]['Free'] == 0:
            box.append(i)
            w=w+f[0]['W']
    return box,w

m=0

for i in Networks:
    File=open(i,"r")
    Lines=File.readlines()
    
    NumNodes=int(Lines[0])
    NumReservoirs=int(Lines[1])
    NumPipes=int(Lines[2])
    
    Nodes=list()
    NyE=list()
    
    for i in range(NumNodes):
        Var=dict()
        Var['ID']=int(Lines[3+i])
        Var['X']=float(Lines[3+NumNodes+i])
        Var['Y']=float(Lines[3+2*NumNodes+i])
        Var['Z']=float(Lines[3+3*NumNodes+i])
        Var['Q']=float(Lines[3+4*NumNodes+i])
        Var['HGL']=float(Lines[3+5*NumNodes+i])
        Var['W']=0
        Var['Free']=0
        Nodes.append(Var)
        NyE.append(Var)
    
    Reservoirs=list()
    
    for i in range(NumReservoirs):
        Var=dict()
        Var['ID']=int(Lines[3+6*NumNodes+i])
        Var['X']=float(Lines[3+6*NumNodes+NumReservoirs+i])
        Var['Y']=float(Lines[3+6*NumNodes+2*NumReservoirs+i])
        Var['Z']=float(Lines[3+6*NumNodes+3*NumReservoirs+i])
        Var['HGL']=float(Lines[3+6*NumNodes+4*NumReservoirs+i])
        Var['W']=0
        Var['Free']=0
        Reservoirs.append(Var)
        NyE.append(Var)
    
    Pipes=list()
    
    for i in range(NumPipes):
        Var=dict()
        Var['ID']=int(Lines[3+6*NumNodes+5*NumReservoirs+i])
        Var['NI']=int(Lines[3+6*NumNodes+5*NumReservoirs+NumPipes+i])
        Var['NF']=int(Lines[3+6*NumNodes+5*NumReservoirs+2*NumPipes+i])
        Var['NIyNF']=[Var['NI'],Var['NF']]
        Var['D']=float(Lines[3+6*NumNodes+5*NumReservoirs+3*NumPipes+i])
        Var['L']=float(Lines[3+6*NumNodes+5*NumReservoirs+4*NumPipes+i])
        Var['km']=float(Lines[3+6*NumNodes+5*NumReservoirs+5*NumPipes+i])
        Var['Q']=float(Lines[3+6*NumNodes+5*NumReservoirs+6*NumPipes+i])
        Pipes.append(Var)
        
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

    grid_x , grid_y=np.mgrid[Xmin:Xmax:StepSizeL[m],Ymin:Ymax:StepSizeL[m]]
    
    HGLInt1=griddata((HGLX,HGLY),HGLZ,(grid_x,grid_y),method='linear')
    HGLInt2=np.nan_to_num(HGLInt1, copy=True, nan=0.0, posinf=None, neginf=None)
    
    numrows=len(HGLInt2)
    numcols=len(HGLInt2[0])
    Rmax=math.floor((min(numrows,numcols)-1)/2)
    
    Radius=list()
    Variation=list()
    
    for R in range(1,Rmax):
        L=2*R+1
        NDH=numrows-L+1
        NDV=numcols-L+1
        ad=0
        el=0
        for j in range(NDH):
            for k in range(NDV):
                var=cal_var(HGLInt2,L,k,j)
                if math.isnan(var) == False:
                    ad=ad+var
                    el=el+1
        Ve=float(ad/el)
        Variation.append(Ve)
        Radius.append(R)
    
    LogVe=np.log10(Variation)
    LogRad=np.log10(Radius)
    mVar,bVar,rVar,pVar,stdVar=linregress(LogRad,LogVe)
    
    CDVar=rVar**2
    DVar=3-mVar
    DOHGS.append(round(DVar,4))
    R2OHGS.append(round(CDVar,2))
    
    m=m+1
    
    NE=NumNodes+NumReservoirs
    
    aR=0
    for i in NyE:
        aR=aR+1
        i['ID']=aR
        for j in Pipes:
            if j['NIyNF'][0]==i['ID']:
                j['NIyNF'][0]=aR
            elif j['NIyNF'][1]==i['ID']:
                j['NIyNF'][1]=aR
    
    graph=dict()
    for i in NyE:
        Var=list()
        for j in Pipes:
            try:
                v=j['NIyNF'].index(i['ID'])
            except ValueError:
                v=-1
            if v==0:
                Var.append(j['NIyNF'][1])
            elif v==1:
                Var.append(j['NIyNF'][0])  
        graph[i['ID']]=Var
        
    A=np.zeros((NE,NE))
    
    for i in range(NE):
        for j in range(NE):
            a=0
            for t in Pipes:
                if (i+1) in t['NIyNF'] and (j+1) in t['NIyNF']:
                    a=1
            if i==j:
                a=0
            A[i][j]=a
    
    SD=shortest_path(A,method='D',directed=False)
    
    for k in WCriterion:
        logNB=list()
        logLB=list()
        Step=list()
        NBVect=list()
        LBVect=list()
        
        for i in NyE:
            i['W']=indweight_calculator(i['ID'],k)
        
        if NE<250:
            LB=-1
            if NE%2==0:
                LBmax=NE-1
            else:
                LBmax=NE
            while LB<LBmax:
                LB=LB+2
                LBVect.append(LB)
                NB=0
                FU=NE
                for i in NyE:
                    i['Free']=0
                step=(LB-1)/2
                Step.append(step)
                W=0
                Box=list()
                if step==0:
                    NB=NE
                    logNB.append(np.log10(NB))
                    logLB.append(np.log10(LB))
                    NBVect.append(NB)
                else:
                    while FU>0:
                        for j in NyE:
                            if j['Free']==0:
                                box,w=box_builder(j['ID'],step)     
                            if w>W:
                                W=w
                                Box=box
                        if Box:
                            NB=NB+1
                            FU=FU-len(Box)
                            for i in NyE:
                                if i['ID'] in Box:
                                    i['Free']=1;
                        W=0
                    NBVect.append(NB)
                    logNB.append(np.log10(NB))
                    logLB.append(np.log10(LB))
            MaxBoxNum=logNB[-1]
            logNBnew=list()
            logLBnew=list()
            
            for i in range(len(logNB)):
                if logNB[i]!=MaxBoxNum:
                    logNBnew.append(logNB[i])
                    logLBnew.append(logLB[i])
                else:
                    logNBnew.append(logNB[i])
                    logLBnew.append(logLB[i])
                    break
            mBC,bBC,rBC,pBC,sBC=linregress(logLBnew,logNBnew)
            FractalDimension=-mBC
            CD=rBC**2
            
        else:
            LBVect.append(1)
            if np.ceil(np.sqrt(NE))%2==0:
                LBmax=np.ceil(np.sqrt(NE)-1)
            else:
                LBmax=np.ceil(np.sqrt(NE))
            LBVect.append(LBmax)
            LBVect.insert(1,LBmax-2)
            LBVect.insert(1,LBmax-4)
            LBVect.insert(1,LBmax-6)
            LBVect.insert(1,LBmax-8)
            LBVect.insert(1,LBmax-10)
            
            for s in LBVect:
                NB=0
                FU=NE
                for i in NyE:
                    i['Free']=0
                step=(s-1)/2
                Step.append(step)
                W=0
                Box=list()
                if step==0:
                    NB=NE
                    logNB.append(np.log10(NB))
                    logLB.append(np.log10(s))
                    NBVect.append(NB)
                else:
                    while FU>0:
                        for j in NyE:
                            if j['Free']==0:
                                box,w=box_builder(j['ID'],step)     
                            if w>W:
                                W=w
                                Box=box
                        if Box:
                            NB=NB+1
                            FU=FU-len(Box)
                            for i in NyE:
                                if i['ID'] in Box:
                                    i['Free']=1;
                        W=0
                    NBVect.append(NB)
                    logNB.append(np.log10(NB))
                    logLB.append(np.log10(s))
            mBC,bBC,rBC,pBC,sBC=linregress(logLB,logNB)
            FractalDimension=-mBC
            CD=rBC**2
        
        if k==1:
            DTopology.append(round(FractalDimension,4))
            R2Topology.append(round(CD,2))
        if k==2:
            DFlow.append(round(FractalDimension,4))
            R2Flow.append(round(CD,2))
        if k==3:
            DEnergy.append(round(FractalDimension,4))
            R2Energy.append(round(CD,2))
        if k==4:
            DInfrastructural.append(round(FractalDimension,4))
            R2Infrastructural.append(round(CD,2))

Table2 = open("ID_26.txt", "w")

t=1

Table2.write("\n")
Table2.write("\n")
Table2.write("---------------------\n")
Table2.write("OHGS\n")
Table2.write("---------------------\n")

Table2.write("D")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(DOHGS[i]))

Table2.write("\n")
Table2.write("---------------------\n")

Table2.write("R2")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(R2OHGS[i]))

Table2.write("\n")
Table2.write("\n")
Table2.write("---------------------\n")
Table2.write("Topological criterion\n")
Table2.write("---------------------\n")

Table2.write("D")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(DTopology[i]))

Table2.write("\n")
Table2.write("---------------------\n")

Table2.write("R2")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(R2Topology[i]))

Table2.write("\n")
Table2.write("\n")
Table2.write("---------------------\n")
Table2.write("Flow criterion\n")
Table2.write("---------------------\n")

Table2.write("D")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(DFlow[i]))

Table2.write("\n")
Table2.write("---------------------\n")

Table2.write("R2")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(R2Flow[i]))

Table2.write("\n")
Table2.write("\n")
Table2.write("---------------------\n")
Table2.write("Energy criterion\n")
Table2.write("---------------------\n")

Table2.write("D")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(DEnergy[i]))

Table2.write("\n")
Table2.write("---------------------\n")

Table2.write("R2")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(R2Energy[i]))

Table2.write("\n")
Table2.write("\n")
Table2.write("---------------------\n")
Table2.write("Infrastructural criterion\n")
Table2.write("---------------------\n")

Table2.write("D")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(DInfrastructural[i]))

Table2.write("\n")
Table2.write("---------------------\n")

Table2.write("R2")
for i in range(t):
    Table2.write("\n")
    Table2.write(str(R2Infrastructural[i]))

Table2.close()