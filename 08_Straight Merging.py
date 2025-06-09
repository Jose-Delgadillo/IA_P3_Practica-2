"""
Método de Ordenamiento Externo - Straight Merging (Mezcla Directa)

Straight Merging simula la ordenación de archivos grandes que no caben en memoria RAM.
Divide los datos en bloques pequeños que se ordenan individualmente (generalmente en memoria)
y luego se mezclan de forma secuencial para formar un archivo ordenado.

Esta versión simplificada en Python asume que todos los datos están en memoria, y simula
la estrategia de dividir en partes, ordenar individualmente y luego hacer una mezcla directa.

Observaciones:
- Algoritmo externo (ideal para datos en disco).
- Versión simplificada aquí con listas en memoria.
- Utiliza la técnica de Merge (como MergeSort).
- Complejidad: O(n log n)
"""

def merge(lista1, lista2):
    """
    Fusión (merge) de dos listas ordenadas.

    Retorna una nueva lista con todos los elementos ordenados.
    """
    resultado = []
    i = j = 0

    # Mezclamos los elementos uno por uno
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregamos los elementos restantes
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

def straight_merge_sort(arr):
    """
    Ordenamiento por mezcla directa simulada en memoria.

    Parámetros:
    arr -- lista de elementos a ordenar
    """
    n = len(arr)

    # Paso 1: dividir en sublistas de un solo elemento
    bloques = [[x] for x in arr]

    # Paso 2: mezclar secuencialmente las sublistas hasta que quede una sola lista ordenada
    while len(bloques) > 1:
        nuevos_bloques = []

        # Mezclamos de dos en dos
        for i in range(0, len(bloques), 2):
            if i + 1 < len(bloques):
                mezclado = merge(bloques[i], bloques[i + 1])
            else:
                mezclado = bloques[i]
            nuevos_bloques.append(mezclado)

        bloques = nuevos_bloques
        print(f"Etapa de mezcla: {bloques}")

    # La lista ordenada final está en el único bloque restante
    return bloques[0] if bloques else []

# Bloque principal para probar la función
if __name__ == "__main__":
    datos = [9, 3, 1, 5, 4, 2, 8]

    print("Arreglo original:", datos)

    resultado = straight_merge_sort(datos)

    print("Arreglo ordenado: ", resultado)
