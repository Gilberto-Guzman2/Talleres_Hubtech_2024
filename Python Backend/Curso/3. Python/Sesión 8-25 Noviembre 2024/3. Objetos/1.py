import uuid

# Clase: Molde, Objeto: Instancia, Atributo: Propiedad del objeto, Método: Funciones definidas dentro de una clase

# Clase
class Jugador:
    nombre = "Jhon"
    vida = 10
    puntaje = 0

# Objeto
player_one = Jugador()

print(type(player_one))

# ------------------------------

# Clase
class Computadora:

    has_keyboard = True

    # Self (this): Identifica la instancia actual
    def __init__ (self, color, procesador, pulgadas, cantidad_ram, cantidad_rom):

        # Atributos
        self.color = color
        self.procesador = procesador
        self.pulgadas = pulgadas
        self.cantidad_Ram = cantidad_ram
        self.cantidad_rom = cantidad_rom
        self.generar_serial()
        pass

    # Método
    def conectar_wifi(self, red):
        print(f"Dispositivo {self.uuid} | Conectando a Red: {red}")

    def generar_serial(self):
        # self.uuid = "123" # Harcodeado
        self.uuid = uuid.uuid4()

# Instanciar, crear un objeto apartir de la clase
laptop_15 = Computadora(
    color="Space Gray",
    procesador="i5",
    pulgadas=15,
    cantidad_ram="1024mb",
    cantidad_rom="1tb"
)
print(type(laptop_15))

print(f"Pulgadas de Laptop 15: {laptop_15.color}")

laptop_15.generar_serial()
laptop_15.conectar_wifi("TotalPlay94839")
print(hex(id(laptop_15)))

laptop_13 = Computadora(
    color="Black",
    procesador="i5",
    pulgadas=13,
    cantidad_ram="1024mb",
    cantidad_rom="1tb"
)
print(type(laptop_13))

print(f"Pulgadas de Laptop 13: {laptop_13.color}")
