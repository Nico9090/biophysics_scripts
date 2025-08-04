#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
L1=[]
PKHD1=[]
with open("L1vs1.txt",'r')as aligned_seq:
    for line in aligned_seq:
        if line.startswith("Query "):
            L1.append(line[13:72])
        elif line.startswith("Sbjct"):
            PKHD1.append(line[13:72])
separator = ''
L1=separator.join(L1)
for i in L1:
    if i.isdigit():
        L1=L1.replace(i,"")
L1=" ".join(L1.split())
PKHD1=separator.join(PKHD1)
for i in PKHD1:
    if i.isdigit():
        PKHD1=PKHD1.replace(i,"")
PKHD1=" ".join(PKHD1.split())
#print(PKHD1)

dot_plot = np.zeros((len(L1), len(PKHD1)))

for i in range(len(L1)):
   for j in range(len(PKHD1)):
      if L1[i] == PKHD1[j]:
         dot_plot[i, j] = 1

plt.figure(figsize=(10, 10))
plt.imshow(dot_plot, cmap='binary',interpolation='nearest')
plt.xticks(ticks=np.arange(0, len(L1), step=500), labels=list(np.arange(0,len(L1))[::500]))
plt.yticks(ticks=np.arange(0, len(PKHD1), step=500), labels=list(np.arange(0,len(PKHD1))[::500]))
plt.xlabel('PKHD1L1')
plt.ylabel('PKHD1')
plt.title('PKHD1 and PKHD1L1 Conservation in Humans')
plt.show()
