# -*- coding: utf-8 -*-
"""
1. Algoritmul din spate al jocului
2. Schelet de interfata
3. Recunoastere comenzi vocale
4. Algoritm U interfata
"""
import numpy as np

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
                print("Îmi trebuie două numere, între 1 și 3")
            continue
        if(ord(a)<49) or (ord(b)<49) or (ord(a)>51) or (ord(b)>51):
            n+=1
            if(n!=3):
                print("Îmi trebuie două numere, între 1 și 3")
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


class point:
    
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
        
p = point(3,0)
m = np.array([ [p,p,p], [p,p,p], [p,p,p] ])
a=0
b=0

for i in range(2):
    
    print("Jucatorul X alege pozitia:")
    t = erori_citire()
    if(type(t)==int) :
        print("Jucatorul X a pierdut deoarece a greșit de 3 ori consecutiv citirea.")
        print("Felicitări jucătorului Y cu această victorie ușoară!")
        break
 
    # atentie, valori deja decrementate
    a= int(t[0])
    b = int(t[1])
    m[a][b] = point(1,1)
    
    
    
    print("++++++++++++++++++++++++")
    for i in range(3):
        for j in range(3):
            print(m[i][j].v2, " ",end = "")
        print()
    
    
    print("Jucatorul Y alege pozitia:")
    
    t = erori_citire()
    if(type(t)==int) :
        print("Jucatorul Y a pierdut deoarece a greșit de 3 ori consecutiv citirea.")
        print("Felicitări jucătorului X cu această victorie ușoară!")
        break
     
    # atentie, valori deja decrementate
    a= int(t[0])
    b = int(t[1])
    m[a][b] = point(0,1)
    
    
    print("++++++++++++++++++++++++")
    for i in range(3):
        for j in range(3):
            print(m[i][j].v2, " ",end = "")
        print()
    
print("--------------------------")
for i in range(3):
    for j in range(3):
        print(m[i][j].v1, " ",end = "")
    print()
print("----------------------------------")
for i in range(3):
    for j in range(3):
        print(m[i][j].v2, " ",end = "")
    print()
    