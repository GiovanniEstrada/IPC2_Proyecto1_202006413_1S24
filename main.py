# LIBRERIAS PYTHON
from xml.dom import minidom
from tkinter import filedialog
import tkinter as tk

# LISTAS DOBLEMENTE ENLAZADAS
from Listas.ListasEnlazadas.ListaPisos import ListaPisos
from Listas.ListasEnlazadas.ListaPatrones import ListaPatrones
from Listas.ListasEnlazadas.ListaAzulejos import ListaAzulejos

# NODOS
from Listas.Nodos.NodoPisos import NodoPiso
from Listas.Nodos.NodoPatrones import NodoPatron
from Listas.Nodos.NodoAzulejos import NodoAzulejo


def cargarArchivo(vlListaPisos):
    urlArchivo = filedialog.askopenfile(filetype=[('XML files', '*.xml')])
    if not urlArchivo:
        print("Fallo al cargar el archivo, vuelva a intentarlo!")

    xml = minidom.parse(urlArchivo)
    pisos = xml.getElementsByTagName('piso')
    
    for piso in pisos:

        # OBTENEMOS LOS PATRONES CORRESPONDIENTES AL PISO
        listaPatrones = ListaPatrones()
        patrones = piso.getElementsByTagName('patrones')[0].getElementsByTagName('patron')
        for patron in patrones:

            # OBTENEMOS EL COLOR DE CADA AZULEJO
            listaAzulejos = ListaAzulejos()
            azulejos = patron.firstChild.data.strip()
            for azulejo in azulejos:
                nuevoAzulejo = NodoAzulejo(azulejo)
                listaAzulejos.insertar(nuevoAzulejo)

            nuevoPatron = NodoPatron(patron.getAttribute("codigo"),
                                     listaAzulejos)
            listaPatrones.insertar(nuevoPatron)

        # SE INSERTAN LOS ATRIBUTOS DEL PISO
        nuevoPiso = NodoPiso(piso.getAttribute("nombre"),
                             piso.getElementsByTagName("R")[0].firstChild.data,
                             piso.getElementsByTagName("C")[0].firstChild.data,
                             piso.getElementsByTagName("F")[0].firstChild.data,
                             piso.getElementsByTagName("S")[0].firstChild.data,
                             listaPatrones)
        
        vlListaPisos.insertar(nuevoPiso)
    
    #return vlListaPisos

def main():
#     xml = minidom.parse('entrada.xml')
#     pisos = xml.getElementsByTagName('piso')
    
#     listaPisos = ListaPisos()
#     for piso in pisos:

#         # OBTENEMOS LOS PATRONES CORRESPONDIENTES AL PISO
#         listaPatrones = ListaPatrones()
#         patrones = piso.getElementsByTagName('patrones')[0].getElementsByTagName('patron')
#         for patron in patrones:

#             # OBTENEMOS EL COLOR DE CADA AZULEJO
#             listaAzulejos = ListaAzulejos()
#             azulejos = patron.firstChild.data.strip()
#             for azulejo in azulejos:
#                 nuevoAzulejo = NodoAzulejo(azulejo)
#                 listaAzulejos.insertar(nuevoAzulejo)

#             nuevoPatron = NodoPatron(patron.getAttribute("codigo"),
#                                      listaAzulejos)
#             listaPatrones.insertar(nuevoPatron)

#         # SE INSERTAN LOS ATRIBUTOS DEL PISO
#         nuevoPiso = NodoPiso(piso.getAttribute("nombre"),
#                              piso.getElementsByTagName("R")[0].firstChild.data,
#                              piso.getElementsByTagName("C")[0].firstChild.data,
#                              piso.getElementsByTagName("F")[0].firstChild.data,
#                              piso.getElementsByTagName("S")[0].firstChild.data,
#                              listaPatrones)
        
#         listaPisos.insertar(nuevoPiso)
    listaPisos = ListaPisos()
    # cargarArchivo("entrada.xml", listaPisos)
    root = tk.Tk()

    boton_carga = tk.Button(root, text="Cargar Archivo", command = cargarArchivo(listaPisos))
    boton_carga.pack()

    root.mainloop()

    listaPisos.imprimir()
    listaPisos.ordenarPisos()
    print("------------ ORDENANDO POR NOMBRE ---------------------")
    listaPisos.imprimir()
    listaPisos.graficarPisos("PRUEBA")

if __name__ == "__main__":
    main()