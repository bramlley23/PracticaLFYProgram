from tkinter import *
from tkinter import filedialog

raiz=Tk()
class ArchivoDEntrada:
    def __init__(self,nomArchivo):
        self.nomArchivo=nomArchivo

    def ordenarLista(self):

        pass


    def buscarEnLista(self):
        arc = open(self.nomArchivo)
        linea = arc.readlines()
        arc.close()
        print(linea)

    def ordenarBuscar(self):
        pass

    def mostrarListas(self):
        pass


    def mostrarHTML(self):
        pass

archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")
abrir = ArchivoDEntrada(archivo)
abrir.buscarEnLista()
