#Actividad 1
#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

#print(actividad1("Esta es una prueba para pasar a una lista",3))

"""def actividad1(x,n):
    palabra = []
    frase = x.split()
    for i in frase:
        if len(i) > n:
            palabra.append(i)
    print(palabra)
 

a = input(" --- ingrese una frase --- ")
b = int(input(" --- ingrese un numero entero n ---  "))
actividad1(a,b)
"""
""""for i in range(3):
    x = int(input(" un numero"))
    if x > 5 :
        break
    else :
        
"""
i = 0
while i<3:
    x= int(input("di un numero    "))
    y = input(" una letra:  a   o   b   ")
    if  x  and y == "a":
        print("good job ")
    else:
        continue
    i +=1

