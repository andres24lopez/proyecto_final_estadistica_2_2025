import tkinter as tk

# Crear ventana principal
raiz = tk.Tk()
raiz.title("Programa de Andrés")
raiz.geometry("800x600")
raiz.resizable(False, False)

# Crear frames
haedf = tk.Frame(raiz, bg="blue", width=800, height=50, bd=5)
bodyf = tk.Frame(raiz, bg="yellow", width=800, height=500, bd=25)
footf = tk.Frame(raiz, bg="white", width=800, height=50)

# Posicionar los frames
haedf.pack(fill='x')
bodyf.pack(fill='both', expand=True)
footf.pack(fill='x')

# Título en header
titulo = tk.Label(
    haedf,
    text="Bienvenidos a mi primera aplicación",
    bg="blue",
    fg="white",
    font=("Arial", 20, "bold")
)
titulo.place(x=100, y=5)

# Crear un sub-frame para el formulario
form_frame = tk.Frame(bodyf, bg="yellow")
form_frame.place(relx=0.10, rely=0.05)

# Etiquetas y campos de entrada
campos = [
    ("Primer nombre", 1, 1),
    ("Segundo nombre", 2, 1),
    ("Primer apellido", 3, 1),
    ("Segundo apellido", 4, 1),
    ("Dirección", 5, 1),
    ("Teléfono", 1, 3),
    ("Edad", 2, 3),
    ("Sexo", 3, 3),
]

entradas = {}

for texto, fila, columna in campos:
    tk.Label(form_frame, text=texto).grid(row=fila, column=columna, padx=10, pady=5, sticky='w')
    entrada = tk.Entry(form_frame)
    entrada.grid(row=fila, column=columna + 1, padx=10, pady=5)
    entradas[texto] = entrada  # Guardamos por si se quieren usar luego

# Ejecutar la ventana
raiz.mainloop()



