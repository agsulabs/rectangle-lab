from .shapes_canvas import canvas_draw
from .footer import update_footer

def update_draw(canvas, shape, frame, area_val, perimeter_val):
    shape_obj = canvas_draw(canvas, shape, frame)

    if shape_obj is None:
        update_footer(None, None, area_val, perimeter_val)
        return

    area = shape_obj.area()
    perimeter = shape_obj.perimeter()
    
    update_footer(area, perimeter, area_val, perimeter_val)    