#!/usr/bin/env python3
#Calculate volume
import math
import numpy as np
v=open('volumes.txt','w')

with open('distances.txt','r')as f:
        volume=[]
        for num in f:
                volume.append((4/3)*math.pi*(float(num))**2)
for x in volume:
        print(x,file=v)

#N is the total number of atoms?
N=173755

#g(r)
t=open('packing.txt','w')
g=[]
for x in volume:
        if x!=0:
                g.append(N/x)
for x in g:
        print(x,file=t)
