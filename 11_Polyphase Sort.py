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

def merge(lista1, lista2):
    """Fusiona dos listas ordenadas en una lista ordenada."""
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

def merge_por_fases(runs):
    """
    Simula la fusión en fases de múltiples runs ordenados,
    fusionando de dos en dos hasta quedar un único run.
    
    runs -- lista de runs ordenadas (listas).
    """
    fase = 1
    runs_actuales = runs.copy()
    
    while len(runs_actuales) > 1:
        print(f"\nFase {fase}: {len(runs_actuales)} runs a fusionar")
        nuevos_runs = []
        
        # Fusionar pares de runs
        for i in range(0, len(runs_actuales), 2):
            if i + 1 < len(runs_actuales):
                run1 = runs_actuales[i]
                run2 = runs_actuales[i + 1]
                fusion = merge(run1, run2)
                print(f"Mezclando {run1} + {run2} -> {fusion}")
                nuevos_runs.append(fusion)
            else:
                # Si queda un run sin pareja, pasa directo a la siguiente fase
                print(f"Run sin pareja que pasa directo: {runs_actuales[i]}")
                nuevos_runs.append(runs_actuales[i])
        
        runs_actuales = nuevos_runs
        fase += 1
    
    return runs_actuales[0] if runs_actuales else []

# Bloque principal para probar la función
if __name__ == "__main__":
    runs = [
        [3],
        [8],
        [2],
        [5],
        [1],
        [9],
        [4],
        [7],
        [6]
    ]
    
    print("Runs iniciales:", runs)
    
    resultado_final = merge_por_fases(runs)
    
    print("\nResultado ordenado final:", resultado_final)