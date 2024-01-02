# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:48:11 2023

@author: Viorel
"""

# -*- coding: utf-8 -*-
"""
1. Algoritmul din spate al jocului
2. Schelet de interfata
3. Recunoastere comenzi vocale
4. Algoritm U interfata
"""
import time
import speech_recognition as sr
import numpy as np
#backend file

recognizer = sr.Recognizer()
#functie pentru citirea pozitiilor, se opreste dupa 5 secunde daca nu a fost spus nimic
# utilizatorul are 3 secunde pentru a spune pozitiile
def capture_voice_input():
    
    while(True):
        with sr.Microphone() as source:
            print("Ascult...")
            audio = recognizer.listen(source,timeout = 5, phrase_time_limit=3)
        
        try:
            text = recognizer.recognize_google(audio, language = "ro-RO")
            text = text.replace('unu', '1').replace('doi', '2').replace('trei', '3')
            return text
            
        except sr.UnknownValueError:
            text = ""
            print("Scuze, nu te-am înțeles ")
            time.sleep(1.5)
            continue
        
        except sr.RequestError as e:
            text = ""
            print("Error; {0}".format(e))
            continue

# functie pentru corectarea inputului potential gresit
# ex index in afara matricii, ex utilizatorul a spus ceva in afara de nr liniei si a coloanei
# ex pozitie deja ocupata
def erori_citire():
    
       
    #verificare citire corecta
    
    while(True):     
        text = capture_voice_input()
        try:
            a = int(text[0])
            b = int(text[2])
            
        except:
            
            print("Spune doar numarul liniei si numarul coloanei!")
            continue
        
        if(a<1) or(b<1) or (a>3) or (b>3):
            
            print("Ai 3 linii si 3 coloane din care sa alegi!")
            continue
        a = int(a) -1
        b = int(b) -1
        if(m[a][b]!=4) :
        
            print("Poziție ocupată, mai incearcă")
            continue
    
        
        else : return a,b

# verificarea indeplinirii conditiei de castig
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
            
# m matricea jocului, 1 - X 0 - O
m = np.array([ [4,4,4], [4,4,4], [4,4,4] ])

a=0
b=0

for i in range(5):
    
    print("Jucatorul X alege pozitia:")
    t = erori_citire()
    
    # atentie, valori deja decrementate
    a= int(t[0])
    b = int(t[1])
    m[a][b] = 1
     
    print(m)
    if(win_condition()) : 
        print("Jucatorul X a castigat!")
        break
    if(i==4):
        print("A castigat prietenia")
        
        break
    time.sleep(3)    
    print("Jucatorul O alege pozitia:")
    
    t = erori_citire()

    a= int(t[0])
    b = int(t[1])
    m[a][b] = 0
   
    
    print(m)
    if(win_condition()) : 
        print("Jucatorul O a castigat!")
        break
    time.sleep(3)   
    
    



    