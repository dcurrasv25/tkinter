import tkinter as tk

def actualizar_valor(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio 11: Scale")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_valor)
scale.pack(padx=10, pady=10)

etiqueta = tk.Label(root, text="Valor seleccionado: 0")
etiqueta.pack(pady=5)

root.mainloop()
