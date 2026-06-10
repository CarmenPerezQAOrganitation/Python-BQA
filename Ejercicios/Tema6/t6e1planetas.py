#Lista de planetas
Planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#Pide a la usuaria un número del 1 al 8
numero = int(input("Introduce un número del 1 al 8: "))

#Comprobar si es valido
if numero >= 1 and numero <= 8:
    print("El planeta en la posición", numero, "es", Planetas[numero - 1])
else:
    print("Error: número inválido.")
