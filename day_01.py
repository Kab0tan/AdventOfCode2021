# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:31:24 2021

@author: justi
"""

from numpy import loadtxt
lines = loadtxt("input day 1.txt", comments="#", delimiter=",", unpack=False)
print(lines)


#------------part 1--------------------

count=0
for i in range(1,len(lines)):
    if lines[i]>lines[i-1]:
        count+=1        
print(count)


#--------part 2-------------------------

count3=0
for i in range(len(lines)-2):
    if sum(lines[i:i+3])<sum(lines[i+1:i+4]):
        count3+=1      
print(count3)
