from graphviz import Digraph

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
            
    def ordenarPisos(self):
        if self.cabeza == None:
            return
        
        tmpNodo1 = self.cabeza.siguiente

        while tmpNodo1:
            tmpNombreNodo = tmpNodo1.Nombre
            tmpFilaNodo = tmpNodo1.Fila
            tmpColumnaNodo = tmpNodo1.Columna
            tmpVoltearNodo = tmpNodo1.Voltear
            tmpIntercambioNodo = tmpNodo1.Intercambio
            tmpPatronesNodo = tmpNodo1.Patrones
            tmpNodoAnterior = tmpNodo1.anterior
            
            while tmpNodoAnterior != None and tmpNodoAnterior.Nombre > tmpNombreNodo:
                tmpNodoAnterior.siguiente.Nombre = tmpNodoAnterior.Nombre
                tmpNodoAnterior.siguiente.Fila = tmpNodoAnterior.Fila
                tmpNodoAnterior.siguiente.Columna = tmpNodoAnterior.Columna
                tmpNodoAnterior.siguiente.Intercambio = tmpNodoAnterior.Intercambio
                tmpNodoAnterior.siguiente.Voltear = tmpNodoAnterior.Voltear
                tmpNodoAnterior.siguiente.Patrones = tmpNodoAnterior.Patrones
                tmpNodoAnterior = tmpNodoAnterior.anterior

            if tmpNodoAnterior == None:
                self.cabeza.Nombre = tmpNombreNodo
                self.cabeza.Fila = tmpFilaNodo
                self.cabeza.Columna = tmpColumnaNodo
                self.cabeza.Intercambio = tmpIntercambioNodo
                self.cabeza.Voltear = tmpVoltearNodo
                self.cabeza.Patrones = tmpPatronesNodo
            else:
                tmpNodoAnterior.siguiente.Nombre = tmpNombreNodo
                tmpNodoAnterior.siguiente.Fila = tmpFilaNodo
                tmpNodoAnterior.siguiente.Columna = tmpColumnaNodo
                tmpNodoAnterior.siguiente.Intercambio = tmpIntercambioNodo
                tmpNodoAnterior.siguiente.Voltear = tmpVoltearNodo
                tmpNodoAnterior.siguiente.Patrones = tmpPatronesNodo

            tmpNodo1 = tmpNodo1.siguiente


    def graficarPisos(self, vlNombrePiso):

        # SE HACE AL BUSQUEDA DEL PISO Y SU PATRON
        pisos = self.cabeza
        while pisos:
            if pisos.Nombre == vlNombrePiso:
                break
            pisos = pisos.siguiente

        # SE VALIDA QUE EL PISO SE HAYA ENCONTRADO
        if pisos == None:
            print("No se ha encontrado el piso, ingrese nuevamente...")
            return False
        

        while pisos.Patrones:
                
                NodoPatrones = pisos.Patrones
                if pisos.Patrones == None:
                    break
                if NodoPatrones.cabeza == None:
                    break

                dot = Digraph('G')
                dot.attr(rankdir='TB')
                dot.attr('node', shape='box', style='filled')
            
                n = int(pisos.Fila)
                m = int(pisos.Columna)
                with dot.subgraph(name='matriz_azulejos') as c:
                    # GENERA EL PATRON

                    c.node('T', f'Nombre piso: {vlNombrePiso}', fontsize='15', shape='plaintext')

                    c.node('S', f'Código: {NodoPatrones.cabeza.Codigo}', fontsize='15', shape='plaintext')

                    for i in range(n):
                        for j in range(m):
                            tmpNodoAzulejo = pisos.Patrones.cabeza.Patron.buscarAzulejo(m, j, i)
                            idNodo = node_id = f'{str(n - i) + str(m - j)}'
                            if str(tmpNodoAzulejo.CodAzulejo) == "N":
                                c.node(f'{idNodo}', 'N', fillcolor='black', fontcolor='white')
                            else:
                                c.node(f'{idNodo}', 'B', fillcolor='white')
                            
                            if j > 0:
                                c.edge(f'{idNodo}', node_id, style='invis')
                            # Add invisible edges between the nodes in the same column
                            if i > 0:
                                c.edge(f'{idNodo}', node_id, style='invis')


                for i in range(n):
                    tmpFilaA = ''
                    tmpFilaB = ''
                    tmpEdgeNode = []
                    for j in range(m):
                        tmpNodoAzulejo = NodoPatrones.cabeza.Patron.buscarAzulejo(m, i, j)
                        tmpFilaB = tmpFilaA
                        tmpFilaA = f'{str(n - i) + str(m - j)}'
                        if(tmpFilaB != ''):
                            tmpEdgeNode.append((f'{tmpFilaB}', f'{tmpFilaA}'))

                    dot.edges(tmpEdgeNode)
                    dot.edge_attr.update(style='invis')
                    print(tmpEdgeNode)

                    # Guardar el gráfico
                dot.render(f'{pisos.Patrones.cabeza.Codigo}.gv', view=True)

                NodoPatrones.cabeza = NodoPatrones.cabeza.siguiente

    