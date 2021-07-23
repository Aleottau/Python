#Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 
# y que retorne el factorial de cada número ingresado usando un ciclo Para (For).

print("El programa finalizara cuando ingrese el numero -1: ")
numero = int(input("Ingrese un numero al que desea hallar su factorial: (num!): "))
factorial = 1
while numero != -1:
    for i in range(1, numero+1):
        factorial *= i
        if i == numero:
            print(i, end=" = ")
        else:
             print(i, end=" * ")
    print(factorial)

    numero = int(input("Ingrese un numero al que desea hallar su factorial: (num!): "))
    factorial = 1