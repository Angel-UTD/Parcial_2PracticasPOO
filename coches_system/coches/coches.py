class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    # ---------- GET (@property) ----------
    @property
    def marca(self):
        return self._marca

    @property
    def color(self):
        return self._color

    @property
    def modelo(self):
        return self._modelo

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def potencia(self):
        return self._potencia

    @property
    def asientos(self):
        return self._asientos

    # ---------- SET (@variable.setter) ----------
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @color.setter
    def color(self, color):
        self._color = color

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @asientos.setter
    def asientos(self, asientos):
        self._asientos = asientos
