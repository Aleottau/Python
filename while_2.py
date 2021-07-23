#1. Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números 
# pares desde 2 hasta el número. 

num = int(input("ingrese un numero : "))
acum = 2
while num >= acum :
    print(f"---> {acum}")
    acum += 2
