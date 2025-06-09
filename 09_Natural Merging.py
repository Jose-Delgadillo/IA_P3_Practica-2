"""
Método de Ordenamiento Externo - Natural Merging (Mezcla Natural)

Natural Merging mejora la mezcla directa detectando secuencias ya ordenadas en el arreglo
original (runs) y aprovechándolas para hacer menos particiones y mezclas.

Esta versión en memoria identifica estas runs y las fusiona hasta ordenar completamente la lista.

Observaciones:
- Algoritmo externo (simulado aquí en memoria).
- Aprovecha las subsecuencias ordenadas preexistentes.
- Complejidad: O(n log n) en el peor caso, mejor si los datos ya están parcialmente ordenados.
"""

def detectar_runs(arr):
    """
    Detecta subsecuencias ordenadas (runs) dentro de la lista.

    Retorna una lista de listas (cada una una run).
    """
    if not arr:
        return []

    runs = []
    run_actual = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            run_actual.append(arr[i])
        else:
            runs.append(run_actual)
            run_actual = [arr[i]]

    runs.append(run_actual)
    return runs

def merge(lista1, lista2):
    """
    Fusión (merge) de dos listas ordenadas.
    """
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

def natural_merge_sort(arr):
    """
    Algoritmo de ordenamiento por mezcla natural.

    Parámetros:
    arr -- lista de números a ordenar
    """
    # Paso 1: detectar subsecuencias ordenadas (runs)
    runs = detectar_runs(arr)

    # Paso 2: mezclar hasta obtener una sola secuencia ordenada
    while len(runs) > 1:
        nuevas_runs = []

        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                fusionada = merge(runs[i], runs[i + 1])
            else:
                fusionada = runs[i]
            nuevas_runs.append(fusionada)

        runs = nuevas_runs
        print(f"Etapa de mezcla: {runs}")

    # Resultado final
    return runs[0] if runs else []

# Bloque principal para probar la función
if __name__ == "__main__":
    datos = [3, 5, 7, 2, 4, 1, 9, 10, 6]

    print("Arreglo original:", datos)

    resultado = natural_merge_sort(datos)

    print("Arreglo ordenado: ", resultado)
