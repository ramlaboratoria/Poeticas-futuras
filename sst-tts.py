import speech_recognition as sr
import os
import markovify

# Convierte una arreglo (lista) a string
def listToString(s):   
    # Inicializa un string vacío
    str1 = " "
    # Regresa el string junto
    return (str1.join(s))
 
#Agrega una linea cada que entra el texto 
def write_to_file(text):
    with open('/home/ramlab/git/ram/Poeticas-futuras/salida.txt', 'a') as f:
        f.write(text + "\n")
        f.close()

# INPUT Y RECONOCIMIENTO DE VOZ

# Inicializa el reconocimiento

# Obtiene el audio del micrófono
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
#    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)
    MyText = r.recognize_google(audio, language="es")
            
    print("You said:  "+MyText)
    write_to_file(MyText)
    
    
with open('/home/ramlab/git/ram/Poeticas-futuras/salida.txt') as g:
    text_a = g.read()
    
model_a = markovify.Text(text_a)
model_combo = markovify.combine([ model_a ])  #en esta línea agregar los nuevos textos en el array separados por comas
#    texto_final=model_combo.make_sentence()
texto_final = []; 

for i in range(10):
    #print(texto_final)    
    texto_final.append(model_combo.make_sentence()); 
    
#AGREGAR CODIGO DEL GATO PARA IMPRIMIR 

print(texto_final)


# REPRODUCIR EL ARCHIVO CON FESTIVAL

#os.system("echo "+listToString(texto_final)+" | iconv -f utf-8 -t iso-8859-1 | festival --tts")     
    
    
# ABRIR EL ARCHIVO TXT


# ALMACENAMIENTO EN TXT


# PROCESAMIENTO TXT - MARKOV 


# SALIDA TXT - FESTIVAL


