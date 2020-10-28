"""
Crear:

Una función que convierta grados Celsius a grados Farenheit (https://es.wikipedia.org/wiki/Grado_Fahrenheit)
Una función que convierta grados Celsius a grados Kelvin (https://es.wikipedia.org/wiki/Kelvin)
"""


def toFarenheit(celsius):
    if celsius < 0:
        print("Ingrese un valor mayor a cero.")
    else:
        farenheit = celsius * (9/5) + 32
    return farenheit


print(toFarenheit(float(input("Ingrese temperatura en Celsius:"))), "F")


def toKelvin(celsius):
    if celsius < 0:
        print("Ingrese un valor mayor a cero.")
    else:
        kelvin = float(celsius + 273.15)
    return kelvin


print(toKelvin(float(input("Ingrese temperatura en Celsius:"))), "K")
