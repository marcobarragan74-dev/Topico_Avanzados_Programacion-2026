import customtkinter as ct

ventana = ct.CTk()
ventana.geometry("300x400")
ventana.title("Mi Calculadora")

#Variable para guardar los numeros
operacion = ""
texto_pantalla = ct.StringVar()

#Funcion de botones
def presionar_tecla(tecla):
    global operacion
    operacion = operacion + str(tecla)
    texto_pantalla.set(operacion) #Refresh de pagina

def calcular():
    global operacion
    resultado = str(eval(operacion)) 
    texto_pantalla.set(resultado)
    operacion = resultado # Guarda el resultado para seguir usandolo (si se quiere)

def borrar_todo():
    global operacion
    operacion = ""
    texto_pantalla.set("")

#interfaz de la calculadora
pantalla = ct.CTkEntry(ventana, textvariable=texto_pantalla, font=("Arial", 24), justify="right")
# Espacio de 4 botones en interfaz
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

# Creacion de botones 

# F1
boton_7 = ct.CTkButton(ventana, text="7", width=50, command=lambda: presionar_tecla(7))
boton_7.grid(row=1, column=0, padx=5, pady=5)

boton_8 = ct.CTkButton(ventana, text="8", width=50, command=lambda: presionar_tecla(8))
boton_8.grid(row=1, column=1, padx=5, pady=5)

boton_9 = ct.CTkButton(ventana, text="9", width=50, command=lambda: presionar_tecla(9))
boton_9.grid(row=1, column=2, padx=5, pady=5)

boton_div = ct.CTkButton(ventana, text="/", width=50, fg_color="gray", command=lambda: presionar_tecla("/"))
boton_div.grid(row=1, column=3, padx=5, pady=5)

# F2
boton_4 = ct.CTkButton(ventana, text="4", width=50, command=lambda: presionar_tecla(4))
boton_4.grid(row=2, column=0, padx=5, pady=5)

boton_5 = ct.CTkButton(ventana, text="5", width=50, command=lambda: presionar_tecla(5))
boton_5.grid(row=2, column=1, padx=5, pady=5)

boton_6 = ct.CTkButton(ventana, text="6", width=50, command=lambda: presionar_tecla(6))
boton_6.grid(row=2, column=2, padx=5, pady=5)

boton_mult = ct.CTkButton(ventana, text="*", width=50, fg_color="gray", command=lambda: presionar_tecla("*"))
boton_mult.grid(row=2, column=3, padx=5, pady=5)

# F3
boton_1 = ct.CTkButton(ventana, text="1", width=50, command=lambda: presionar_tecla(1))
boton_1.grid(row=3, column=0, padx=5, pady=5)

boton_2 = ct.CTkButton(ventana, text="2", width=50, command=lambda: presionar_tecla(2))
boton_2.grid(row=3, column=1, padx=5, pady=5)

boton_3 = ct.CTkButton(ventana, text="3", width=50, command=lambda: presionar_tecla(3))
boton_3.grid(row=3, column=2, padx=5, pady=5)

boton_resta = ct.CTkButton(ventana, text="-", width=50, fg_color="gray", command=lambda: presionar_tecla("-"))
boton_resta.grid(row=3, column=3, padx=5, pady=5)

# F4
boton_borrar = ct.CTkButton(ventana, text="C", width=50, fg_color="red", command=borrar_todo)
boton_borrar.grid(row=4, column=0, padx=5, pady=5)

boton_0 = ct.CTkButton(ventana, text="0", width=50, command=lambda: presionar_tecla(0))
boton_0.grid(row=4, column=1, padx=5, pady=5)

boton_igual = ct.CTkButton(ventana, text="=", width=50, fg_color="green", command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

boton_suma = ct.CTkButton(ventana, text="+", width=50, fg_color="gray", command=lambda: presionar_tecla("+"))
boton_suma.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()