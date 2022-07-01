# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 08:47:24 2022

@author: justi
"""
from collections import Counter
from operator import itemgetter
import string
import pandas as pd
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

import time


data = loadtxt("input day 14.txt",dtype=np.str, delimiter=" -> ") 
column1_data = data[:,1]

unique_letter = set(column1_data)

table_occur = np.zeros((2,len(unique_letter)))
table_occur = table_occur.astype(np.str)
table_occur[0] = list(unique_letter)

#input premier polymere
template= 'CFFPOHBCVVNPHCNBKVNV'

#--------------------part 1-------------------------

step = 10
for l in range(step):
    cpy = str(template)
    j=0
    for i in range(len(template)-1):
        for pair in data:
            if pair[0] == template[i:i+2]:
                cpy = cpy[:i+1+j]+pair[1]+cpy[i+1+j:]
                j+=1
    template = cpy



def occur(chain):
    for letter in chain:
        letter_index = np.where(table_occur == letter)[1][0]
        nb_occur = float(table_occur[1,letter_index])
        nb_occur += 1
        table_occur[1,letter_index] = str(nb_occur) 
        
occur(cpy)

float_occur = table_occur[1].astype(float)
print( float_occur.max() - float_occur.min())






#--------part 2------------------------------------------
start_time = time.time()
dictionary = {}
for line in data:
    dictionary[line[0]] = line[1]

temp_dict = dict.fromkeys(dictionary,0)

poly_dict = dict.fromkeys(dictionary,0)

#init de poly_dict
for i in range(len(template)-1):
        poly_dict[template[i:i+2]] += 1


for step in range(40): 
    for key in [x for x, v in poly_dict.items() if v != 0]: #on prend que les pairs qui ne sont pas déjà apparus, donc de valeur non nulle
        temp_dict[key[0]+dictionary.get(key)] += poly_dict.get(key)
        temp_dict[dictionary.get(key)+key[1]] += poly_dict.get(key)
    poly_dict = temp_dict.copy()    
    # print(poly_dict)
    temp_dict = dict.fromkeys(temp_dict,0)
    
# print(poly_dict)

def occur_dict(dictionary_):
    for pairs in dictionary_:
        letter_index = np.where(table_occur == pairs[0])[1][0]
        nb_occur = float(table_occur[1,letter_index])
        nb_occur += dictionary_.get(pairs)
        table_occur[1,letter_index] = str(nb_occur) 
    #cas spéciale pour la dernière lettre de template qui ne change jamais, donc il faut la rajouter 1 fois 
    letter_index = np.where(table_occur == template[-1])[1][0]
    nb_occur = float(table_occur[1,letter_index])
    nb_occur += 1
    table_occur[1,letter_index] = str(nb_occur) 
    
occur_dict(poly_dict)

float_occur = table_occur[1].astype(float)
print( float_occur.max() - float_occur.min())

print("--- %s seconds ---" % (time.time() - start_time))