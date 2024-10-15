import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import math

# Crear la ventana con un tema
root = ThemedTk(theme="black")
root.title("Aplicación Completa")
root.geometry("1000x800")

# Variable para almacenar el resultado de la raíz cuadrada
resultado_raiz = tk.StringVar()

# Función para calcular la raíz cuadrada
def calcular_raiz():
    try:
        numero = float(entry_raiz.get())
        raiz_resultado = math.sqrt(numero)
        resultado_raiz.set(f"Su raíz es: {raiz_resultado:.2f}")
    except ValueError:
        resultado_raiz.set("Por favor, ingrese un número válido.")

# Crear un cuaderno (notebook)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Pestaña 1: Raíz Cuadrada
frame_raiz = ttk.Frame(notebook)
notebook.add(frame_raiz, text="Raíz Cuadrada")

# Campo de entrada para ingresar el número
entry_raiz = ttk.Entry(frame_raiz)
entry_raiz.pack(padx=10, pady=10)

# Botón para calcular la raíz cuadrada
ttk.Button(frame_raiz, text="Calcular", command=calcular_raiz).pack(padx=10, pady=10)

# Etiqueta para mostrar el resultado de la raíz cuadrada
ttk.Label(frame_raiz, textvariable=resultado_raiz).pack(padx=10, pady=10)

# Pestaña 2: Calculadora de Áreas
frame_area = ttk.Frame(notebook)
notebook.add(frame_area, text="Calculadora de Áreas")

