from models import Triangle

def create_triangle(left_side, right_side, base):
    if left_side is None or right_side is None or base is None:
        return None
        
    trilange = Triangle(left_side, right_side, base)
    
    if not trilange.is_valid():
        return None
    
    return trilange