from graphviz import Digraph
from Listas.ListasEnlazadas.ListaAzulejos import ListaAzulejos
from Listas.Nodos.NodoAzulejos import NodoAzulejo

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
        self.ordenarPisos()
        tmpNodoActual = self.cabeza
        with open("ListaPisos.txt", "w") as archivo:
            archivo.write("")
        with open("ListaPisos.txt", "a") as archivo:
            while tmpNodoActual:
                archivo.write(f"Nombre:         {tmpNodoActual.Nombre}\n")
                archivo.write(f"Filas:          {tmpNodoActual.Fila}\n")
                archivo.write(f"Columnas:       {tmpNodoActual.Columna}\n")
                archivo.write(f"Voltear:        {tmpNodoActual.Voltear}\n")
                archivo.write(f"Intercambiar:   {tmpNodoActual.Intercambio}\n")
                tmpNodoActual.Patrones.imprimir(archivo)
                tmpNodoActual = tmpNodoActual.siguiente
                archivo.write(f"------------------------------- \n\n")
            
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

            tmpNodo1.Patrones.ordenarPatron()
            tmpNodo1 = tmpNodo1.siguiente


    def graficarPisos(self, vlNombrePiso, vlNombrePatron):

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
        
        if pisos.Patrones.cabeza.Codigo == vlNombrePatron:
            NodoPatrones = pisos.Patrones.cola
        else:
            NodoPatrones = pisos.Patrones.cabeza


        dot = Digraph('G')
        dot.attr(rankdir='TB')
        dot.attr('node', shape='box', style='filled')
    
        n = int(pisos.Fila)
        m = int(pisos.Columna)
        with dot.subgraph(name='matriz_azulejos') as c:

            c.node('T', f'Nombre piso: {vlNombrePiso}', fontsize='15', shape='plaintext')

            c.node('S', f'Código: {NodoPatrones.Codigo}', fontsize='15', shape='plaintext')

            for i in range(n):
                for j in range(m):
                    
                    tmpNodoAzulejo = NodoPatrones.Patron.buscarAzulejo(m, i, j)
                    idNodo = node_id = f'{str(n - i) + str(m - j)}'
                    
                    if tmpNodoAzulejo is None:
                        break

                    if str(tmpNodoAzulejo.CodAzulejo) == "N":
                        c.node(f'{idNodo}', 'N', fillcolor='black', fontcolor='white')
                    else:
                        c.node(f'{idNodo}', 'B', fillcolor='white')
                    
                    if j > 0:
                        c.edge(f'{idNodo}', f'{node_id[:-1]}{m-j}', style='invis')
                    if i > 0:
                        c.edge(f'{idNodo}', f'{node_id[:-1]}{m-j}', style='invis')


        for i in range(n):
            tmpFilaA = ''
            tmpFilaB = ''
            tmpEdgeNode = []
            for j in range(m):
                tmpNodoAzulejo = NodoPatrones.Patron.buscarAzulejo(m, i, j)
                tmpFilaB = tmpFilaA
                tmpFilaA = f'{str(n - i) + str(m - j)}'
                if(tmpFilaB != ''):
                    tmpEdgeNode.append((f'{tmpFilaB}', f'{tmpFilaA}'))

            dot.edges(tmpEdgeNode)
            dot.edge_attr.update(style='invis')
            print(tmpEdgeNode)

            # Guardar el gráfico
        dot.render(f'{NodoPatrones.Codigo}.gv', view=True)

        NodoPatrones = NodoPatrones.siguiente



    def buscarPiso(self, piso):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            if tmpNodoActual.Nombre == piso:
                return True
            tmpNodoActual = tmpNodoActual.siguiente
        
        return False
    
    def buscarPatron(self, piso, patron):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            if tmpNodoActual.Nombre == piso:
                if tmpNodoActual.Patrones.buscarPatron(patron):
                    return True
            tmpNodoActual = tmpNodoActual.siguiente
        return False

    
    def instruccionCambio(self, piso, patron, tipo):
        # SE HACE AL BUSQUEDA DEL PISO Y SU PATRON
        pisos = self.cabeza
        while pisos:
            if pisos.Nombre == piso:
                break
            pisos = pisos.siguiente

        if pisos.Patrones.cabeza == patron:
            patronInicial = pisos.Patrones.cabeza.Patron.cabeza
            patronFinal = pisos.Patrones.cola.Patron.cabeza
        else:
            patronInicial = pisos.Patrones.cola.Patron.cabeza
            patronFinal = pisos.Patrones.cabeza.Patron.cabeza

        m = 0
        n = 0
        costo = 0

        tmpListaAzulejo = ListaAzulejos()

        while patronInicial:
            tmpCodInicial = patronInicial.CodAzulejo
            tmpNodoAzulejo = NodoAzulejo(str(tmpCodInicial))
            tmpListaAzulejo.insertar(tmpNodoAzulejo)
            patronInicial = patronInicial.siguiente

        if pisos.Patrones.cabeza == patron:
            patronInicial = pisos.Patrones.cabeza.Patron.cabeza
            patronFinal = pisos.Patrones.cola.Patron.cabeza
        else:
            patronInicial = pisos.Patrones.cola.Patron.cabeza
            patronFinal = pisos.Patrones.cabeza.Patron.cabeza

        while patronInicial:

            if tipo == "Txt":
                with open(f"Instruccion-{pisos.Nombre}.txt", "w") as archivo:
                    archivo.write("INSTRUCCIONES PARA CAMBIO DE PISO: \n")

                with open(f"Instruccion-{pisos.Nombre}.txt", "a") as archivo:
                    tmpPatronInicial = patronInicial
                    tmpCodInicial = patronInicial.CodAzulejo

                    m += 1
                    if m > int(pisos.Columna):
                        m = 1
                        n += 1

                    if patronInicial.CodAzulejo == patronFinal.CodAzulejo:
                        archivo.write(f"{m}x{n + 1}: No hubo movimiento\n")
                        patronInicial = patronInicial.siguiente
                        patronFinal = patronFinal.siguiente
                        continue

                    if int(pisos.Intercambio) < int(pisos.Voltear):

                        if m < int(pisos.Columna) and not patronInicial.siguiente is None:
                            if patronInicial.siguiente.CodAzulejo == patronFinal.CodAzulejo:
                                # patronInicial.CodAzulejo = patronInicial.siguiente.CodAzulejo
                                # patronInicial.siguiente.CodAzulejo = tmpCodInicial
                                archivo.write(f"{m}x{n + 1}: Intercambio con {m + 1}x{n + 1} | Costo: Q{pisos.Intercambio}\n") 
                                costo += int(pisos.Intercambio)
                                patronInicial.CodAzulejo = patronInicial.siguiente.CodAzulejo
                                patronInicial.siguiente.CodAzulejo = tmpCodInicial
                                patronInicial = patronInicial.siguiente
                                patronFinal = patronFinal.siguiente
                                continue
                        
                        flgIntercambio = False

                        if n < int(pisos.Fila):
                            i = n       # Fila salto
                            j = m       # Columna salto

                            # SE ITERA HASTA EL AZULEJO DE ABAJO
                            while True:
                                if patronInicial is None:
                                    break

                                patronInicial = patronInicial.siguiente

                                j += 1
                                if j > int(pisos.Columna):
                                    j = 1
                                    i += 1

                                if i == (n + 1) and j == m:
                                    if patronInicial is None:
                                        break

                                    if patronFinal.CodAzulejo == patronInicial.CodAzulejo:
                                        patronInicial.CodAzulejo = tmpCodInicial

                                        flgIntercambio = True
                                        break

                            # SE DEVUELVE EL APUNTADOR HACIA EL AZULEJO QUE HA CAMBIADO
                            patronInicial = tmpPatronInicial
                            patronInicial.CodAzulejo = patronFinal.CodAzulejo

                        if flgIntercambio:

                            archivo.write(f"{m}x{n + 1}: Intercambio con {j}x{i + 1} | Costo: Q{pisos.Intercambio}\n")
                            costo += int(pisos.Intercambio)
                            patronInicial = patronInicial.siguiente
                            patronFinal = patronFinal.siguiente
                            continue

                        # SE VOLTEA EL AZULEJO
                        patronInicial.CodAzulejo = patronFinal.CodAzulejo
                        costo += int(pisos.Voltear)
                        archivo.write(f"{m}x{n + 1}: Voltear Azulejo | Costo: Q{pisos.Voltear}\n")
                        patronInicial = patronInicial.siguiente
                        patronFinal = patronFinal.siguiente
                    else:
                        patronInicial.CodAzulejo = patronFinal.CodAzulejo
                        costo += int(pisos.Voltear)
                        archivo.write(f"{m}x{n + 1}: Voltear Azulejo | Costo: Q{pisos.Voltear}\n")
                        patronInicial = patronInicial.siguiente
                        patronFinal = patronFinal.siguiente

            else:
                # SE IMPRIME POR CONSOLA -------------------------------------

                tmpPatronInicial = patronInicial
                tmpCodInicial = patronInicial.CodAzulejo
                tmpNodoAzulejo = NodoAzulejo(str(tmpCodInicial))
                tmpListaAzulejo.insertar(tmpNodoAzulejo)

                m += 1
                if m > int(pisos.Columna):
                    m = 1
                    n += 1

                if patronInicial.CodAzulejo == patronFinal.CodAzulejo:
                    print(f"{m}x{n + 1}: No hubo movimiento")
                    patronInicial = patronInicial.siguiente
                    patronFinal = patronFinal.siguiente
                    continue

                if int(pisos.Intercambio) < int(pisos.Voltear):

                    if m < int(pisos.Columna) and not patronInicial.siguiente is None:
                        if patronInicial.siguiente.CodAzulejo == patronFinal.CodAzulejo:
                            # patronInicial.CodAzulejo = patronInicial.siguiente.CodAzulejo
                            # patronInicial.siguiente.CodAzulejo = tmpCodInicial
                            print(f"{m}x{n + 1}: Intercambio con {m + 1}x{n + 1} | Costo: Q{pisos.Intercambio}") 
                            costo += int(pisos.Intercambio)
                            patronInicial.CodAzulejo = patronInicial.siguiente.CodAzulejo
                            patronInicial.siguiente.CodAzulejo = tmpCodInicial
                            patronInicial = patronInicial.siguiente
                            patronFinal = patronFinal.siguiente
                            continue
                    
                    flgIntercambio = False

                    if n < int(pisos.Fila):
                        i = n       # Fila salto
                        j = m       # Columna salto

                        # SE ITERA HASTA EL AZULEJO DE ABAJO
                        while True:
                            if patronInicial is None:
                                break

                            patronInicial = patronInicial.siguiente

                            j += 1
                            if j > int(pisos.Columna):
                                j = 1
                                i += 1

                            if i == (n + 1) and j == m:
                                if patronInicial is None:
                                    break

                                if patronFinal.CodAzulejo == patronInicial.CodAzulejo:
                                    patronInicial.CodAzulejo = tmpCodInicial

                                    flgIntercambio = True
                                    break

                        # SE DEVUELVE EL APUNTADOR HACIA EL AZULEJO QUE HA CAMBIADO
                        patronInicial = tmpPatronInicial
                        patronInicial.CodAzulejo = patronFinal.CodAzulejo

                    if flgIntercambio:

                        print(f"{m}x{n + 1}: Intercambio con {j}x{i + 1} | Costo: Q{pisos.Intercambio}")
                        costo += int(pisos.Intercambio)
                        patronInicial = patronInicial.siguiente
                        patronFinal = patronFinal.siguiente
                        continue

                    # SE VOLTEA EL AZULEJO
                    patronInicial.CodAzulejo = patronFinal.CodAzulejo
                    costo += int(pisos.Voltear)
                    print(f"{m}x{n + 1}: Voltear Azulejo | Costo: Q{pisos.Voltear}")
                    patronInicial = patronInicial.siguiente
                    patronFinal = patronFinal.siguiente
                else:
                    patronInicial.CodAzulejo = patronFinal.CodAzulejo
                    costo += int(pisos.Voltear)
                    print(f"{m}x{n + 1}: Voltear Azulejo | Costo: Q{pisos.Voltear}")
                    patronInicial = patronInicial.siguiente
                    patronFinal = patronFinal.siguiente

        if pisos.Patrones.cabeza == patron:
            pisos.Patrones.cabeza.Patron = None
            pisos.Patrones.cabeza.Patron = tmpListaAzulejo
        else:
            pisos.Patrones.cola.Patron = None          
            pisos.Patrones.cola.Patron = tmpListaAzulejo          

        if (tipo == "Txt"):
            archivo.write("-----------------------------")
            archivo.write(f"Costo total: Q{costo}")
        else:
            print("-----------------------------")
            print(f"Costo total: Q{costo}")
