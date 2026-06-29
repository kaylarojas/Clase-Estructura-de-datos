class GestorRecursos:
    def __init__(self, recursos, objetivo):
        self.recursos = sorted(recursos)
        self.objetivo = objetivo
        self.soluciones = []

    def _buscar_subconjuntos(self, indice, ruta_actual, suma_actual):
        if suma_actual == self.objetivo:
            if ruta_actual not in self.soluciones:
                self.soluciones.append(ruta_actual.copy())
            return

        if suma_actual > self.objetivo or indice >= len(self.recursos):
            return

        # Caso 1: Incluir el recurso actual
        ruta_actual.append(self.recursos[indice])
        self._buscar_subconjuntos(indice + 1, ruta_actual, suma_actual + self.recursos[indice])
        ruta_actual.pop()  # Backtracking

        # Caso 2: Ignorar el recurso actual
        self._buscar_subconjuntos(indice + 1, ruta_actual, suma_actual)

    def ejecutar(self):
        self.soluciones.clear()
        self._buscar_subconjuntos(0, [], 0)
        
        print("\nSubconjuntos válidos encontrados:")
        if self.soluciones:
            for sol in self.soluciones:
                print(sol)
            print(f"Total de soluciones: {len(self.soluciones)}")
        else:
            print("No existe ninguna combinación que sume la cantidad objetivo.")
            print("Total de soluciones: 0")