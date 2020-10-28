"""
Realizar un programa que ordena nombres alfabeticamente. Primero debe pedir al usuario que ingrese el número de nombres que serán ingresados, luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada. Los nombres se deben ir agregando a una lista. Por último, ordenar la lista alfabéticamente y mostrar en pantalla de a uno por vez los nombres ordenados (usando un for).
"""


lista = []
numeroNombres = int(input("Ingrese el num de nombres a ingresar:"))
for x in range(0, numeroNombres, 1):
    nombre = input("Ingrese un nombre:")
    lista.append(nombre)
lista.sort()
for elemento in lista:
    print(elemento)
