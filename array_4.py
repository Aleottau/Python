#sort  ordena los datos de un vector numero...
print("*   Insercion en una lista de valores Ordenados **")

v = [2, 5, 15, 20, 35, 50]
print(v)

pos = 0
numero = int(input("Ingrese un valor a Insertar: "))


while (pos <= len(v)-1) and (v[pos] < numero) :
    pos += 1

v.append(0)

for i in range(len(v)-1, pos-1, -1):
    v[i] = v[i-1]

v[pos] = numero
print("Nueva lista ordenada: ", v)