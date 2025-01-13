url = 'https://academy.loopgk.com/'

def sumar(a, b):
    # print(f'En global esta: {url}')
    return a + b

def restar(a, b):
    return a - b


sumar(5, 10)

print('Llamando al modulo funciones.py')

# __ guiones bajos, atributos especiales, dunder methods
if __name__ == "__main__":
    print("Llamando al módulo funciones.py de manera directa")