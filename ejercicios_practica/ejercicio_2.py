# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
print ("             ")
print ("Ejercicio 1-1")
print ("-------------")
if texto_1 > texto_2:
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))
 
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

print ("             ")
print ("Ejercicio 1-2")
print ("-------------")
if len(texto_1) > len(texto_2):
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
print ("             ")
print ("Ejercicio 1-3")
print ("-------------")
primer_letra = texto_1[0]
segunda_letra = texto_2[0]

if primer_letra > segunda_letra :
    print ("La primer letra de la primer palabra ES mayor que la primer letra de la segunda palabra")
else :
    print ("La primer letra de la primer palabra NO ES mayor que la primer letra de la segunda palabra")


print ("             ")
print ("Ejercicio 1-4")
print ("-------------")


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1 :
    print ("copia_texto_1 es igual a texto_1")
else :
    print ("copia_texto_1 es diferente a texto_1")


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

print ("             ")
print ("Ejercicio 1-5")
print ("-------------")

if copia_texto_1 == texto_2 :
    print ("copia_texto_1 es igual a texto_2")
else :
    print ("copia_texto_1 es diferente a texto_2")