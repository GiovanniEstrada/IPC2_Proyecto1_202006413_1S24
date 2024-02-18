from ..Nodos.NodoPisos import NodoPiso

class ListaPisos:

    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def insertar(self, vlNodo):
        # SE VALIDA SI SE ESTA INGRESANDO EL PRIMER NODO
        if self.cabeza == None:
            self.cabeza = vlNodo
            self.cola = vlNodo
        else:
            vlNodo.anterior = self.cola
            self.cola.siguiente = vlNodo
            self.cola = vlNodo

    def imprimir(self):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            print("NOMBRE: ", tmpNodoActual.Nombre)
            print("Filas: ", tmpNodoActual.Fila)
            print("Columnas: ", tmpNodoActual.Columna)
            print("Voltear: ", tmpNodoActual.Voltear)
            print("Intercambiar: ", tmpNodoActual.Intercambio)
            tmpNodoActual.Patrones.imprimir()
            tmpNodoActual = tmpNodoActual.siguiente
            print("------------------- \n")
            
                
    