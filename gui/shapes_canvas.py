
from logic import create_rectangle, create_triangle, create_circle

from utils import read_values
from utils import get_points

from config import color

def canvas_draw(canvas, shape, frame):
    canvas.delete("all")
    offset_x = 100
    offset_y = 100
    if shape is None:
        return

    elif shape == "Rechteck":
        
        width = read_values(frame.entry_width)
        height = read_values(frame.entry_height)

        rectangle_obj = create_rectangle(width, height)
        if rectangle_obj is None:
            return None
        
        shape_points = rectangle_obj.points()
        if shape_points is None:
            return None
        
        points = get_points(offset_x, offset_y, shape_points)
        if points is None:
            return None
        
        canvas.create_polygon(
            points, 
            outline=color.ACCENT_COLOR, 
            fill="", 
            width=2)        

        return rectangle_obj
    
    elif shape == "Dreieck":

        left_side = read_values(frame.entry_left_side)
        right_side = read_values(frame.entry_right_side)
        base = read_values(frame.entry_base)

        triangle_obj = create_triangle(left_side, right_side, base)
        if triangle_obj is None:
            return None

        shape_points = triangle_obj.points()
        if shape_points is None:
            return None
        
        points = get_points(offset_x, offset_y, shape_points)
        if points is None:
            return None

        canvas.create_polygon(
            points,
            outline=color.ACCENT_COLOR,
            fill="",
            width=2
        )
        
        return triangle_obj
    
    elif shape == "Kreis":

        radius = read_values(frame.entry_radius)

        circle_obj = create_circle(radius)
        if circle_obj is None:
            return None
        
        shape_points = circle_obj.bounding_box()
        if shape_points is None:
            return None
        
        points = get_points(offset_x, offset_y, shape_points)
        if points is None:
            return None

        canvas.create_oval(points, outline=color.ACCENT_COLOR, width=2)

        return circle_obj