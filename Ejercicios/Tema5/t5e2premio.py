# Pide a la usuaria 5 colores
for i in range(5):
    color = input("Introduce un color: ").lower()

    if color == "azul":
        print("¡Premio conseguido!")
        break;
    elif i<4:
        print("Prueba otro color.")