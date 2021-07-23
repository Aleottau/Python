#1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#informar si es par o impar.

#Escribe el código de la primera opción aquí

num = int(input("ingrese un numero de 4 digitos :  "))
a = num % 10
ra = num//10
b = ra % 10
rb = num//100
c = rb %10
rc = num//1000
d = rc % 10

if a == b == c == d :
    if (a % 2 == 0) :
        print(f"los 4 digitos son iguales. entonces el mayor digito es {a}. \n ademas {a} es par.  ")
    else :
        print(f"los 4 digitos son iguales. entonces el mayor digito es {a}. \n ademas {a} es impar.  ")
else :
    if  a>= b and a >= c and a >= d : 
        if (a % 2 == 0):
            print(f"el digito mayor es {a}. \n ademas  {a} es par.  ")
        else : 
            print(f"el digito mayor es {a}. \n ademas  {a} es impar.  ")
    elif b >=a  and b >= c and b >= d :
        if (b % 2 == 0) :
            print(f"el digito mayor es {b}. \n ademas  {b} es par.  ")
        else :
            print(f"el digito mayor es {b}. \n ademas  {b} es impar.  ")
    elif c >= a and c >= b and c >= d :
        if (c % 2 == 0):
            print(f"el digito mayor es {c}. \n ademas  {c} es par.  ")
        else :
            print(f"el digito mayor es {c}. \n ademas  {c} es impar.  ")
    elif d >= a and d >= b  and d >= c :
        if (d % 2== 0):
            print(f"el digito mayor es {d}. \n ademas  {d} es par.  ")
        else :
            print(f"el digito mayor es {d}. \n ademas  {d} es impar.  ")
