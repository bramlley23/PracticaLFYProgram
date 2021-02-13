from tkinter import *
from tkinter import filedialog
from io import open

lista=[]
raiz=Tk()

def ventanaEmergente():
    archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")
    print(archivo)



    with open(archivo)as f_obj:
        lineas = f_obj.readlines()

    for line in lineas:
        print(line.rstrip())
