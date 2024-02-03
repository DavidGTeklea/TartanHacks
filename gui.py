import customtkinter as ctk

# window
window = ctk.CTk()
window.title('minecraft displayer')
window.geometry('150x100')

# widgets
label = ctk.CTkLabel(
    window, 
    text = 'number', 
    fg_color = 'green',
    text_color = 'black',
    corner_radius = 10)
label.pack()

# run GUI
window.mainloop()