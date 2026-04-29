import tkinter as tk

header_bg_color = "#1A1B26"
body_bg_color = "#24283B"
canvas_bg_color = "#1F2335"

accent_color = "#7AA2F7"
menu_bg_color = "#6B1B46"
text_color = "#C0CAF5"

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

def on_button_click(shape, overlay, menu_frame, canvas):
    clear_frame(menu_frame)
    shape_param(menu_frame, shape, canvas)
    close_menu(overlay)
        
def menu_button(overlay, shapes, menu_frame, canvas):
    rnd_x = overlay.winfo_width() / 2 - 50
    rnd_y = overlay.winfo_height() / 2 -100
    for index, text in enumerate(shapes):
        rnd_x, rnd_y = menu_button_coordinate(rnd_x, rnd_y)
        button = tk.Button(
            overlay,
            text=text,
            command=lambda shape=text: on_button_click(shape, overlay, menu_frame, canvas),
            bg=menu_bg_color,
            fg=text_color,
            font=("Arial", 12, "bold")
        )   
        button.place(relx=0.5, rely=0.5, x=rnd_x, y=rnd_y)

def rectangle(canvas, frame):
    x0 = 100
    y0 = 100
    width = read_values(frame.entry_width)
    height = read_values(frame.entry_height)

    if width is None or height is None:
        return
    else:
        x1 = x0 + width * 10
        y1 = y0 + height * 10

        canvas.create_rectangle(x0, y0, x1, y1, outline=accent_color, width=2)

def triangle(canvas, frame):
    left = read_values(frame.entry_left)
    right = read_values(frame.entry_right)
    base = read_values(frame.entry_base)

    if left is None or right is None or base is None:
        return
    else:
        scale = 2

        x0 = 100
        y0 = 300

        a = left * scale
        b = right * scale
        c = base * scale

        # prüfen, ob das Dreieck möglich ist
        if a + b <= c or a + c <= b or b + c <= a:
            return

        x1 = x0 + c
        y1 = y0

        x2 = x0 + (a**2 - b**2 + c**2) / (2 * c)
        height = (a**2 - (x2 - x0)**2) ** 0.5
        y2 = y0 - height

        canvas.create_polygon(
            x0, y0,
            x1, y1,
            x2, y2,
            outline=accent_color,
            fill="",
            width=2
        )

def circle(canvas, frame):
    radius = read_values(frame.entry_radius)

    if radius is None:
        return
    else:
        scale = 10

        x0 = 100
        y0 = 100

        r = radius * scale

        canvas.create_oval(
            x0,
            y0,
            x0 + r * 2,
            y0 + r * 2,
            outline=accent_color,
            width=2
        )

def menu(window, menu_frame, canvas):
    overlay = tk.Canvas(window, bg=canvas_bg_color)
    overlay.place(x=0, y=0, relwidth=1, relheight=1)
    overlay.bind("<Button-1>", lambda event: close_menu(overlay, menu_frame))
    overlay.tk.call("raise", overlay._w)
    menu_list = ["Rechteck", "Dreieck", "Kreis"]
    menu_button(overlay, menu_list, menu_frame, canvas)

def read_values(entry):
    try:
        text = entry.get().replace(",", ".")
        value = float(text)
        if value > 0 :
            return value       
    except ValueError:
        return None

def input_field(frame, field_name, field_text, column, canvas, shape):
    var_name =  field_name + "_var"
    entry_name = "entry_" + field_name
    setattr(frame, var_name, tk.StringVar())
    var = getattr(frame, var_name)

    label = tk.Label(frame, text=field_text, bg=menu_bg_color, fg=text_color, font=("Arial", 10))
    label.grid (row=0, column=column, padx=5, pady=5)
    entry = tk.Entry(frame, width=8, textvariable=var)
    entry.grid(row=0, column=column+1, padx=5, pady=5)

    setattr(frame, entry_name, entry)

    var.trace_add("write", lambda *args: update_draw(canvas, shape, frame))

    return entry

def shape_param(frame, shape = None, canvas = None):
    if shape == "Rechteck":

        input_field(frame, "width", "Breite:", 0, canvas, shape)
        input_field(frame, "height", "Höhe:", 2, canvas, shape)

    elif shape == "Dreieck":

        input_field(frame, "left", "Linke Seite:", 0, canvas, shape)
        input_field(frame, "right", "Rechte Seite:", 2, canvas, shape)
        input_field(frame, "base", "Basis:", 4, canvas, shape)

    elif shape == "Kreis":
        input_field(frame, "radius", "Radius:", 0, canvas, shape)

def update_draw(canvas, shape, frame):
       
    canvas_draw(canvas, shape, frame)    

def canvas_draw(canvas, shape, frame):
    canvas.delete("all")

    if shape is None:
        return

    elif shape == "Rechteck":
        rectangle(canvas, frame)
    elif shape == "Dreieck":
        triangle(canvas, frame)
    elif shape == "Kreis":
        circle(canvas, frame)
        
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

    header_frame = tk.Frame(window, bg=header_bg_color, height=80)
    header_frame.grid(row=0, column=0, sticky="ew")

    menu_frame = tk.Frame(header_frame, bg=header_bg_color, height=30)
    menu_frame.grid(row=1, column=2, pady=5, padx=5)

    header_frame.grid_propagate(False)

    body_frame = tk.Frame(window, bg=body_bg_color)
    body_frame.grid(row=1, column=0, sticky="nsew")
    

    body_frame.grid_columnconfigure(0, weight=1)
    body_frame.grid_rowconfigure(0, weight=1)

    footer_frame = tk.Frame(window, bg=header_bg_color, height=50)
    footer_frame.grid(row=2, column=0, sticky="ew")
    footer_frame.grid_propagate(False)

    canvas = tk.Canvas(body_frame, bg=canvas_bg_color)
    canvas.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    button = tk.Button(header_frame, text="Figur auswählen", command=lambda: menu(window, menu_frame, canvas), bg=accent_color, fg=body_bg_color, font=("Arial", 12, "bold"))
    button.grid(row=1, column=1, pady=10, padx=5)

    window.mainloop()