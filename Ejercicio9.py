import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Función 'Abrir' no implementada aún.")

def salir():
    root.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Ejemplo de menú en Tkinter\nAutor: Diego Currás Vidal :)")

root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio 9: Menú")

barra_menu = tk.Menu(root)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=barra_menu)
root.mainloop()
