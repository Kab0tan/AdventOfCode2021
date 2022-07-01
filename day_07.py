# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 23:11:43 2021

@author: justi
"""
import numpy as np
from numpy import loadtxt
lines = loadtxt("input day 7.txt",dtype=int, delimiter=",")


def move(depart,destination):
    fuel=0
    for i in range(abs(destination-depart)+1):
        fuel+=i
    depart= destination
    return depart, fuel


list_tot_fuel=[]
for dest in range(min(lines),max(lines)):
    list_fuel=[]
    for dep in range(len(lines)):
        list_fuel.append(move(lines[dep],dest)[1])
    list_tot_fuel.append(sum(list_fuel))
    

print(min(list_tot_fuel))



    
