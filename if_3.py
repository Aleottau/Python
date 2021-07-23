print("actividad3")
#Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
#1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
#retornar el resultado de la operación indicada.
a = float(input("ingrese valor de la variable a.    : "))
b = float(input("ingrese valor de la variable b.    : "))
p = int(input("que operacion desea realizar : \n  1.) sumar  2.) multiplicar  3.) resta (a-b)  4.) dividir (a/b) \n"))

if p == 1 :
    r = a+b
    print("resultado es : " , r)
elif p == 2 : 
    r = a*b
    print("resultado es : " , r)
elif p == 3 : 
    r = (a-b)
    print("resultado es : " , r)
elif p == 4 :
    r = a/b
    print("resultado es : " , r)
else : 
    print("error en la digitacion")