#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y
#  100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

#actividad1()

from random import randint , randrange

def actividad1() :
    mayor = 0
    menor =101
    pos_fs = 0
    pos_cs =0
    posm = 0
    posmm = 0
    matriz =[]
    for i in range(5):
        fila =[]
        for j in range(10):
            fila.append(randint(1,100))
            if fila[j] > mayor :
                mayor = fila[j]
                pos_fs = i
                pos_cs = j
            if fila[j] < menor :
                menor = fila[j]
                posm = i
                posmm = j
        matriz.append(fila)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j] ,  end=" ")
        print()
    
    print(f"--- El valor mayor de la matriz es: \n {mayor}  y se encuentra en la posicion [{pos_fs+1}],[{pos_cs+1}]  ")
    print(f"--- El valor menor de la matriz es: \n {menor} y se encuentra en la posicion [{posm + 1}], [{posmm +1}]")

actividad1()