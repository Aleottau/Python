import math
from math import ceil
area =  float(input("ingrese  el area de la zona en la que desea instalar  las nuevas antenas en metro cuadrado:  "))
antenav = int(input("ingrese cantidad de antenas previamente instaladas:  "))
tipo = input(" Que tipo de antena desea instalar  A. 50.600 m^2  B. 19.200 m^2  C. 36.900 m^2  D. 40.500 m^2  E. 34.200 m^2   ")
av = 16600
a = 50600
b = 19200
c = 36900
d = 40500
e = 34200

if (tipo.lower() == "a"  and  antenav >= 0) :
    r= (area - (av*antenav))/a
    print(ceil(r))
elif (tipo.lower() == "b"  and  antenav >= 0) :
    r = (area - (av*antenav))/b
    print(ceil(r))
elif (tipo.lower() == "c"  and  antenav >= 0) :
    r = (area - (av*antenav))/c
    print(ceil(r))
elif (tipo.lower() == "d"  and  antenav >= 0) :
    r = (area - (av*antenav))/d
    print(ceil(r))
elif (tipo.lower() == "e"  and  antenav >= 0) :
    r = (area - (av*antenav))/e
    print(ceil(r))
else :
    print("error en los datos")