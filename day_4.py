# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:04:36 2021

@author: justi
"""
#--------part 1-------------------------------
# import numpy as np
# f=open("input day 4.txt","r")
# lines=f.readlines()
# lines[0]=lines[0].replace(',',' ')
# bingo=[]
# lines[0]=lines[0].split()
# for i in range(1,len(lines)):
#     lines[i]=lines[i].split()
#     if lines[i]==[]:
#         bingo.append(lines[i+1:i+6])


# for i in range(len(bingo)):
#     for j in range(len(bingo[i])):
#         bingo[i][j]=bingo[i][j].split()


# bingo_check=np.zeros((len(bingo),len(bingo[0])*2))

# def check():
#     for indice_num_sortant in range(len(lines[0])):
#         for tableau in range(len(bingo)):
#             for ligne_tableau in range(len(bingo[tableau])):
#                 for indice_ligne_tableau in range(len(bingo[tableau][ligne_tableau])):  
#                     if lines[0][indice_num_sortant]==bingo[tableau][ligne_tableau][indice_ligne_tableau]:
#                         bingo_check[tableau][ligne_tableau]+=1
#                         bingo_check[tableau][5+indice_ligne_tableau]+=1
#                         # print( x,y,z,t,bingo_check[y][z])
#                         if bingo_check[tableau][ligne_tableau]==5:
#                             return tableau,ligne_tableau,indice_num_sortant 
#                         elif bingo_check[tableau][5+indice_ligne_tableau]==5:
#                             return tableau,5+indice_ligne_tableau,indice_num_sortant
                        
    
# y_,z_,x_=check()                     

# def sum_marked(Y,X):
#     bingo_line=sum(bingo[Y],[])
#     for t in range(X+1):
#         for i in range(len(bingo_line)):
#             if lines[0][t]==bingo_line[i]:
#                 bingo_line[i]='0'
#     return sum(map(int,bingo_line)),lines[0][X]
    
# S,I=sum_marked(y_,x_)        
# print(S*int(I))


#-----------part 2---------------------------

import numpy as np
f=open("input day 4.txt","r")
lines=f.readlines()
lines[0]=lines[0].replace(',',' ')
bingo=[]
lines[0]=lines[0].split()
for i in range(1,len(lines)):
    lines[i]=lines[i].split()
    if lines[i]==[]:
        bingo.append(lines[i+1:i+6])
        
for i in range(len(bingo)):
    for j in range(len(bingo[i])):
        bingo[i][j]=bingo[i][j].split()

def check2():
    bingo_check=np.zeros((len(bingo),len(bingo[0])*2))
    indice_num_sortant=0
    while len(bingo)!=1:
        for tableau in bingo[:]:
            for ligne_tableau in range(len(tableau)):
                for indice_ligne_tableau in range(len(tableau[ligne_tableau])):  
                    if lines[0][indice_num_sortant]==tableau[ligne_tableau][indice_ligne_tableau]:
                        bingo_check[bingo.index(tableau)][ligne_tableau]+=1
                        bingo_check[bingo.index(tableau)][5+indice_ligne_tableau]+=1
                        if bingo_check[bingo.index(tableau)][ligne_tableau]==5 :
                            bingo_check=np.delete(bingo_check,bingo.index(tableau),0)
                            bingo.remove(tableau)                            
                        elif bingo_check[bingo.index(tableau)][5+indice_ligne_tableau]==5 :
                            bingo_check=np.delete(bingo_check,bingo.index(tableau),0)
                            bingo.remove(tableau)
        indice_num_sortant+=1
                    
    return  indice_num_sortant

num_last_indice=check2()

def sum_marked(Y,X):
    bingo_line=sum(bingo[Y],[])
    for t in range(X+1):
        for i in range(len(bingo_line)):
            if lines[0][t]==bingo_line[i]:
                bingo_line[i]='0'
    return sum(map(int,bingo_line)),lines[0][X]

Sbis,Ibis=sum_marked(0,num_last_indice)#bingo est de taille 1 mtn

print(Sbis*int(Ibis))