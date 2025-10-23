import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="Texto cambiado")

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Ejercicio 1 - Label")

etiqueta1 = tk.Label(ventana, text="¡Bienvenido!")
etiqueta1.pack()

etiqueta2 = tk.Label(ventana, text="Diego Currás Vidal")
etiqueta2.pack()

etiqueta3 = tk.Label(ventana, text="Texto original")
etiqueta3.pack()

boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack()

ventana.mainloop()
