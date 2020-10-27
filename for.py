"""
Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if:

0, 1, 4, 9, 16, 25, 6, 7, 8, 9
"""


for x in range(0, 10, 1):
    if(x <= 5):
        print(x**2)
    else:
        print(x)
