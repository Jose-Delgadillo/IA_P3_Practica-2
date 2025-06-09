"""
Métodos de Ordenamiento - Selección (SelectionSort)

Este código implementa el algoritmo de ordenamiento por selección. La idea principal es 
buscar el valor mínimo (o máximo) en el arreglo y colocarlo en su posición correcta,
repitiendo el proceso para el resto de los elementos no ordenados.

Observaciones:
- Algoritmo interno.
- No usa librerías externas.
- Simple pero ineficiente para grandes volúmenes de datos.
- Complejidad en el peor caso: O(n^2)
- No es estable (puede cambiar el orden de elementos iguales).
"""

def selection_sort(arr):
    """
    Función que ordena una lista utilizando el método de selección.

    Parámetros:
    arr -- lista de números a ordenar (se modifica en el lugar)
    """

    # Recorremos la lista desde el primer hasta el penúltimo elemento
    for i in range(len(arr)):
        # Suponemos que el elemento actual es el mínimo
        indice_minimo = i

        # Recorremos el resto del arreglo para encontrar el valor mínimo
        for j in range(i + 1, len(arr)):
            # Si encontramos un valor menor, actualizamos el índice mínimo
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        # Si encontramos un valor menor, lo intercambiamos con el actual
        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

        # Imprimimos el estado del arreglo en cada paso (opcional)
        print(f"Paso {i + 1}: {arr}")

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos el algoritmo de selección
    selection_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
