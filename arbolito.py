f = 5
c = 9
arbolito = ["*",
            "***",
            "*****",
            "*******",
            "*********"]
longitud = len(arbolito)


def imprimir_arbolito(arbolito, orientacion):
    arbolito_pirata = arbolito.copy()

    if orientacion == 3 or orientacion == 4:
        arbolito_pirata.reverse()
    for i in range(len(arbolito_pirata)):
        if orientacion == 1:
            print(arbolito_pirata[i])
        elif orientacion == 2:
            print(" " * (8 - (i*2)), arbolito_pirata[i])
        elif orientacion == 3:
            print(arbolito_pirata[i])
        elif orientacion == 4:
            print(" " * (i*2), arbolito_pirata[i])
        elif orientacion == 5:
            print(" " * (c-1-i), arbolito_pirata[i])


imprimir_arbolito(arbolito, 5)
