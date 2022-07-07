# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 23:42:33 2022

@author: justi
"""

#----------part 1-----------------------

"""
no code here because since y always decrement, the highest value it could reach while still
reaching the target area, is always n(n+1)/2 with n = y's maximum abs - 1

My input is : target area: x=150..193, y=-136..-86
y's maximum abs -1  = 136 -1 = 135
So through each iteration we have :
    0+135+134+...+2+1+0-1-2-3...-134-135 - 136 = 0 - 136 = 136 which is still inside
the target area.
We can't take n= 136 otherwise we woudl have :
    0+316+135+134+...+2+1+0-1-2-3...-134-135-136-137 = -137, outside our target area 
So with 136 we have the highest sum which is 135+134+133+...+3+2+1 thus n(n+1)/2 = 135*136/2

= 9180, my solution for part 1
"""




#--------------part 2---------------------


def isInArea(a,b):
    x1 = 0
    y1 = 0
    while True:
        x1 += a
        y1 += b
        if a != 0:
            a -=1
        b -=1
        if ( 150 <= x1 <= 193) and (-136 <= y1 <= -86):
            return True
        elif (x1 > 193) or (y1 < -136):
            return False

l=[]
for a in range(193+1):
    for b in range(-136,136+1):
        if isInArea(a,b):
            l.append([a,b])

                    

l= set(tuple(i) for i in l)
print(len(l))