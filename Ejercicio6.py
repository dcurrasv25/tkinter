import tkinter as tk

def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion[0])
        etiqueta.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta.config(text="No se ha seleccionado ninguna fruta")

root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio 6: Listbox")

lista = tk.Listbox(root)
frutas = ["Manzana", "Banana", "Naranja"]
for fruta in frutas:
    lista.insert(tk.END, fruta)
lista.pack(pady=10)

boton = tk.Button(root, text="Mostrar fruta", command=mostrar_fruta)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)

root.mainloop()
