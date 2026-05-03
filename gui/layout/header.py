import tkinter as tk
from config import color
from ..menu import menu

def build_header(parent):
    parent.header_frame = tk.Frame(parent.root, bg=color.HEADER_BG_COLOR, height=80)
    parent.header_frame.grid(row=0, column=0, sticky="ew")
    parent.header_frame.grid_propagate(False)

    parent.menu_frame = tk.Frame(parent.header_frame, bg=color.HEADER_BG_COLOR, height=30)
    parent.menu_frame.grid(row=1, column=2, pady=5, padx=5)

    button = tk.Button(
        parent.header_frame,
        text="Figur auswählen",
        command=lambda: menu(
            parent.root, 
            parent.menu_frame, 
            parent.canvas, 
            parent.area_var, 
            parent.perimeter_var),
        bg=color.ACCENT_COLOR,
        fg=color.BODY_BG_COLOR,
        font=("Arial", 12, "bold"),
    )   
    button.grid(row=1, column=1, pady=10, padx=5)   