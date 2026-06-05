
def ruleta_de_colores(color):
    if color == "Rojo":
        mensaje = "Pasión y energía."
    if color == "Verde":
        mensaje = "Esperanza y crecimiento."  
    if color == "Azul":
        mensaje = "Calma y serenidad."
    if color == "Amarillo":
        mensaje = "Felicidad y optimismo."
    if color == "Morado":
        mensaje = "Sabiduría y creatividad."
    return mensaje
# Pide a la usuaria que elija un color
color_elegido = input("Elige un color (Rojo, Verde, Azul, Amarillo, Morado): ")

# Llamamos a color y mostramos el mensaje
mensaje = ruleta_de_colores(color_elegido)

# Muestra por pantalla el color elegido y el mensaje.
print(f"El color {color_elegido} representa: {mensaje}")