import tkinter as tk

def mostrar_texto():
    etiqueta_resultado.config(text=f"Texto: {entrada.get()}")

def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8: Frame")

# Frame superior
frame_superior = tk.Frame(root, padx=10, pady=10)
frame_superior.pack()

tk.Label(frame_superior, text="Etiqueta 1:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_superior, text="Etiqueta 2:").grid(row=1, column=0, padx=5, pady=5)

entrada = tk.Entry(frame_superior, width=25)
entrada.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

# Frame inferior
frame_inferior = tk.Frame(root, padx=10, pady=10)
frame_inferior.pack()

tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto).grid(row=0, column=0, padx=5)
tk.Button(frame_inferior, text="Borrar", command=borrar_texto).grid(row=0, column=1, padx=5)

etiqueta_resultado = tk.Label(frame_inferior, text="")
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
