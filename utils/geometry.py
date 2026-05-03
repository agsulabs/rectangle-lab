
def get_points(offset_x, offset_y, shape_points):

    points = [
        (point_x + offset_x, point_y + offset_y)
        for point_x, point_y in shape_points
    ]

    return points