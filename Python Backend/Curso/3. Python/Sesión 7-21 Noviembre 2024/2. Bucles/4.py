execute = True
i = 0

while execute:
    i = i + 1
    print(f"{i} - Hola Mundo")

    if i == 10:
        break

while True:
    instruccion = input("Ingresa una palabra. si ingresas SALIR se termina el programa: ")

    if instruccion == "SALIR":
        break

print("FIN DEL PROGRAMA")