import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14: Registro de Usuarios (con clases)")
        self.usuarios = []

        # ===== Frame superior =====
        frame_form = tk.Frame(root, padx=10, pady=10)
        frame_form.pack(fill="x")

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=0, column=1, columnspan=2, pady=5, sticky="w")

        tk.Label(frame_form, text="Edad:").grid(row=1, column=0, sticky="w")
        self.scale_edad = tk.Scale(frame_form, from_=0, to=100, orient="horizontal")
        self.scale_edad.set(18)
        self.scale_edad.grid(row=1, column=1, columnspan=2, pady=5, sticky="we")

        tk.Label(frame_form, text="Género:").grid(row=2, column=0, sticky="w")
        self.genero_var = tk.StringVar(value="Otro")
        tk.Radiobutton(frame_form, text="Masculino", variable=self.genero_var, value="Masculino").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(frame_form, text="Femenino", variable=self.genero_var, value="Femenino").grid(row=2, column=2, sticky="w")
        tk.Radiobutton(frame_form, text="Otro", variable=self.genero_var, value="Otro").grid(row=2, column=3, sticky="w")

        # ===== Frame botones =====
        frame_bot = tk.Frame(root, padx=10, pady=5)
        frame_bot.pack(fill="x")

        tk.Button(frame_bot, text="Añadir", width=10, command=self.añadir_usuario).pack(side="left", padx=5)
        tk.Button(frame_bot, text="Eliminar", width=10, command=self.eliminar_usuario).pack(side="left", padx=5)
        tk.Button(frame_bot, text="Salir", width=10, command=self.salir).pack(side="right", padx=5)

        # ===== Frame lista =====
        frame_list = tk.Frame(root, padx=10, pady=10)
        frame_list.pack(fill="both", expand=True)

        self.scroll = tk.Scrollbar(frame_list)
        self.scroll.pack(side="right", fill="y")

        self.lista = tk.Listbox(frame_list, yscrollcommand=self.scroll.set)
        self.lista.pack(side="left", fill="both", expand=True)

        self.scroll.config(command=self.lista.yview)

        # ===== Menú =====
        menubar = tk.Menu(root)
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Aplicación de Registro — Ejercicio 14"))
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        root.config(menu=menubar)

    # ===== Métodos funcionales =====
    def añadir_usuario(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Introduce un nombre.")
            return
        edad = self.scale_edad.get()
        genero = self.genero_var.get()
        usuario = (nombre, edad, genero)
        self.usuarios.append(usuario)
        self.lista.insert(tk.END, f"{nombre} — {edad} años — {genero}")
        self.entry_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        sel = self.lista.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Selecciona un usuario para eliminar.")
            return
        idx = sel[0]
        self.lista.delete(idx)
        del self.usuarios[idx]

    def salir(self):
        self.root.quit()

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Función 'Guardar Lista' no implementada.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Función 'Cargar Lista' no implementada.")


# ===== Programa principal =====
root = tk.Tk()
app = RegistroApp(root)
root.mainloop()
