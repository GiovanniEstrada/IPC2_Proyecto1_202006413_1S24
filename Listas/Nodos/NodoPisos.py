class NodoPiso:

    def __init__(self, vlNombre, vlR, vlC, vlF, vlS, vlPatron):
        self.anterior = None
        self.Nombre = vlNombre
        self.Fila = vlR
        self.Columna = vlC
        self.Voltear = vlF
        self.Intercambio = vlS
        self.Patrones = vlPatron
        self.siguiente = None
