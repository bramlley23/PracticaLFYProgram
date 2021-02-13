from tkinter import *
from tkinter import filedialog

raiz=Tk()
class ArchivoDEntrada:
    def __init__(self,nomArchivo):
        self.nomArchivo=nomArchivo

    def ordenarLista(self):
        print("<------------------------>")
        archi = open(self.nomArchivo)
        lineas = archi.readlines()
        archi.close()
        contador = 1
        ordenar=[]

        for linea in lineas:
            if linea[0] in 'ORDENAR':
                print(True,"numLInea=",contador)
                ordenar.append(linea)
            contador += 1
        print(ordenar)
        print("<------------------------>")

    def buscarEnLista(self):
        arc = open(self.nomArchivo)
        linea = arc.readlines()
        arc.close()
        print(linea)

    def ordenarBuscar(self):
        print("<-----------ORDENAR,BUSCAR-------------->")
        f = open(self.nomArchivo)
        fila=f.readlines()
        f.close()
        contador = 1
        buscar=[]
        for recta in fila:
            if recta[2] in 'BUSCAR':
                print(True,"numLInea=",contador)
                buscar.append(recta)
            contador += 1
        print(buscar)

        print("<--------------------------------------->")

    def mostrarListas(self):
        pass


    def mostrarHTML(self):
        pass

archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")
abrir = ArchivoDEntrada(archivo)
abrir.ordenarLista()
#abrir.buscarEnLista()
#abrir.ordenarBuscar()
