# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:42:03 2021

@author: justi
"""

#----------part 1--------------------------------
f=open("input day 3.txt","r")
lines=f.readlines()

gamma=[]
epsilon=[]

for j in range(len(lines[0])-1):
    zero=0
    un=0
    for i in range(len(lines)):
        if lines[i][j]=='0':
            zero+=1
        else:
            un+=1
    if zero<un:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

gamma = ''.join(str(e) for e in gamma)
epsilon = ''.join(str(e) for e in epsilon)
power=int(gamma,2)*int(epsilon,2)
print(power)

#----------part 2--------------------------------
def oxygen():
    index=list(range(0,len(lines)))
    j=0
    while len(index)!=1 :
        zero=0
        un=0
        zero_list=[]
        one_list=[]
        for i in range(len(index)):
            if lines[index[i]][j]=='0':
                zero+=1
                zero_list.append(index[i])
            else:
                un+=1
                one_list.append(index[i])
        if zero<=un: 
            index=one_list
        else:   
            index=zero_list
        j+=1    
    return int(lines[index[0]],2)

def CO2():
    index=list(range(0,len(lines)))
    j=0
    while len(index)!=1 :
        zero=0
        un=0
        zero_list=[]
        one_list=[]
        for i in range(len(index)):
            if lines[index[i]][j]=='0':
                zero+=1
                zero_list.append(index[i])
            else:
                un+=1
                one_list.append(index[i])
        if zero<=un: 
            index=zero_list
        else:   
            index=one_list
        j+=1    
    return int(lines[index[0]],2)

print(oxygen()*CO2())
