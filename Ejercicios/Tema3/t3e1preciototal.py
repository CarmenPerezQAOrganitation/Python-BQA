# Función para calcular el precio con descuento
def calcular_descuento(precio, cantidad, descuento):
    total = precio * cantidad
    total_descuento = total - (total * descuento / 100)
    return total_descuento

# Función para añadir el IVA
def aplicar_iva(cantidad):
    return cantidad * 1.21

# Pedir datos a la usuaria
producto = input("Nombre del producto: ")
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))

# Calcular precio con descuento
total_descuento = calcular_descuento(precio, cantidad, descuento)

# Mostrar información
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", total_descuento)

# Calcular y mostrar precio con IVA
total_iva = aplicar_iva(total_descuento)

print("Precio total con IVA:", total_iva)