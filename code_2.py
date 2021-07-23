#ejercicio 2 . sobre la renta anual.
rent = float(input("ingresa monto de su renta anual : "))
if rent < 10000 :
    imp = (rent * 0.05) 
    print("saldo a pagar es del valor de $ : "  , imp)
elif (rent >= 10000  and rent < 20000) :
    imp = (rent * 0.15) 
    print("saldo a pagar es del valor de $ : "  , imp)
elif (rent >= 20000  and rent < 35000) :
    imp = (rent * 0.20) 
    print("saldo a pagar es del valor de $ : "  , imp)
elif (rent >= 35000  and rent < 60000) :
    imp = (rent * 0.30) 
    print("saldo a pagar es del valor de $ : "  , imp)
else :
    imp = (rent * 0.45)
    print("saldo a pagar es del valor de $ : "  , imp)