
import tkinter as tk
from config import color
from .controller import update_draw

def input_field(frame, field_name, field_text, column, canvas, shape, area_val, perimeter_val):
    var_name =  field_name + "_var"
    entry_name = "entry_" + field_name
    setattr(frame, var_name, tk.StringVar())
    var = getattr(frame, var_name)

    label = tk.Label(frame, text=field_text, bg=color.MENU_BG_COLOR, fg=color.TEXT_COLOR, font=("Arial", 10))
    label.grid (row=0, column=column, padx=5, pady=5)
    entry = tk.Entry(frame, width=8, textvariable=var)
    entry.grid(row=0, column=column+1, padx=5, pady=5)

    setattr(frame, entry_name, entry)

    var.trace_add("write", lambda *args: update_draw(canvas, shape, frame, area_val, perimeter_val))

    return entry

def shape_param(frame, shape = None, canvas = None, area_val = None, perimeter_val = None):
    if shape == "Rechteck":

        input_field(frame, "width", "Breite:", 0, canvas, shape, area_val, perimeter_val)
        input_field(frame, "height", "Höhe:", 2, canvas, shape, area_val, perimeter_val)

    elif shape == "Dreieck":

        input_field(frame, "left_side", "Linke Seite:", 0, canvas, shape, area_val, perimeter_val)
        input_field(frame, "right_side", "Rechte Seite:", 2, canvas, shape, area_val, perimeter_val)
        input_field(frame, "base", "Basis:", 4, canvas, shape, area_val, perimeter_val)

    elif shape == "Kreis":
        input_field(frame, "radius", "Radius:", 0, canvas, shape, area_val, perimeter_val)