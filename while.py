"""
Implementar un programa que muestre la siguiente secuencia:

1, 2, 3, 4, 5, 4, 3, 2, 1, 0
"""

i = 1
while i <= 10:

    if (i <= 5):
        print(i)
    else:
        print(10 - i)
    i += 1
