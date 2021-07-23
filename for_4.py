 #Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene 
 # y las letras hasta que, o bien termine la palabra o encuentre la letra a. .
letra = str(input("---> ingrese  una palabra:  "))
t = 0
for i in letra:
    if i =="a":
        break
    t +=1
    print(i)
print(t)