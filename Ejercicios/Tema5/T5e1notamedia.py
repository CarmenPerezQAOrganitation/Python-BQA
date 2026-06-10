# Función para calcular la nota media
def calcular_media():
    cantidad_notas = int(input("¿Cuántas notas deseas introducir? "))

    suma = 0

    for i in range(cantidad_notas):
        nota = float(input("Introduce una nota: "))
        suma = suma + nota

    media = suma / cantidad_notas
    return media

# Obtener y mostrar la media
media = calcular_media()

print("La nota media es:", media)