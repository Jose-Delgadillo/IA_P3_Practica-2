"""
Método de Ordenamiento - Intercambio (Bubble Sort)

Este código implementa el algoritmo de ordenamiento burbuja. Funciona recorriendo
la lista repetidamente, comparando elementos adyacentes y cambiándolos de posición
si están en el orden incorrecto. El proceso se repite hasta que la lista esté ordenada.

Observaciones:
- Algoritmo interno.
- Muy simple, pero ineficiente para listas grandes.
- Complejidad en el peor caso: O(n^2)
- Estable (mantiene el orden relativo de elementos iguales).
"""

def bubble_sort(arr):
    """
    Función que ordena una lista utilizando el método de burbuja.

    Parámetros:
    arr -- lista de números a ordenar (se modifica en el lugar)
    """

    n = len(arr)
    # Recorremos la lista n-1 veces
    for i in range(n - 1):
        # Variable para optimizar el algoritmo (detiene si ya está ordenado)
        hubo_intercambio = False

        # Recorremos desde el inicio hasta el último elemento no ordenado
        for j in range(n - 1 - i):
            # Comparamos elementos adyacentes
            if arr[j] > arr[j + 1]:
                # Si están en el orden incorrecto, los intercambiamos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_intercambio = True

        # Imprimimos el estado del arreglo en cada paso
        print(f"Paso {i + 1}: {arr}")

        # Si no hubo ningún intercambio, el arreglo ya está ordenado
        if not hubo_intercambio:
            break

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos el algoritmo burbuja
    bubble_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
"""
Método de Ordenamiento - Intercambio (Bubble Sort)

Este código implementa el algoritmo de ordenamiento burbuja. Funciona recorriendo
la lista repetidamente, comparando elementos adyacentes y cambiándolos de posición
si están en el orden incorrecto. El proceso se repite hasta que la lista esté ordenada.

Observaciones:
- Algoritmo interno.
- Muy simple, pero ineficiente para listas grandes.
- Complejidad en el peor caso: O(n^2)
- Estable (mantiene el orden relativo de elementos iguales).
"""

def bubble_sort(arr):
    """
    Función que ordena una lista utilizando el método de burbuja.

    Parámetros:
    arr -- lista de números a ordenar (se modifica en el lugar)
    """

    n = len(arr)
    # Recorremos la lista n-1 veces
    for i in range(n - 1):
        # Variable para optimizar el algoritmo (detiene si ya está ordenado)
        hubo_intercambio = False

        # Recorremos desde el inicio hasta el último elemento no ordenado
        for j in range(n - 1 - i):
            # Comparamos elementos adyacentes
            if arr[j] > arr[j + 1]:
                # Si están en el orden incorrecto, los intercambiamos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_intercambio = True

        # Imprimimos el estado del arreglo en cada paso
        print(f"Paso {i + 1}: {arr}")

        # Si no hubo ningún intercambio, el arreglo ya está ordenado
        if not hubo_intercambio:
            break

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos el algoritmo burbuja
    bubble_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
