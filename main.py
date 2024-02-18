from xml.dom import minidom
from Listas.ListasEnlazadas.ListaPisos import ListaPisos
from Listas.Nodos.NodoPisos import NodoPiso
from Listas.ListasEnlazadas.ListaPatrones import ListaPatrones
from Listas.Nodos.NodoPatrones import NodoPatron

def main():
    xml = minidom.parse('entrada.xml')
    pisos = xml.getElementsByTagName('piso')
    
    listaPisos = ListaPisos()
    for piso in pisos:

        # OBTENEMOS LOS PATRONES CORRESPONDIENTES AL PISO
        listaPatrones = ListaPatrones()
        patrones = piso.getElementsByTagName('patrones')[0].getElementsByTagName('patron')
        for patron in patrones:
            nuevoPatron = NodoPatron(patron.getAttribute("codigo"),
                                     patron.firstChild.data.strip())
            listaPatrones.insertar(nuevoPatron)

        # SE INSERTAN LOS ATRIBUTOS DEL PISO
        nuevoPiso = NodoPiso(piso.getAttribute("nombre"),
                             piso.getElementsByTagName("R")[0].firstChild.data,
                             piso.getElementsByTagName("C")[0].firstChild.data,
                             piso.getElementsByTagName("F")[0].firstChild.data,
                             piso.getElementsByTagName("S")[0].firstChild.data,
                             listaPatrones)
        
        listaPisos.insertar(nuevoPiso)

    listaPisos.imprimir()



if __name__ == "__main__":
    main()