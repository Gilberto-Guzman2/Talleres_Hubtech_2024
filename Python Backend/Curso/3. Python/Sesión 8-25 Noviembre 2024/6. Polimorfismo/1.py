
# Clase Padre
class Animal:
    
    # Constructor
    def __init__(self, nombre):
        # Atributo
        self.nombre = nombre

    # Método
    def hacer_sonido(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: Muuu!")

def hacer_sonidos(animal):
    animal.hacer_sonido()

animales = [Perro("Rex"), Gato("Michi"), Vaca("Lola")]

for animal in animales:
    hacer_sonidos(animal)