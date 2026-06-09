# Cancion favorita
canción = input("¿Cuál es tu canción favorita? ")
artista = input("¿Quién es el artista?")
álbum = input("¿A qué álbum pertenece la canción?")
año_de_lanzamiento = int(input("¿En qué año se lanzo? "))
segundos = float(input("¿Cuánto dura la canción? "))
videoclip = input("¿Tiene videoclip? (sí/no) ").lower() == "sí"

# Mostrar la información de la canción
print("Canción:", canción)
print("Artista:", artista)
print("Álbum:", álbum)
print("En el año:", año_de_lanzamiento)
print("La canción dura:", segundos, "segundos")
print("La canción tiene videoclip:", videoclip)


# Cancion que menos le gusta
canción_menos_gustada = input("¿Cuál es la canción que menos te gusta? ")
artista_menos_gustado = input("¿Quién es el artista?")
álbum_menos_gustado = input("¿A qué álbum pertenece la canción?")
año_de_lanzamiento_menos_gustado = int(input("¿En qué año se lanzo? "))
segundos_menos_gustados = float(input("¿Cuánto dura la canción? "))
videoclip_menos_gustado = input("¿Tiene videoclip? (sí/no) ").lower() == "sí"

# Mostrar la información de la canción que no gusta
print("Canción:", canción_menos_gustada)
print("Artista:", artista_menos_gustado)
print("Álbum:", álbum_menos_gustado)
print("En el año:", año_de_lanzamiento_menos_gustado)
print("La canción dura:", segundos_menos_gustados, "segundos")
print("La canción tiene videoclip:", videoclip_menos_gustado)

