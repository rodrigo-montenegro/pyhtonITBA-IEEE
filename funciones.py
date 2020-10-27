"""
Escribir una función que chequee los siguientes usuarios y contraseñas:

Usuario: Juan - Contraseña: 12345_
Usuario: Pablo - Contraseña: xDcFvGbHn
La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.
"""


def chequarLogin(user, password):
    if (user == "Juan" and password == "12345_") or (user == "Pablo" and password == "xDcFvGbHn"):
        return True
    else:
        return False


print(chequarLogin("Pablo", "xDcFvGbHn"))
print(chequarLogin("Juan", "12345_"))
print(chequarLogin("Pablo", "12345_"))
