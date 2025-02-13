"# Repositorio1"
import tkinter as tk
from tkinter import messagebox

# Función para manejar el envío del formulario
def enviar_formulario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    grado = entry_grado.get()
    correo = entry_correo.get()
    
    if nombre and edad and grado and correo:
        messagebox.showinfo("Información", f"Nombre: {nombre}\nEdad: {edad}\nGrado: {grado}\nCorreo: {correo}")
    else:
        messagebox.showwarning("Error", "Por favor, complete todos los campos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Escuela")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

label_grado = tk.Label(ventana, text="Grado:")
label_grado.grid(row=2, column=0, padx=10, pady=5)
entry_grado = tk.Entry(ventana)
entry_grado.grid(row=2, column=1, padx=10, pady=5)

label_correo = tk.Label(ventana, text="Correo Electrónico:")
label_correo.grid(row=3, column=0, padx=10, pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=3, column=1, padx=10, pady=5)

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
boton_enviar.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
