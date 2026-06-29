from validaciones import Validador
from n_reinas import VigilanciaCastillo
from subconjuntos import GestorRecursos

def menu():
    while True:
        print("\n=============================================")
        print("      SISTEMA DE SEGURIDAD Y LOGÍSTICA       ")
        print("=============================================")
        print("1. Vigilancia del Castillo (N-Reinas)")
        print("2. Gestión de Recursos (Subconjuntos)")
        print("3. Salir")
        print("=============================================")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- CONFIGURACIÓN DE VIGILANCIA ---")
            n = Validador.solicitar_entero("Tamaño del tablero (N): ", minimo=1)
            problema1 = VigilanciaCastillo(n)
            problema1.ejecutar()

        elif opcion == "2":
            print("\n--- DISTRIBUCIÓN DE RECURSOS ---")
            cargamentos = Validador.solicitar_lista("Lista de cargamentos (ej: 2,3,5,7): ")
            objetivo = Validador.solicitar_entero("Suma objetivo: ", minimo=0)
            problema2 = GestorRecursos(cargamentos, objetivo)
            problema2.ejecutar()

        elif opcion == "3":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()