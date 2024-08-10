"""Página de inicio interactiva:
Componentes: Menú desplegable, Reloj simple.
Descripción: Una página de inicio con un menú desplegable para
navegar entre diferentes secciones de la página y un reloj
simple que muestra la hora actual en la esquina superior derecha."""


import tkinter as tk
from tkinter import Menu
import time

# Función para actualizar el reloj
def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_reloj)
    
# Otras funciones
def mostrar_seccion1():
    etiqueta_principal.config(text="Ingresaste a la sección 1")

def mostrar_seccion2():
    etiqueta_principal.config(text="Ingresaste a la sección 2")
    
def mostrar_seccion3():
    etiqueta_principal.config(text="Ingresaste a la sección 3")

def salir():
    root.quit()
    
# ventana principal
root = tk.Tk()
root.title("Página de Inicio Interactiva del Grupo 9")
root.geometry("800x500")
root.configure(bg="lightgreen")  # Color verde claro para la ventana principal

# armado del menú desplegable
menu_bar = Menu(root, bg="lightgreen", fg="violet")
root.config(menu=menu_bar)

menu_navegacion = Menu(menu_bar, tearoff=0, bg="light blue", fg="blue",
                       activebackground="yellow", activeforeground="red")
menu_bar.add_cascade(label="Navegar", menu=menu_navegacion, background="lightblue")  # Fondo celeste para "Navegar"
menu_navegacion.add_command(label="Sección 1", command=mostrar_seccion1)
menu_navegacion.add_command(label="Sección 2", command=mostrar_seccion2)
menu_navegacion.add_command(label="Sección 3", command=mostrar_seccion3)
menu_navegacion.add_separator()
menu_navegacion.add_command(label="Salir", command=salir)   

# Etiqueta principal
etiqueta_principal = tk.Label(root, text="Bienvenido a la Página de Inicio del Grupo 9", font=('Arial', 25))
etiqueta_principal.pack(pady=100)



root.mainloop()



