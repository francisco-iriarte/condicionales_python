# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto
from turtle import clearscreen


clearscreen
numero_1 = 8
numero_2 = 70
texto_1 = str(numero_1)
texto_2 = str(numero_2)
# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

print ("             ")
print ("Ejercicio 1-1")
print ("-------------")
print (" ")
print (" ")
if texto_1 > texto_2:
    print('texto_1 = {} es mayor que texto=2 {}'.format(texto_1, texto_2))
elif texto_1 < texto_2:
    print('texto_1 = {} es menor que texto=2 {}'.format(texto_1, texto_2))
else :
    print('texto_1 = {} es igual a texto_2 = {}'.format(texto_1, texto_2))
print (" ")
print ("Otra forma")
print (" ")
if texto_1 > texto_2:
    print ("texto_1 = ", texto_1, " es mayor que texto_2 =", texto_2)
elif texto_1 < texto_2 :
    print ("texto_1 = ", texto_1, " es menor que texto_2 =", texto_2)
else :
    print ("texto_1 = ", texto_1, " es igual a texto_2 =", texto_2)

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

nuevo_numero_1 = int(texto_1)
nuevo_numero_2 = int(texto_2)

print ("             ")
print ("Ejercicio 1-2")
print ("-------------")
if numero_1 > numero_2:
    print ("nuevo_numero_1 = ", nuevo_numero_1, " es MAYOR que nuevo_numero_2 = ", nuevo_numero_2)
elif numero_1 < numero_2:
    print ("nuevo_numero_1 = ", nuevo_numero_1, " es MENOR que nuevo_numero_2 = ", nuevo_numero_2)
else :
    print ("nuevo_numero_1 = ", nuevo_numero_1, " es IGUAL que nuevo_numero_2 = ", nuevo_numero_2)
#
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
# 
# Según lo hallado en Google se explica por UNICODE
#