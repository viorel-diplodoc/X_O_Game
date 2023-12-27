# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:15:30 2023

@author: Viorel
"""
import numpy as np

class point:
    
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    

p = point(3,1)
m = np.array([ [p,p,p], [p,p,p], [p,p,p] ])

#functia returneaza 0 daca au fost facute 3 introduceri gresite
# si pozitiile introduse daca sunt corecte, dar decrementate cu o unitate
def erori_citire():
    n=0
       
    #verificare citire corecta
    while(n!=3):    
        if(n==1): print("Mai ai 2 încercări inainte să pierzi")
        if(n==2): print("Mai ai o încercare inainte să pierzi")
        
        a = input()
        b = input()
        
        if(len(a)!=1) or (len(b)!=1):
            n+=1
            if(n!=3):
                print("Îmi trebuie două numere, pe linii diferite, între 1 și 3")
            continue
        if(ord(a)<49) or (ord(b)<49) or (ord(a)>51) or (ord(b)>51):
            n+=1
            if(n!=3):
                print("Îmi trebuie două numere,pe linii diferite, între 1 și 3")
            continue
        a = int(a) -1
        b = int(b) -1
        if(m[a][b].v2==1) :
            n+=1
            if(n!=3):
                print("Poziție ocupată, mai incearcă")
            continue
        break
        
    if(n==3):
        print("Felicitări, ai pierdut")
        return 0
    else : return a,b

t= erori_citire()
print(t)
print(type(t))



