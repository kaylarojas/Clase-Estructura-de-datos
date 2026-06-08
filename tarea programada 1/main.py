from gestor_csv import cargar_pokedex, guardar_pokedex
from algoritmos import merge_sort, quick_sort

def procesar_ordenamiento(lista_pokemones, encabezado, criterio, algoritmo):
    copia_lista = list(lista_pokemones)
    
    print(f"\nOrdenando la Pokédex por {criterio.upper()} mediante {algoritmo.upper()}...")
    
    if algoritmo == "mergesort":
        datos_ordenados = merge_sort(copia_lista, criterio)
    elif algoritmo == "quicksort":
        datos_ordenados = quick_sort(copia_lista, criterio)
        
    nombre_archivo_salida = f"pokemones_{criterio}_{algoritmo}.csv"
    guardar_pokedex(nombre_archivo_salida, encabezado, datos_ordenados)

def menu():
    encabezado = None
    lista_pokemones = None

    while True:
        print("\n" + "="*45)
        print("     SISTEMA DE REPORTES POKÉDEX    ")
        print("="*45)
        print("1. Leer archivo CSV")
        print("2. Ordenar por nombre")
        print("3. Ordenar por ataque")
        print("4. Ordenar por defensa")
        print("5. Salir")
        print("="*45)
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            encabezado, lista_pokemones = cargar_pokedex("pokemones.csv")
            
            # --- AGREGAR UNA VISTA PREVIA ---
            if lista_pokemones:
                print("\n> VISTA PREVIA DE LOS PRIMEROS 5 REGISTROS CARGADOS <")

                print(f"{'ID':<6} {'Nombre':<25} {'Tipo 1':<12} {'Ataque':<8} {'Defensa':<8}")
                print("-" * 65)
                
                for p in lista_pokemones[:3]:
                    print(f"{p.numero:<6} {p.nombre:<25} {p.tipo1:<12} {p.ataque:<8} {p.defensa:<8}")
                print("-" * 65)
                print(f"Total de registros listos en memoria: {len(lista_pokemones)}\n")
            # ----------------------------------------

        elif opcion in ["2", "3", "4"]:
            if lista_pokemones is None:
                print("\n[ADVERTENCIA] Debe cargar los datos primero (Opción 1).")
                continue
            
            mapa_criterios = {"2": "nombre", "3": "ataque", "4": "defensa"}
            criterio_actual = mapa_criterios[opcion]
            
            print(f"\n--- Algoritmo para ordenar por {criterio_actual.upper()} ---")
            print("a. Utilizar Merge Sort")
            print("b. Utilizar Quick Sort")
            sub_opcion = input("Seleccione una opción (a/b): ").strip().lower()

            if sub_opcion == "a":
                procesar_ordenamiento(lista_pokemones, encabezado, criterio_actual, "mergesort")
            elif sub_opcion == "b":
                procesar_ordenamiento(lista_pokemones, encabezado, criterio_actual, "quicksort")
            else:
                print("\n[ERROR] Selección de algoritmo inválida.")
                
        elif opcion == "5":
            print("\nCerrando el sistema de la Pokédex. ¡Éxito en la investigación, Profesor Oak!")
            break
        else:
            print("\n[ERROR] Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()