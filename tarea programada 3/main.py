# main.py
import json
import os

from dijkstra import ejecutar_dijkstra, obtener_ruta_dijkstra
from tsp import ejecutar_tsp

def cargar_datos_seguro():
    carpeta_del_script = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta_json = os.path.join(carpeta_del_script, "grafo.json")
    
    if not os.path.exists(ruta_absoluta_json):
        raise FileNotFoundError(f"No se encontró el archivo json en la ruta: {ruta_absoluta_json}")
        
    with open(ruta_absoluta_json, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    paises = datos["vertices"]
    grafo = {v: {} for v in paises}
    for arista in datos["aristas"]:
        grafo[arista["origen"]][arista["destino"]] = arista["peso"]
        
    return paises, grafo

def main():
    try:
        paises, grafo = cargar_datos_seguro()
        print(" ¡Grafo y archivo JSON cargados correctamente!")
    except Exception as e:
        print(f" Error crítico de carga:\n{e}")
        return

    origen = "Japón"
    
    print("=" * 60)
    print("                OPERACIÓN SHADALOO GLOBAL")
    print("=" * 60)
    
    # PROBLEMA 1: DIJKSTRA
    print("\n--- PROBLEMA 1: CAMINO MÁS CORTO DESDE JAPÓN ---")
    distancias, predecesores = ejecutar_dijkstra(grafo, origen)
    for pais in paises:
        if pais == origen: 
            continue
        if distancias[pais] == float('inf'):
            print(f" {pais:15} -> ¡Inalcanzable!")
        else:
            camino = obtener_ruta_dijkstra(predecesores, pais)
            print(f" {pais:15} -> Costo: {distancias[pais]:<2} | Ruta: {' ➔ '.join(camino)}")
            
    # PROBLEMA 2: GIRA MUNDIAL (TSP)
    print("\n--- PROBLEMA 2: GIRA MUNDIAL OPTIMIZADA (TSP) ---")
    ruta, costo = ejecutar_tsp(grafo, origen)
    if costo != float('inf'):
        print(f" Ruta óptima: {' ➔ '.join(ruta)}")
        print(f" Costo total de viaje: {costo}")
    else:
        print(" No hay una ruta válida que recorra todos los países una vez y regrese.")
    print("=" * 60)

if __name__ == "__main__":
    main()