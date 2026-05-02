

def update_footer(area, perimeter, area_val, perimeter_val):


    if area is not None and perimeter is not None:
        area_val.set(f"Fläche: {area:.2f}")
        perimeter_val.set(f"Umfang: {perimeter:.2f}")
    else:
        area_val.set("Fläche: -")
        perimeter_val.set("Umfang: -")