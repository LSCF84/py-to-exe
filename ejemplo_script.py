# ejemplo_script.py

import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    """Función que muestra un mensaje simple."""
    messagebox.showinfo("¡Éxito!", "El ejecutable de Python ha sido creado y ejecutado correctamente.")

# Configuración básica de la ventana
root = tk.Tk()
root.title("Demo PyInstaller")

# Botón para activar la función
boton = tk.Button(root, text="Ejecutar Prueba EXE", command=mostrar_mensaje)
boton.pack(padx=50, pady=50)

# El ejecutable no mostrará la consola gracias a este script y el comando PyInstaller
root.mainloop()
