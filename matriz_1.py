import os

a = [ [1,2,3], 
      [4,5,6],
      [7,8,9]
    ]

b = [[0 for j in range(3)] for i in range(3)]
c = [[0 for j in range(3)] for i in range(3)]

for i in range(len(b)):
    for j in range(len(b[i])):
        print(f" --- digite el valor en la posicion: [{i}] , [{j}]  ----")
        b[i][j] =  int(input())
    print()

for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] = a[i][j] + b[i][j]
    print()

for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j] ,  end=" ")
    print()

"""print(a)
len(a) # filas de la matriz
len(a[0]) # columnas de la matriz
print(a[2])
print(a[2][3])
"""
"""for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()"""

print()

"""b = [[0 for j in range(3)] for i in range(2)]
for i in range(len(b)):
    for j in range(len(b[i])):
        print(f" --- digite el valor en la posicion: [{i}] , [{j}]  ----")
        b[i][j] =  int(input())
    print()

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j] ,  end=" ")
    print()"""