import customtkinter as ctk

# window
window = ctk.CTk()
window.title('minecraft displayer')

frame = ctk.CTkFrame(window)
frame.pack()

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