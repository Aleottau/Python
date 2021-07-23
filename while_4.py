#3. Escribe el código que solicite números al usuario hasta que éste ingrese -1.
#Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados 
# hasta ese momento (sin contar con el -1).

num = int(input("ingrese un numero cualquiera :  "))
acum = 0
cont = 0
while num != (-1) :
    acum = num + acum 
    cont += 1
    num = int(input("ingrese un numero cualquiera :  "))

r= (acum)/(cont)
print(f"el promedio de los numeros ingresados es:  " , r )