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
                print("Îmi trebuie două numere, pe linii diferite, între 1 și 3")
            continue
        if(ord(a)<49) or (ord(b)<49) or (ord(a)>51) or (ord(b)>51):
            n+=1
            if(n!=3):
                print("Îmi trebuie două numere,pe linii diferite, între 1 și 3")
            continue
        a = int(a) -1
        b = int(b) -1
        if(l[a][b]==1) :
            n+=1
            if(n!=3):
                print("Poziție ocupată, mai incearcă")
            continue
        break
        
    if(n==3):
        print("Felicitări, ai pierdut")
        return 0
    else : return a,b


def win_condition():
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
            

m = np.array([ [4,4,4], [4,4,4], [4,4,4] ])
l = np.array([ [0,0,0], [0,0,0], [0,0,0] ])
a=0
b=0

for i in range(5):
    
    print("Jucatorul X alege pozitia:")
    t = erori_citire()
    if(type(t)==int) :
        print("Jucatorul X a pierdut deoarece a greșit de 3 ori consecutiv citirea.")
        print("Felicitări jucătorului O cu această victorie ușoară!")
        break
 
    # atentie, valori deja decrementate
    a= int(t[0])
    b = int(t[1])
    m[a][b] = 1
    l[a][b] = 1    
    if(win_condition()) : 
        print("Jucatorul X a castigat!")
        break
    if(i==4):
        print("A castigat prietenia")
        print(m)
        break
    
    
    
    print("Jucatorul O alege pozitia:")
    
    t = erori_citire()
    if(type(t)==int) :
        print("Jucatorul O a pierdut deoarece a greșit de 3 ori consecutiv citirea.")
        print("Felicitări jucătorului X cu această victorie ușoară!")
        break
     
    # atentie, valori deja decrementate
    a= int(t[0])
    b = int(t[1])
    m[a][b] = 0
    l[a][b]=1
    if(win_condition()) : 
        print("Jucatorul O a castigat!")
        break
    print()
    print(m)
print()
print(m)



    