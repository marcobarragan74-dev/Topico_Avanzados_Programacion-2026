import tkinter as tk
from tkinter import ttk

#Ventana
root = tk.Tk()
root.title("Treeview Demo")
root.geometry("600x200")

#Constructor del arbol
frame = ttk.Frame(root)
treeview = ttk.Treeview()

#Columnas
treeview = ttk.Treeview(columns=("Salary", "Bonus"))

treeview.heading("#0", text="Empleado")
treeview.heading("Salary", text="Salario")
treeview.heading("Bonus", text="Bono")

#Scroll Vertical
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=v_scrollbar.set)

#Iconos
icon_city = tk.PhotoImage(file=r"C:\Users\mabc_\Downloads\city.png")
icon_female = tk.PhotoImage(file=r"C:\Users\mabc_\Downloads\female.png")
icon_male = tk.PhotoImage(file=r"C:\Users\mabc_\Downloads\male.png")

treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame.pack(fill=tk.BOTH, expand=True, padx="20", pady="20")

#Primer nivel
level1 = treeview.insert("", tk.END, text="Veracruz", image=icon_city)
treeview.insert(level1, tk.END, text="Miranda Ibañez", values=("$1200", "$500"), image=icon_female)
treeview.insert(level1, tk.END, text="Jaime Uriel", values=("$3000", "$800"), image=icon_male)
treeview.insert(level1, tk.END, text="Pablo Angel", values=("$6999", "$2499"), image=icon_male)

treeview.pack(fill=tk.BOTH, expand=True, padx="20", pady="20")

root.mainloop()