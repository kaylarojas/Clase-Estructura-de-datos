class Validador:
    @staticmethod
    def solicitar_entero(mensaje, minimo=1):
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= minimo:
                    return valor
                print(f"Debe ingresar un número mayor o igual a {minimo}.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

    @staticmethod
    def solicitar_lista(mensaje):
        while True:
            entrada = input(mensaje)
            try:
                lista = [int(x.strip()) for x in entrada.split(",") if x.strip() != ""]
                if not lista:
                    print("La lista no puede estar vacía.")
                    continue
                if any(x < 0 for x in lista):
                    print("No se permiten números negativos.")
                    continue
                return lista
            except ValueError:
                print("Formato incorrecto. Use números separados por comas (ej: 2,3,5).")