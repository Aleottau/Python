#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
num = int(input("ingrese un numero de 3 digitos:  "))
a = num % 10
a1 =  num //10 
b= a1 % 10
b1 = num // 100
c = b1 %10 

if a == b == c :
    print(str(a)+str(a)+str(a))
else :
    if a >= b and a >= c :
        if b>= c :
            print(str(a)+str(b)+str(c))
        else : 
            print(str(a)+str(c)+str(b))
    elif b >= a and b >= c : 
        if a >= c :
            print(str(b)+str(a)+str(c))
        else :
            print(str(b)+str(c)+str(a))
    else :
        if a >= b :
            print(str(c)+str(a)+str(b))
        else :
            print(str(c)+str(b)+str(a))