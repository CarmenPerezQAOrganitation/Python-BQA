
def ruleta_de_colores(color):
    color = color.lower()
    if color == "rojo":
        mensaje = "Pasión y energía."
    elif color == "verde":
        mensaje = "Esperanza y crecimiento."
    elif color == "azul":
        mensaje = "Calma y serenidad."
    elif color == "amarillo":
        mensaje = "Felicidad y optimismo."
    elif color == "morado":
        mensaje = "Sabiduría y creatividad."
    else:
        mensaje = "Color no válido."
    return mensaje
# Pide a la usuaria que elija un color
color_elegido = input("Elige un color (Rojo, Verde, Azul, Amarillo, Morado): ")

# Llamamos a color y mostramos el mensaje
mensaje = ruleta_de_colores(color_elegido)

# Muestra por pantalla el color elegido y el mensaje.
print("Has elegido el color", color_elegido)
print("Mensaje:", mensaje)
