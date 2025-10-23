import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 20
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue")

def limpiar(event):
    if event.char == "c":
        canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13: Eventos de teclado y ratón")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Detectar clic izquierdo
canvas.bind("<Button-1>", dibujar_circulo)
# Detectar tecla presionada
root.bind("<Key>", limpiar)

root.mainloop()
