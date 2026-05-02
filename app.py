import tkinter as tk

from gui import menu
from config import color


def run_app():
    window = tk.Tk()
    window.title("Rectangle Lab")

    window_width = 800
    window_height = 600

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    header_frame = tk.Frame(window, bg=color.HEADER_BG_COLOR, height=80)
    header_frame.grid(row=0, column=0, sticky="ew")

    menu_frame = tk.Frame(header_frame, bg=color.HEADER_BG_COLOR, height=30)
    menu_frame.grid(row=1, column=2, pady=5, padx=5)

    header_frame.grid_propagate(False)

    body_frame = tk.Frame(window, bg=color.BODY_BG_COLOR)
    body_frame.grid(row=1, column=0, sticky="nsew")

    body_frame.grid_columnconfigure(0, weight=1)
    body_frame.grid_rowconfigure(0, weight=1)

    footer_frame = tk.Frame(window, bg=color.HEADER_BG_COLOR, height=50)

    area_var = tk.StringVar(value="Fläche: -")
    perimeter_var = tk.StringVar(value="Umfang: -")

    area_label = tk.Label(
        footer_frame,
        textvariable=area_var,
        bg=color.HEADER_BG_COLOR,
        fg=color.TEXT_COLOR,
    )
    area_label.grid(row=0, column=0, padx=20, pady=15)

    perimeter_label = tk.Label(
        footer_frame,
        textvariable=perimeter_var,
        bg=color.HEADER_BG_COLOR,
        fg=color.TEXT_COLOR,
    )
    perimeter_label.grid(row=0, column=1, padx=20, pady=15)

    footer_frame.grid(row=2, column=0, sticky="ew")
    footer_frame.grid_propagate(False)

    canvas = tk.Canvas(body_frame, bg=color.CANVAS_BG_COLOR)
    canvas.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    button = tk.Button(
        header_frame,
        text="Figur auswählen",
        command=lambda: menu(window, menu_frame, canvas, area_var, perimeter_var),
        bg=color.ACCENT_COLOR,
        fg=color.BODY_BG_COLOR,
        font=("Arial", 12, "bold"),
    )
    button.grid(row=1, column=1, pady=10, padx=5)

    window.mainloop()