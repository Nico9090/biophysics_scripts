#!/usr/bin/env python3
#Get all the coordinates into a list as a float
import math
import numpy as np
with open('filename','r')as atomsfile:
        xval=[]
        yval=[]
        for line in atomsfile:
                xval.append(line[32:39])
                yval.append(line[40:46])

xval = [i.strip(' ') for i in xval]
yval= [i.strip(' ') for i in yval]
xcoord=[]
ycoord=[]
for element in xval:
        xcoord.append(float(element))
for element in yval:
        ycoord.append(float(element))

#Calculating distances between everything
dist=[]
i=0
while i<=588:
        j=i+1
        dist.append(math.sqrt((xcoord[j]-xcoord[i])**2+ (ycoord[j]-ycoord[i])**2))
#print(dist)
i=588
t=2
dist2=[]
while i>0:
        while t<=588:
                dist2.append(math.sqrt((xcoord[i]-xcoord[i-t])**2+ (ycoord[i]-ycoord[i-t])**2))
                t+=1
        if t==589:
                i-=1
                t-=589
f=open('filename','w')
for num in dist2:
        print(num, file=f)
for num in dist:
        print(num, file=f)
  
