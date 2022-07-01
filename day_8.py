# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:35:24 2021

@author: justi
"""

import numpy as np
from numpy import loadtxt
lines = loadtxt("input day 8.txt",dtype=np.str, delimiter="|")
# lines = loadtxt("input day 8 poubelle.txt",dtype=np.str, delimiter="|")

#-------part 1-------------
# somme=0
# for l in lines:
#     ligne1bis=l[1].split()
#     for element in ligne1bis:
#         if len(element)==2:
#             somme+=1
#         elif len(element)==4:
#             somme+=1
#         elif len(element)==3:
#             somme+=1
#         elif len(element)==7:
#             somme+=1

        
#-------part 2-----------------


def prob(L1,x,grille):    
    
    if x==51:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,3]+=1/3
            grille[i,0]+=1/3
            grille[i,6]+=1/3
    elif x==52:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,2]+=1/4
            grille[i,1]+=1/4
            grille[i,4]+=1/4
            grille[i,5]+=1/4
    elif x==61:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,1]+=1/4
            grille[i,5]+=1/4
            grille[i,0]+=1/4
            grille[i,6]+=1/4
    elif x==62:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,2]+=1/3
            grille[i,3]+=1/3
            grille[i,4]+=1/3
    elif x==41:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,1]+=1/4
            grille[i,2]+=1/4
            grille[i,3]+=1/4
            grille[i,5]+=1/4
    elif x==31:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,2]+=1/3
            grille[i,0]+=1/3
            grille[i,5]+=1/3
    elif x==21:
        for element in L1:
            if element=='a':
                i=0
            elif element=='b':
                i=1
            elif element=='c':
                i=2
            elif element=='d':
                i=3
            elif element=='e':
                i=4
            elif element=='f':
                i=5
            elif element=='g':
                i=6
            grille[i,2]+=1/2
            grille[i,5]+=1/2

def resolution_1_ligne(x): 
    grille=np.zeros((7,7))
    L5=[]
    L6=[]
    for element in lines[x][0].split():
        if len(element)==5:
            L5.append(element)
        elif len(element)==6:
            L6.append(element)
        elif len(element)==3:
            L3=list(element)
        elif len(element)==2:
            L2=list(element)
        elif len(element)==4:
            L4=list(element)
    L5a=set(L5[0]).intersection(L5[1],L5[2])
    L5b=L5a^{'a','b','c','d','e','f','g'}
    L5a=list(L5a)
    L5b=list(L5b)
    L6a=set(L6[0]).intersection(L6[1],L6[2])
    L6b=L6a^{'a','b','c','d','e','f','g'}
    L6a=list(L6a)
    L6b=list(L6b)
    
    prob(L5a,51,grille)
    prob(L5b,52,grille) 
    prob(L6a,61,grille)
    prob(L6b,62,grille)
    prob(L3,31,grille)
    prob(L4,41,grille)
    prob(L2,21,grille)
    
    maximum=[]
    for i in range(len(grille)):
        maximum.append([np.amax(grille[i]),np.where(grille[i]==np.amax(grille[i]))[0],i])
    maximum=np.array(maximum,dtype=object)
    
    A=sorted(maximum, key=lambda value: value[0],reverse=True)
    
    indices=[]
    indices_ligne=[]
    for j in range(len(grille)):
        if A[j][1][0] not in indices:
            indices.append(A[j][1][0])
            indices_ligne.append(A[j][2])
        else:
            indices.append(A[j][1][1])
            indices_ligne.append(A[j][2])
            
    final=list(zip(indices,indices_ligne))
    
    decodage_tot=[]
    for element in lines[x][1].split():
        decodage=[]
        for lettre in element:
            if lettre=='a':
                for i in range(len(final)):
                    if final[i][1]==0:
                        decodage.append(final[i][0])
            elif lettre=='b':
                for i in range(len(final)):
                    if final[i][1]==1:
                        decodage.append(final[i][0])
            elif lettre=='c':
                for i in range(len(final)):
                    if final[i][1]==2:
                        decodage.append(final[i][0])
            elif lettre=='d':
                for i in range(len(final)):
                    if final[i][1]==3:
                        decodage.append(final[i][0])
            elif lettre=='e':
                for i in range(len(final)):
                    if final[i][1]==4:
                        decodage.append(final[i][0])
            elif lettre=='f':
                for i in range(len(final)):
                    if final[i][1]==5:
                        decodage.append(final[i][0])
            elif lettre=='g':
                for i in range(len(final)):
                    if final[i][1]==6:
                        decodage.append(final[i][0])
        decodage_tot.append(decodage)
    
    nombre=0
    L=len(decodage_tot)
    for i in range(L):
        if sorted(decodage_tot[i])==[0,1,2,4,5,6]:
            nombre+=0*10**(L-i-1)
        elif sorted(decodage_tot[i])==[2,5]:
            nombre+=1*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,2,3,4,6]:
            nombre+=2*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,2,3,5,6]:
            nombre+=3*10**(L-i-1)
        elif sorted(decodage_tot[i])==[1,2,3,5]:
            nombre+=4*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,1,3,5,6]:
            nombre+=5*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,1,3,4,5,6]:
            nombre+=6*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,2,5]:
            nombre+=7*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,1,2,3,4,5,6]:
            nombre+=8*10**(L-i-1)
        elif sorted(decodage_tot[i])==[0,1,2,3,5,6]:
            nombre+=9*10**(L-i-1)
    return nombre


total=0
for l in range(len(lines)):
    total+=resolution_1_ligne(l)

print(total)