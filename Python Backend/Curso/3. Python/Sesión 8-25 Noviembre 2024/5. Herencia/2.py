class Volador:
    def volar(self):
        print ("Estoy volando")

class Nadador:
    def nadar(self):
        print("Estoy nadando")

class SuperHeroe(Volador, Nadador):
    def saludar(self):
        pass

heroe = SuperHeroe()

heroe.volar()
heroe.nadar()