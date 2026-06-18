import csv
import os  
from pokemon import Pokemon

def cargar_pokedex(nombre_archivo="pokemones.csv"):
    lista_pokemones = []
    
    ruta_carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta_csv = os.path.join(ruta_carpeta_actual, nombre_archivo)

    try:
        with open(ruta_absoluta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            
            for fila in lector:
                if fila:
                    nuevo_pokemon = Pokemon(*fila)
                    lista_pokemones.append(nuevo_pokemon)
                    
        print(f"\n[ÉXITO] Archivo cargado desde: {ruta_absoluta_csv}")
        return encabezado, lista_pokemones
    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo en: {ruta_absoluta_csv}")
        return None, None

def guardar_pokedex(nombre_archivo, encabezado, lista_pokemones):

    ruta_carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta_csv = os.path.join(ruta_carpeta_actual, nombre_archivo)
    
    try:
        with open(ruta_absoluta_csv, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(encabezado)
            filas_convertidas = [p.to_list() for p in lista_pokemones]
            escritor.writerows(filas_convertidas)
        print(f"[ÉXITO] Reporte generado con éxito en: '{nombre_archivo}'")
    except Exception as e:
        print(f"[ERROR] No se pudo escribir el archivo: {e}")