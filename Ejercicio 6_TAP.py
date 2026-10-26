import customtkinter as ctk

# Modo dark
ctk.set_appearance_mode("dark") 

app = ctk.CTk()
app.title("Login Panel")
app.geometry("600x420")
app.resizable(False, False)

# Funciones de Lógica
def imprimir_datos():
    usuario = username_entry.get()
    contrasena = password_entry.get()
    print(f"Usuario: {usuario}")
    print(f"Contraseña: {contrasena}")

def mostrar_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        eye_button.configure(text="👁")
    else:
        password_entry.configure(show="*")
        eye_button.configure(text="◉")

# DISEÑO (Se reajustó la altura a 310 para reequilibrar el espacio vertical)
main_frame = ctk.CTkFrame(app, width=400, height=310, corner_radius=20, fg_color="#1E1E24")
main_frame.place(relx=0.5, rely=0.5, anchor="center") 

# Textos
title_label = ctk.CTkLabel(main_frame, text="Bienvenido", font=("Helvetica", 28, "bold"), text_color="#00D2FF")
title_label.place(relx=0.5, y=45, anchor="center")

subtitle_label = ctk.CTkLabel(main_frame, text="Por favor ingresa tus datos", font=("Helvetica", 12), text_color="gray")
subtitle_label.place(relx=0.5, y=75, anchor="center")

username_entry = ctk.CTkEntry(main_frame, width=280, height=45, placeholder_text="👤 Username", 
                              corner_radius=10, border_color="#3A3A42", fg_color="#2B2B31", text_color="white")
username_entry.place(relx=0.5, y=130, anchor="center")

password_entry = ctk.CTkEntry(main_frame, width=280, height=45, placeholder_text="🔒 Password", 
                              corner_radius=10, border_color="#3A3A42", fg_color="#2B2B31", text_color="white", show="*")
password_entry.place(relx=0.5, y=190, anchor="center")

eye_button = ctk.CTkButton(main_frame, text="◉", width=30, height=30, fg_color="transparent", 
                           hover_color="#3A3A42", text_color="gray", command=mostrar_password)
eye_button.place(x=315, y=190, anchor="center")

# BOTÓN PRINCIPAL
login_button = ctk.CTkButton(main_frame, text="LOGIN", width=280, height=45, corner_radius=10, 
                             font=("Helvetica", 14, "bold"), fg_color="#00D2FF", text_color="black", 
                             hover_color="#009BCC", command=imprimir_datos)
login_button.place(relx=0.5, y=250, anchor="center")

app.mainloop()