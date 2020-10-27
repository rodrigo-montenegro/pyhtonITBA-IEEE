"""
Escriba un programa que imprima los números del 1 al 100, pero que para cada número que sea múltiplo de 3 imprima N3, para los múltiplos de 5 imprima N5, y para los múltiplos de los dos, N3N5.
"""

for x in range(1, 101, 1):
    if (x % 3 == 0 and x % 5 == 0):
        print("N3N5")
    elif x % 3 == 0:
        print("N3")
    elif x % 5 == 0:
        print("N5")
    else:
        print(x)
