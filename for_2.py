# Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
    # La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es 
    # posible calcular el siguiente valor como la suma de los dos valores anteriores. 
    # Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son:
    #  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    # Creemos un programa que a partir de un número N ingresado, imprima los primeros N números 
    # de la serie de Fibonacci.
 
n = int(input("---> ingrese un numero N :   "))
a = 0
b = 1
if n>=1 :
    print(a,end=",")
if n>=2 :
    print(b, end=",")

for i in range(3,n+1):
    act = b
    b = a+b
    a = act
    print(b , end=",")
