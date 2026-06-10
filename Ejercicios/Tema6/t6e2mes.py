#Lista de meses
Meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Pide a la usuaria un número del 1 al 12
numero = int(input("Introduce un número del 1 al 12: "))

#Comprobar si es valido
if numero >= 1 and numero <= 12:
    print("El mes en la posición", numero, "es", Meses[numero - 1])
if numero == 6:
    print("EL MEJOR MES.")