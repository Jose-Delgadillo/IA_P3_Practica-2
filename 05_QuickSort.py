"""
Método de Ordenamiento - QuickSort (Ordenamiento Rápido)

QuickSort es un algoritmo de ordenamiento eficiente de tipo "divide y vencerás".
Selecciona un elemento como pivote, y particiona el arreglo en dos subarreglos:
uno con elementos menores que el pivote y otro con los mayores. Luego, aplica
recursivamente el mismo proceso a los subarreglos.

Observaciones:
- Algoritmo interno.
- Muy eficiente en la práctica.
- Complejidad promedio: O(n log n), peor caso: O(n^2) si el pivote es mal elegido.
- No es estable (puede cambiar el orden de elementos iguales).
"""

def quicksort(arr, inicio, fin):
    """
    Función recursiva que aplica QuickSort sobre una sublista del arreglo.

    Parámetros:
    arr -- lista de elementos a ordenar
    inicio -- índice del primer elemento del subarreglo
    fin -- índice del último elemento del subarreglo
    """
    if inicio < fin:
        # Obtenemos la posición del pivote luego de la partición
        indice_pivote = particionar(arr, inicio, fin)

        # Imprimimos el estado actual del arreglo después de la partición
        print(f"Pivote en índice {indice_pivote}: {arr}")

        # Aplicamos QuickSort de forma recursiva a las sublistas
        quicksort(arr, inicio, indice_pivote - 1)  # Lado izquierdo del pivote
        quicksort(arr, indice_pivote + 1, fin)     # Lado derecho del pivote

def particionar(arr, inicio, fin):
    """
    Reorganiza el subarreglo de modo que todos los elementos menores o iguales al pivote
    queden a la izquierda, y los mayores a la derecha. El pivote queda en su posición correcta.

    Retorna:
    La posición final del pivote.
    """
    pivote = arr[fin]  # Usamos el último elemento como pivote
    i = inicio - 1     # i rastrea la posición del último elemento menor que el pivote

    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos si el elemento es <= al pivote

    # Colocamos el pivote en su posición final
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos QuickSort sobre toda la lista
    quicksort(datos, 0, len(datos) - 1)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
