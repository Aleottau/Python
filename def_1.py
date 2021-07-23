def fibonacci(num):
    ant = 0
    sig = 1
    print(ant, end=", ")
    print(sig, end=", ")
    for i in range(num-2):
        nuevo = ant + sig
        print(nuevo, end=", ")
        ant = sig
        sig = nuevo


numero = int(input("Ingresa un número: "))
fibonacci(numero)