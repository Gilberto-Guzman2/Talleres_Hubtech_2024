# Sin usar self, dara error

class Jugador:
    def __init__(self, nombre):
        nombre = nombre

player_one = Jugador("Jhon")

print(player_one.nombre)