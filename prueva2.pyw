import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math

# --- Función para calcular Pearson y graficar ---
def calcular_pearson():
    try:
        x = [float(x_vars[i].get()) for i in range(5)]
        y = [float(y_vars[i].get()) for i in range(5)]

        # Pearson
        n = 5
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum([x[i] * y[i] for i in range(n)])
        sum_x2 = sum([i**2 for i in x])
        sum_y2 = sum([i**2 for i in y])

        numerador = n * sum_xy - sum_x * sum_y
        denominador = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

        if denominador == 0:
            resultado.set("Error: división por cero")
        else:
            r = numerador / denominador
            resultado.set(f"Coef. de Pearson (r): {r:.4f}")

        # --- Crear gráfica ---
        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color='blue', label="Datos")
        ax.set_title("Gráfico de Dispersión")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.grid(True)
        ax.legend()

        canvas.draw()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresá solo números válidos.")

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Pearson con Gráfico")
ventana.geometry("800x500")
ventana.configure(bg="#f0f4f7")

# Contenedor principal dividido
contenedor = tk.Frame(ventana, bg="#f0f4f7")
contenedor.pack(fill="both", expand=True)

# Panel izquierdo (entradas y resultado)
panel_izquierdo = tk.Frame(contenedor, bg="#f0f4f7")
panel_izquierdo.pack(side="left", fill="y", padx=20, pady=20)

tk.Label(panel_izquierdo, text="Ingresá 5 valores para X y Y", font=("Arial", 14), bg="#f0f4f7").pack(pady=10)

frame_entradas = tk.Frame(panel_izquierdo, bg="#f0f4f7")
frame_entradas.pack()

x_vars = [tk.StringVar() for _ in range(5)]
y_vars = [tk.StringVar() for _ in range(5)]

for i in range(5):
    tk.Label(frame_entradas, text=f"X{i+1}:", bg="#f0f4f7").grid(row=i, column=0, padx=5, pady=5, sticky="e")
    tk.Entry(frame_entradas, textvariable=x_vars[i], width=10).grid(row=i, column=1, padx=5, pady=5)

    tk.Label(frame_entradas, text=f"Y{i+1}:", bg="#f0f4f7").grid(row=i, column=2, padx=5, pady=5, sticky="e")
    tk.Entry(frame_entradas, textvariable=y_vars[i], width=10).grid(row=i, column=3, padx=5, pady=5)

# Botón calcular
tk.Button(panel_izquierdo, text="Calcular Pearson", command=calcular_pearson, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=15)

resultado = tk.StringVar()
tk.Label(panel_izquierdo, textvariable=resultado, font=("Arial", 12), bg="#f0f4f7", fg="#333").pack(pady=5)

# Panel derecho (gráfica)
panel_derecho = tk.Frame(contenedor, bg="#ffffff")
panel_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=20)

# Crear figura matplotlib
fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=panel_derecho)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()
