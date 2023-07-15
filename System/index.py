import tkinter as tk
from Conections.Articulos import hacer_clic_articulos

# Crear la ventana principal
ventana = tk.Tk()
ventana.state('zoomed')  # Maximizar la ventana
ventana.title('Warehouse System')  # Establecer el título de la ventana

# Función para actualizar la altura del label al cambiar el tamaño de la ventana
def actualizar_altura_label(event):
    altura_ventana = event.height
    label.config(height=altura_ventana)

# Crear un label en la ventana
label = tk.Label(ventana, bg="#1F1C54", width=10)
label.pack(side=tk.LEFT)

# Función para mostrar un mensaje relacionado con "Articulos"
def mostrar_mensaje_articulos():
    Label_central = tk.Label(ventana, text="¡Mensaje de Articulos!", bg="#73708E")
    Label_central.pack(fill=tk.BOTH, expand=True)

# Vincular la función de actualización de altura al evento de cambio de tamaño de ventana
ventana.bind("<Configure>", actualizar_altura_label)

# Crear un botón "Articulos" dentro del label
ancho_boton = 150
alto_boton = 5
boton_articulos = tk.Button(label, text="Articulos", width=ancho_boton, height=alto_boton, command=hacer_clic_articulos)
boton_articulos.bind(False)
boton_articulos.pack(fill=tk.BOTH)

# Boton cerrar ventana
def cerrar_ventana():
    ventana.destroy()
    
# Crear un botón "Salir" fuera del label
boton_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana)
boton_salir.pack(side=tk.RIGHT)

# Iniciar el bucle principal del programa
ventana.mainloop()
