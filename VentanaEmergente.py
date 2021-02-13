from tkinter import *
from tkinter import filedialog

lista=[]
raiz=Tk()
archivo=''
def ventanaEmergente():
    archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")

    with open(archivo)as f_obj:
        lineas = f_obj.readlines()

    for line in lineas:

        print(line.rstrip())


Button(raiz, text="Abrir Archivo",command=ventanaEmergente).pack()
raiz.mainloop()
