# Función para convertir a dólares
def convertir_a_dolares(euros):
    return euros * 1.1

# Función para convertir a libras
def convertir_a_libras(euros):
    return euros * 0.87

# Pedir cantidad en euros
cantidad_euros = float(input("Introduce una cantidad en euros: "))

# Guardar resultados
dolares = convertir_a_dolares(cantidad_euros)
libras = convertir_a_libras(cantidad_euros)

# Mostrar resultados
print(cantidad_euros, "euros son", dolares, "dólares.")
print(cantidad_euros, "euros son", libras, "libras.")