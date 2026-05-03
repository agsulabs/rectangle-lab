
import tkinter as tk
from config import color
from .input_panel import shape_param

def close_menu(overlay, frame = None):
    overlay.destroy()
    if frame:
        clear_frame(frame)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def menu_button_coordinate(x, y):
    btn_x = x
    btn_y = y+50
    return btn_x, btn_y

def menu_button(overlay, shapes, menu_frame, canvas, area_val, perimeter_val):
    rnd_x = overlay.winfo_width() / 2 - 50
    rnd_y = overlay.winfo_height() / 2 -100
    for index, text in enumerate(shapes):
        rnd_x, rnd_y = menu_button_coordinate(rnd_x, rnd_y)
        button = tk.Button(
            overlay,
            text=text,
            command=lambda shape=text: on_button_click(shape, overlay, menu_frame, canvas, area_val, perimeter_val),
            bg=color.MENU_BG_COLOR,
            fg=color.TEXT_COLOR,
            font=("Arial", 12, "bold")
        )   
        button.place(relx=0.5, rely=0.5, x=rnd_x, y=rnd_y)

def on_button_click(shape, overlay, menu_frame, canvas, area_val, perimeter_val):
    clear_frame(menu_frame)
    shape_param(menu_frame, shape, canvas, area_val, perimeter_val)
    close_menu(overlay)
        
def menu(root, menu_frame, canvas, area_val, perimeter_val):
    overlay = tk.Canvas(root, bg=color.CANVAS_BG_COLOR)
    overlay.place(x=0, y=0, relwidth=1, relheight=1)
    overlay.bind("<Button-1>", lambda event: close_menu(overlay, menu_frame))
    overlay.tk.call("raise", overlay._w)
    menu_list = ["Rechteck", "Dreieck", "Kreis"]
    menu_button(overlay, menu_list, menu_frame, canvas, area_val, perimeter_val)