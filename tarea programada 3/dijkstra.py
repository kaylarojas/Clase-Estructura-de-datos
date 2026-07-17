# dijkstra.py

def ejecutar_dijkstra(grafo, inicio):
    distancias = {v: float('inf') for v in grafo}
    predecesores = {v: None for v in grafo}
    distancias[inicio] = 0
    no_visitados = list(grafo.keys())
    
    while no_visitados:
        nodo_actual = min(no_visitados, key=lambda n: distancias[n])
        if distancias[nodo_actual] == float('inf'):
            break
        no_visitados.remove(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            if distancias[nodo_actual] + peso < distancias[vecino]:
                distancias[vecino] = distancias[nodo_actual] + peso
                predecesores[vecino] = nodo_actual
                
    return distancias, predecesores

def obtener_ruta_dijkstra(predecesores, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = predecesores[actual]
    return camino[::-1]