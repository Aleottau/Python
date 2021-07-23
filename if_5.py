#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
num1 = int(input("ingrese un numero de 3 digitos:  "))
num2 = int(input("ingrese otro numero de 3 digitos:  "))
a1 = num1% 10
ra1 =  num1 //10 
b1= ra1 % 10
rb1 = num1 // 100
c1 = rb1 %10 
a2 = num2% 10
ra2 =  num2 //10 
b2= ra2 % 10
rb2 = num2 // 100
c2 = rb2 %10 
if a1 == b1 == c1 and a2 == b2 == c2 :
    print( str(a1)+str(a2))
else : 
    if a1 >= b1 and a1 >= c1 :
        if a2 <= b2  and a2<= c2 :
            print(str(a1)+str(a2))
        elif b2 <= a2  and b2 <= c2 : 
            print(str(a1)+str(b2))
        else :
            print(str(a1)+str(c2))
    elif b1>=a1 and b1>=c1 :
        if a2 <= b2  and a2<= c2 :
            print(str(b1)+str(a2))
        elif b2 <= a2  and b2 <= c2 : 
            print(str(b1)+str(b2))
        else :
            print(str(b1)+str(c2))
    else :
        if a2 <= b2  and a2<= c2 :
            print(str(c1)+str(a2))
        elif b2 <= a2  and b2 <= c2 : 
            print(str(c1)+str(b2))
        else :
            print(str(c1)+str(c2))