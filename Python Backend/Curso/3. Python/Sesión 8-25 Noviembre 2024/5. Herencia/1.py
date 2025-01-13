
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

# perro = Animal("Rex")
# gato = Animal("Michi")

perro = Perro("Rex")
gato = Gato("Michi")

perro.hacer_sonido()
gato.hacer_sonido()
