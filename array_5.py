print("**---- insercion de un elemeto en una lista no ordena por posicion ----**")
print()

v = [89, 23, 0, 15, 19]
print(v)

numero = int(input("Cual es el numero a Insertar.?: "))
pos = int(input("En que posicion dese insertare el numero.?: "))
v.append(0)

for i in range(len(v)-1, pos-1, -1):
    v[i] = v[i-1]

v[pos-1] = numero
print("Nueva lista no ordenada: ", v)