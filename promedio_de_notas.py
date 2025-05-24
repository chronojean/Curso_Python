def pedir_notas(num_estudiantes, num_lapsos=3, num_notas=3):
    estudiantes = []
    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante #{i+1}: ")
        lapsos = []
        for l in range(num_lapsos):
            notas = []
            for n in range(num_notas):
                nota = float(input(f"Ingrese la nota #{n+1} del lapso #{l+1} para {nombre}: "))
                notas.append(nota)
            lapsos.append(notas)
        estudiantes.append({'nombre': nombre, 'lapsos': lapsos})
    return estudiantes

def calcular_promedios(estudiantes, num_lapsos=3, num_notas=3):
    promedios_lapso = [0.0 for _ in range(num_lapsos)]
    promedios_estudiantes = []
    for est in estudiantes:
        promedios_por_lapso = []
        for l in range(num_lapsos):
            promedio_lapso = sum(est['lapsos'][l]) / num_notas
            promedios_por_lapso.append(promedio_lapso)
            promedios_lapso[l] += promedio_lapso
        promedio_total = sum(promedios_por_lapso) / num_lapsos
        promedios_estudiantes.append({'nombre': est['nombre'], 'por_lapso': promedios_por_lapso, 'total': promedio_total})
    promedios_lapso = [p / len(estudiantes) for p in promedios_lapso]
    promedio_global = sum(promedios_lapso) / num_lapsos
    return promedios_lapso, promedio_global, promedios_estudiantes

def mostrar_resultados(promedios_lapso, promedio_global, promedios_estudiantes, num_lapsos=3):
    print("\nPromedio global por lapso:")
    for i, p in enumerate(promedios_lapso):
        print(f"Lapso #{i+1}: {p:.2f}")
    print(f"\nPromedio global total de todos los lapsos: {promedio_global:.2f}")

    for l in range(num_lapsos):
        max_est = max(promedios_estudiantes, key=lambda x: x['por_lapso'][l])
        min_est = min(promedios_estudiantes, key=lambda x: x['por_lapso'][l])
        print(f"\nLapso #{l+1}:")
        print(f"  Mayor promedio: {max_est['nombre']} ({max_est['por_lapso'][l]:.2f})")
        print(f"  Menor promedio: {min_est['nombre']} ({min_est['por_lapso'][l]:.2f})")

    max_total = max(promedios_estudiantes, key=lambda x: x['total'])
    min_total = min(promedios_estudiantes, key=lambda x: x['total'])
    print(f"\nMayor promedio general: {max_total['nombre']} ({max_total['total']:.2f})")
    print(f"Menor promedio general: {min_total['nombre']} ({min_total['total']:.2f})")

def main():
    try:
        N = int(input("Ingrese el número de estudiantes: "))
        estudiantes = pedir_notas(N)
        promedios_lapso, promedio_global, promedios_estudiantes = calcular_promedios(estudiantes)
        mostrar_resultados(promedios_lapso, promedio_global, promedios_estudiantes)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()