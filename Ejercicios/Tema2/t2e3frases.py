# Pide a la usuaria una frase
frase = input("Ingresa una frase: ")

#Longitud de la frase
texto = frase.replace(" ", "")  # Elimina los espacios para contar solo las letras
longitud = len(texto)
print(longitud)  

# Convertir a mayúsculas
mayusculas = frase.upper()
print(mayusculas) 

# Convertir a minusculas
minusculas = frase.lower()
print(minusculas)  