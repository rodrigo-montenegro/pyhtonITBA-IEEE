"""
Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión:

A: 90–100

B: 80–89

C: 70–79

D: 60–69

F: 0–59
"""
porcentaje = int(input("Ingrese nota porcentual:"))
if porcentaje <= 100 and porcentaje >= 90:
    print("A")
elif porcentaje <= 89 and porcentaje >= 80:
    print("B")
if porcentaje <= 79 and porcentaje >= 70:
    print("C")
if porcentaje <= 69 and porcentaje >= 60:
    print("D")
if porcentaje <= 59 and porcentaje >= 0:
    print("F")
