import tkinter as tk
from  Conections.Articulos import hacer_clic_articulos

ventana = tk.Tk()
ventana.state('zoomed')
ventana.title('Warehouse System')

def actualizar_altura_label(event):
    altura_ventana = event.height
    label.config(height=altura_ventana)

label = tk.Label(ventana, bg="#1F1C54", width=10)
label.pack(side=tk.LEFT)

def mostrar_mensaje_articulos():
    
    Label_central = tk.Label(ventana, text="¡Mensaje de Articulos!", bg="#73708E")
    Label_central.pack(fill=tk.BOTH, expand=True)

ventana.bind("<Configure>", actualizar_altura_label)

def cerrar_ventana():
    ventana.destroy()

ancho_boton = 150
alto_boton = 5

boton_articulos = tk.Button(label, text="Articulos", width=ancho_boton, height=alto_boton, command=hacer_clic_articulos)
boton_articulos.pack(fill=tk.BOTH)

boton_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana)
boton_salir.pack(side=tk.RIGHT)

ventana.mainloop()