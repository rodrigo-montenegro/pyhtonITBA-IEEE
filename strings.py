"""
Hacer un programa que permita ingresar un nombre y un apellido usando dos veces la función input( ). Luego debe crear la variable nombre_y_apellido que contenga ambos datos separados por un espacio. Un fabricante de tarjetas admite la impresión de hasta 26 caracteres para el nombre del dueño de la tarjeta, el programa debe imprimir "Nombre admitido" si nombre_y_apellido cumple con esta restricción y "Nombre no admitido" en caso contrario (el espacio cuenta como uno de los 26 caracteres disponibles).
"""

nombre = input("Ingresa tu nombre:")
apellido = input("ingresa tu apellido:")

nombre_y_apellido = nombre + " " + apellido
if len(nombre_y_apellido) < 26:
    print("Nombre admitido")
    print(nombre_y_apellido)
else:
    print("Nombre no admitido")
    print(nombre[0] + " " + apellido)
