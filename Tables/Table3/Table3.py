# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:43:14 2021

@author: Andrés Jaramillo
"""

import statistics

F=[[0.9428,0.9428,0.9428,0.9342,1.0977,0.9221,0.9221,0.9428,0.9342,0.9221,0.9221],
[1.0517,0.9311,	1.0517,	0.9311,	1.0517,	1.0317,	1.0317,	0.9311,	1.0317,	1.0517,	1.0517],
[1.0908,1.0963,	1.1126,	1.0773,	1.1126,	1.0963,	1.1126,	1.1126,	1.0963,	1.0745,	1.0963],
[1.1686,1.1686,	1.1686,	1.1686,	1.2088,	1.1686,	1.1538,	1.1538,	1.1686,	1.1686,	1.1686],
[1.0698,1.0698,	1.0698,	1.0605,	1.0605,	1.0698,	1.0698,	1.0605,	1.0605,	1.0794,	1.0794],
[1.4307,1.4307,	1.4086,	1.2537,	1.4185,	1.4391,	1.4086,	1.3978,	1.2537,	1.4307,	1.4086],
[1.0524,1.0458,	1.0524,	1.0524,	1.0524,	1.0524,	0.9312,	1.0524,	0.9368,	1.0458,	1.0524],
[1.0899,1.0899,	1.0899,	1.0899,	1.0899,	1.0794,	1.0734,	1.0839,	1.0839,	1.3098,	1.0839],
[1.2940,1.2940,	1.3006,	1.2860,	1.2760,	1.2760,	1.2940,	1.2860,	1.2796,	1.2840,	1.3039],
[1.2738,1.2700,	1.2559,	1.2559,	1.2944,	1.2944,	1.2285,	1.2652,	1.2917,	1.1807,	1.2700],
[0.9252,0.9307,	0.9602,	0.9733,	1.0346,	1.0354,	0.9685,	0.9770,	0.9936,	0.9941,	0.9436],
[1.2085,1.1946,	1.2232,	1.1962,	1.2085,	1.2078,	1.2283,	1.2055,	1.1916,	1.1956,	1.2095],
[0.5712,0.5710,	0.5696,	0.5724,	0.5717,	0.5717,	0.5717,	0.5728,	0.5727,	0.5717,	0.5717],
[1.1575,1.1575,	1.1575,	1.1542,	1.1575,	1.1575,	1.1542,	1.1575,	1.1575,	1.1575,	1.1575],
[1.2443,1.2443,	1.2443,	1.2443,	1.2443,	1.2443,	1.2443,	1.2443,	1.2443,	1.2443,	1.2443],
[0.6192,0.6192,	0.6192,	0.6192,	0.6192,	0.6192,	0.6192,	0.6192,	0.6192,	0.6192,	0.6192],
[1.2397,1.2428,	1.2428,	1.2397,	1.2428,	1.1536,	1.2397,	1.2397,	1.2431,	1.2398,	1.2412],
[0.9816,0.9649,	0.9393,	0.9830,	0.9594,	0.9639,	0.9726,	0.9696,	0.9734,	0.9983,	0.9833],
[1.3054,1.3054,	1.3146,	1.3006,	1.3001,	1.3001,	1.3078,	1.2991,	1.2881,	1.3363,	1.2794],
[1.1153,1.1180,	1.1182,	1.1180,	1.1141,	1.1230,	1.1314,	1.1181,	1.1430,	1.1213,	1.1253],
[1.1863,1.1863,	1.1909,	1.1899,	1.1880,	1.2051,	1.1758,	1.1991,	1.2674,	1.2509,	1.2635],
[1.0582,1.0582,	1.0781,	1.1246,	1.0462,	1.0720,	1.1318,	1.0317,	1.1276,	1.1186,	1.0371],
[1.2084,1.2084,	1.1887,	1.1927,	1.1717,	1.1961,	1.1958,	1.1993,	1.1793,	1.1963,	1.1822],
[1.2806,1.2518,	1.2615,	1.2311,	1.2382,	1.2279,	1.2451,	1.2051,	1.2222,	1.2376,	1.2391],
[0.4657,0.4647,	0.4530,	0.4279,	0.4153,	0.4152,	0.4167,	0.4249,	0.4171,	0.4172,	0.4162],
[0.4030,0.4027,	0.4030,	0.4028,	0.4027,	0.4023,	0.4023,	0.4032,	0.4033,	0.4030,	0.4030],
[1.4533,1.4489,	1.4616,	1.4637,	1.4941,	1.4614,	1.4515,	1.4757,	1.5086,	1.5239,	1.5009],
[1.0871,1.0871,	1.0903,	1.0948,	1.1059,	1.1029,	1.1072,	1.1706,	1.1795,	1.1089,	1.1184]]

E=[[1.1394,1.1394,	1.1981,	1.1981,	1.1394,	1.1394,	1.1394,	1.1981,	1.1981,	1.1981,	1.1981],
[1.2319,1.2386,	1.2386,	1.2386,	1.2386,	1.2386,	1.2386,	1.2386,	1.2319,	1.2319,	1.2386],
[1.2768,1.2768,	1.2768,	1.2768,	1.2768,	1.2768,	1.2768,	1.2768,	1.2768,	1.2768,	1.2768],
[1.3755,1.3755,	1.3755,	1.3853,	1.3944,	1.3755,	1.3755,	1.3755,	1.3755,	1.3755,	1.3755],
[1.2107,1.2042,	1.2107,	1.2042,	1.2042,	1.2042,	1.2042,	1.1998,	1.1998,	1.2107,	1.2107],
[1.4158,1.4158,	1.4158,	1.4158,	1.4158,	1.4158,	1.4158,	1.4158,	1.4158,	1.4059,	1.4158],
[1.0617,1.0469,	1.0469,	1.0617,	1.0469,	1.0535,	1.0389,	1.0683,	1.0469,	1.0617,	1.0683],
[1.3018,1.3018,	1.3018,	1.3018,	1.3018,	1.3018,	1.3018,	1.3018,	1.3018,	1.3018,	1.3018],
[1.4495,1.4495,	1.4435,	1.4396,	1.4396,	1.4396,	1.4396,	1.4396,	1.4396,	1.4396,	1.4396],
[1.322,	1.3114,	1.3169,	1.325,	1.3114,	1.3114,	1.3275,	1.3549,	1.3289,	1.3468,	1.334],
[0.6105,0.6074,	0.6074,	0.6045,	0.6089,	0.5961,	0.6002,	0.6014,	0.6012,	0.5956,	0.5979],
[1.2489,1.2588,	1.2596,	1.2588,	1.2322,	1.2362,	1.2482,	1.237,	1.2362,	1.2378,	1.2378],
[0.5877,0.5816,	0.5877,	0.5823,	0.5877,	0.5877,	0.5864,	0.582,	0.5819,	0.5819,	0.5819],
[1.1274,1.1274,	1.1071,	1.1071,	1.1071,	1.1274,	1.1071,	1.1274,	1.1071,	1.1274,	1.1274],
[1.2163,1.2163,	1.2163,	1.2163,	1.2256,	1.2163,	1.2163,	1.221,	1.2256,	1.2256,	1.221],
[0.112,	0.112,	0.112,	0.1086,	0.112,	0.1086,	0.112,	0.1141,	0.112,	0.112,	0.1141],
[1.1652,1.1673,	1.1673,	1.1673,	1.1673,	1.1673,	1.1652,	1.1673,	1.1652,	1.1694,	1.1742],
[1.0108,1.0102,	1.0117,	1.0111,	1.0129,	1.0192,	1.0392,	1.0219,	1.0111,	1.0016,	1.0373],
[1.2747,1.2747,	1.2747,	1.2747,	1.2747,	1.2747,	1.2747,	1.2747,	1.2554,	1.2747,	1.2747],
[1.1541,1.1541,	1.1541,	1.1541,	1.1541,	1.1658,	1.1658,	1.1519,	1.166,	1.1912,	1.1658],
[1.183,	1.183,	1.183,	1.1809,	1.183,	1.1831,	1.183,	1.1872,	1.183,	1.1811,	1.183],
[1.2351,1.2307,	1.2351,	1.2353,	1.225,	1.2239,	1.2297,	1.2353,	1.2307,	1.2254,	1.2309],
[1.2441,1.2441,	1.2441,	1.2441,	1.2455,	1.2441,	1.2441,	1.2441,	1.2441,	1.2441,	1.241],
[1.3435,1.3435,	1.3435,	1.3435,	1.3435,	1.3435,	1.3435,	1.3435,	1.3435,	1.3475,	1.3435],
[0.4192,0.4190,	0.4186,	0.4186,	0.4186,	0.4188,	0.4192,	0.4188,	0.4188,	0.4184,	0.4188],
[0.2041,0.2041,	0.2041,	0.2041,	0.2041,	0.2041,	0.2042,	0.2042,	0.2042,	0.2041,	0.2041],
[1.4793,1.4882,	1.4882,	1.4522,	1.4522,	1.4648,	1.4522,	1.4522,	1.4522,	1.4522,	1.4522],
[1.1321,1.1352,	1.1321,	1.1321,	1.1321,	1.1352,	1.1321,	1.1321,	1.1321,	1.1321,	1.1352]]

I=[[1.0977,1.0977,	1.0977,	0.9221,	1.0977,	1.0977,	1.0977,	1.1394,	1.1394,	1.1981,	0.9221],
[1.0317,1.0317,	0.9382,	0.9382,	0.9382,	0.9382,	0.9382,	0.9382,	1.0317,	0.9382,	0.9635],
[1.2996,1.2768,	1.2996,	1.2996,	1.1996,	1.2224,	1.2224,	1.2907,	1.2768,	1.1368,	1.2224],
[1.2517,1.2517,	1.2517,	1.289,	1.289,	1.289,	1.3815,	1.3815,	1.3905,	1.3944,	1.3944],
[1.2208,1.2142,	1.2142,	1.2173,	1.2173,	1.2274,	1.2173,	1.2274,	1.2274,	1.2274,	1.2173],
[1.4059,1.3346,	1.4391,	1.4135,	1.4185,	1.3978,	1.4158,	1.2327,	1.4158,	1.3401,	1.4216],
[1.0296,1.0376,	1.0617,	1.0444,	1.0444,	1.0535,	1.0442,	1.0469,	1.0444,	1.0296,	1.0524],
[1.3073,1.3073,	1.3073,	1.3048,	1.3073,	1.2893,	1.3048,	1.1934,	1.2893,	1.3,	1.2438],
[1.4495,1.4495,	1.3508,	1.467,	1.4495,	1.4586,	1.4586,	1.4495,	1.4495,	1.3841,	1.3841],
[1.298,	1.3114,	1.3169,	1.325,	1.3114,	1.3114,	1.3275,	1.3549,	1.3289,	1.3468,	1.334],
[0.8867,0.854,	0.9676,	0.9432,	0.9949,	0.978,	0.9224,	0.939,	0.9777,	0.9267,	0.9807],
[1.2676,1.2653,	1.2168,	1.2335,	1.2466,	1.2424,	1.2271,	1.2473,	1.2553,	1.2634,	1.2546],
[0.5787,0.5806,	0.5816,	0.5796,	0.5787,	0.5787,	0.5787,	0.5799,	0.5796,	0.5744,	0.5744],
[1.1191,1.1244,	1.0938,	1.0842,	1.1077,	1.09,	1.1089,	1.115,	1.1284,	1.1285,	1.1234],
[1.1902,1.1961,	1.1855,	1.1998,	1.2101,	1.1835,	1.1965,	1.2018,	1.2636,	1.1904,	1.2094],
[0.6558,0.5293,	0.428,	0.6558,	0.5982,	0.5098,	0.6534,	0.6192,	0.6537,	0.6534,	0.4855],
[1.1392,1.1407,	1.1427,	1.1426,	1.1567,	1.1552,	1.1083,	1.1037,	1.0961,	1.203,	1.1972],
[1.0016,1.028,	0.9856,	0.9743,	0.9907,	0.9808,	0.9822,	0.9994,	0.9805,	1.0133,	0.9833],
[1.2347,1.2337,	1.2335,	1.3118,	1.3286,	1.3276,	1.2287,	1.3177,	1.2374,	1.262,	1.2694],
[1.1456,1.1456,	1.1307,	1.1477,	1.1403,	1.1623,	1.1573,	1.0615,	1.1432,	1.1453,	1.1124],
[1.1235,1.1345,	1.1796,	1.1608,	1.1612,	1.1574,	1.1479,	1.1518,	1.1852,	1.1642,	1.188],
[1.1736,1.1751,	1.1644,	1.176,	1.2238,	1.2573,	1.2112,	1.2318,	1.1752,	1.227,	1.1517],
[1.2167,1.2167,	1.2092,	1.2065,	1.2224,	1.2095,	1.2174,	1.2278,	1.2084,	1.2131,	1.1898],
[1.3184,1.3376,	1.2896,	1.2907,	1.3141,	1.3347,	1.2966,	1.3295,	1.2851,	1.2736,	1.2403],
[0.4167,0.4176,	0.4168,	0.4163,	0.4151,	0.4167,	0.4175,	0.4157,	0.4191,	0.4125,	0.4152],
[0.2042,0.2042,	0.2041,	0.204,	0.204,	0.2042,	0.204,	0.2043,	0.2038,	0.2036,	0.2036],
[1.4482,1.4547,	1.4533,	1.4533,	1.4549,	1.4426,	1.4426,	1.4337,	1.4398,	1.4459,	1.4588],
[1.1159,1.1115,	1.1178,	1.1065,	1.1182,	1.1094,	1.1012,	1.1068,	1.0936,	1.1162,	1.1043]]

std_F=list()
std_E=list()
std_I=list()

max_F=list()
max_E=list()
max_I=list()

min_F=list()
min_E=list()
min_I=list()

CF_F=list()
CF_E=list()
CF_I=list()

for i in range(28): 
    std_F.append(statistics.stdev(F[i]))
    std_E.append(statistics.stdev(E[i]))
    std_I.append(statistics.stdev(I[i]))
    
    max_F.append(max(F[i]))
    max_E.append(max(E[i]))
    max_I.append(max(I[i]))
    
    min_F.append(min(F[i]))
    min_E.append(min(E[i]))
    min_I.append(min(I[i]))
    
    OptF=F[i][0]
    OptE=E[i][0]
    OptI=I[i][0]
    
    cF=0
    cE=0
    cI=0
    
    for j in range(1,11):
        if F[i][j]<=OptF:
            cF=cF+1
        if E[i][j]<=OptE:
            cE=cE+1
        if I[i][j]<=OptI:
            cI=cI+1
    
    CF_F.append(cF)
    CF_E.append(cE)
    CF_I.append(cI)

list_tabulate=list()
ID=0

for i in range(28):
    dummy=list()
    ID=ID+1
    dummy.append(ID)
    dummy.append(CF_F[i])
    dummy.append(std_F[i])
    dummy.append(min_F[i])
    dummy.append(max_F[i])
    
    dummy.append(CF_E[i])
    dummy.append(std_E[i])
    dummy.append(min_E[i])
    dummy.append(max_E[i])
    
    dummy.append(CF_I[i])
    dummy.append(std_I[i])
    dummy.append(min_I[i])
    dummy.append(max_I[i])
    
    list_tabulate.append(dummy)
    
Table3 = open("Table3.txt", "w")
Table3.write("---------------------\n")
Table3.write("ID")

ID=range(1,29)

for i in range(28):
    Table3.write("\n")
    Table3.write(str(ID[i]))
    
Table3.write("\n")
Table3.write("\n")
Table3.write("---------------------\n")
Table3.write("Flow criterion\n")
Table3.write("---------------------\n")

Table3.write("CF")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(CF_F[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("s")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(round(std_F[i],3)))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmin")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(min_F[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmax")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(max_F[i]))

Table3.write("\n")
Table3.write("\n")
Table3.write("---------------------\n")
Table3.write("Energy criterion\n")
Table3.write("---------------------\n")

Table3.write("CF")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(CF_E[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("s")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(round(std_E[i],3)))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmin")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(min_E[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmax")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(max_E[i]))
    
Table3.write("\n")
Table3.write("\n")
Table3.write("---------------------\n")
Table3.write("Infrastructural criterion\n")
Table3.write("---------------------\n")

Table3.write("CF")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(CF_I[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("s")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(round(std_I[i],3)))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmin")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(min_I[i]))

Table3.write("\n")
Table3.write("---------------------\n")

Table3.write("Dmax")
for i in range(28):
    Table3.write("\n")
    Table3.write(str(max_I[i]))

Table3.close()