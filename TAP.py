import customtkinter as ct

root = ct.CTk()

frame1 = ct.CTkFrame(root, fg_color="red")
frame1.pack(side="left", fill="x", expand=True)
frame2 = ct.CTkFrame(root, fg_color="orange")
frame2.pack(side="left", fill="x", expand=True)
frame3 = ct.CTkFrame(root, fg_color="green")
frame3.pack(side="right", fill="y", expand=True)

boton = ct.CTkButton(
    master=root,
    text="HOLA",
    fg_color="blue",
)
boton.pack(pady=20)

root.mainloop()