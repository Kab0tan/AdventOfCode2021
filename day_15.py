# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:24:08 2022

@author: justi
"""
import heapq
import numpy as np
from collections import defaultdict
with open("input day 15.txt") as lines:
    data = [[int(n) for n in list(line.strip())] for line in lines]  
    
data1 = np.array(data)



#------------------part 1-----------------------
def fastest_path(data):
    checkpoint =[(0,0,0)]
    heapq.heapify(checkpoint)
    visited = set()
    
    max_x = len(data)
    max_y = len(data[0])
    
    
    while (1):
        cost, x, y = heapq.heappop(checkpoint)
        
        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        
        if x == max_x-1 and y == max_y-1:
            print(cost)
            break
        
        for x_neighbor, y_neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + x_neighbor
            new_y = y + y_neighbor
            
            if (new_x <0 or new_y <0) or (new_x >= max_x or new_y >= max_y):
                continue
            
            heapq.heappush(checkpoint, (cost + data[new_x][new_y], new_x, new_y ))
 
# fastest_path(data)
#------------------ part 2-----------------
# permet de créer les nouvelles données du problème, remplacer alors 'data' par 'data_part2'
def incr_array(M,n):
    for i in range(n):
        M=M+1
        while np.any(M>=10):
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if M[i,j]==10:
                        M[i,j]=1
    return M



def extend(array1):
    
    array_incr_1 = incr_array(array1, 1)
    array_incr_2 = incr_array(array1, 2)
    array_incr_3 = incr_array(array1, 3)
    array_incr_4 = incr_array(array1, 4)
    array_incr_5 = incr_array(array1, 5)
    array_incr_6 = incr_array(array1, 6)
    array_incr_7 = incr_array(array1, 7)
    array_incr_8 = incr_array(array1, 8)
    
    
    line1 = np.concatenate((array1,array_incr_1,array_incr_2,array_incr_3,array_incr_4),1)
    line2 = np.concatenate((array_incr_1,array_incr_2,array_incr_3,array_incr_4,array_incr_5),1)
    line3 = np.concatenate((array_incr_2,array_incr_3,array_incr_4,array_incr_5,array_incr_6),1)
    line4 = np.concatenate((array_incr_3,array_incr_4,array_incr_5,array_incr_6,array_incr_7),1)
    line5 = np.concatenate((array_incr_4,array_incr_5,array_incr_6,array_incr_7,array_incr_8),1)
    
    array2 = np.concatenate((line1,line2,line3,line4,line5),0)
    return array2   

data_part2 = extend(data1)

fastest_path(data_part2)



#---------alternate part 2----------


# def incr_array_bis(array, n):
#     return (array + n-1)%9 + 1

# def extend_bis(array1,m):
#     line= array1.copy()
#     for i in range(1,m+1):
#         line = np.concatenate((line, incr_array_bis(array1,i)),1)
#     M= line.copy()
#     for j in range(1,m+1):
#         M = np.concatenate((M, incr_array_bis(line,j)),0)
#     return M

# data_part2 = extend_bis(data1,4)

# fastest_path(data_part2)