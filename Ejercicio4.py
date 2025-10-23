import tkinter as tk

def actualizar_aficiones():
    seleccionadas = []
    if leer_var.get():
        seleccionadas.append("Leer")
    if deporte_var.get():
        seleccionadas.append("Deporte")
    if musica_var.get():
        seleccionadas.append("Música")
    etiqueta.config(text="Aficiones: " + ", ".join(seleccionadas))

root = tk.Tk()
root.geometry("300x300")
root.title("Ejercicio 4: Checkbutton")

leer_var = tk.IntVar()
deporte_var = tk.IntVar()
musica_var = tk.IntVar()

tk.Checkbutton(root, text="Leer", variable=leer_var, command=actualizar_aficiones).pack(anchor="w")
tk.Checkbutton(root, text="Deporte", variable=deporte_var, command=actualizar_aficiones).pack(anchor="w")
tk.Checkbutton(root, text="Música", variable=musica_var, command=actualizar_aficiones).pack(anchor="w")

etiqueta = tk.Label(root, text="Aficiones:")
etiqueta.pack(pady=10)

root.mainloop()
