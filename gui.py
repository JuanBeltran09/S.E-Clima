import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from main import WeatherExpert, Weather  # Importar motor de inferencia desde main.py

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto de Clima")
root.geometry("400x300")

# Inicializar el motor de inferencia
engine = WeatherExpert()

# Función para mostrar la ventana de resultado
def show_result():
    result_window = tk.Toplevel(root)
    result_window.title("Resultado del Clima")
    result_window.geometry("400x400")

    # Mostrar el clima
    clima_label = tk.Label(result_window, text=engine.result, font=("Arial", 14))
    clima_label.pack(pady=20)

    image_width = 200
    image_height = 200

    # Seleccionar la imagen correspondiente al clima
    if engine.result == "El clima es caluroso":
        img = Image.open("img/sun.jpg").resize((image_width, image_height), Image.LANCZOS)  # Imagen de sol
    elif engine.result == "El clima es frío":
        img = Image.open("img/cold.png").resize((image_width, image_height), Image.LANCZOS)  # Imagen de frío
    elif engine.result == "El clima es lluvioso":
        img = Image.open("img/rain.jpg").resize((image_width, image_height), Image.LANCZOS)  # Imagen de lluvia
    elif engine.result == "El clima es ventoso":
        img = Image.open("img/wind.jpeg").resize((image_width, image_height), Image.LANCZOS)  # Imagen de viento
    elif engine.result == "El clima es nublado":
        img = Image.open("img/cloudy.png").resize((image_width, image_height), Image.LANCZOS)  # Imagen de nublado
    elif engine.result == "El clima es huracán":
        img = Image.open("img/hurricane.jpg").resize((image_width, image_height), Image.LANCZOS)  # Imagen de huracán
    else:  # Clima extraño
        img = Image.open("img/unknown.png").resize((image_width, image_height), Image.LANCZOS)  # Imagen para clima extraño

    img = ImageTk.PhotoImage(img)

    # Mostrar la imagen en la ventana
    img_label = tk.Label(result_window, image=img)
    img_label.image = img  # Necesario para que la imagen no sea recolectada por el garbage collector
    img_label.pack()

    # Botón para regresar a la ventana principal
    def regresar():
        result_window.destroy()

    regresar_button = tk.Button(result_window, text="Regresar", command=regresar)
    regresar_button.pack(pady=10)

# Función para calcular el clima
def calcular_clima():
    try:
        temp = float(temp_entry.get())
        hum = float(hum_entry.get())
        wind = float(wind_entry.get())

        if hum > 100:
            messagebox.showerror("Error", "La humedad no puede ser mayor al 100%")
            return

        if not (wind >= 0):  # Verificar que la humedad esté en el rango de 0 a 100
            messagebox.showerror("Error", "La velocidad del viento no puede ser negativa")
            return

        # Declarar los hechos en el motor de inferencia
        engine.reset()
        engine.declare(Weather(temperature=temp, humidity=hum, wind_speed=wind))
        engine.run()

        show_result()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

# Etiquetas y entradas
temp_label = tk.Label(root, text="Temperatura (°C):")
temp_label.pack(pady=5)
temp_entry = tk.Entry(root)
temp_entry.pack(pady=5)

hum_label = tk.Label(root, text="Humedad (%):")
hum_label.pack(pady=5)
hum_entry = tk.Entry(root)
hum_entry.pack(pady=5)

wind_label = tk.Label(root, text="Velocidad del viento (km/h):")
wind_label.pack(pady=5)
wind_entry = tk.Entry(root)
wind_entry.pack(pady=5)

# Botón para calcular el clima
calcular_button = tk.Button(root, text="Calcular Clima", command=calcular_clima)
calcular_button.pack(pady=20)

# Ejecutar la ventana principal
root.mainloop()
