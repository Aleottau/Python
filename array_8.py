#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden
from array import array
from random import randrange
import os
os.system("cls")
def mayor(list):
    print()
    print(" ---  Funcion que haya el mayor valor de una lista.. ")
    mayor=0
    for i in list:
        if i > mayor:
            mayor = i 
    print()
    print(f" --- El mayor valor es {mayor}")
    print()

def primos(list):
    print()
    print(" --- Funcion que imprime el/los valores primo(s) de una lista.. ")
    for i in list:
        primo = True
        for j in range(2,i):
            if i% j == 0:
                primo = False
                break
        if primo:
            print(i)
    print()

def ordenar(list):
    print(" --- Funcion que organiza de forma ascendente los valores de la lista --- ")
    for i in range(len(list)):
        for m in range(len(list)):
            if list[i] < list[m]:
                tmp = list[i]
                list[i] = list[m]
                list[m] = tmp
    print("Lista ordenada: ", list)
    print()

def menu():
    lista = []
    for i in range(6):
        lista.append(randrange(1,20))
    print(f" Litsa generada: {lista}")
    print()
    opc = 0
    while opc != 4:
        print("*****  Menu de opciones  *****")
        print()
        print("1. -  Hallar el mayor valor de la lista. ")
        print("2. -  Obtener los numeros primos de una lista. ")
        print("3. -  Ordenar Ascendentemente los numeros de una lista. ")
        print("4. -  Salir. ")
        print()

        opc =int(input("--- Elija una opcion del menu.  ----"))
        print()

        if opc ==1:
            mayor(lista)
        elif opc ==2:
            primos(lista)
        elif opc==3:
            ordenar(lista)
        elif opc ==4:
            print("--- Final ---")
        else : 
            print(" --- Opcion invalida ---")
        
menu()