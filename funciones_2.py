#Actividad 2
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números aleatorios 
#entre 0 y 9 y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

#actividad2(3,3)
from random import randrange
def crearmatriz(n,m):
    matriz = []
    for i in range(0,n):
        lista =[]
        for j in range(0,m):
            lista.append(randrange(0,9))
        matriz.append(lista)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] ,  end=" ")
        print()
    return matriz

def promedio(t):
    suma = 0
    cont = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            suma += t[i][j]
            cont += 1
    suma = suma/cont 
    print(f" --  el promedio es : {suma}")
    return suma

def actividad2(n,m):
    matriz = crearmatriz(n,m)
    prom = promedio(matriz)
    c= []
    for i in range(0,n):
        lista = []
        for j in range(0,m):
            if matriz[i][j] >= prom :
                lista.append(1)
            else:
                lista.append(0)
        c.append(lista)
    for i in range(len(c)):
        for j in range(len(c[i])):
            print(c[i][j] ,  end=" ")
        print()


actividad2(int(input(" -- ingrese numero de filas ---  ")),int(input(" -- ingrese numero de columnas --- ")))