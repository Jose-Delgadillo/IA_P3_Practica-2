"""
Método de Ordenamiento - Ordenamiento de Árbol (Tree Sort)

Este algoritmo inserta los elementos en un Árbol Binario de Búsqueda (BST).
Luego realiza un recorrido en orden (in-order) que devuelve los elementos
de menor a mayor, ya que en un BST el recorrido in-order genera una lista ordenada.

Observaciones:
- Algoritmo interno.
- Requiere estructura adicional (el árbol).
- Eficiente si el árbol está balanceado.
- Complejidad promedio: O(n log n), peor caso: O(n^2)
- No estable (elementos iguales pueden cambiar de orden).
"""

# Definición de un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un nuevo valor en el árbol
def insertar_nodo(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    elif valor < raiz.valor:
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz

# Recorrido inorden para obtener los elementos ordenados
def recorrido_inorden(nodo, resultado):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        recorrido_inorden(nodo.derecha, resultado)

# Función principal que ordena una lista con Tree Sort
def tree_sort(arr):
    raiz = None

    # Insertamos todos los elementos del arreglo en el árbol
    for valor in arr:
        raiz = insertar_nodo(raiz, valor)

    # Recorrido inorden para obtener los valores ordenados
    resultado = []
    recorrido_inorden(raiz, resultado)

    # Copiamos el resultado en la lista original
    for i in range(len(arr)):
        arr[i] = resultado[i]

# Bloque principal para probar la función
if __name__ == "__main__":
    # Lista desordenada de ejemplo
    datos = [9, 3, 1, 5, 4, 2, 8]

    # Mostramos el estado original del arreglo
    print("Arreglo original:", datos)

    # Aplicamos el algoritmo Tree Sort
    tree_sort(datos)

    # Mostramos el arreglo ordenado
    print("Arreglo ordenado: ", datos)
