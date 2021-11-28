#importacion de dependencias
import random

#valores que constituyen la contraseña
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
#En caso de tener que borrar carácteres, para recuperarlos
#utilizar el siguiente comentario:
#",;.:-_´¨`^+*?'>¿º\<¡*%$}€#""=[]{+/"
simbolos =",;.:-_´¨`^+*?'>¿º\<¡*%$}€#""=[]{+/"
base = minus+mayus+numeros+simbolos

#inputs
longitud=32 #el input no puede ser mayor que la longitud de "base"
#print(len(base))

muestra = random.sample(base,longitud)
password = "".join(muestra)
print(password)

