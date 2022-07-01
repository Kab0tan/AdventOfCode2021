# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 18:50:01 2021

@author: justi
"""

import numpy as np
from numpy import loadtxt

with open("input day 10.txt") as lines:
# with open("input day 10 bin.txt") as lines:
    m = [[str(n) for n in list(line.strip())] for line in lines]
    

    
#----------part 1------------
list1=[')',']','>']
list2=['}',']','>']
list3=[')','}','>']
list4=[')','}',']']
fact_bracket=0
fact_parenthesis=0
fact_Sbracket=0
fact_arrow=0
incomplete=[]


def analyse(x):
    L=[m[x][0]]
    i=1
    global fact_arrow
    global fact_bracket
    global fact_Sbracket
    global fact_parenthesis
    global incomplete
    c=0
    while i!=len(m[x]):
        L.append(m[x][i])
        c+=1
        # print(L)
        if len(L)!=1:
            if L[-2]=='[' and L[-1]==']':
                L.pop()
                L.pop()
                c-=2
            elif L[-2]=='(' and L[-1]==')':
                L.pop()
                L.pop()
                c-=2
            elif L[-2]=='<' and L[-1]=='>':
                L.pop()
                L.pop()
                c-=2
            elif L[-2]=='{' and L[-1]=='}':
                L.pop()
                L.pop()
                c-=2
            # elif (L[-2]=='{' and L[-1]!='}') or (L[-2]=='(' and L[-1]!=')') or (L[-2]=='[' and L[-1]!=']') or (L[-2]=='<' and L[-1]!='>'):
            elif (L[-2]=='{' and L[-1] in list1) or (L[-2]=='(' and L[-1] in list2 ) or (L[-2]=='[' and L[-1] in list3) or (L[-2]=='<' and L[-1] in list4):
                if L[-1]==')':
                    fact_parenthesis+=1
                elif L[-1]==']':
                    fact_bracket+=1
                elif L[-1]=='>':
                    fact_arrow+=1
                elif L[-1]=='}':
                    fact_Sbracket+=1
                # print("Corrupted line=",x)
                return L
            i+=1
    if c!=0:
        # print(L)
        incomplete.append(L)
        # print("incomplete line")
    return L


for i in range(len(m)):
    analyse(i)
print(fact_parenthesis*3+fact_bracket*57+fact_Sbracket*1197+fact_arrow*25137)


#--------part 2--------------
#création d'une liste de listes incomplètes dans la partie 1


def completion(j):
    score =0
    global incomplete
    while len(incomplete[j])!=0:
        if incomplete[j][-1]=='(':
            score=score*5+1
            incomplete[j].pop()
        elif incomplete[j][-1]=='<':
            score=score*5+4
            incomplete[j].pop()
        elif incomplete[j][-1]=='[':
            score=score*5+2
            incomplete[j].pop()
        elif incomplete[j][-1]=='{':
            score=score*5+3
            incomplete[j].pop()
    return score
      
score_tab=[]      
for x in range(len(incomplete)):
    score_tab.append(completion(x))
score_tab=sorted(score_tab)
print(score_tab[len(score_tab)//2])