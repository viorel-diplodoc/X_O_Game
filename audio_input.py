import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_voice_input():
    
    while(True):
        with sr.Microphone() as source:
            print("Ascult...")
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language = "ro-RO")
            text = text.replace('unu', '1').replace('doi', '2').replace('trei', '3')
            return text
            
        except sr.UnknownValueError:
            text = ""
            print("Scuze, nu te-am înțeles ")
            continue
        
        except sr.RequestError as e:
            text = ""
            print("Error; {0}".format(e))
            continue
        

text = capture_voice_input()
try:
    a = int(text[0])
    b = int(text[2])
    
except:
    print("wrong input")
    
