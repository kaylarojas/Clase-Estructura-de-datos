# tsp.py

def ejecutar_tsp(grafo, inicio):
    vertices = list(grafo.keys())
    n = len(vertices)
    ruta_optima = []
    costo_optimo = float('inf')
    
    def backtrack(nodo_actual, visitados, ruta_actual, costo_actual):
        nonlocal ruta_optima, costo_optimo
        
        if len(visitados) == n:
            if inicio in grafo[nodo_actual]:
                costo_total = costo_actual + grafo[nodo_actual][inicio]
                if costo_total < costo_optimo:
                    costo_optimo = costo_total
                    ruta_optima = list(ruta_actual) + [inicio]
            return
            
        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in visitados and costo_actual + peso < costo_optimo:
                visitados.add(vecino)
                ruta_actual.append(vecino)
                backtrack(vecino, visitados, ruta_actual, costo_actual + peso)
                ruta_actual.pop()
                visitados.remove(vecino)

    backtrack(inicio, {inicio}, [inicio], 0)
    return ruta_optima, costo_optimo