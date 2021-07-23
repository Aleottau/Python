#1 .  Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números 
    # pares desde 2 hasta el número pero que termine el proceso si llega al 10.

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

num = int(input("---> ingrese un numero:   "))
par = 0
while par < num :
    par += 2
    print(f"---> {par}")
    if par == 10 :
        break

