print("actividad1")
    #Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare
luz = input("ingrese color del semaforo:  verde 'v' / amarillo 'a' / rojo 'r' ")
if luz.lower() == "v" : 
    print("siga")
else :
    if luz.lower() == "a" :
        print("precaucion")
    else : 
        if luz.lower() == "r":
            print("pare")