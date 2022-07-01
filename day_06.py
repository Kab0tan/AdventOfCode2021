# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:52:11 2021

@author: justi
"""
import time
start_time = time.time()


import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt
lines = loadtxt("input day 6.txt", delimiter=",")


#------------part 1---------------
# long=np.array([])
# nb_day=80
# for day in range(nb_day):
#     print("jour", day)
#     print((lines))
#     print(len(lines))
#     long=np.append(long,len(lines))
#     if 0 in lines:
#         nb_zero=np.count_nonzero(lines==0)
#         lines=np.where(lines==0,7,lines)
#         for i in range(nb_zero):
#             lines=np.append(lines,9)
#     lines-=1

# print(len(lines))
#------------part 2-----------------

long=np.array([])
nb_day=4
for day in range(nb_day):
    # print("jour", day)
    # print((lines))
    # print(len(lines))
    long=np.append(long,len(lines))
    if 0 in lines:
        nb_zero=np.count_nonzero(lines==0)
        lines=np.where(lines==0,7,lines)
        for i in range(nb_zero):
            lines=np.append(lines,9)
    lines-=1

tab_num=[np.count_nonzero(lines==0),np.count_nonzero(lines==1),np.count_nonzero(lines==2),np.count_nonzero(lines==3),np.count_nonzero(lines==4),np.count_nonzero(lines==5),np.count_nonzero(lines==6),np.count_nonzero(lines==7),np.count_nonzero(lines==8)]

tab_num=np.int64(tab_num)
somme=0
somme=np.int64(somme)
for day in range(36):
    copie=np.copy(tab_num)        
    tab_num[0]+=tab_num[7]
    tab_num[1]+=tab_num[8]
    tab_num[2]+=copie[0]
    tab_num[3]+=copie[1]
    tab_num[4]+=copie[2]
    tab_num[5]+=copie[3]
    tab_num[6]+=copie[4]
    tab_num[7]=copie[5]
    tab_num[8]=copie[6]

for element in tab_num:
    somme+=element
    
print("somme=",somme)    
print("--- %s seconds ---" % (time.time() - start_time))


