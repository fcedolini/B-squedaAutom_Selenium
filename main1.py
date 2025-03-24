import tkinter as tk
from tkinter import messagebox
from app_personajes1 import iniciar_app
from mercado1 import buscar_mercado

# Diccionario de usuarios
USUARIOS = {
    "fede": "2121",  # Usuario 1 -> Va a buscar personajes de Rick y Morty
    "mario": "2323",  # Usuario 2 -> Va a buscador de Mercado Libre
}


def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario in USUARIOS and USUARIOS[usuario] == contrasena:
        messagebox.showinfo("Login exitoso", f"Bienvenido, {usuario}")
        ventana_login.destroy()  # Cierra el login

        if usuario == "fede":
            iniciar_app()  # Redirige a la app de buscar pesonajes
        elif usuario == "mario":
            buscar_mercado()  # Redirige a la app de Mercado Libre
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# Ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("300x200")
ventana_login.config(bg="#3498db")

tk.Label(ventana_login, text="Usuario:", bg="#3498db", fg="white").pack(pady=5)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack(pady=5)

tk.Label(ventana_login, text="Contraseña:",
         bg="#3498db", fg="white").pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="*")
entry_contrasena.pack(pady=5)

tk.Button(ventana_login, text="Ingresar",
          command=verificar_login).pack(pady=10)

ventana_login.mainloop()
