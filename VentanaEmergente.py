from tkinter import *
from tkinter import filedialog

lista=[]
ordenar=[]
raiz=Tk()
def ventanaEmergente():
    archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")


    print(archivo)

    with open(archivo)as f_obj:
        lineas = f_obj.readlines()

    for line in lineas:

        print(line.rstrip())

    ordenarLista(archivo)


Button(raiz, text="Abrir Archivo",command=ventanaEmergente).pack()
raiz.mainloop()

def ordenarLista(self, archivo):
    archivo = open(archivo,'r')
    arc= archivo.readlines()
    archivo.close()

    #para mostrar ordenar linea[0]
    for linea in arc:
        if linea[0] in 'ORDEN':
            ordenar.append(linea)
    print(ordenar)
