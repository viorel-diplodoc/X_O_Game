from tkinter import Tk, Button, Text, Scrollbar

import speech_recognition as sr
recognizer = sr.Recognizer()

# Global variable to store the voice input
global_voice_input = ""

def capture_voice_input():
    global global_voice_input  # Declare the global variable
    with sr.Microphone() as source:
        display_output("Ascult!...")
        audio = recognizer.listen(source,timeout = 5, phrase_time_limit = 5)

    try:
        text = recognizer.recognize_google(audio, language="ro-RO")
        text = text.replace('unu', '1').replace('doi', '2').replace('trei', '3')
        global_voice_input = text  # Save the voice input in the global variable
        return text

    except sr.UnknownValueError:
        display_output("Scuze, nu te-am înțeles ")
        return ""

    except sr.RequestError as e:
        display_output("Error; {0}".format(e))
        return ""

def display_output(message):
    output_text.insert("end", message + "\n")
    output_text.see("end")  # Scroll the Text widget to show the latest message

def custom_command_1():
        
        global global_voice_input
        global_voice_input = capture_voice_input()
        display_output("Numele tău este " + global_voice_input+"?     Da/Nu")
        if(capture_voice_input()=="da"):
            display_output("dabro")
            
    

def custom_command_2():
    global global_voice_input
    voice_input = capture_voice_input()
    display_output("Button 2 was clicked! Voice input: " + voice_input)
    display_output("Global voice input: " + global_voice_input)

# Create an instance of the Tkinter window
window = Tk()
window.title("X și O")

# Create a Text widget for output display
output_text = Text(window, height=10, width=40)
output_text.pack(padx=10, pady=10)

# Create a Scrollbar for the Text widget
scrollbar = Scrollbar(window, command=output_text.yview)
scrollbar.pack(side="right", fill="y")
output_text.config(yscrollcommand=scrollbar.set)

# Create two buttons and associate them with custom commands
button1 = Button(window, text="Introdu numele jucătorului X", command=custom_command_1)
button2 = Button(window, text="Introdu numele jucătorului Y", command=custom_command_2)

# Pack the buttons into the window
button1.pack(pady=10)
button2.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
