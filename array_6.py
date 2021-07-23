# eliminacion por valor...
print("--- Eliminar elemento por valor en lista/vector ----")
v = [2,5,15,20,35,50]
print("--- lista original: " , v)

numero  = int(input("---- cual es el numero  que desea eliminar:  "))
if numero in v:
    v.remove(numero)
    print("--- Valor eliminado exitosamente ! ...")
else :
    print("--- valor no existe...")
    
print("lista resultando: ", v)