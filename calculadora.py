import tkinter as tk

# Función para actualizar la expresión en el campo de texto
def click_boton(valor):
    if estado_calculadora.get():  # Solo funciona si la calculadora está encendida
        current = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, current + valor)

# Función para evaluar la expresión y mostrar el resultado
def calcular():
    if estado_calculadora.get():  # Solo funciona si la calculadora está encendida
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Error")

# Función para limpiar el campo de texto
def limpiar():
    if estado_calculadora.get():  # Solo funciona si la calculadora está encendida
        entrada.delete(0, tk.END)

# Función para encender o apagar la calculadora
def encender_apagar():
    if estado_calculadora.get():  # Si está encendida, la apagamos
        estado_calculadora.set(False)
        entrada.config(state=tk.DISABLED)
        boton_encender_apagar.config(text="Encender")
    else:  # Si está apagada, la encendemos
        estado_calculadora.set(True)
        entrada.config(state=tk.NORMAL)
        boton_encender_apagar.config(text="Apagar")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x450")

# Variable para controlar el estado de la calculadora (encendida/apagada)
estado_calculadora = tk.BooleanVar(value=True)

# Crear un campo de texto para mostrar la expresión y el resultado
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right", state=tk.NORMAL)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Definir los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Crear y colocar los botones en la ventana
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, font=("Arial", 18), command=calcular).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    else:
        tk.Button(ventana, text=boton, font=("Arial", 18), command=lambda valor=boton: click_boton(valor)).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón para limpiar
tk.Button(ventana, text="C", font=("Arial", 18), command=limpiar).grid(row=fila, column=columna, padx=5, pady=5, ipadx=20, ipady=20)

# Botón para encender/apagar
boton_encender_apagar = tk.Button(ventana, text="Apagar", font=("Arial", 18), command=encender_apagar)
boton_encender_apagar.grid(row=fila + 1, column=0, columnspan=4, padx=5, pady=5, ipadx=20, ipady=20)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
