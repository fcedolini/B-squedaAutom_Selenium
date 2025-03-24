import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# ----------------- Ventana Buscar Personajes ------------------


# Función que inicia la app después del login exitoso
def iniciar_app():
    global ventana, entrada, etiqueta_imagen, nombre_var, estado_var, especie_var, ubicacion_var

    ventana = tk.Tk()
    ventana.title("Busca tu personaje preferido")
    ventana.geometry("400x500")
    ventana.config(bg="#2c3e50")

    # Variables de texto
    nombre_var = tk.StringVar()
    estado_var = tk.StringVar()
    especie_var = tk.StringVar()
    ubicacion_var = tk.StringVar()

    # Etiqueta de título
    tk.Label(ventana, text="Buscador de Personajes", font=(
        "Arial", 12, "bold"), bg="#2c3e50", fg="white").pack(pady=10)

    # Entrada y botón de búsqueda
    tk.Label(ventana, text="Nombre del personaje:",
             bg="#2c3e50", fg="white").pack()
    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)
    tk.Button(ventana, text="Buscar", command=buscar_personaje).pack(pady=5)

    # Etiqueta para la imagen
    etiqueta_imagen = tk.Label(ventana, bg="#2c3e50")
    etiqueta_imagen.pack(pady=10)

    # Mostrar información del personaje
    tk.Label(ventana, textvariable=nombre_var, font=(
        "Arial", 14, "bold"), bg="#2c3e50", fg="white").pack()
    tk.Label(ventana, textvariable=estado_var, bg="#2c3e50", fg="white").pack()
    tk.Label(ventana, textvariable=especie_var,
             bg="#2c3e50", fg="white").pack()
    tk.Label(ventana, textvariable=ubicacion_var,
             bg="#2c3e50", fg="white").pack()

    ventana.mainloop()


# Función para buscar personaje en la API
def buscar_personaje():
    nombre = entrada.get().strip()
    if not nombre:
        return

    url = f"https://rickandmortyapi.com/api/character/?name={nombre}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos["results"]:
            personaje = datos["results"][0]
            mostrar_datos(personaje)


# Función para mostrar los datos en la GUI
def mostrar_datos(personaje):
    nombre_var.set(personaje["name"])
    estado_var.set(f"Estado: {personaje['status']}")
    especie_var.set(f"Especie: {personaje['species']}")
    ubicacion_var.set(f"Ubicación: {personaje['location']['name']}")

    # Cargar imagen
    img_url = personaje["image"]
    img_data = requests.get(img_url).content
    img_pil = Image.open(BytesIO(img_data))
    img_pil = img_pil.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_pil)

    etiqueta_imagen.config(image=img_tk)
    etiqueta_imagen.image = img_tk
