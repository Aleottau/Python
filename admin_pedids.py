# Elaborar un programa en python que permita gestionar un puesto de comida rapida la
# cual entrega a cada uno de sus clientes un ticket(random 1 - 1000) 
# de pedido, a medida que van entrando los pedidos debe mostrar la lista de pedidos 
# en espera y la lista de los pedidos despachados , adicional debe mostrar cuantos 
# pedidos quedan por entregar.
# Gestionar la documentacion interna al Codigo.

from modulos import caja_fact
def limpiar():
    """ Funcion que realiza la limpieza de pantalla para posteriormente mostrar funciones
        de pedidos pendientes y entregados """
    os.system('clear')
    print(' --- Sistema de Admin de Pedidos ---\n')
    mostrarlistas()

def mostrarlistas():
    """ Funcion que imprime informacion sobre los pedidos pendientes y entregados """
    print(f'Pedidos pendientes: ',len(pendiente), pendiente)
    print(f'Pedidos entregados: ', len(entregados), entregados)

def agregarpedido(numero):
    """ Funcion que Genera un numero aleatorio como Numero de pedido (Ticket) y lo agrega 
        a la lista de Pedidos pendientes """
    #numero = randrange(1, 1000)
    if numero in pendiente:
        agregarpedido()
    else:
        pendiente.append(numero)

def realizarentrega(ticket):
    """ Funcion que realiza el borrado de pedidos solicitados y los agrega a lista de entregados
        Parameters
        ------------
        ticket - int - recibida como parametro

        Returns
        --------
        NO retorna nada
        """
    if ticket in pendiente:
        pendiente.remove(ticket)
        entregados.append(ticket)
    else:
        print('Este ticket no se encuentra registrado')
    p = input('Oprima la Tecla <ENTER> para continuar')

def menu(estado):
    num_ped = 0
    while estado == True:
        limpiar()
        try:
            menu = int(input('\n 1. Solicitar ticket \n 2. Entregar pedido \n 3. Salir  :'))
            if menu == 1:
                num_ped += 1
                agregarpedido(num_ped)
            if menu == 2:
                n_pedido = int(input('No. pedido:  '))
                realizarentrega(n_pedido)
            if menu == 3:
                r = str(input('Desea salir del sistema S/N:  '))
                if r.upper() != 'S' and r.upper() != 'N':
                    print('Debe seleccionar una opcion valida')
                    p = input('Presione <ENTER> para continuar') 
                if r.upper() == 'S':
                    print('Gracias por preferirnos')
                    estado = False
            if menu > 3:
                print("Opcion invalida. Solo 1 - 3")
                p = input("Presione <ENTER> para continuar")    
        except ValueError:
            print("Error: Valor invalido, se espera un valor numerico entero")
            p = input("Presione <ENTER> para continuar")


from random import randrange
import  os

pendiente = []
entregados = []

menu(True) 

""" print(limpiar.__name__)
print(limpiar.__doc__)
print()
print(mostrarlistas.__name__)
print(mostrarlistas.__doc__)
print()
print(agregarpedido.__name__)
print(agregarpedido.__doc__) """

""" help(limpiar)
help(mostrarlistas)
help(agregarpedido)
help(caja_fact) """
