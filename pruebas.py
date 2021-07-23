import math
def convert_type_to_int(type_):
    type_list = ['a', 'b', 'c', 'd', 'e']
    return type_list.index(type_)


acum_type_ant =[]
for i in range( 3  ):  # Aqui el ciclo debe ir hasta la cantidad de departamentos (n)
    acum_type_ant.append([0 for i in range(5)])
print(acum_type_ant)
for i in range( 5  ):  # Aqui el ciclo debe ir hasta la cantidad de terrenos a analizar (m)
        ant_old = -1
        while ant_old < 0:
            input_data = input().split(' ')
            depart, area, ant_old, type_new = int(input_data[0]), float(input_data[1]), int(input_data[2]), input_data[3]
        area_old = 16600
        if 0 < depart <= 3:
            if type_new ==  'a':  # Aqui debes verificar que el tipo de antena nueva sea 'a'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil( (area - area_old * ant_old) / 50600 ))  # Aqui debes realizar el calculo de las antenas de tipo a con su rango respectivo
                print(acum_type_ant)
            elif type_new == 'b':
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil( (area - area_old * ant_old) / 19200 ))  # Aqui debes realizar el calculo de las antenas de tipo b con su rango respectivo
                print(acum_type_ant)
            elif type_new ==  'c':  # Aqui debes verificar que el tipo de antena nueva sea 'c'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil(  (area - area_old * ant_old) / 36900 ))  # Aqui debes realizar el calculo de las antenas de tipo c con su rango respectivo
                print(acum_type_ant)
            elif type_new ==  'd':  # Aqui debes verificar que el tipo de antena nueva sea 'd'
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil((area - area_old * ant_old) / 40500))
                print(acum_type_ant)
            elif type_new == 'e':
                acum_type_ant[depart - 1][convert_type_to_int(type_new)] += max(0, math.ceil( (area - area_old * ant_old) / 34200 ))  # Aqui debes realizar el calculo de las antenas de tipo e con su rango respectivo
                print(acum_type_ant)
