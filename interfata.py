# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:24:10 2023

@author: Viorel
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:44:09 2023

@author: jitia
"""

from tkinter import *
import speech_recognition as sr


window = Tk()

jucator_1 = StringVar()
jucator_2 = StringVar()
#pentru afisarea casutelor de x si 0


def recunoastere_nume(variabila_jucator,eticheta):
    recunoastere = sr.Recognizer()

    with sr.Microphone() as source:
        recunoastere.adjust_for_ambient_noise(source)
        audio = recunoastere.listen(source)
    try:
        nume_jucator = recunoastere.recognize_google(audio, language="ro-RO")
        print(f"Ati spus: {nume_jucator}")
        variabila_jucator.set(nume_jucator)
        eticheta.insert(END,''+str(nume_jucator))# Actualizare interfață grafică

    except sr.UnknownValueError:
        print(f"Recunoașterea vocii a eșuat. Vă rugăm să încercați din nou.")
    except sr.RequestError as e:
        print(f"Eroare la cerere pentru recunoaștere vocală; {e}")
        

def afiseaza_tabel():
    print(f"Nume jucator x: {jucator_1.get()}, nume jucator 0: {jucator_2.get()}")
    # Șterge tot conținutul din fereastra actuală
    global eticheta_joc
    for widget in window.winfo_children():
        widget.destroy()
    
    # Creează un tabel cu etichete
    eticheta_titlu = Label(window, text='Joc X și 0')
    eticheta_titlu.grid(row=0, column=0, padx=10, pady=10)
    
    
    for i, litera in enumerate(['A', 'B', 'C']):
        eticheta_coloana = Label(window, text=litera)
        eticheta_coloana.grid(row=1, column=i + 1, padx=10, pady=10)

    # Creează etichete pentru rânduri (1, 2, 3)
    for i in range(1, 4):
        eticheta_rand = Label(window, text=str(i))
        eticheta_rand.grid(row=i + 1, column=0, padx=10)

    # Creează tabelul de joc X și 0 cu 3x3
    for i in range(1, 4):
        for j in range(1, 4):
            eticheta_joc = Label(window, text='d', width=10, height=2, relief='solid', borderwidth=1)
            eticheta_joc.grid(row=i + 1, column=j)
    verifica_continut()
    
def verifica_continut():
    for eticheta in eticheta_joc:
       if "text" in eticheta.keys():
           valoare = eticheta.cget("text")
           print(valoare)
       else:
           print("Eticheta nu are un atribut 'text' setat.")
    print("verific continut\n")
      # titlu joc  
titlu = Label(window, text='Joc X și 0')
titlu.grid(row=0, column=1, padx=50, pady=20)

#etichete pentru nume 
label_eticheta_1 = Label(window, text='Jucator 1: ')
label_eticheta_1.grid(row=1,column=1,padx=10,pady=10)
eticheta_nume_1 = Text(window, height=1, width=10)
eticheta_nume_1.grid(row = 2,column=1)

label_eticheta_2 = Label(window, text='Jucator 2: ')
label_eticheta_2.grid(row=1,column=2,padx=10,pady=10)
eticheta_nume_2 = Text(window, height=1, width=10)
eticheta_nume_2.grid(row = 2,column=2)


#butoane pt inserare nume
buton_nume1 = Button(window, text='Introdu jucator 1 (x)', command=lambda: recunoastere_nume(jucator_1,eticheta_nume_1))
buton_nume1.grid(row=3, column=1, padx= 10, pady=15)

buton_nume2 = Button(window, text='Introdu jucator 2 (0)', command=lambda: recunoastere_nume(jucator_2,eticheta_nume_2))
buton_nume2.grid(row=3, column=2, padx= 10, pady=15)

#la apasarea lui incepe jocul
buton_start = Button(window, text='Start Joc', command=afiseaza_tabel)
buton_start.grid(row=4, column=1, padx=50,pady=20)

#window.mainloop()