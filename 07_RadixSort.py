"""
Método de Ordenamiento - RadixSort

RadixSort ordena los números procesando sus dígitos, uno a uno, comenzando
por el dígito menos significativo (LSD). Utiliza una técnica auxiliar de
conteo o distribución (como Counting Sort) para mantener el orden relativo
de los elementos en cada paso.

Observaciones:
- Algoritmo interno.
- No usa comparaciones directas entre elementos.
- Requiere enteros no negativos (esta versión).
- Complejidad: O(d * n), donde d es el número de dígitos del número más grande.
- Estable.
"""

def counting_sort_por_digito(arr, digito):
    """
    Ordena el arreglo según el dígito actual usando Counting Sort.

    Parámetros:
    arr -- lista de números a ordenar
    digito -- posición del dígito actual (1 para unidades, 10 para decenas, etc.)
    """
    n = len(arr)
    salida = [0] * n         # Lista de salida ordenada
    conteo = [0] * 10        # Dígitos del 0 al 9

    # Contamos la frecuencia de cada dígito
    for numero in arr:
        indice = (numero // digito) % 10
        conteo[indice] += 1

    # Acumulamos los conteos para conocer posiciones finales
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construimos el arreglo de salida (de derecha a izquierda para estabilidad)
    for i in reversed(range(n)):
        indice = (arr[i] // digito) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1

    # Copiamos el arreglo ordenado de salida al original
    for i in range(n):
        arr[i] = salida[i]

    print(f"Después de ordenar por dígito {digito}: {arr}")

def radix_sort(arr):
    """
    Ordena una lista de enteros no negativos usando RadixSort.

    Parámetros:
    arr -- lista de números a ordenar (se modifica en el lugar)
    """
    if len(arr) == 0:
        return

    # Encontramos el número máximo para saber cuántos dígitos procesar
    maximo = max(arr)

    # Aplicamos Counting Sort por cada dígito (unidades, decenas, centenas, ...)
    digito = 1
    while maximo // digito > 0:
        counting_sort_por_digito(arr, digito)
        digito *= 10

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista de ejemplo con enteros no negativos
    datos = [170, 45, 75, 90, 802, 24, 2, 66]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos RadixSort
    radix_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
