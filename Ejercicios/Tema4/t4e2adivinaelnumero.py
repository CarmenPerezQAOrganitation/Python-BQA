def adivina_un_numero(numero):
    if numero == 4:
        mensaje = "¡Correcto! Has adivinado el número."
    elif numero < 1 or numero >10:
        mensaje = "Ese número no está en el rango del 1 al 10."
    else:
        mensaje = "¡Fallido! Ese número no es."
    return mensaje

# Pide a la usuaria que adivine un número del 1 al 10
numero_elegido = int(input("Elige un número del 1 al 10: "))

# Llamamos a la función y mostramos el mensaje
mensaje = adivina_un_numero(numero_elegido)

# Muestra por pantalla el número elegido y el mensaje.
print("Has elegido el número", numero_elegido)
print("Mensaje:", mensaje)