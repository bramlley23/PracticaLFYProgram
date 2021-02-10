import sys
from tkinter.filedialog import askopenfilename
from tkinter import *

nombres={}
datos={}
def ingreso():
 root=Tk()
 root.withdraw()
 root.update()
 pathString = askopenfilename(filetypes=[("Text files","*.txt")])

 ar=open(pathString,'r')
 sep1=ar.read().split("\n")
 x=0
 t1=sep1.__len__()
 while x<=t1-1:
     sep2=sep1[x].split("=")
     nombres[x]=sep2[0]
     datos[x]=sep2[1]
     x+=1
     print(nombres[0])
     print(datos[0])
     ar.close()


ingreso()
