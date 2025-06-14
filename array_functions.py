# --------------------------------
# ----Declaración de funciones----
# Duplica un número
def duplicar(n):
    return n*2

def sumar_cinco(n):
    return n+5

def potencia_2(n):
    return n**2

def es_par(n):
    return n % 2 == 0  # True or False
# ---------------------------------
# ---------------------------------
numeros = [10, 20, 25, 30, 40]

# Función MAP:
numeros_aumentados = list(map(es_par, numeros))
print(duplicar(33))
print(numeros_aumentados)
print(numeros)
