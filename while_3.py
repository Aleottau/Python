#2.  Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

num = int(input("ingrese un numero entero cualquiera:   "))
cont = 0
while num != 0 :
    num = num//10
    cont += 1
print(f"---> el numero tiene {cont} digitos")
