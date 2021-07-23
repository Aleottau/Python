#Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario 
# pero saltarse si el digito es 4.

#actividad2()

num = int(input("---> ingrese un numero:   "))
acum = 0
cont = 0
while num != 0 : 
    acum = num % 10
    num //= 10
    if  acum == 4 :
        continue
    cont += 1
print(f"---> el numero tiene {cont} digitos.  ")