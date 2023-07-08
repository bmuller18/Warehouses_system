import tkinter as tk

ventana = tk.Tk()

# Obtener el ancho de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()

# Función para actualizar la altura del Label
def actualizar_altura_label(event):
    altura_ventana = event.height
    label.config(height=altura_ventana)

# Configurar el Label con el color de fondo #1F1C54
label = tk.Label(ventana, bg="#1F1C54")
label.pack(side=tk.LEFT, fill=tk.Y, expand=True)

# Asociar el evento de cambio de tamaño de la ventana a la función actualizar_altura_label
ventana.bind("<Configure>", actualizar_altura_label)

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Crear los botones en el Label
nombres_botones = ["articulos", "clientes", "compras", "ventas", "remito", "consultas", "notas", "salir"]
for nombre in nombres_botones:
    boton = tk.Button(label, text=nombre)
    boton.pack(fill=tk.BOTH, expand=True)

# Ajustar el ancho del Label al ancho de los botones
label.update_idletasks()
ancho_label = ventana.winfo_width()
label.config(width=ancho_label)

# Crear el botón de salida
boton_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana)
boton_salir.pack(side=tk.BOTTOM)

# Establecer el ancho de la ventana
ventana.geometry(f"{ancho_pantalla}x{ventana.winfo_screenheight()}")

ventana.mainloop()
