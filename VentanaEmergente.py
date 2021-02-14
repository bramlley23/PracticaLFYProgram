from tkinter import *
from tkinter import filedialog
from io import open

lista=[]
raiz=Tk()

def ventanaEmergente():
    archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")
<<<<<<< HEAD
    print(archivo)



=======
    
>>>>>>> 89ce93191e005c41c4a63bf0a64e7e7ee96c156e
    with open(archivo)as f_obj:
        lineas = f_obj.readlines()

    for line in lineas:
        print(line.rstrip())
<<<<<<< HEAD
=======
    print("Sigo vivo")


Button(raiz, text="Abrir Archivo",command=ventanaEmergente).pack()
raiz.mainloop()
>>>>>>> 89ce93191e005c41c4a63bf0a64e7e7ee96c156e
