# Pide a la usuaria la cantidad de euros a convertir
cantidad_en_euros = float(input("Ingresa la cantidad de euros: "))

#Convierte euros a dólares
tasa_de_cambio = 1.1  
cantidad_en_dolares = cantidad_en_euros * tasa_de_cambio
print(f"{cantidad_en_euros} euros son equivalentes a {cantidad_en_dolares} dólares.")

#Convierte euros a libras
tasa_de_cambio_libras = 0.87 
cantidad_en_libras = cantidad_en_euros * tasa_de_cambio_libras
print(f"{cantidad_en_euros} euros son equivalentes a {cantidad_en_libras} libras.")

# Muestra la cancidad en euros, dólares y libras
print(f"{cantidad_en_euros} euros son equivalentes a {cantidad_en_dolares} dólares y {cantidad_en_libras} libras.")