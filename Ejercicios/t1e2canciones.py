# Obtener un valor de la usuaria
canción = input("¿Cuál es tu canción favorita? ")

# Obtener un valor de la usuaria
artista = input("¿Quién es el artista?")

# Obtener un valor de la usuaria
álbum = input("¿A qué álbum pertenece la canción?")

# Convertir la entrada a un número entero
año_de_lanzamiento = int(input("¿En qué año se lanzo? "))

# Convertir la entrada a un número decimal
segundos = float(input("¿Cuánto dura la canción? "))

# Obtener un valor de la usuaria
videoclip = input("¿Tiene videoclip? ") == "sí"


#imprimir toda la información de la canción
print("Canción:", canción)
print("Artista:", artista)
print("Álbum:", álbum)
print("En el año:", año_de_lanzamiento)
print("La canción dura:", segundos, "segundos")
print("La canción tiene videoclip:", videoclip)