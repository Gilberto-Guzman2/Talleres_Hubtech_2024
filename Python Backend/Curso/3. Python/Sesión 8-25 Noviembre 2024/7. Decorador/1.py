def mi_decorador(func):
    def envoltura(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Despues de ejecutar la función")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("John")
