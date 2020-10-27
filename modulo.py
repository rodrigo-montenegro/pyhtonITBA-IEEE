"""Mini-desafio
Realizar un programa al cual se ingresa el día del año mediante un número de 0 a 364, y que muestra en pantalla a qué día de la semana corresponde mediante un número de 0 a 6 (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo)

Suponemos que el día 0 del año cae un Lunes.
"""

diaAnio = int(input("Ingrese dia del año:"))
if diaAnio % 7 == 0:
    print("Lunes :0")
elif diaAnio % 7 == 1:
    print("Martes : 1")
elif diaAnio % 7 == 2:
    print("Miercoles : 2")
elif diaAnio % 7 == 3:
    print("Jueves : 3")
elif diaAnio % 7 == 4:
    print("Viernes : 4")
elif diaAnio % 7 == 5:
    print("Sabado : 5")
elif diaAnio % 7 == 6:
    print("Domingo : 6")
