class ListaPatrones:

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
            print("Codigo: ", tmpNodoActual.Codigo)
            tmpNodoActual.Patron.imprimir()
            tmpNodoActual = tmpNodoActual.siguiente            
    
    def buscarPatron(self, patron):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            if tmpNodoActual.Codigo == patron:
                return True
            tmpNodoActual = tmpNodoActual.siguiente
        
        return False
    