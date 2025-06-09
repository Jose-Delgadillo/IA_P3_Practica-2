"""
Método de Ordenamiento Externo - Balanced Multiway Merging

Este algoritmo divide el archivo o lista en múltiples bloques ordenados (runs), y luego
utiliza varios "caminos" (vías) para fusionarlos de forma equilibrada. En vez de mezclar
dos listas a la vez, se mezclan k listas al mismo tiempo, lo que acelera el proceso.

En esta versión simulada en memoria, usaremos un heap mínimo (cola de prioridad)
para realizar la mezcla de varias listas ordenadas (como si fueran archivos separados).

Observaciones:
- Algoritmo externo (simulado aquí con listas en memoria).
- Utiliza estructura de heap para eficiencia en la mezcla.
- Complejidad: O(n log k), donde k es el número de runs.
"""

import heapq

def balanced_multiway_merge(runs):
    """
    Mezcla múltiples listas ordenadas usando un heap mínimo (cola de prioridad).

    Parámetros:
    runs -- lista de listas, cada una previamente ordenada

    Retorna:
    Una lista con todos los elementos ordenados
    """
    resultado = []
    heap = []

    # Inicializamos el heap con el primer elemento de cada run
    for i, run in enumerate(runs):
        if run:
            # Cada entrada en el heap es una tupla: (valor, índice_run, índice_dentro_de_run)
            heapq.heappush(heap, (run[0], i, 0))

    # Mientras el heap no esté vacío, seguimos extrayendo el menor elemento
    while heap:
        valor, run_idx, idx_dentro = heapq.heappop(heap)
        resultado.append(valor)

        # Si la run aún tiene elementos, insertamos el siguiente en el heap
        if idx_dentro + 1 < len(runs[run_idx]):
            siguiente_valor = runs[run_idx][idx_dentro + 1]
            heapq.heappush(heap, (siguiente_valor, run_idx, idx_dentro + 1))

    return resultado

# Bloque principal para probar la función
if __name__ == "__main__":
    # Simulamos 4 runs previamente ordenadas (como si vinieran de archivos)
    runs = [
        [1, 4, 7],
        [2, 5, 8],
        [0, 6],
        [3, 9]
    ]

    print("Runs originales:")
    for i, r in enumerate(runs):
        print(f"Run {i + 1}: {r}")

    resultado = balanced_multiway_merge(runs)

    print("\nResultado ordenado:", resultado)
