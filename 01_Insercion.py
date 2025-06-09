"""
Prácticas de Programación IV
Métodos de Ordenamiento - Inserción (InsertionSort)

Este código implementa el algoritmo de ordenamiento por inserción. Es un algoritmo simple
que construye el arreglo final ordenado uno a la vez, insertando cada nuevo elemento
en la posición correcta respecto a los anteriores ya ordenados.

Observaciones:
- Algoritmo interno.
- No usa librerías externas.
- Eficiente para listas pequeñas o casi ordenadas.
- Complejidad en el peor caso: O(n^2)
- Estable (no cambia el orden de elementos iguales).
"""

def insertion_sort(arr):
    """
    Función que ordena una lista utilizando el método de inserción.

    Parámetros:
    arr -- lista de números a ordenar (se modifica en el lugar)
    """

    # Recorremos el arreglo desde la segunda posición (índice 1)
    for i in range(1, len(arr)):
        # Guardamos el valor actual que vamos a insertar
        valor_actual = arr[i]

        # Comenzamos comparando con el elemento anterior
        j = i - 1

        # Mientras no lleguemos al inicio y el valor anterior sea mayor al actual
        while j >= 0 and arr[j] > valor_actual:
            # Movemos el valor mayor una posición a la derecha
            arr[j + 1] = arr[j]
            # Decrementamos j para seguir comparando hacia la izquierda
            j -= 1

        # Insertamos el valor actual en la posición correcta
        arr[j + 1] = valor_actual

        # Imprimimos el estado del arreglo en cada paso (opcional)
        print(f"Paso {i}: {arr}")

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos el algoritmo de inserción
    insertion_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
