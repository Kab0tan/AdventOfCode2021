# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:32:52 2022

@author: justi
"""

import string
import pandas as pd
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

text = loadtxt("input day 13.txt",dtype=np.str, delimiter=",") #our coordinates
text2 = loadtxt("input day 13_2.txt",dtype=np.str, delimiter="=") #axis of folding

#deleting string 'fold along' to only get the axis letter
for line in text2:
    line[0] = line[0].strip('fold along')


text3 = text.astype(np.int64)

#extract each column of our coordinates table
x = text3[:,0]
y = text3[:,1]



#---------------part 1------------------

def first_folding():
    if text2[0,0] == 'y':
        for coordinates in text3:
            if coordinates[1] > int(text2[0,1]):
                coordinates[1] = 2*int(text2[0,1])- coordinates[1]
    elif text2[0,0] == 'x':
        for coordinates in text3:
            if coordinates[0] > int(text2[0,1]):
                coordinates[0] = 2*int(text2[0,1])- coordinates[0]
            
            
# first_folding()

def second_folding():
    if text2[1,0] == 'y':
        for coordinates in text3:
            if coordinates[1] > int(text2[1,1]):
                coordinates[1] = 2*int(text2[1,1])- coordinates[1]
    elif text2[1,0] == 'x':
        for coordinates in text3:
            if coordinates[0] > int(text2[1,1]):
                coordinates[0] = 2*int(text2[1,1])- coordinates[0]

# second_folding()

#------------------part 2-----------

def total_folding(fold):
    if fold[0] == 'y':
        for coordinates in text3:
            if coordinates[1] > int(fold[1]):
                coordinates[1] = 2*int(fold[1])- coordinates[1]
    elif fold[0] == 'x':
        for coordinates in text3:
            if coordinates[0] > int(fold[1]):
                coordinates[0] = 2*int(fold[1])- coordinates[0]

for fold in text2:
    print(fold)
    total_folding(fold)


#------count duplicate of dots for part 1-------
test = text3.tolist()

text_tupled = list(map(tuple, test))
print(len(set(text_tupled)))

#-------vizualize our dots--------
plt.scatter(x,y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
ax = plt.gca()
ax.invert_yaxis()
plt.grid(True)
plt.show()