#Pedir al usuario que introduzca dos números.
#Convertimos a numero
numero1= float(input("Introduce un numero: "))
numero2= float(input("Introduce el segundo número: "))

#Hacemos operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

#mostrar resultados
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división es:", division)