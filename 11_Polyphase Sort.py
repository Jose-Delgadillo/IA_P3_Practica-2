"""
Método de Ordenamiento Externo - Polyphase Sort

Polyphase Sort es una variante del Balanced Multiway Merge que optimiza el uso de cintas
(dispositivos de almacenamiento) al minimizar el número de fases de mezcla. Se basa en
la distribución de las secuencias ordenadas (runs) según una serie de Fibonacci para que
en cada paso haya un mínimo de cintas activas y una mejor redistribución de los datos.

Este ejemplo **simula** el proceso en memoria con listas y muestra cómo se haría el
ordenamiento por fases usando solo 3 "cintas".

Observaciones:
- Algoritmo externo real (simulado aquí).
- Reduce I/O usando estrategia de redistribución optimizada.
- Complejidad: O(n log n)
"""

"""
Polyphase Sort (corregido) - Simulación en memoria con 3 cintas
"""

def merge(lista1, lista2):
    """Fusión de dos listas ordenadas."""
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

def polyphase_sort_simulado(runs):
    """
    Versión corregida de ordenamiento polifásico simulado.
    
    runs -- lista de listas ordenadas (simulando archivos)
    """
    # Inicialmente todas las runs están en la cinta A
    cinta_A = runs.copy()
    cinta_B = []
    cinta_C = []

    fase = 1
    while True:
        print(f"\nFase {fase}:")
        nueva_cinta = []

        # Mezclamos de dos en dos desde cinta_A y cinta_B
        while cinta_A and cinta_B:
            run_A = cinta_A.pop(0)
            run_B = cinta_B.pop(0)
            mezcla = merge(run_A, run_B)
            print(f"Mezclando {run_A} + {run_B} -> {mezcla}")
            nueva_cinta.append(mezcla)

        # Mover sobrantes (si hay) sin mezclar
        nueva_cinta.extend(cinta_A)
        nueva_cinta.extend(cinta_B)

        # Si solo queda una run total, hemos terminado
        if len(nueva_cinta) == 1:
            return nueva_cinta[0]

        # Rotamos las cintas: C -> A, nueva -> B, vaciamos C
        cinta_A, cinta_B, cinta_C = cinta_C, nueva_cinta, []
        fase += 1

# Bloque principal para probar
if __name__ == "__main__":
    runs = [
        [3], [8], [2], [5],
        [1], [9], [4], [7],
        [6]
    ]

    print("Runs iniciales:", runs)

    resultado = polyphase_sort_simulado(runs)

    print("\nResultado ordenado final:", resultado)
