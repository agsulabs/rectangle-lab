from models import Rectangle


def create_rectangle(width, height):
    if width is None or height is None:
        return None

    rectangle = Rectangle(width, height)

    if not rectangle.is_valid():
        return None

    return rectangle