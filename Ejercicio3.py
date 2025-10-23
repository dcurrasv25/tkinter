import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"¡Hola, {nombre}!")

root = tk.Tk()
root.geometry("300x300")
root.title("Ejercicio 3: Entry")

entrada = tk.Entry(root)
entrada.pack(pady=10)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)

root.mainloop()
