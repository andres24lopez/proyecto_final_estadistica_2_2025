import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math

# Variables globales para los coeficientes de regresión
m_valor = None
b_valor = None

# --- Función para calcular Pearson ---
def calcular_pearson():
    ocultar_prediccion()
    try:
        x = [float(x_vars[i].get()) for i in range(5)]
        y = [float(y_vars[i].get()) for i in range(5)]

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
            resultado.set(f"Coef. de correlación (r): {r:.4f}")

        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color='blue', label="Datos")
        ax.set_title("Gráfico de Dispersión", fontsize=14)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)
        ax.grid(True)
        ax.legend()
        canvas.draw()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresá solo números válidos.")

# --- Función para regresión lineal ---
def calcular_regresion_lineal():
    global m_valor, b_valor
    try:
        x = [float(x_vars[i].get()) for i in range(5)]
        y = [float(y_vars[i].get()) for i in range(5)]

        n = 5
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum([x[i] * y[i] for i in range(n)])
        sum_x2 = sum([i**2 for i in x])

        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        b = (sum_y - m * sum_x) / n

        m_valor = m
        b_valor = b

        resultado.set(f"Regresión: y = {m:.2f}x + {b:.2f}")

        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(x, y, color='blue', label="Datos")
        x_line = [min(x), max(x)]
        y_line = [m * xi + b for xi in x_line]
        ax.plot(x_line, y_line, color='red', label="Línea de regresión")
        ax.set_title("Regresión Lineal", fontsize=14)
        ax.set_xlabel("X", fontsize=12)
        ax.set_ylabel("Y", fontsize=12)
        ax.grid(True)
        ax.legend()
        canvas.draw()

        mostrar_prediccion()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresá solo números válidos.")
    except ZeroDivisionError:
        resultado.set("Error: división por cero")

# --- Predecir Y para un valor dado de X ---
def predecir_y():
    global m_valor, b_valor
    try:
        x_val = float(entry_x_prediccion.get())
        y_pred = m_valor * x_val + b_valor
        resultado_prediccion.set(f"Para X = {x_val}, Y = {y_pred:.2f}")
    except ValueError:
        resultado_prediccion.set("Error: ingresá un número válido.")

# --- Mostrar sección de predicción ---
def mostrar_prediccion():
    frame_prediccion.pack(pady=10)
    entry_x_prediccion.delete(0, tk.END)
    resultado_prediccion.set("")

# --- Ocultar sección de predicción ---
def ocultar_prediccion():
    frame_prediccion.pack_forget()

# --- Ejecutar operación seleccionada ---
def ejecutar_opcion():
    if opcion_menu.get() == "Correlación":
        calcular_pearson()
    elif opcion_menu.get() == "Regresión Lineal":
        calcular_regresion_lineal()

# --- Limpiar datos ---
def limpiar():
    for var in x_vars + y_vars:
        var.set("")
    resultado.set("")
    resultado_prediccion.set("")
    fig.clear()
    canvas.draw()
    ocultar_prediccion()

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Análisis de Datos")
ventana.geometry("1000x800")
ventana.configure(bg="#246ba2")

style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox", font=("Arial", 14), padding=8)

contenedor = tk.Frame(ventana, bg="#3c78a5")
contenedor.pack(fill="both", expand=True)

# Panel izquierdo
panel_izquierdo = tk.Frame(contenedor, bg="#f0f4f7")
panel_izquierdo.pack(side="left", fill="y", padx=20, pady=20)

tk.Label(panel_izquierdo, text="Ingresá 5 valores para X y Y", font=("Arial", 16), bg="#f0f4f7").pack(pady=10)

frame_entradas = tk.Frame(panel_izquierdo, bg="#f0f4f7")
frame_entradas.pack()

x_vars = [tk.StringVar() for _ in range(5)]
y_vars = [tk.StringVar() for _ in range(5)]

for i in range(5):
    tk.Label(frame_entradas, text=f"X{i+1}:", bg="#f0f4f7", font=("Arial", 12)).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    tk.Entry(frame_entradas, textvariable=x_vars[i], width=10, font=("Arial", 12)).grid(row=i, column=1, padx=5, pady=5)
    tk.Label(frame_entradas, text=f"Y{i+1}:", bg="#f0f4f7", font=("Arial", 12)).grid(row=i, column=2, padx=5, pady=5, sticky="e")
    tk.Entry(frame_entradas, textvariable=y_vars[i], width=10, font=("Arial", 12)).grid(row=i, column=3, padx=5, pady=5)

# Menú desplegable
frame_menu = tk.Frame(panel_izquierdo, bg="#f0f4f7")
frame_menu.pack(pady=20)

tk.Label(frame_menu, text="Seleccioná operación:", bg="#f0f4f7", font=("Arial", 16, "bold")).pack(pady=5)

# Estilo personalizado para el Combobox
combo_style = ttk.Style()
combo_style.configure("TCombobox",
                      font=("Arial", 18),         # Tamaño del texto visible
                      padding=10)
combo_style.map("TCombobox",
                fieldbackground=[("readonly", "white")],
                foreground=[("readonly", "#000")])

# Variable y combobox
opcion_menu = tk.StringVar()
combo = ttk.Combobox(frame_menu,
                     textvariable=opcion_menu,
                     values=["Correlación", "Regresión Lineal"],
                     state="readonly",
                     width=25)
combo.set("Correlación")
combo.pack(pady=5)

# Botones
tk.Button(panel_izquierdo, text="Ejecutar", command=ejecutar_opcion,
          bg="#4C4EAF", fg="white", font=("Arial", 14), width=20).pack(pady=10)

tk.Button(panel_izquierdo, text="Limpiar", command=limpiar,
          bg="#d9534f", fg="white", font=("Arial", 14), width=20).pack(pady=5)

resultado = tk.StringVar()
tk.Label(panel_izquierdo, textvariable=resultado, font=("Arial", 14), bg="#f0f4f7", fg="#333").pack(pady=10)

# Sección de predicción de Y
frame_prediccion = tk.Frame(panel_izquierdo, bg="#f0f4f7")
tk.Label(frame_prediccion, text="Ingresá un valor de X:", bg="#f0f4f7", font=("Arial", 13)).pack()
entry_x_prediccion = tk.Entry(frame_prediccion, font=("Arial", 13), width=10)
entry_x_prediccion.pack(pady=5)
tk.Button(frame_prediccion, text="Predecir Y", command=predecir_y,
          bg="#0275d8", fg="white", font=("Arial", 12)).pack(pady=5)
resultado_prediccion = tk.StringVar()
tk.Label(frame_prediccion, textvariable=resultado_prediccion, font=("Arial", 13), bg="#f0f4f7", fg="#333").pack(pady=5)
ocultar_prediccion()

# Panel derecho (gráfico)
panel_derecho = tk.Frame(contenedor, bg="#ffffff")
panel_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=20)

fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=panel_derecho)
canvas.get_tk_widget().pack(fill="both", expand=True)

ventana.mainloop()


