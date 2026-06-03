# Define los precios
camiseta = 10 
sudadera = 20.5 
gorra = 5.5 

# Cantidades de cada prenda
cantidad_camisetas = int(input("¿Cuántas camisetas quieres comprar? "))
cantidad_sudaderas = int(input("¿Cuántas sudaderas quieres comprar? "))
cantidad_gorras = int(input("¿Cuántas gorras quieres comprar? "))

# Calcular el total
total_camisetas = camiseta * cantidad_camisetas
total_sudaderas = sudadera * cantidad_sudaderas
total_gorras = gorra * cantidad_gorras
total = total_camisetas + total_sudaderas + total_gorras
total_con_iva = total * 1.21

# Mostrar el total
print("Total sin IVA: ", total, "euros")
print("Total con IVA: ", total_con_iva, "euros")
