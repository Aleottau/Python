#Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos 
# y cuantos neutros(0).
positivos = 0
negativos = 0
neutros = 0
for i in range(10):
    print("ingrese el numero: ", i+1, end=": ")
    num = int(input())
    if num == 0:
        neutros += 1
    elif num > 0:
        positivos += 1
    else:
        negativos += 1
    
print("La cantidad de numeros neutros fue de: ", neutros)
print("La cantidad de numeros positivos fue de: ", positivos)
print("La cantidad de numeros negativos fue de: ", negativos)