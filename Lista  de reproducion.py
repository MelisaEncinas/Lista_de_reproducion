# Definimos la clase Song
class Song:
    def __init__(self, title, artist, minutes, seconds):
        self.title = title
        self.artist = artist
        self.duration = minutes * 60 + seconds  # Convertimos minutos y segundos a solo segundos

    def print(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{self.title} por {self.artist} - {minutes}:{seconds:02d} min"

# Definimos la clase Playlist
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []  # Lista que almacenará objetos Song

    def add_song(self, song):
        self.songs.append(song)
        print(f'Se ha agregado la canción: {song.print()}')

    def remove_song(self, song_title):
        for song in self.songs:
            if song.title == song_title:
                self.songs.remove(song)
                print(f'Se ha eliminado la canción: {song.print()}')
                return
        print(f'La canción {song_title} no está en la lista de reproducción')

    def total_duration(self):
        total_seconds = sum(song.duration for song in self.songs)
        minutes, seconds = divmod(total_seconds, 60)
        return f"Duración total: {minutes}:{seconds:02d} minutos."

    def show_songs(self):
        if not self.songs:
            print("La lista de reproducción está vacía.")
        else:
            print(f"Lista de canciones en '{self.name}':")
            for song in self.songs:
                print(song.print())

# Función para convertir la entrada de minutos:segundos en un formato usable
def obtener_duracion():
    while True:
        duracion = input("Introduce la duración de la canción (minutos:segundos, por ejemplo, 1:05): ")
        try:
            minutos, segundos = map(int, duracion.split(":"))
            if 0 <= segundos < 60:
                return minutos, segundos
            else:
                print("Los segundos deben estar entre 0 y 59. Inténtalo de nuevo.")
        except ValueError:
            print("Formato incorrecto. Introduce la duración en el formato minutos:segundos.")

# Función principal interactiva
def interactivo():
    print("Bienvenido a tu gestor de listas de reproducción de música.")
    playlists = []

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Crear nueva lista de reproducción")
        print("2. Agregar canción a una lista")
        print("3. Ver lista de reproducción")
        print("4. Eliminar canción de una lista")
        print("5. Eliminar una lista de reproducción")
        print("6. Salir")

        choice = input("Elige una opción (1-6): ")

        if choice == "1":
            name = input("Introduce el nombre de la nueva lista de reproducción: ")
            playlist = Playlist(name)
            playlists.append(playlist)
            print(f"Se ha creado la lista de reproducción '{name}'.")

            while True:
                print("\nAgrega una canción a tu lista de reproducción:")
                title = input("Introduce el título de la canción: ")
                artist = input("Introduce el artista de la canción: ")
                minutos, segundos = obtener_duracion()

                song = Song(title, artist, minutos, segundos)
                playlist.add_song(song)

                more_songs = input("¿Deseas agregar otra canción? (sí/no): ").lower()
                if more_songs != "sí":
                    break

        elif choice == "2":
            if not playlists:
                print("No hay listas de reproducción creadas. Crea una primero.")
            else:
                playlist_name = input("Introduce el nombre de la lista de reproducción a la que deseas agregar una canción: ")
                playlist = next((pl for pl in playlists if pl.name == playlist_name), None)
                if playlist:
                    title = input("Introduce el título de la canción: ")
                    artist = input("Introduce el artista de la canción: ")
                    minutos, segundos = obtener_duracion()

                    song = Song(title, artist, minutos, segundos)
                    playlist.add_song(song)
                else:
                    print(f"No se encontró la lista de reproducción '{playlist_name}'.")

        elif choice == "3":
            if not playlists:
                print("No hay listas de reproducción creadas.")
            else:
                playlist_name = input("Introduce el nombre de la lista de reproducción que deseas ver: ")
                playlist = next((pl for pl in playlists if pl.name == playlist_name), None)
                if playlist:
                    print(f"\nNombre de la lista: {playlist.name}")
                    print(playlist.total_duration())
                    playlist.show_songs()
                else:
                    print(f"No se encontró la lista de reproducción '{playlist_name}'.")

        elif choice == "4":
            if not playlists:
                print("No hay listas de reproducción creadas.")
            else:
                playlist_name = input("Introduce el nombre de la lista de reproducción: ")
                playlist = next((pl for pl in playlists if pl.name == playlist_name), None)
                if playlist:
                    song_title = input("Introduce el título de la canción que deseas eliminar: ")
                    playlist.remove_song(song_title)
                else:
                    print(f"No se encontró la lista de reproducción '{playlist_name}'.")

        elif choice == "5":
            if not playlists:
                print("No hay listas de reproducción creadas.")
            else:
                playlist_name = input("Introduce el nombre de la lista de reproducción que deseas eliminar: ")
                playlist = next((pl for pl in playlists if pl.name == playlist_name), None)
                if playlist:
                    playlists.remove(playlist)
                    print(f"Se ha eliminado la lista de reproducción '{playlist_name}'.")
                else:
                    print(f"No se encontró la lista de reproducción '{playlist_name}'.")

        elif choice == "6":
            print("Gracias por usar el gestor de listas de reproducción. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamada a la función interactiva para iniciar el programa
interactivo()
