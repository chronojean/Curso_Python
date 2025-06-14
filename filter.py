numeros = [10, 20, 25, 30, 40,99,88,57,14,25,41,63]


def es_par(n):
    return n % 2 == 0  # True si es par or False si es impar


def es_impar(n):
    return not (n % 2 == 0)  # True si es impar or False si es par


numeros_pares = list(filter(es_par, numeros))
print("Lista de Números pares", numeros_pares)
numeros_impares = list(filter(es_impar, numeros))
print("Lista de Números impares", numeros_impares)

#Te daré un enunciado de una tarea de repaso, para verificar el martes
#Tómate el tiempo de entender la clase y revisar todos los ejercicios.
#El sábado tendremos una prueba. Sí, leíste bien.
