# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:53:33 2021

@author: justi
"""
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

with open("input day 9.txt") as lines:
# with open("input day 9 bin.txt") as lines:
    m = [[int(n) for n in list(line.strip())] for line in lines]

M=np.array(m)    

L=[]
I=[]
if m[0][0]<m[1][0] and m[0][0]<m[0][1]:#coin sup gauche
    L.append(m[0][0])
    I.append([0,0])
if m[0][len(m[0])-1]<m[1][len(m[0])-1] and m[0][len(m[0])-1]<m[0][len(m[0])-2]:#coin sup droit
    L.append(m[0][len(m[0])-1])
    I.append([0,len(m[0])-1])
if m[len(m)-1][0]<m[len(m)-2][0] and m[len(m)-1][0]<m[len(m)-1][1]:#coin inf gauche
    L.append(m[len(m)-1][0])
    I.append([len(m)-1,0])
if m[len(m)-1][len(m[0])-1]<m[len(m)-2][len(m[0])-1] and m[len(m)-1][len(m[0])-1]<m[len(m)-1][len(m[0])-2]:#coin in droit
    L.append(m[len(m)-1][len(m[0])-1])
    I.append([len(m)-1,len(m[0])-1])

for i in range(1,len(m[0])-1):
    if m[0][i]<m[0][i-1] and m[0][i]<m[0][i+1] and m[0][i]<m[1][i]:
        L.append(m[0][i])
        I.append([0,i])
    if m[len(m)-1][i]<m[len(m)-1][i-1] and m[len(m)-1][i]<m[len(m)-1][i+1] and m[len(m)-1][i]<m[len(m)-2][i]:
        L.append(m[len(m)-1][i])        
        I.append([len(m)-1,i])
for i in range(1,len(m)-1):
    if m[i][0]<m[i-1][0] and m[i][0]<m[i+1][0] and m[i][0]<m[i][1]:
        L.append(m[i][0])
        I.append([i,0])
    if m[i][len(m)-1]<m[i-1][len(m)-1] and m[i][len(m)-1]<m[i+1][len(m)-1] and m[i][len(m)-1]<m[i][len(m)-2]:
        L.append(m[i][len(m)-1])
        I.append([i,len(m)-1])

for j in range(1,len(m)-1):
    for l in range(1,len(m)-1):
        if m[j][l]<m[j+1][l] and m[j][l]<m[j-1][l] and m[j][l]<m[j][l+1] and m[j][l]<m[j][l-1]:
            L.append(m[j][l])
            I.append([j,l])
            
L=np.array(L)+1
print(sum(L))


indice=[]
def surrounding(i, j):
    count = 1
    for y1 in range(max(0, j - 1), min(j + 2, len(m[0]))):
        # if (m[i][y1] == m[i][j] + 1 or m[i][y1] == m[i][j]) and m[i][y1]!=9 and (i,y1) not in indice:
        if  m[i][y1]!=9 and (i,y1) not in indice:
            # print("y1=",(i,y1))
            # print("value=",m[i][y1])
            indice.append((i,y1))
            count += surrounding(i, y1)
    for x1 in range(max(0, i - 1), min(i + 2, len(m))):
        # if (m[x1][j] == m[i][j] + 1 or m[x1][j] == m[i][j]) and m[x1][j]!=9 and (x1,j) not in indice:
        if  m[x1][j]!=9 and (x1,j) not in indice:
            # print("x1=",(x1,j))
            # print("value=",m[x1][j])
            indice.append((x1,j))
            count += surrounding(x1, j)
    return count

bassin=[]
for i in range(len(I)):
    bassin.append(surrounding(I[i][0],I[i][1])-1)

bassin=sorted(bassin,reverse=True)
print(bassin[0]*bassin[1]*bassin[2])


# print(surrounding(87,92))
# print(surrounding(60,54))
