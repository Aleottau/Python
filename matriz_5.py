#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

def actividad1(matriz):
    ''' if len(matriz) != (len(matriz[0]) or len(matriz[1]) or len(matriz[2])):
        print('La matriz no es cuadrada')
    else:
        for filas in range(len(matriz)):
            for columnas in range(len(matriz[filas])):
                if filas == columnas:
                    print(matriz[filas][columnas]) '''
   
    lista = []
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            lista.append(matriz[i][i])          # Guarda los elemen de la Diaginal Ppal en una lista
        else:
            print("La matriz no es cuadrada")
            return
    print(lista)            # Al Final imprimo la Lista



actividad1([[1,1,1],
            [2,7,2],
            [3,3,3]])