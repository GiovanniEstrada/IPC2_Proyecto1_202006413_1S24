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

    def imprimir(self, archivo):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            archivo.write(f"Codigo Patron:  {tmpNodoActual.Codigo}\n")
            tmpNodoActual.Patron.imprimir(archivo)
            tmpNodoActual = tmpNodoActual.siguiente            
    
    def buscarPatron(self, patron):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            if tmpNodoActual.Codigo == patron:
                return True
            tmpNodoActual = tmpNodoActual.siguiente
        
        return False
    
    def ordenarPatron(self):
        if self.cabeza == None:
            return
        
        tmpNodo1Nombre = self.cabeza.Codigo
        tmpNodo1Patron = self.cabeza.Patron
        if self.cabeza.Codigo > self.cola.Codigo:
            self.cabeza.Codigo = self.cola.Codigo
            self.cabeza.Patron = self.cola.Patron
            self.cola.Codigo = tmpNodo1Nombre
            self.cola.Patron = tmpNodo1Patron