print("actividad2")
#Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
#Verde -------- Si hay peaton - Pare, Sino - Siga
#Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
#Rojo = Pare
luz = input("ingrese color del semaforo:  verde 'v' / amarillo 'a' / rojo 'r'   :  ")
p = input("hay peaton en la via?  S/N  ")
if p.lower() == "s" :
    peaton = True
else :
    peaton = False


if luz.lower() == "v" and peaton : 
    print("pare")
elif luz.lower() == "v" and not(peaton) : 
    print("siga") 
elif luz.lower() == "a"  and peaton :
    print("pare")
elif luz.lower() == "a" and not(peaton) : 
    print("precaucion")
elif luz.lower() == "r" : 
    print("pare")
