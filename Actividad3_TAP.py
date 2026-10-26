import customtkinter as ctk
import tkinter as tk

#Configuración de la ventana principal
app = ctk.CTk()
app.geometry("780x520")
app.title("Inventario de Libros")
#Color de fond
app.configure(fg_color="#8ed8d0") 

font_labels = ("Arial", 14)

#Contenedor Superior
header_frame = ctk.CTkFrame(app, fg_color="#102bb8", corner_radius=0, height=90)
header_frame.pack(fill="x", side="top")
header_frame.pack_propagate(False) # Evita que el frame se encoja

#Título Header
title_label = ctk.CTkLabel(header_frame, text="Inventario de Libros", 
                           font=("Arial", 32), text_color="white")
title_label.place(relx=0.5, rely=0.5, anchor="center")

#Estrella
logo_label = ctk.CTkLabel(header_frame, text="★\nLOGO", 
                          font=("Arial", 16, "bold"), text_color="white")
logo_label.place(relx=0.92, rely=0.5, anchor="center")

#Contenedor Principal
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=40, pady=30)

#Entradas de Texto superirores
entries_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
entries_frame.pack(fill="x", pady=(0, 20))

labels_text = ["Titulo", "Autor", "ISBN"]
for i, text in enumerate(labels_text):
    ctk.CTkLabel(entries_frame, text=text, font=font_labels, text_color="black").grid(row=i, column=0, sticky="w", pady=8, padx=(0, 20))
    ctk.CTkEntry(entries_frame, width=550, fg_color="#d9d9d9", text_color="black", 
                 border_width=0, corner_radius=0).grid(row=i, column=1, sticky="w", pady=8)

#Categorias Inferiores
bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
bottom_frame.pack(fill="both", expand=True)

# Área de Conocimiento
col1 = ctk.CTkFrame(bottom_frame, fg_color="transparent")
col1.grid(row=0, column=0, sticky="nw", padx=(0, 30))

ctk.CTkLabel(col1, text="Area de conocimiento", font=font_labels, text_color="black").pack(anchor="w")

list_container = ctk.CTkFrame(col1, fg_color="transparent")
list_container.pack(anchor="w", pady=(5,0))

# Listbox
listbox = tk.Listbox(list_container, height=8, width=20, bg="#d9d9d9", 
                     font=("Arial", 12), borderwidth=0, highlightthickness=0)
listbox.pack(side="left", fill="y")
scrollbar = tk.Scrollbar(list_container, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

areas = ["Sociales", "Humanidades", "Arte", "Ingeniería", 
         "Computación", "Musica", "Idiomas", "Literatura"]
for area in areas:
    listbox.insert(tk.END, area)

#idioma y Tipo de Pasta
col2 = ctk.CTkFrame(bottom_frame, fg_color="transparent")
col2.grid(row=0, column=1, sticky="nw", padx=(0, 30))

ctk.CTkLabel(col2, text="Idioma", font=font_labels, text_color="black").pack(anchor="w")
ctk.CTkComboBox(col2, values=["Inglés", "Español", "Francés"], 
                fg_color="#d9d9d9", text_color="black", border_width=0, 
                button_color="#333333", corner_radius=0).pack(anchor="w", pady=(0, 20))

ctk.CTkLabel(col2, text="Tipo de pasta:", font=font_labels, text_color="black").pack(anchor="w")
pasta_var = tk.StringVar(value="Dura")

for pasta in ["Dura", "Suave", "Plastificada"]:
    ctk.CTkRadioButton(col2, text=pasta, variable=pasta_var, value=pasta, 
                       text_color="black", fg_color="#c0c0c0", 
                       border_color="#d9d9d9", hover_color="#a0a0a0").pack(anchor="w", pady=5)

#Carreras
col3 = ctk.CTkFrame(bottom_frame, fg_color="transparent")
col3.grid(row=0, column=2, sticky="nw")

ctk.CTkLabel(col3, text="Carreras:", font=font_labels, text_color="black").pack(anchor="w")

carreras = ["Sistemas computacionales", "Administración", "Mecánica", 
            "Mecatrónica", "Química", "Industrial"]
for carrera in carreras:
    ctk.CTkCheckBox(col3, text=carrera, text_color="black", 
                    fg_color="#c0c0c0", border_color="#d9d9d9", 
                    hover_color="#a0a0a0", corner_radius=0).pack(anchor="w", pady=4)

#Botones de Acción
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.place(relx=0.95, rely=0.95, anchor="se")

ctk.CTkButton(btn_frame, text="Clear Form", fg_color="white", text_color="black", 
              border_color="#a855f7", border_width=2, corner_radius=10, 
              hover_color="#f3e8ff", width=100).pack(side="left", padx=10)

ctk.CTkButton(btn_frame, text="Print Info", fg_color="white", text_color="black", 
              border_color="#f97316", border_width=2, corner_radius=10, 
              hover_color="#ffedd5", width=100).pack(side="left")

app.mainloop()