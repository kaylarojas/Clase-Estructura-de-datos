class VigilanciaCastillo:
    def __init__(self, n):
        self.n = n
        self.tablero = [['.' for _ in range(n)] for _ in range(n)]
        self.soluciones = []

    def _es_seguro(self, fila, col):
        # Verificar columna superior
        for i in range(fila):
            if self.tablero[i][col] == 'Q':
                return False

        # Diagonal superior izquierda
        i, j = fila - 1, col - 1
        while i >= 0 and j >= 0:
            if self.tablero[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Diagonal superior derecha
        i, j = fila - 1, col + 1
        while i >= 0 and j < self.n:
            if self.tablero[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def _buscar_soluciones(self, fila):
        if fila == self.n:
            self.soluciones.append([f.copy() for f in self.tablero])
            return

        for col in range(self.n):
            if self._es_seguro(fila, col):
                self.tablero[fila][col] = 'Q'
                self._buscar_soluciones(fila + 1)
                self.tablero[fila][col] = '.'  # Backtracking

    def ejecutar(self):
        self.soluciones.clear()
        self._buscar_soluciones(0)
        total = len(self.soluciones)
        
        print(f"\nTotal de soluciones encontradas: {total}")
        if total > 0:
            print("\nUna solución válida:")
            for fila in self.soluciones[0]:
                print(" ".join(fila))
        else:
            print("No se encontró ninguna solución para este tamaño.")