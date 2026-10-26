import customtkinter as ct

# Estructura principal
ventana = ct.CTk()
ventana.geometry("400x400") 

# Etiqueta principal
etiqueta = ct.CTkLabel(ventana, text="Mensaje")
etiqueta.pack(pady=(40, 20))

def enviar_mensaje():
    texto_ingresado = campo_texto.get()
    print(f"Texto Ingresado: {texto_ingresado}")
    
    # Cambia el texto del labe
    if texto_ingresado.strip() != "":
        etiqueta.configure(text=texto_ingresado)

def borrar_texto():
    campo_texto.delete(0, ct.END)

def cambiar_color(event):
    if boton_enviar.cget("fg_color") == "orange":
        boton_enviar.configure(fg_color="gray")
    else:
        boton_enviar.configure(fg_color="orange")

# Diseño de la interfaz Vertical

# Botón superior
boton_borrar = ct.CTkButton(ventana, text="BORRAR", command=borrar_texto, fg_color="#ef4444")
boton_borrar.pack(pady=10)

# Caja de texto
campo_texto = ct.CTkEntry(ventana, placeholder_text="Ingresa tu mensaje.", width=200)
campo_texto.pack(pady=10)

#Botón inferior
boton_enviar = ct.CTkButton(ventana, text="ENVIAR", command=enviar_mensaje, fg_color="light green", text_color="black")
boton_enviar.pack(pady=10)

#Evento de click
boton_enviar.bind("<Double-1>", cambiar_color)

ventana.mainloop()