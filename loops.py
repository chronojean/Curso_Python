resp = "y"
while (resp == "y"):
    print("Hola!")
    while True:
        resp = input("¿Deseas continuar? (Y/N): ").lower()
        if resp in ("y", "n"):
            break
        else:
            print("Por favor, ingresa solo 'Y' o 'N'.")
print("Adiós!")
