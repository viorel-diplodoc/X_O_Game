# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:05:21 2023

@author: Viorel
"""

import numpy as np

def conditie_castig():
    s1 = 0
    s2=0
    column_sums = [sum([row[i] for row in m]) for i in range(0,len(m[0]))]
    row_sums = [sum(row) for row in m]
    if(3 in column_sums) or(0 in column_sums) :return True
    if(3 in row_sums)  or (0 in row_sums) :return True
    
    for i in range(3) :
    
        s1 += m[i][i];
        s2 += m[i][2 - i ];        
    if(s1 == 3) or (s1 == 0) : return True
    if(s2 == 3 ) or (s2 == 0) : return True
    return False
    

m = np.array([[0,1,0], 
              [1,0,4], 
              [0,4,0] ])

if (conditie_castig()): print(True)

