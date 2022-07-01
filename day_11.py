# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:22:28 2021

@author: justi
"""
import numpy as np
with open("input day 11.txt") as lines:
# with open("input day 11 bin.txt") as lines:
    m = [[int(n) for n in list(line.strip())] for line in lines]  

M=np.array(m)


#---part 1-----------------------                       
def step(M):
    M=M+1
    while np.any(M>=10):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i,j]>=10:
                    M[i,j]=0
                    for x in range(max(0,i-1),min(i+2,len(M))):
                        for y in range(max(0,j-1),min(j+2,len(M[0]))):
                            if M[x,y]!=0:
                                M[x,y]+=1
    return M


# flash_=0
# for i in range(100):
#     M=step(M)
#     flash_+=(M==0).sum()


#-------part 2-------------
iteration=0
while np.all(M==0)==False:
    M=step(M)
    iteration+=1