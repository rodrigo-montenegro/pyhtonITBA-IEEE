vainilla = {"Juan", "Marina", "Tomas", "Paula"}
chocolate = {"Pedro", "Paula", "Marina"}
dulceDeLeche = {"Juan", "Julian", "Pedro", "Marina"}

print("Persona que le gustan todos los gustos:",
      vainilla & chocolate & dulceDeLeche)
print("Persona que le guste la vainilla y no el dulce de leche:",
      vainilla - dulceDeLeche)
print("Cantidad de personas distintas:", len(
    vainilla | chocolate | dulceDeLeche))
