nombres = ["Ana", "Carlos", "Sofía", "Javier", "Lucía",
           "Miguel", "Elena", "Diego", "Valeria", "Adrián",
           "Isabel", "Roberto", "Carmen", "Fernando", "Patricia",
           "Hugo", "Laura", "Ricardo", "Beatriz", "Antonio"]
size = len(nombres)  # 20
desde = size-1  # 19
# range (START, STOP, STEP)
# Desde 19 hasta 0, de -1 en -1


def imprimir_nombres(lista):
    for i in range(len(lista)):
        print(i+1, ")", lista[i])


nombres.reverse()

imprimir_nombres(nombres)

nombres.pop(0)  # Eliminar el primer elemento
nombres.remove("Hugo")  # Eliminar el elemento "Hugo"
nombres.insert(0, "Alejandra")
nombres.sort()  # Ordenar la lista alfabéticamente
nombres.reverse()  # Invertir el orden de la lista
nombres.append("Victoria")  # Añadir un nuevo nombre al final
nombres.insert(5, "Gabriel")  # Insertar "Gabriel" en la posición 5

print("----------------------------")
imprimir_nombres(nombres)
