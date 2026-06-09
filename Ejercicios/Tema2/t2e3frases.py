# Pide a la usuaria una frase
frase = input("Ingresa una frase: ")

#Longitud de la frase
texto = frase.replace(" ", "")  # Elimina los espacios para contar solo las letras
longitud = len(texto)
print("La longitud de la frase es:", longitud)

# Convertir a mayúsculas
mayusculas = frase.upper()
print("La frase en mayúsculas es:", mayusculas)

# Convertir a minusculas
minusculas = frase.lower()
print("La frase en minusculas es:", minusculas)  