#!/usr/bin/env python3

#Density using an atom as a reference point and then N as the total number of the same atoms

with open('filename','r') as pdbfile: #Put the pdb file in place of filepath
        atoms=' '
        for line in pdbfile:
                if line[0:4]=='ATOM':
                        atoms+=line

atom_dest=open('filename','w')
print(atoms,file=atom_dest)

#Find the total number of atoms of the same type(testing nitrogen)

tot_atom=0
with open('filename','r')as atomsfile:
        for line in atomsfile:
                if line[13]=='N':
                        tot_atom+=1
print('Total number of nitrogen atoms is', tot_atom)

#Calculating the density with ρ(r¯)=∑i=1Nδ(r¯−ri¯)

#How to find position of the particle?
