#Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los 
# numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

#actividad1()


valor = []
par = 2
for i in range(0,5):
    valor.append(i)
    valor[i] = par
    par += 2
    
print(valor)

def numeros():
    num_pares = [2, 4, 6, 8, 10]
    for i in num_pares:
        print(i)


def numeros1():
    lista = [1 for i in range(2, 200+1, 2)]     # Compresion
    for i in lista:
        print(i)

numeros1()