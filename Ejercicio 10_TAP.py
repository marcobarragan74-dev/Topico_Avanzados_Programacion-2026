import customtkinter as ctk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#CONFIGURACIÓN DEL ORM-
Base = declarative_base()

class Evento(Base):
    __tablename__ = 'eventos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    fecha = Column(String(50), nullable=False)
    lugar = Column(String(100), nullable=False)
    descripcion = Column(String(200))

engine = create_engine('sqlite:///eventos_campus.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#INTERFAZ
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AppEventos(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Control de Eventos - Campus")
        self.geometry("850x650")
        
        #Formulario de Captura
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=20, padx=20, fill="x")
        
        ctk.CTkLabel(self.frame_form, text="Nombre del Evento:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_form, width=250, placeholder_text="Ej. Simposio de Ingeniería")
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text="Fecha (DD/MM/AAAA):").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.entry_fecha = ctk.CTkEntry(self.frame_form, width=200, placeholder_text="28/09/2026")
        self.entry_fecha.grid(row=0, column=3, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text="Lugar:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_lugar = ctk.CTkEntry(self.frame_form, width=250, placeholder_text="Ej. Auditorio ITVER")
        self.entry_lugar.grid(row=1, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text="Descripción:").grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.entry_desc = ctk.CTkEntry(self.frame_form, width=200)
        self.entry_desc.grid(row=1, column=3, padx=10, pady=10)
        
        #Botón Guardar
        self.btn_guardar = ctk.CTkButton(self.frame_form, text="Guardar Evento", command=self.guardar_evento)
        self.btn_guardar.grid(row=2, column=0, columnspan=4, pady=20)
        
        #Tabl
        self.frame_tabla = ctk.CTkFrame(self)
        self.frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)
        
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2a2d2e", 
                        foreground="white", 
                        rowheight=25, 
                        fieldbackground="#2a2d2e", 
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#1f538d')])
        style.configure("Treeview.Heading", background="#1f538d", foreground="white", relief="flat")
        
        columnas = ("ID", "Nombre", "Fecha", "Lugar", "Descripción")
        self.tree = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")
        
        anchos = {"ID": 50, "Nombre": 200, "Fecha": 100, "Lugar": 150, "Descripción": 200}
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=anchos[col], anchor="center")
            
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        #Botón Borrar
        self.btn_borrar = ctk.CTkButton(
            self.frame_tabla, 
            text="Borrar Registro Seleccionado", 
            fg_color="#e74c3c", 
            hover_color="#c0392b", 
            command=self.borrar_evento
        )
        self.btn_borrar.pack(pady=10)
        
        #Cargar los datos
        self.cargar_eventos()

    #LÓGICA DE BASE DE DATOS
    def guardar_evento(self):
        nombre = self.entry_nombre.get()
        fecha = self.entry_fecha.get()
        lugar = self.entry_lugar.get()
        desc = self.entry_desc.get()
        
        if not nombre or not fecha or not lugar:
            messagebox.showwarning("Campos incompletos", "Nombre, Fecha y Lugar son obligatorios.")
            return
            
        nuevo_evento = Evento(nombre=nombre, fecha=fecha, lugar=lugar, descripcion=desc)
        
        try:
            session.add(nuevo_evento)
            session.commit()
            
            # Limpiar entradas
            self.entry_nombre.delete(0, 'end')
            self.entry_fecha.delete(0, 'end')
            self.entry_lugar.delete(0, 'end')
            self.entry_desc.delete(0, 'end')
            
            self.cargar_eventos()
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"No se pudo guardar el evento: {e}")

    def cargar_eventos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        eventos_db = session.query(Evento).all()
        for ev in eventos_db:
            self.tree.insert("", "end", values=(ev.id, ev.nombre, ev.fecha, ev.lugar, ev.descripcion))

    def borrar_evento(self):
        seleccion = self.tree.selection()
        
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona un evento de la lista para eliminarlo.")
            return
            
        item = seleccion[0]
        valores_fila = self.tree.item(item, 'values')
        evento_id = valores_fila[0]
        nombre_evento = valores_fila[1]
        
        confirmacion = messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar el evento:\n'{nombre_evento}'?")
        if not confirmacion:
            return
            
        try:
            evento_db = session.query(Evento).filter(Evento.id == evento_id).first()
            if evento_db:
                session.delete(evento_db)
                session.commit()
                self.cargar_eventos()
                
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"No se pudo borrar el registro: {e}")

if __name__ == "__main__":
    app = AppEventos()
    app.mainloop()