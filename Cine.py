"""
Sesión 14 - Ejercicio 4
La empresa cine-mintic esta requiriendo
un nuevo software para la compra de
boletos. El programa se encargara de
vender boletos mostrando la distribucion
de silla de una sala "N"x"N". Cuando una
silla se encuentre vacia se representara
con un 0, cuando la silla se encuentre
ocupada se representara con un 1. Si se
intenta comprar una silla ya comprada el
sistema alertara que no es posible la
compra de este asiento. El programa contara
con la siguientes opciones:
1. Vender boletos
2. Cancelar boletos
3. Estadisticas
4. Salir
   1  2  3  4
1 [1, 1, 1, 0]
2 [0, 0, 1, 1]
3 [0, 0, 0, 0]
4 [0, 0, 0, 0]
--------------
"""
# Librerias
import os

# Funcion para crear
# sala vacia
def crear_sala(n):
   rows = []
   for i in range(n):
      cols = []
      for j in range(n):
         cols.append(0)
      rows.append(cols)
   return rows

# Funcion para imprimir
# la sala
def imp_sala(a, n):
   print("  ", end=" ")
   for i in range(n):
      print(i+1, end="  ")
   print()
   for i in range(n):
      print(i+1, a[i])
   print(n*"---"+"--")

# Funcion que calcula cuantas
# sillas fueron vendidas
def estadisticas(a):
   contar = 0
   for i in a:
      contar += i.count(1)
   return contar

# Funcion para vender boletos
def vender(a, n):
   num = int(input("Cantidad de boletos: "))
   sillas = n ** 2
   asignadas = estadisticas(a)
   # Validar disponibilidad
   if num > sillas - asignadas:
      print("No hay sucientes sillas disponibles")
   else:
      i = 1
      # Ciclo de venta
      while i <= num:
         # silla = "1 2"
         # pos = ['1', '2']
         # fil = int('1') - 1 = 0
         # col = int('2') - 1 = 1
         silla = input("Fila y columna del boleto " + str(i) + ":")
         pos = silla.split()
         fil = int(pos[0]) - 1
         col = int(pos[1]) - 1
         if fil >= 0 and col >= 0 and fil <= n-1 and col <= n-1:
            if a[fil][col] == 0:
               a[fil][col] = 1
               i += 1
            else:
               input("Silla ocupada. Presione enter para continuar...")
               continue
         else:
            input("Silla no existe. Presione enter para continuar...")
            continue

# Funcion para cancelar boletos
def cancelar(a, n):
   num = int(input("Cantidad de boletos: "))
   asignadas = estadisticas(a)
   # Validar disponibilidad
   if num > asignadas:
      print("No hay sucientes sillas asignadas")
   else:
      i = 1
      # Ciclo de venta
      while i <= num:
         # silla = "1 2"
         # pos = ['1', '2']
         # fil = int('1') - 1 = 0
         # col = int('2') - 1 = 1
         silla = input("Fila y columna del boleto " + str(i) + ":")
         pos = silla.split()
         fil = int(pos[0]) - 1
         col = int(pos[1]) - 1
         if fil >= 0 and col >= 0 and fil <= n-1 and col <= n-1:
            if a[fil][col] == 1:
               a[fil][col] = 0
               i += 1
            else:
               input("Silla no ocupada. Presione enter para continuar...")
               continue
         else:
            input("Silla no existe. Presione enter para continuar...")
            continue

# Funcion que imprime el menu
def menu():
   os.system("cls")
   print("+---------------------+")
   print("| 1. Vender boletos   |")
   print("| 2. Cancelar boletos |")
   print("| 3. Estadisticas     |")
   print("| 4. Cancelar funcion |")
   print("| 5. Salir            |")
   print("+---------------------+")

opc = 0

n = 8
a = crear_sala(n)

# Ciclo de menu
while opc != 5:
   # Ejecutar funcion del menu
   menu()
   # Pedir opcion por pantalla
   opc = int(input("Digite una opcion: "))
   # Validar salida
   if opc == 5:
      break

   imp_sala(a, n)
   if opc == 1:
      vender(a, n)
   elif opc == 2:
      cancelar(a, n)
   elif opc == 3:
      e = estadisticas(a)
      print("Total de sillas: ", n ** 2)
      print("Sillas vendidas: ", e)
      print("Sillas disponibles: ", (n ** 2) - e)
   elif opc == 4:
      a = crear_sala(n)

   input("Presione enter para continuar...")