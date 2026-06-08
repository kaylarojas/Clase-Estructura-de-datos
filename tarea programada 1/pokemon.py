class Pokemon:
    def __init__(self, numero, nombre, tipo1, tipo2, total, hp, ataque, defensa, sp_atk, sp_def, velocidad, generacion, legendario):
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.total = int(total)
        self.hp = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.sp_atk = int(sp_atk)
        self.sp_def = int(sp_def)
        self.velocidad = int(velocidad)
        self.generacion = int(generacion)
        self.legendario = legendario

    def obtener_valor_por_criterio(self, criterio):
        """
        Retorna el atributo correcto convertido para su respectiva comparación.
        """
        if criterio == "nombre":
            return self.nombre.lower()  # Minúsculas para orden alfabético correcto
        elif criterio == "ataque":
            return self.ataque
        elif criterio == "defensa":
            return self.defensa
        return self.numero

    def to_list(self):
        """
        Convierte de nuevo el objeto a una lista de strings para poder guardarlo en el CSV.
        """
        return [
            self.numero, self.nombre, self.tipo1, self.tipo2, self.total,
            self.hp, self.ataque, self.defensa, self.sp_atk, self.sp_def,
            self.velocidad, self.generacion, self.legendario
        ]