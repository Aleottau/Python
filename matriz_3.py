#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

#actividad2()

def actividad2():
    a = [[0  for j in range(4)] for i in range(3)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f" --- digite el valor en la posicion: [{i+1}] , [{j+1}]  ----")
            a[i][j] =  int(input())
        print()
    x = int(input(" --- Digite el valor escalar "))
    c = []
    for i in range(len(a)):
        fila_c=[]
        for j in range(len(a[i])):
            fila_c.append(a[i][j]* x)
        c.append(fila_c)

    for i in range(len(c)):
        for j in range(len(c[0])):
            print(c[i][j] ,  end=" ")
        print()

actividad2()