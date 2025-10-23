import tkinter as tk
from tkinter import messagebox

def añadir():
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Aviso", "Introduce un nombre.")
        return
    edad = scale_edad.get()
    genero = genero_var.get()
    usuario = (nombre, edad, genero)
    usuarios.append(usuario)
    lista.insert(tk.END, f"{nombre} — {edad} años — {genero}")
    entry_nombre.delete(0, tk.END)

def eliminar():
    sel = lista.curselection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecciona un usuario para eliminar.")
        return
    idx = sel[0]
    lista.delete(idx)
    del usuarios[idx]

def salir():
    root.quit()

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Función 'Guardar Lista' no implementada.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Función 'Cargar Lista' no implementada.")

root = tk.Tk()
root.title("Registro de Usuarios")

# Frame superior: formulario
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(frame_form, width=30)
entry_nombre.grid(row=0, column=1, columnspan=2, pady=5, sticky="w")

tk.Label(frame_form, text="Edad:").grid(row=1, column=0, sticky="w")
scale_edad = tk.Scale(frame_form, from_=0, to=100, orient="horizontal")
scale_edad.set(18)
scale_edad.grid(row=1, column=1, columnspan=2, pady=5, sticky="we")

tk.Label(frame_form, text="Género:").grid(row=2, column=0, sticky="w")
genero_var = tk.StringVar(value="Otro")
tk.Radiobutton(frame_form, text="Masculino", variable=genero_var, value="Masculino").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_form, text="Femenino", variable=genero_var, value="Femenino").grid(row=2, column=2, sticky="w")
tk.Radiobutton(frame_form, text="Otro", variable=genero_var, value="Otro").grid(row=2, column=3, sticky="w")

# Frame central: botones añadir/eliminar
frame_bot = tk.Frame(root, padx=10, pady=5)
frame_bot.pack(fill="x")
tk.Button(frame_bot, text="Añadir", width=10, command=añadir).pack(side="left", padx=5)
tk.Button(frame_bot, text="Eliminar", width=10, command=eliminar).pack(side="left", padx=5)
tk.Button(frame_bot, text="Salir", width=10, command=salir).pack(side="right", padx=5)

# Frame inferior: listbox + scrollbar
frame_list = tk.Frame(root, padx=10, pady=10)
frame_list.pack(fill="both", expand=True)
scroll = tk.Scrollbar(frame_list)
scroll.pack(side="right", fill="y")
lista = tk.Listbox(frame_list, yscrollcommand=scroll.set)
lista.pack(side="left", fill="both", expand=True)
scroll.config(command=lista.yview)

# Datos
usuarios = []

# Menú
menubar = tk.Menu(root)
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(menubar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Registro de Usuarios — Ejercicio"))
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=menubar)
root.mainloop()
