# LIBRERIAS PYTHON
from xml.dom import minidom
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

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

def abrir_Programa(listaPisos, piso, patron, imprimir):
    if piso == "" or patron == "":
        messagebox.showerror("Error", "Falta llenar un campo")
        return
    
    if not listaPisos.buscarPiso(piso):
        messagebox.showerror("Error", "No se encontró el piso")
        return
    
    if not listaPisos.buscarPatron(piso, patron):
        messagebox.showerror("Error", "No se encontró el patrón")
        return
    
    pisosTmp = listaPisos
    pisosTmp.graficarPisos(piso, patron)
    pisosTmp.instruccionCambio(piso, patron)

    seleccionPiso.destroy()


        
def abrir_seleccionPiso(listaPisos):

    if listaPisos.cabeza is None:
        messagebox.showerror("Error", "Primero se debe de cargar un archivo")
        return

    seleccionPiso = tk.Tk()
    seleccionPiso.title("SELECCION PISO Y PATRON")
    seleccionPiso.geometry("500x200")

    # Cuadros de texto para ingresar piso y patrón
    lblPiso = tk.Label(seleccionPiso, text="Ingresa el piso:")
    lblPiso.pack()

    txtbPiso = tk.Entry(seleccionPiso)
    txtbPiso.pack()

    lblPatron = tk.Label(seleccionPiso, text="Ingresa el patrón:")
    lblPatron.pack()

    txtbPatron = tk.Entry(seleccionPiso)
    txtbPatron.pack()

    opciones = ["Consola", "Txt"]

    opcion_var = tk.StringVar()

    combo = ttk.Combobox(seleccionPiso, textvariable=opcion_var, values=opciones)
    combo.pack(pady=10)


    # Botón para confirmar selección
    btnConfirmar = tk.Button(seleccionPiso, text="Confirmar", command=lambda: abrir_Programa(listaPisos, txtbPiso.get(), txtbPatron.get(), combo.get()))
    btnConfirmar.pack()


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
    root.geometry("500x400")
    root.title("PANTALLA PRINCIPAL")

    btnCargaArchivo = tk.Button(root, text="Cargar Archivo", width=40, height=5, command = lambda: cargarArchivo(listaPisos))
    btnCargaArchivo.pack(pady=10)

    btnSeleccionPatron = tk.Button(root, text="Seleccionar Piso", width=40, height=5, command = lambda: abrir_seleccionPiso(listaPisos))
    btnSeleccionPatron.pack(pady=15)

    root.mainloop()

    listaPisos.imprimir()
    listaPisos.ordenarPisos()
    print("------------ ORDENANDO POR NOMBRE ---------------------")
    # listaPisos.imprimir()
    # listaPisos.graficarPisos("PRUEBA")

if __name__ == "__main__":
    main()