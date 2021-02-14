from tkinter import *
from tkinter import filedialog

raiz=Tk()
class ArchivoDEntrada:
    def __init__(self,nomArchivo):
        self.nomArchivo=nomArchivo

    def ordenarLista(self):
        print("<------------------------>")

                #abriendo archivo
        ordenar=[]
        buscar=[]

        archivo = open(self.nomArchivo)
        arc = archivo.readlines()
        tama = len(arc)
        contador = 1
        archivo.close()

        #PARA MOSTRAR ORDENAR LINEA[0], SEPONE ORDENAR
        #PARA MOSTRAR ORDENAR,BUSCAR LINEA[2],SE PONE BUSCAR
        for linea in arc:
          if linea[0] in 'ORDENAR':
            print(True,"numLInea=",contador)
            buscar.append(linea)
          contador += 1

        x=[i.replace('ORDENAR\n','')for i in buscar]


        y='='.join(x)


        nueva = y.split('=')

        d=','.join(nueva)
        t=d.split(',')
        print(t)
        #print(d.split(','))
        d=[]
        for h in t:
          if h.isnumeric():
            d.append(h)
        print(d)

        with open("d.txt","w")as fp:
          for line in d:
            fp.write( line+'\n')

        with open("d.txt")as a:
          j=a.read().split('\n')
        tama = len(j)-1
        print("<------------------------------>")
        arraya=[]
        for k in j:
          arraya.append(k)


        for i in range(0,tama):
          for j in range(0,tama):
            if arraya[j]>arraya[j+1]:
              aux=arraya[j]
              arraya[j]=arraya[j+1]
              arraya[j+1]= aux

        print(arraya)


        print("<------------------------>")
#<------------------- Fin del Metodo ORDENAR ---------------------------------->
#<----------------------------------------------------------------------------->
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
