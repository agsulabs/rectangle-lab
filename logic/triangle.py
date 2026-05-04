from models import Triangle

def create_triangle(left_side, right_side, base):
    if left_side is None or right_side is None or base is None:
        return None
        
    triangle = Triangle(left_side, right_side, base)
    
    if not triangle.is_valid():
        return None
    
    return triangle