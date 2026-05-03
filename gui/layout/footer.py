import tkinter as tk
from config import color

def build_footer(parent):
    parent.footer_frame = tk.Frame(parent.root, bg=color.HEADER_BG_COLOR, height=50)
    parent.footer_frame.grid(row=2, column=0, sticky="ew")
    parent.footer_frame.grid_propagate(False)

    parent.area_var = tk.StringVar(value="Fläche: -")
    parent.perimeter_var = tk.StringVar(value="Umfang: -")

    area_label = tk.Label(
        parent.footer_frame,
        textvariable=parent.area_var,
        bg=color.HEADER_BG_COLOR,
        fg=color.TEXT_COLOR,
    )
    area_label.grid(row=0, column=0, padx=20, pady=15)

    perimeter_label = tk.Label(
        parent.footer_frame,
        textvariable=parent.perimeter_var,
        bg=color.HEADER_BG_COLOR,
        fg=color.TEXT_COLOR,
    )
    perimeter_label.grid(row=0, column=1, padx=20, pady=15)

  