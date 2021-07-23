#Actividad 2
#
#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc
def actividad2(list):
    print(" --- impresion de la primera fila ---")
    for j in range(3):
        print(list[0][j] , end=" ")
    print()

    print(" ---  La primera columna ---")
    for i in range(3):
        print(list[i][0] , end=" ")
    print()

    print(" --- imprimir elemento de la fila 1 y columna 1 ---")
    print(list[0][0] , end=" ")


# este codigo crea la mtriz ingresando datos
matriz =[]  # lista vacia que va a ser la matriz principal
for i in range(3):
    lista = []    #lista vacia que recibe los datos de filas
    for j in range(3):
        lista.append(input(f" --- digite el valor en la posicion: [{i+1}] , [{j+1}]  ----"))
    matriz.append(lista)

for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j] ,  end=" ")
        print()

actividad2(matriz)