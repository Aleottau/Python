# **   Eliminacion por Posicion  **

print("Eliminar elemento por posicion en una lista/vector: ")
v = [2, 5, 15, 20, 35, 50]
print("Lista Original: ", v)

pos = int(input("Cual es la posicion donde se encuentra el valor a eliminar.?: "))
if pos < len(v)+1:
    v.pop(pos-1)
    print("Valor Borrado exitosamente..")
else:
    print("Posicion invalida")

print("Lista resultante..", v)