# Cancion favorita
canción = input("¿Cuál es tu canción favorita? ")

artista = input("¿Quién es el artista?")

álbum = input("¿A qué álbum pertenece la canción?")

año_de_lanzamiento = int(input("¿En qué año se lanzo? "))

segundos = float(input("¿Cuánto dura la canción? "))

videoclip = input("¿Tiene videoclip? ") == "sí"


#mostrar la información de la canción
print("Canción:", canción)
print("Artista:", artista)
print("Álbum:", álbum)
print("En el año:", año_de_lanzamiento)
print("La canción dura:", segundos, "segundos")
print("La canción tiene videoclip:", videoclip)