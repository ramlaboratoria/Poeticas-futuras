import speech_recognition as sr
import os
# import markovify

#Función que agrega una linea cada que entra el texto 
def write_to_file(text):
    with open('/home/ramlab/git/ram/Poeticas-futuras/salida.txt', 'a') as f:
        f.write(text + "\n")
        f.close()


# Obtiene el audio del micrófono
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Te escucho")
#    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)
    MyText = r.recognize_google(audio, language="es")
            
    print("Dijiste:  "+MyText)
    write_to_file(MyText)
