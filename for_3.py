cap = float(input("ingrese la cantidad a invertir :  "))
interes = float(input(" interes anual :   "))
n = int(input(" numero de años de la inversion :  "))
for i in range(n):
    cap = (cap*interes)/100 + cap
    print(cap)