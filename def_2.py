#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos 
# de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a 
#       ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

#caja()
def imprimaProducto(nombre, precio):
    print("Producto: [", nombre, "]  -  Precio: [", precio,"]")
    print()

def caja(l_pro,l_pre):
    nombre = input("Ingrese el Nombnre del Producto: ")
    precio = int(input("Ingrese el Precio del producto: "))
    l_pro.append(nombre)
    l_pre.append(precio)
    total_fact = precio

    continuar = True
    while continuar:
        imprimaProducto(nombre, precio)
        seguir = input("Desea ingresar mas articulos? (Si/ s - No/n): ")
        if seguir == "Si" or seguir == "s":
            nombre = input("Ingrese el Nombnre del Producto: ")
            precio = int(input("Ingrese el Precio del producto: "))
            l_pro.append(nombre)
            l_pre.append(precio)
            total_fact += precio
        else:
            continuar = False
    
    print("El Total de la Compra fue de: ", total_fact)

def facturacion(l_pro,l_pre):
    print("***  Factuacion almacenes D1 ***")
    print("Producto \t\t    Precio")
    tot = 0
    for i in range(len(l_pro)):
        print( l_pro[i], end=" - ")
        print("\t\t", l_pre[i])
        tot += l_pre[i]
    print("\n El total de la compra es: ", tot)


l_pro = []
l_pre = []
caja(l_pro, l_pre)
facturacion(l_pro, l_pre)


