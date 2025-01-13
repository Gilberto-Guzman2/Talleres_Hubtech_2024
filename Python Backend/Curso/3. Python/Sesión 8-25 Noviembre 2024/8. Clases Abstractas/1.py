from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.141592 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.141592 * self.radio

class Rectangulo(Figura):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.alto + self.ancho)

# Crear instancias de las figuras
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Imprimir resultados
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")
