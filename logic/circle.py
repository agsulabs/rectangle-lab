
def create_circle(radius):
    if radius is None:
        return None

    from models import Circle
    circle = Circle(radius)

    if not circle.is_valid():
        return None

    return circle