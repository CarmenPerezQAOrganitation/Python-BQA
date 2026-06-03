# Pide a la usuaria 
Nombre_del_producto = input("Ingresa el nombre del producto: ")
Precio_por_unidad = float(input("Ingresa el precio por unidad: "))
Cantidad_a_comprar = int(input("Ingresa la cantidad a comprar: "))
Descuento = float(input("Ingresa el descuento (en porcentaje): "))
Iva = float(input("Ingresa el IVA (en porcentaje): "))

#Total con descuento e IVA
total = (Precio_por_unidad * Cantidad_a_comprar) - ((Precio_por_unidad * Cantidad_a_comprar) * Descuento / 100)
total = total + (total * Iva / 100)
print(f"El precio total de {Nombre_del_producto} es: {total}")