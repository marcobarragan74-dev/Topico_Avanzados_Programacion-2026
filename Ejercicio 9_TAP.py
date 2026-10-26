import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image
import os


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class AppEventosITVER(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Registro de Eventos - ITVER")
        self.geometry("850x650")
        self.minsize(800, 600)
        
        self.contador_id = 1
        
        self.crear_interfaz()
        
    def crear_interfaz(self):

        # Título y Logotipo

        self.frame_header = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_header.pack(pady=10, padx=20, fill="x")
        
        # Intentar cargar logo
        try:
            ruta_logo = os.path.join(os.path.dirname(__file__), "logo.png")
            imagen_logo = ctk.CTkImage(Image.open(ruta_logo), size=(80, 80))
            self.lbl_logo = ctk.CTkLabel(self.frame_header, image=imagen_logo, text="")
        except:
            self.lbl_logo = ctk.CTkLabel(self.frame_header, text="[ LOGO ITVER ]", font=("Arial", 20, "bold"), text_color="blue")
            
        self.lbl_logo.pack(side="left", padx=(0, 20))
        
        self.lbl_titulo = ctk.CTkLabel(self.frame_header, 
                                       text="Sistema de Registro de Eventos - ITVER", 
                                       font=("Arial", 24, "bold"))
        self.lbl_titulo.pack(side="left")


        # SECCIÓN 2: Elemento Treeview 

        self.frame_tree = ctk.CTkFrame(self)
        self.frame_tree.pack(pady=10, padx=20, fill="both", expand=True)
        
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure("Treeview", rowheight=30, font=("Arial", 11))
        estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        
        columnas = ("ID", "Nombre", "Fecha", "Lugar")
        self.tree = ttk.Treeview(self.frame_tree, columns=columnas, show="headings")
        
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre del Evento")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Lugar", text="Lugar")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nombre", width=300)
        self.tree.column("Fecha", width=150, anchor="center")
        self.tree.column("Lugar", width=250)
        
        # Colores
        self.tree.tag_configure("par", background="#FFFACD", foreground="black")   # Amarillo claro
        self.tree.tag_configure("impar", background="#E0F8E0", foreground="black") # Verde claro
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.tree.bind("<ButtonRelease-1>", self.seleccionar_evento)


        # Formulario y Botones

        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=10, padx=20, fill="x")
        
        # Entradas de datos
        ctk.CTkLabel(self.frame_form, text="Nombre del Evento:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.ent_nombre = ctk.CTkEntry(self.frame_form, width=250)
        self.ent_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text="Fecha (DD/MM/AAAA):").grid(row=0, column=2, padx=10, pady=10, sticky="e")
        self.ent_fecha = ctk.CTkEntry(self.frame_form, width=150)
        self.ent_fecha.grid(row=0, column=3, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text="Lugar del Evento:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.ent_lugar = ctk.CTkEntry(self.frame_form, width=250)
        self.ent_lugar.grid(row=1, column=1, padx=10, pady=10)
        
        self.frame_botones = ctk.CTkFrame(self.frame_form, fg_color="transparent")
        self.frame_botones.grid(row=2, column=0, columnspan=4, pady=20)
        
        # Botones de Acción
        self.btn_agregar = ctk.CTkButton(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side="left", padx=10)
        
        self.btn_modificar = ctk.CTkButton(self.frame_botones, text="Modificar Evento", command=self.modificar_evento)
        self.btn_modificar.pack(side="left", padx=10)
        
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento, fg_color="#D9534F", hover_color="#C9302C")
        self.btn_eliminar.pack(side="left", padx=10)
        
        self.btn_limpiar = ctk.CTkButton(self.frame_botones, text="Limpiar Formulario", command=self.limpiar_formulario, fg_color="gray")
        self.btn_limpiar.pack(side="left", padx=10)


    # LÓGICA

    def limpiar_formulario(self):
        self.ent_nombre.delete(0, 'end')
        self.ent_fecha.delete(0, 'end')
        self.ent_lugar.delete(0, 'end')
        self.tree.selection_remove(self.tree.selection())

    def alternar_colores(self):
        for index, item in enumerate(self.tree.get_children()):
            if index % 2 == 0:
                self.tree.item(item, tags=("par",))    # Amarillo
            else:
                self.tree.item(item, tags=("impar",))  # Verde

    def agregar_evento(self):
        nombre = self.ent_nombre.get().strip()
        fecha = self.ent_fecha.get().strip()
        lugar = self.ent_lugar.get().strip()
        
        if not nombre or not fecha or not lugar:
            messagebox.showwarning("Campos Vacíos", "Por favor, llene todos los campos del formulario.")
            return
            
        # Insertar en el Treeview
        self.tree.insert("", "end", values=(self.contador_id, nombre, fecha, lugar))
        self.contador_id += 1
        
        self.alternar_colores()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def seleccionar_evento(self, event):
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            valores = item['values']
            
            self.limpiar_formulario()
            self.ent_nombre.insert(0, valores[1])
            self.ent_fecha.insert(0, valores[2])
            self.ent_lugar.insert(0, valores[3])

    def modificar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un evento de la lista para modificar.")
            return
            
        nombre = self.ent_nombre.get().strip()
        fecha = self.ent_fecha.get().strip()
        lugar = self.ent_lugar.get().strip()
        
        if not nombre or not fecha or not lugar:
            messagebox.showwarning("Campos Vacíos", "Los campos no pueden estar vacíos.")
            return
            
        # Obtener el ID
        id_actual = self.tree.item(seleccion[0])['values'][0]
        
        # Actualizar valores
        self.tree.item(seleccion[0], values=(id_actual, nombre, fecha, lugar))
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Evento modificado correctamente.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección", "Por favor, seleccione un evento de la lista para eliminar.")
            return
            
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
        if confirmacion:
            self.tree.delete(seleccion[0])
            self.alternar_colores() # Reajustar colores
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Evento eliminado.")

if __name__ == "__main__":
    app = AppEventosITVER()
    app.mainloop()