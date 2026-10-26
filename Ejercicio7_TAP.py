import customtkinter as ctk
import tkinter as tk

#Ventana
app = ctk.CTk()
app.title("Dibujo en Canvas - Casa")
app.geometry("500x500")
app.resizable(False, False)

#Creación del Canvas
lienzo = tk.Canvas(app, width=400, height=400, bg="#87CEEB", highlightthickness=0)
lienzo.pack(pady=40)

#Pasto
lienzo.create_rectangle(0, 300, 400, 400, fill="#32CD32", outline="")

#Base de la casa
lienzo.create_rectangle(120, 180, 280, 320, fill="#F5F5DC", outline="black", width=2)

#Techo
lienzo.create_polygon(100, 180, 200, 90, 300, 180, fill="#B22222", outline="black", width=2)

#Puerta
lienzo.create_rectangle(170, 250, 230, 320, fill="#8B4513", outline="black", width=2)

#Perilla de la puert
lienzo.create_oval(215, 280, 225, 290, fill="gold", outline="black")

#Ventana Izquierda
lienzo.create_rectangle(135, 200, 175, 240, fill="#E0FFFF", outline="black", width=2)
# Marcos de la ventana
lienzo.create_line(155, 200, 155, 240, fill="black", width=2)
lienzo.create_line(135, 220, 175, 220, fill="black", width=2)

#Ventana Derecha
lienzo.create_rectangle(225, 200, 265, 240, fill="#E0FFFF", outline="black", width=2)
lienzo.create_line(245, 200, 245, 240, fill="black", width=2)
lienzo.create_line(225, 220, 265, 220, fill="black", width=2)

#Sol
lienzo.create_oval(310, 30, 370, 90, fill="#FFD700", outline="")

app.mainloop()