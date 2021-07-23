#ejercicio 3  categorizar por grupos A y B
print("bienvenido a seleccion de grupo A y B . ")
sex = input("ingrese su genero :  para masculino 'm' , para femenino 'f' : ")
nombre = input("ingrese su nombre : ")[0]

if sex.lower() == "f" :
    if nombre.lower() < "m" :
        print("perteneces al grupo A ")
    else :
        print("perteneces al grupo B ")
elif sex.lower() == "m" :
    if nombre.lower() < "n" :
        print("perteeces al grupo A ")
    else :
        print("perteneces al grupo B ")
else :
    print("datos mal digitados. reinicie la seleccion. ")