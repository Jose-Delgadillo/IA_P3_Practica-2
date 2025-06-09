"""
Método de Ordenamiento - MergeSort (Ordenamiento por mezcla)

MergeSort divide el arreglo en dos mitades, las ordena recursivamente y luego
las combina (merge) en un arreglo ordenado. Es muy eficiente y estable.

Observaciones:
- Algoritmo interno.
- Utiliza memoria adicional (no es in-place).
- Complejidad: O(n log n) en todos los casos (mejor, promedio y peor).
- Estable (mantiene el orden de elementos iguales).
"""

def merge_sort(arr):
    """
    Función principal que ordena un arreglo usando el algoritmo MergeSort.

    Parámetros:
    arr -- lista de números a ordenar (modificada en el lugar)
    """
    if len(arr) > 1:
        # Dividimos el arreglo en dos mitades
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        # Aplicamos recursivamente MergeSort a cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Índices para recorrer izquierda, derecha y arreglo original
        i = j = k = 0

        # Intercalamos los elementos ordenados en arr
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Si quedan elementos en izquierda, los agregamos
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedan elementos en derecha, los agregamos
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

        # Imprimimos el arreglo en cada etapa de mezcla
        print(f"Etapa de mezcla: {arr}")

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos MergeSort
    merge_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
