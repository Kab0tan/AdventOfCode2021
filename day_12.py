# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:53:56 2021

@author: justi
"""
import string
import pandas as pd
import numpy as np
from numpy import loadtxt
# lines = loadtxt("input day 12 bin.txt",dtype=np.str, delimiter="-")
lines = loadtxt("input day 12.txt",dtype=np.str, delimiter="-")

df=pd.DataFrame(lines,columns=['un','deux']) #datatable des données input

da=df.groupby('un')['deux'].apply(list).reset_index(name='deux')
db=df.groupby('deux')['un'].apply(list).reset_index(name='un')
db=db.rename(columns={"deux": "un", "un": "deux"})
dc=db.append(da)
dd=dc.groupby('un')['deux'].apply(list).reset_index(name='new') #datatable de chaque variable de l'input et de tous les points auxquels ils sont connectés

for i in range(len(dd['new'])):
    dd['new'][i]=sum(dd['new'][i],[])
    
# dd[dd['un'].str.match('start')]
start_ind=dd[dd['un'].str.match('start')].index[0] #renvoie num de ligne où il y a 'start'
cop_ind=dd.iloc[start_ind].copy()
dd.iloc[start_ind]=dd.iloc[0] #ligne de 'start' seule
dd.iloc[0]=cop_ind 

ascii_maj=string.ascii_uppercase
ascii_min=string.ascii_lowercase


def path(item):
    index_tab_char = dd[dd['un'].str.match(item)].index[0]
    return dd.iloc[index_tab_char][1]

#----------------part 1-------------------------------
solutions =[]

chemin=['start']

def recur():
    if chemin[-1] != 'end':
        #print(chemin)
        for cave in path(chemin[-1]):
            #print(cave)
            if (cave.upper() == cave) or (cave not in chemin) :
                if cave == 'start' and cave in chemin:
                    continue
                else:
                    chemin.append(cave)
                    recur()
                    #print("ancien chemin",chemin)
                    chemin.pop()
                    #print("new chemin",chemin)
    else:
        solutions.append(chemin.copy())

recur()

#----------------part 2-----------------------------

def small_caves_f():
    list_small_caves=[]
    for letter in dd['un']:
        if letter.islower() and letter != 'start' and letter != 'end':
            list_small_caves.append(letter)
    return list_small_caves

small_caves = small_caves_f()

solutions_part2 =[]

chemin_part2=['start']

def recur_part2(x):
    if chemin_part2[-1] != 'end':
        #print(chemin)
        for cave in path(chemin_part2[-1]):
            #print(cave)
            # if (cave.upper() == cave) or (cave not in chemin) :
            if cave == x:
                if (cave.upper() == cave) or (chemin_part2.count(cave)<=1) :
                    if cave == 'start' and cave in chemin_part2:
                        continue
                    else:
                        chemin_part2.append(cave)
                        recur_part2(x)
                        #print("ancien chemin",chemin)
                        chemin_part2.pop()
                        #print("new chemin",chemin)
            else:
                if (cave.upper() == cave) or (chemin_part2.count(cave)<1) :
                    if cave == 'start' and cave in chemin_part2:
                        continue
                    else:
                        chemin_part2.append(cave)
                        recur_part2(x)
                        #print("ancien chemin",chemin)
                        chemin_part2.pop()
                        #print("new chemin",chemin)
    else:
        solutions_part2.append(chemin_part2.copy())

for small_cave_to_test in small_caves:
    recur_part2(small_cave_to_test)


def duplicate(list_):
    for element in list_:
        if list_.count(element)>1:
            return element
    return False


sol2_tupled = list(map(tuple, solutions_part2))
print(len(set(sol2_tupled)))
