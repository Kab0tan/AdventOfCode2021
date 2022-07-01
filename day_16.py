# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:45:06 2022

@author: justi
"""

from collections import defaultdict
import string
import pandas as pd
import numpy as np
from numpy import loadtxt

# data = loadtxt("input day 16 dict.txt",dtype=np.str, delimiter=" = ") 
data = loadtxt("input day 16 dict.txt",dtype=np.str, delimiter=" = ") 

dico = dict(zip(data[:,0], data[:,1]))

my_string = loadtxt("input day 16.txt",dtype = np.str)

def hextobin(hexa):
    chain = []
    for letter in hexa: 
        chain.append(dico[letter])
    return chain


chain = hextobin('9C0141080250320F1802104A08')
# chain = hextobin(np.str(my_string))
chain = ''.join(chain)


#----------part 1 -------------------------
            

def literal_value(s):
    version = s[0:3]
    type_id = s[3:6]
    num = []
    j=6
    while(1):
        if(s[j] == '0'):
            num.append(s[j+1:j+5])
            end=j+5
            break
        num.append(s[j+1:j+5])
        j+=5
        
        
    return int(version,2), int(type_id,2), int(''.join(num),2), end




# def operator(s,i,V,val):
#     print(s)
#     if s[i] == '1': #if length type id equal 1
#         nb_sub_packets = int(s[i+1:i+12],2)
#         i+=12
#         ite=0
#         while ite != nb_sub_packets:
#             if int(s[i+3:i+6],2) == 4: #if it's a literal value
#                 V.append(literal_value(s[i:])[0])
#                 ite+=1
#                 i += literal_value(s[i:])[3]
                
#             else:
#                 V.append(int(s[i:i+3],2))
#                 ite+=1
#                 i += operator(s[i:],6,V,val)
                
#     elif s[i]  == '0': #if length type id equal 0
#         length_sub_packets = int(s[i+1:i+16],2)
#         i+=16
#         count=0
#         while count != length_sub_packets:
#             if int(s[i+3:i+6],2) == 4:
#                 V.append(literal_value(s[i:])[0])
#                 count += literal_value(s[i:])[3]
#                 i += literal_value(s[i:])[3]
#             else:
#                 V.append(int(s[i:i+3],2))
#                 add  = operator(s[i:],6,V,val)
#                 count += add
#                 i += add
                
#     return i


# version=[int(chain[:3],2)]
# if int(chain[3:6],2) != 4:
#     # operator(chain[6:],0,version,values)
#     print("SOMME VERSION",sum(version))


#-------------part 2---------------------------

def which_operations(type_id,val_sub_packets):
    if type_id == 0:
        return sum(val_sub_packets)
    elif type_id == 1:
        return np.prod(val_sub_packets)
    elif type_id == 2:
        return min(val_sub_packets)
    elif type_id == 3:
        return max(val_sub_packets)
    elif type_id == 5:
        if val_sub_packets[0]>val_sub_packets[1]:
            return 1
        else:
            return 0
    elif type_id == 6:
        if val_sub_packets[0]<val_sub_packets[1]:
            return 1
        else:
            return 0
    elif type_id == 7:
        if val_sub_packets[0] == val_sub_packets[1]:
            return 1
        else:
            return 0

def operator_part2(s,i):
    type_id=int(s[3:6],2)
    val_sub_packets = []
    
    length_id = s[i+3]
    
    # print(type_id)
    # print(s)

    if length_id == '1':
        i+=3
        nb_sub_packets = int(s[i+1:i+12],2)
        i+=12
        ite=0
        while ite != nb_sub_packets:
            if int(s[i+3:i+6],2) == 4: #if it's a literal value
                val_sub_packets.append(literal_value(s[i:])[2])
                
                ite+=1
                i += literal_value(s[i:])[3]
            else:
                val_sub_packets.append(operator_part2(s[i:],3)[0])
                ite+=1
                i += operator_part2(s[i:],3)[1]
            
                
    elif length_id == '0':
        i+=3
        length_sub_packets = int(s[i+1:i+16],2)
        i+=16
        count=0
        while count != length_sub_packets:
            
            if int(s[i+3:i+6],2) == 4:
                
                val_sub_packets.append(literal_value(s[i:])[2])
                count += literal_value(s[i:])[3]
                i += literal_value(s[i:])[3]
            else:
                val_sub_packets.append(operator_part2(s[i:],3)[0])
                add  = operator_part2(s[i:],3)[1]
                count += add
                i += add
    
    # print(val_sub_packets)
    # print(which_operations(type_id, val_sub_packets))
    return which_operations(type_id, val_sub_packets), i   
    
    
    

if int(chain[3:6],2) != 4:
    print("FINAL VALUE",operator_part2(chain,3)[0])
    
