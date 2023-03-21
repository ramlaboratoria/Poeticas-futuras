import os
import markovify



# INPUT DE TEXTO A UN ARCHIVO TXT

# Function to convert 
def listToString(s):   
    # initialize an empty string
    str1 = " "
    # return string 
    return (str1.join(s))

# LEER/ANALIZAR EL ARCHIVO TXT
with open("/home/ramlab/git/ram/Poeticas-futuras/out.txt") as f:
    text_a = f.read()

model_a = markovify.Text(text_a)
model_combo = markovify.combine([ model_a ])  #en esta línea agregar los nuevos textos en el array separados por comas
# texto_final=model_combo.make_sentence()
texto_final = []; 

for i in range(10):
    #print(texto_final)    
    texto_final.append(model_combo.make_sentence()); 
    
#AGREGAR CODIGO DEL GATO PARA IMPRIMIR 

print(listToString(texto_final))

# text_a = "hola esto es una prueba"


# REPRODUCIR EL ARCHIVO CON FESTIVAL

os.system("echo "+listToString(texto_final)+" | iconv -f utf-8 -t iso-8859-1 | festival --tts") 
