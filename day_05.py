# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:58:31 2021

@author: justi
"""
import numpy as np
import matplotlib.pyplot as plt
f=open("input day 5.txt","r")
lines=f.readlines()
lines=[n.split() for n in lines]
for lignes in lines:
    for element in lignes: 
        if element=='->':
           lignes.remove(element) 
lines=[ [list(map(int,m.split(','))) for m in lines[n] ] for n in range(len(lines)) ]

grille=np.zeros((1000,1000))


#--------part 1----------------------
for i in range(len(lines)):
    if lines[i][0][0]==lines[i][1][0] and lines[i][0][1]!=lines[i][1][1]:
        indice1=lines[i][0][1]
        indice2=lines[i][1][1]
        if indice1<indice2:
            grille[indice1:indice2+1,lines[i][0][0]]+=1
        else:
            grille[indice2:indice1+1,lines[i][0][0]]+=1
    elif lines[i][0][0]!=lines[i][1][0] and lines[i][0][1]==lines[i][1][1]:
        indice1=lines[i][0][0]
        indice2=lines[i][1][0]
        if indice1<indice2:
            grille[lines[i][0][1],indice1:indice2+1]+=1
        else:
            grille[lines[i][0][1],indice2:indice1+1]+=1
#--------part 2----------------------
    elif lines[i][0][0]!=lines[i][1][0] and lines[i][0][1]!=lines[i][1][1]:
        
        x1=lines[i][0][0]
        x2=lines[i][1][0]
        y1=lines[i][0][1]
        y2=lines[i][1][1]
        if (x1<x2 and y1<y2) or (x1>x2 and y1>y2):
            for w in range(abs(x2-x1)+1):
                grille[min(y1,y2)+w,min(x1,x2)+w]+=1
        elif (x1>x2 and y1<y2) or (x1<x2 and y1>y2):
            for j in range(abs(x2-x1)+1):
                grille[min(y1,y2)+j,max(x1,x2)-j]+=1

#---------------------------------------
count=0
for i in range(len(grille)):
    for j in range(len(grille[0])):
        if grille[i,j]>=2:
            count+=1
