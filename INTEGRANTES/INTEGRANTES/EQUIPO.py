import tkinter as tk
from tkinter import PhotoImage

# Crear ventana principal
root = tk.Tk()
root.title("Inserción de imagen en Tkinter")
root.geometry("1000x1500")
# direcciones de imagenes
imagen = PhotoImage(file=r"C:\Users\ian\Desktop\python\INTEGRANTES\rap.png")
imagen1 = PhotoImage(file=r"C:\Users\ian\Desktop\python\INTEGRANTES\goku.png")
imagen2 = PhotoImage(file=r"C:\Users\ian\Desktop\python\INTEGRANTES\gato.png")
imagen3 = PhotoImage(file=r"C:\Users\ian\Desktop\python\INTEGRANTES\jk.png")
# TITULOS
NOMBRES = tk.Label(root, text='NOMBRES').grid(column=1, row=0)
MATRICULAS = tk.Label(root, text='MATRICULAS').grid(column=2, row=0)
NUMERODELISTA = tk.Label(root, text='NUMERO DE LISTA ').grid(column=3, row=0)
IMAGENESDEINTEGRANTES = tk.Label(root, text='IMAGENES ').grid(column=4, row=0)
# integrantes
ian = tk.Label(root, text='IAN MISAEL MOYOTL MOYOTL ').grid(column=1, row=1)
JUAN = tk.Label(root, text='JUAN JOSE BAUTISTA ESPINOSA ').grid(
    column=1, row=2)
CARLOS = tk.Label(root, text='CARLOS CASTRO CERECEDO  ').grid(column=1, row=3)
PAO = tk.Label(root, text='PAOLA LESAMA SALAS').grid(column=1, row=4)
# MATRICULAS
Mian = tk.Label(root, text='231403044').grid(column=2, row=1)
MJUAN = tk.Label(root, text='231403169').grid(column=2, row=2)
MCARLOS = tk.Label(root, text=' 231403001').grid(column=2, row=3)
MPAO = tk.Label(root, text='231403009').grid(column=2, row=4)
# NUMEROS DE LISTA
Nian = tk.Label(root, text='13').grid(column=3, row=1)
NJUAN = tk.Label(root, text='1').grid(column=3, row=2)
NCARLOS = tk.Label(root, text='3 ').grid(column=3, row=3)
NPAO = tk.Label(root, text='9').grid(column=3, row=4)
# IMAGENES
label_imagen = tk.Label(root, image=imagen).grid(column=4, row=1)
label_imagen1 = tk.Label(root, image=imagen1).grid(column=4, row=2)
label_imagen2 = tk.Label(root, image=imagen2).grid(column=4, row=3)
label_imagen3 = tk.Label(root, image=imagen3).grid(column=4, row=4)
# Ejecutar la aplicación
root.mainloop()
