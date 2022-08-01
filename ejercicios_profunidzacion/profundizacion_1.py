# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

from turtle import clearscreen


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
clearscreen
numero_1 = int(input("ingrese un número"))
numero_2 = int(input("ingrese otro número"))
diferencia = numero_1 - numero_2
if diferencia > 0:
    print (" La diferencia entre numero_1 y numero_2 es positiva")
elif diferencia < 0 :
    print (" La diferencia entre numero_1 y numero_2 es negativa")
else :
    print ("La diferencia entre numero_1 y numero_2 es 0")



print(numero_1)
print(numero_2)