m1 = [ [1, 2, 3, 4, 5],
       [6, 7, 8, 9, 0],
       [1, 5, 8, 4, 9],
       [7, 8, 10, 1, 0]
     ]

sw = True
for filas in range(len(m1)):
    if sw == True:
        for cols in range(len(m1[filas])):
            print(m1[filas][cols], end=" - ")
            sw = False
    else:
        for cols in range(len(m1[filas])-1, -1, -1):
            print(m1[filas][cols], end=" - ")
            sw = True
    print("\n")
            