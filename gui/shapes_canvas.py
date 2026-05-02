
from logic import create_rectangle, create_triangle, create_circle

from utils import read_values
from config import color

def canvas_draw(canvas, shape, frame):
    canvas.delete("all")

    if shape is None:
        return

    elif shape == "Rechteck":
        x0 = 100
        y0 = 100

        width = read_values(frame.entry_width)
        height = read_values(frame.entry_height)

        rectangle_obj = create_rectangle(width, height)

        if rectangle_obj is None:
            return None
        
        x1 = x0 + rectangle_obj.width
        y1 = y0 + rectangle_obj.height

        canvas.create_rectangle(x0, y0, x1, y1, outline=color.ACCENT_COLOR, width=2)        

        return rectangle_obj
    
    elif shape == "Dreieck":
        x0 = 100
        y0 = 100

        left_side = read_values(frame.entry_left_side)
        right_side = read_values(frame.entry_right_side)
        base = read_values(frame.entry_base)

        triangle_obj = create_triangle(left_side, right_side, base)
       
        if triangle_obj is None:
            return None

        x1 = x0 + triangle_obj.base
        y1 = y0

        x2 = x0 + (triangle_obj.left_side**2 - triangle_obj.right_side**2 + triangle_obj.base**2) / (2 * triangle_obj.base)
        height = (triangle_obj.left_side**2 - (x2 - x0)**2) ** 0.5
        y2 = y0 - height

        canvas.create_polygon(
            x0, y0,
            x1, y1,
            x2, y2,
            outline=color.ACCENT_COLOR,
            fill="",
            width=2
        )
        
        return triangle_obj
    
    elif shape == "Kreis":
        x0 = 100
        y0 = 100

        radius = read_values(frame.entry_radius)

        circle_obj = create_circle(radius)

        if circle_obj is None:
            return None
        
        x1 = x0 + circle_obj.radius * 2
        y1 = y0 + circle_obj.radius * 2

        canvas.create_oval(x0, y0, x1, y1, outline=color.ACCENT_COLOR, width=2)

        return circle_obj