#ciclos repetitivos.
#ejercicio propuesto.
# escriba un programa que pida dos numeros enteros.
# el programa pedira de nuevo el segundo nuemero mientras no sea mayor que el primero.
# el programa terminara escribiendo los dos numeros.

primer = int(input("ingrese un numero:  "))
segun = int(input("ingrese un segundo numero:  "))

while segun < primer :
    segun = int(input(f"--->  ingrese otra vez  un segundo numero ya que  \n ---> {segun}  no es mayor que  {primer}:  "))

print(f"los numeros digitados son {primer} y {segun}")
