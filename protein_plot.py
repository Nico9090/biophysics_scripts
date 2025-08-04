#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
with open("C:/Users/teemo/Downloads/fibrocystin_and_L_models/human_fc_parts/hfbr_1_to_500.pdb",'r')as pdb_file:
    x,y,z=[],[],[]
    for line in pdb_file:
        if line.startswith("ATOM"):
            x.append(float(line[32:39].strip()))
            y.append(float(line[41:47].strip()))
            z.append(float(line[49:55].strip()))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis',marker="+")
ax.set_xlim([min(x), max(x)])
ax.set_ylim([min(y), max(y)])
ax.set_zlim([min(z), max(z)])
#plt.show()

