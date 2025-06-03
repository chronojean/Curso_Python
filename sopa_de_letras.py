sopa_de_letras = [
    ['E', 'L', 'E', 'F', 'A', 'N', 'T', 'E', 'G'],
    ['J', 'I', 'R', 'A', 'F', 'A', 'X', 'O', 'A'],
    ['T', 'O', 'B', 'O', 'P', 'L', 'E', 'O', 'T'],
    ['I', 'S', 'M', 'O', 'N', 'O', 'R', 'S', 'O'],
    ['G', 'E', 'Z', 'C', 'E', 'B', 'R', 'A', 'R'],
    ['R', 'R', 'O', 'L', 'O', 'B', 'O', 'O', 'E'],
    ['E', 'A', 'G', 'A', 'T', 'O', 'P', 'N', 'L'],
    ['L', 'O', 'P', 'E', 'R', 'R', 'O', 'I', 'E'],
    ['O', 'N', 'A', 'R', 'D', 'O', 'L', 'N', 'N']
]

for i in range(len(sopa_de_letras)):
    for j in range(len(sopa_de_letras[i])):
        print(sopa_de_letras[i][j], end=' ')
    print()  # Nueva línea al final de cada fila

