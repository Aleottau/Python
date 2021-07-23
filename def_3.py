#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

#numeros()
from random import randrange
print()
def numale():
    num = 0
    while True:
        num = randrange(100,130)
        if num != 110 and num != 115 and num != 120 :
            return num
print()

def numeros():
    par = True
    i =1
    while i <= 10:
        numero = numale()
        if numero % 2 == 0 and par == True :
            print(f"---- el numero es {numero}")
            par = False
            i +=1
        elif numero % 2 != 0  and par == False :
            print(f"---- el numero es {numero}")
            par = True
            i +=1

## ------------- programa principal -----------------##

numeros()