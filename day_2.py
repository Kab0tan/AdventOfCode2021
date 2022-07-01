# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:03:40 2021

@author: justi
"""


#----------part 1--------------------------------
import numpy as np
from numpy import loadtxt
lines = loadtxt("input day 2.txt",dtype=np.str, comments="#", delimiter=" ", unpack=False)

H=0
D=0
for i in range(len(lines)):
    if lines[i][0]=='forward':
        H+=int(lines[i][1])
    elif lines[i][0]=='down':
        D+=int(lines[i][1])
    else:
        D-=int(lines[i][1])
    
print(H*D)


#-----------part 2----------------------------------

A=0
H=0
D=0
for i in range(len(lines)):
    if lines[i][0]=='forward':
        H+=int(lines[i][1])
        D+=A*int(lines[i][1])
    elif lines[i][0]=='down':
        A+=int(lines[i][1])
    else:
        A-=int(lines[i][1])
        
print(H*D)