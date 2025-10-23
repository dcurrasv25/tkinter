import tkinter as tk

def dibujar():
    canvas.delete("all")  # limpia el canvas antes de dibujar
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        canvas.create_oval(x1, y1, x2, y2, fill="red")
    except ValueError:
        etiqueta.config(text="Introduce valores numéricos válidos")

root = tk.Tk()
root.geometry("500x300")
root.title("Ejercicio 7: Canvas")

tk.Label(root, text="x1:").pack()
entry_x1 = tk.Entry(root)
entry_x1.pack()

tk.Label(root, text="y1:").pack()
entry_y1 = tk.Entry(root)
entry_y1.pack()

tk.Label(root, text="x2:").pack()
entry_x2 = tk.Entry(root)
entry_x2.pack()

tk.Label(root, text="y2:").pack()
entry_y2 = tk.Entry(root)
entry_y2.pack()

boton = tk.Button(root, text="Dibujar", command=dibujar)
boton.pack(pady=5)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10)

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()
