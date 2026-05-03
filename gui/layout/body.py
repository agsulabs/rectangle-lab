
import tkinter as tk
from config import color

def build_body(parent):
    parent.body_frame = tk.Frame(parent.root, bg=color.BODY_BG_COLOR)
    parent.body_frame.grid(row=1, column=0, sticky="nsew")
    parent.body_frame.grid_columnconfigure(0, weight=1)
    parent.body_frame.grid_rowconfigure(0, weight=1)

    parent.canvas = tk.Canvas(parent.body_frame, bg=color.CANVAS_BG_COLOR)
    parent.canvas.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)