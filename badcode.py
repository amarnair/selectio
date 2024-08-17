def calc_area(length, width, thickness):
    area = length * width
    area_thickness = area * thickness
    result = f"The area of the rectangle is {area} square units and the area including thickness is {area_thickness} cubic units"
    return result

print(calc_area(10, 5, 2))
