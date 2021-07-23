#Actividad 2
#
#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
def mayor(a) :
    print("--- Este calcula el maximo de la lista---")
    maximo = 0
    for i in a :
        if i > maximo :
            maximo = i
    print(" el mayor de la lista es: ", maximo)

def primos(list):
    print("Funcion que muestra los Valores primos de una lista")
    for i in list:
        primo = True
        for j in range(2, i):
            if (i % j) == 0:
                primo = False
                break
        if primo:
            print(i)
from random import randrange
a = []

for i in range(6):
    a.append(randrange(1,21))
print(a)

mayor(a)
primos(a)