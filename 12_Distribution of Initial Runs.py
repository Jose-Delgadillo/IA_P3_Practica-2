"""
Método de Ordenamiento Externo - Distribution of Initial Runs

Este no es un algoritmo de ordenamiento en sí, sino una **estrategia previa** utilizada
por algoritmos externos como MergeSort externo, Polyphase o Multiway Merging. Consiste
en dividir un archivo grande en **runs iniciales ordenadas**, que luego serán fusionadas.

En esta versión simulada, se generan estas secuencias ordenadas a partir de bloques
(pequeños lotes que caben en memoria), como si los datos vinieran de un archivo externo.

Observaciones:
- Paso previo en algoritmos externos.
- Aprovecha la memoria limitada para producir bloques ordenados.
- Requiere un sub-algoritmo interno para ordenar los bloques (usamos InsertionSort).
"""

def insertion_sort(arr):
    """Algoritmo de inserción (para ordenar cada bloque)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def distribuir_runs_iniciales(datos, tam_bloque):
    """
    Divide los datos en bloques de tamaño fijo, los ordena y los guarda como runs.

    Parámetros:
    datos -- lista de datos no ordenados
    tam_bloque -- tamaño máximo del bloque que "cabe en memoria"
    
    Retorna:
    Una lista de bloques ordenados (runs).
    """
    runs = []

    for i in range(0, len(datos), tam_bloque):
        bloque = datos[i:i + tam_bloque]       # Extrae un bloque del archivo
        insertion_sort(bloque)                 # Ordena el bloque en memoria
        runs.append(bloque)                    # Guarda como una run
        print(f"Run inicial generada: {bloque}")

    return runs

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista simulando un archivo de datos no ordenados
    datos = [7, 4, 3, 8, 1, 6, 5, 2, 9, 0]

    # Tamaño del bloque que cabe en memoria (simulación)
    tam_bloque = 3

    print("Datos originales:", datos)

    runs = distribuir_runs_iniciales(datos, tam_bloque)

    print("\nRuns ordenadas generadas:")
    for i, r in enumerate(runs):
        print(f"Run {i+1}: {r}")
