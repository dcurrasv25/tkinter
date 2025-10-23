import tkinter as tk

def cambiar_color():
    root.config(bg=color_var.get())

root = tk.Tk()
root.title("Color Favorito")
root.geometry("300x200")

# Variable compartida por los Radiobutton
color_var = tk.StringVar(value="white")  # color inicial

# Radiobuttons
colores = ["red", "green", "blue"]
for c in colores:
    rb = tk.Radiobutton(root, text=c.capitalize(), variable=color_var,
                        value=c, command=cambiar_color)
    rb.pack(anchor='w', padx=20, pady=5)

root.mainloop()
