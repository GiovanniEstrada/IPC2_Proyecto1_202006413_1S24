class ListaAzulejos:

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
            print("COLOR AZULEJO: ", tmpNodoActual.CodAzulejo)
            tmpNodoActual = tmpNodoActual.siguiente            

    def buscarAzulejo(self, vlColumnaT, vlFilaB, vlColumnaB):
        # SE BUSCA EL NUMERO DE ITERACIONES QUE NECESITA PARA LA BUSQUEDA
        iteracion = (vlFilaB) * (vlColumnaT) + vlColumnaB
        tmpNodoActual = self.cabeza
        for i in range(iteracion):
            tmpNodoActual = tmpNodoActual.siguiente
        
        return tmpNodoActual

                
