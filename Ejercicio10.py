import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10: Scrollbar")

# Frame para organizar Text y Scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Widget Text con texto largo
texto = tk.Text(frame, wrap="word", width=50, height=15)
texto.pack(side="left", fill="both", expand=True)

# Scrollbar vertical
scroll = tk.Scrollbar(frame, command=texto.yview)
scroll.pack(side="right", fill="y")

# Conexión entre ambos widgets
texto.config(yscrollcommand=scroll.set)

# Texto de ejemplo
texto.insert(tk.END, """Este es un texto largo de ejemplo.
Puedes escribir varios párrafos aquí para probar la barra de desplazamiento.

Tkinter permite crear interfaces gráficas fácilmente en Python.
El widget Text es ideal para mostrar o editar grandes cantidades de texto.

Desplázate con la barra o con el mouse para explorar todo el contenido.
Sigue escribiendo aquí para llenar el espacio y comprobar el funcionamiento del Scrollbar.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Vivamus facilisis ultricies risus, ut laoreet orci varius in.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.""")

root.mainloop()
