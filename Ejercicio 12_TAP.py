import customtkinter as ctk
from tkinter import messagebox
from supabase import create_client, Client

# --- Credenciales de Supabase (Cámbialas por las de tu panel en Settings > API) ---
SUPABASE_URL: str = "https://seulhziqexiqjqgpumgn.supabase.co"
SUPABASE_KEY: str = "sb_publishable_FLHtqU0Pt8zFi4eYQldBsA_85dHy5eu"

# Inicializar cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Funciones auxiliares de validación y soporte
def validar_usuario(nombre: str) -> bool:
    """Valida que el usuario tenga entre 3 y 30 caracteres alfanuméricos o guiones."""
    if 3 <= len(nombre) <= 30:
        return all(c.isalnum() or c in "._-" for c in nombre)
    return False

def identificador_interno(nombre: str) -> str:
    """Transforma el nombre de usuario en un formato de correo único para Supabase Auth."""
    return f"{nombre}@tudominio.internal"

def ejecutar_async(funcion_crear, funcion_finalizar):
    """Simulador de ejecución para evitar congelar la interfaz gráfica."""
    try:
        resultado = funcion_crear()
        funcion_finalizar(resultado, None)
    except Exception as e:
        funcion_finalizar(None, str(e))


class FormularioRegistroAuth:
    def __init__(self, marco_padre):
        self.marco = marco_padre
        self.memoria = {}
        self.construir_interfaz()

    def limpiar(self):
        """Limpia los widgets anteriores del marco."""
        for widget in self.marco.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        """Función de ejemplo para volver al login."""
        messagebox.showinfo("Navegación", "Aquí volverías a la pantalla de inicio de sesión.")

    def construir_interfaz(self):
        self.limpiar()

        # Título principal
        ctk.CTkLabel(
            self.marco,
            text="Crear cuenta",
            font=("Arial", 28, "bold")
        ).pack(pady=(25, 20))

        # Campo de usuario
        ctk.CTkLabel(self.marco, text="Elige tu nombre de usuario").pack()
        self.usuario = ctk.CTkEntry(
            self.marco,
            width=340,
            height=40,
            placeholder_text="Tu propio usuario"
        )
        self.usuario.pack(pady=(5, 15))

        # Campo de contraseña
        ctk.CTkLabel(self.marco, text="Crea tu contraseña").pack()
        self.clave = ctk.CTkEntry(
            self.marco,
            width=340,
            height=40,
            show="*",
            placeholder_text="Mínimo 8 caracteres"
        )
        self.clave.pack(pady=(5, 15))

        # Mensaje informativo o de error
        self.mensaje = ctk.CTkLabel(
            self.marco,
            text="Usa de 3 a 30 caracteres para el usuario.",
            text_color="gray",
            wraplength=340
        )
        self.mensaje.pack(pady=5)

        # Botón de registro
        self.boton_registrar = ctk.CTkButton(
            self.marco,
            text="Registrarse",
            width=340,
            height=40,
            command=self.registrar
        )
        self.boton_registrar.pack(pady=8)

        # Botón para volver al inicio
        ctk.CTkButton(
            self.marco,
            text="Volver al inicio",
            width=340,
            height=40,
            fg_color="transparent",
            command=self.mostrar_login
        ).pack(pady=5)

        # Eventos de teclado (Enter)
        self.clave.bind("<Return>", self.registrar)
        self.usuario.bind("<Return>", self.registrar)
        self.usuario.focus()

    def finalizar(self, datos, error):
        self.boton_registrar.configure(state="normal")

        if error:
            detalle = str(error).lower()
            print("Error de Supabase al registrar:", error)
            
            if any(x in detalle for x in ("already registered", "user already exists", "duplicate key", "unique constraint")):
                texto = "Ese usuario ya existe. Elige otro."
            elif "password" in detalle:
                texto = "La contraseña no cumple los requisitos."
            elif any(x in detalle for x in ("database error saving new user", "database error", "trigger", "violates not-null constraint")):
                texto = "Error al guardar el usuario en la base de datos. Revisa el trigger en Supabase."
            else:
                texto = "No se pudo registrar. Revisa la consola."
                
            self.mensaje.configure(text=texto, text_color="#F87171")
            return

        if not datos or not datos.user:
            self.mensaje.configure(text="Supabase no devolvió los datos de la cuenta.", text_color="#F87171")
            return

        if not datos.session:
            self.mensaje.configure(
                text="Cuenta creada, pero no hay sesión activa. Revisa si la confirmación de correo está desactivada en Supabase.",
                text_color="#FBBF24"
            )
            return

        # Éxito
        self.memoria["usuario"] = self.usuario.get().strip().lower()
        messagebox.showinfo(
            "Registro exitoso",
            "Tu cuenta se creó correctamente. Ya puedes iniciar sesión."
        )
        self.mostrar_login()

    def registrar(self, event=None):
        nombre = self.usuario.get().strip().lower()
        password = self.clave.get()

        if not validar_usuario(nombre):
            self.mensaje.configure(
                text="Usa de 3 a 30 caracteres: letras, números, punto, guion o guion bajo.",
                text_color="#F87171"
            )
            return

        if len(password) < 8:
            self.mensaje.configure(
                text="La contraseña debe tener al menos 8 caracteres.",
                text_color="#F87171"
            )
            return

        self.boton_registrar.configure(state="disabled")
        self.mensaje.configure(text="Creando cuenta...", text_color="#60A5FA")

        def crear():
            return supabase.auth.sign_up({
                "email": identificador_interno(nombre),
                "password": password,
                "options": {
                    "data": {
                        "nombre_usuario": nombre
                    }
                }
            })

        ejecutar_async(crear, self.finalizar)


# --- Código para probar la ventana directamente ---
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    app = ctk.CTk()
    app.geometry("450x600")
    app.title("Registro de Usuarios - Supabase")

    marco_principal = ctk.CTkFrame(app, fg_color="transparent")
    marco_principal.pack(fill="both", expand=True, padx=20, pady=20)

    app_registro = FormularioRegistroAuth(marco_principal)
    app.mainloop()