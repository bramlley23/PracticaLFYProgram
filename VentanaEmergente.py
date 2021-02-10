from tkinter import *
from tkinter import filedialog

lista=[]
raiz=Tk()
def ventanaEmergente():
    archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")


    print(archivo)

    with open(archivo)as f_obj:
        lineas = f_obj.readlines()

    for line in lineas:

        print(line.rstrip())
    print("Sigo vivo")


Button(raiz, text="Abrir Archivo",command=ventanaEmergente).pack()
raiz.mainloop()