# Funciones para calcular el área según la figura seleccionada
def mostrar_campos_figura(event):
    figura = combo.get()
    limpiar_campos()

    if figura == "Cuadrado":
        label_1.config(text="Lado:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Rectángulo":
        label_1.config(text="Base:")
        label_2.config(text="Altura:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Triángulo":
        label_1.config(text="Base:")
        label_2.config(text="Altura:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Círculo":
        label_1.config(text="Radio:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        boton_area.pack(pady=10)

    elif figura == "Polígono Regular":
        label_1.config(text="Perímetro:")
        label_2.config(text="Apotema:")
        label_1.pack(pady=5)
        entry_1.pack(pady=5)
        label_2.pack(pady=5)
        entry_2.pack(pady=5)
        boton_area.pack(pady=10)

def calcular_area():
    figura = combo.get()
    try:
        if figura == "Cuadrado":
            lado = float(entry_1.get())
            area = lado ** 2
        elif figura == "Rectángulo":
            base = float(entry_1.get())
            altura = float(entry_2.get())
            area = base * altura
        elif figura == "Triángulo":
            base = float(entry_1.get())
            altura = float(entry_2.get())
            area = 0.5 * base * altura
        elif figura == "Círculo":
            radio = float(entry_1.get())
            area = math.pi * (radio ** 2)
        elif figura == "Polígono Regular":
            perimetro = float(entry_1.get())
            apotema = float(entry_2.get())
            area = (perimetro * apotema) / 2
        resultado_area.config(text=f"Área: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

def limpiar_campos():
    label_1.pack_forget()
    label_2.pack_forget()
    entry_1.pack_forget()
    entry_2.pack_forget()
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    boton_area.pack_forget()
    resultado_area.config(text="Área:")

# Pestaña 2: Configuración de la calculadora de áreas
label_figura = ttk.Label(frame_area, text="Seleccione la figura:")
label_figura.pack(pady=5)

combo = ttk.Combobox(frame_area, values=["Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Polígono Regular"], state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", mostrar_campos_figura)

label_1 = ttk.Label(frame_area)
label_2 = ttk.Label(frame_area)
entry_1 = ttk.Entry(frame_area)
entry_2 = ttk.Entry(frame_area)

boton_area = ttk.Button(frame_area, text="Calcular Área", command=calcular_area)
resultado_area = ttk.Label(frame_area, text="Área:")
resultado_area.pack(pady=5)

# Pestaña 3: Calculadora Básica
frame_calculadora = ttk.Frame(notebook)
notebook.add(frame_calculadora, text='Calculadora Básica')

# Funciones de la calculadora básica
expresion = ""
input_text = tk.StringVar()

def click_boton(item):
    global expresion
    expresion += str(item)
    input_text.set(expresion)

def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        input_text.set(resultado)
        expresion = resultado
    except Exception as e:
        input_text.set("Error")
        expresion = ""

def limpiar():
    global expresion
    expresion = ""
    input_text.set("")

pantalla = tk.Entry(frame_calculadora, textvariable=input_text, font=('arial', 18, 'bold'), bd=20, insertwidth=4, width=14, borderwidth=4, justify="right")
pantalla.grid(row=0, column=0, columnspan=4)

botones = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', 'C', '0', '=', '+']

fila = 1
columna = 0

for boton in botones:
    if boton == '=':
        tk.Button(frame_calculadora, text=boton, width=10, height=3, command=calcular).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(frame_calculadora, text=boton, width=10, height=3, command=limpiar).grid(row=fila, column=columna)
    else:
        tk.Button(frame_calculadora, text=boton, width=10, height=3, command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Pestaña 4: Integrantes con imágenes y barra de progreso
frame_integrantes = ttk.Frame(notebook)
notebook.add(frame_integrantes, text="Integrantes e Imágenes")

# Cargar imágenes
imagen = PhotoImage(file=r"C:\perifericos\INTEGRANTES\INTEGRANTES\rap.png")
imagen1 = PhotoImage(file=r"C:\perifericos\INTEGRANTES\INTEGRANTES\goku.png")
imagen2 = PhotoImage(file=r"C:\perifericos\INTEGRANTES\INTEGRANTES\gato.png")
imagen3 = PhotoImage(file=r"C:\perifericos\INTEGRANTES\INTEGRANTES\jk.png")

# Títulos
tk.Label(frame_integrantes, text='NOMBRES').grid(column=1, row=0)
tk.Label(frame_integrantes, text='MATRÍCULAS').grid(column=2, row=0)
tk.Label(frame_integrantes, text='NÚMERO DE LISTA').grid(column=3, row=0)
tk.Label(frame_integrantes, text='IMÁGENES').grid(column=4, row=0)

# Integrantes
tk.Label(frame_integrantes, text='IAN MISAEL MOYOTL MOYOTL').grid(column=1, row=1)
tk.Label(frame_integrantes, text='JUAN JOSE BAUTISTA ESPINOSA').grid(column=1, row=2)
tk.Label(frame_integrantes, text='CARLOS CASTRO CERECEDO').grid(column=1, row=3)
tk.Label(frame_integrantes, text='PAOLA LEZAMA SALAS').grid(column=1, row=4)

# Matrículas
tk.Label(frame_integrantes, text='231403044').grid(column=2, row=1)
tk.Label(frame_integrantes, text='231403169').grid(column=2, row=2)
tk.Label(frame_integrantes, text='231403001').grid(column=2, row=3)
tk.Label(frame_integrantes, text='231403009').grid(column=2, row=4)

# Números de lista
tk.Label(frame_integrantes, text='13').grid(column=3, row=1)
tk.Label(frame_integrantes, text='1').grid(column=3, row=2)
tk.Label(frame_integrantes, text='3').grid(column=3, row=3)
tk.Label(frame_integrantes, text='9').grid(column=3, row=4)

# Imágenes
tk.Label(frame_integrantes, image=imagen).grid(column=4, row=1)
tk.Label(frame_integrantes, image=imagen1).grid(column=4, row=2)
tk.Label(frame_integrantes, image=imagen2).grid(column=4, row=3)
tk.Label(frame_integrantes, image=imagen3).grid(column=4, row=4)

# Barra de progreso
progress = ttk.Progressbar(frame_integrantes, orient="horizontal", length=400, mode="determinate")
progress.grid(column=1, row=5, columnspan=4, pady=20)

# Botón para iniciar la barra de progreso
def update_progress():
    progress["value"] = 0
    step_progress()

def step_progress():
    if progress["value"] < 100:
        progress["value"] += 10
        root.after(900, step_progress)
    else:
        root.destroy()

start_button = tk.Button(frame_integrantes, text="Iniciar", command=update_progress)
start_button.grid(column=1, row=6, columnspan=4)

# Ejecutar la aplicación
root.mainloop()
