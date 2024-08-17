AREA_TOLERANCE = 0.1
THICKNESS_UNIT = "square units"

def calc_area(length: float, width: float, thickness: float) -> tuple:
    area = length * width
    area_thickness = area * thickness
    result = f"The area of the rectangle is {area:.2f} {THICKNESS_UNIT} and the area including thickness is {area_thickness:.2f} cubic units"
    return area, area_thickness, result

length, width, thickness = 10, 5, 2
area, area_thickness, result = calc_area(length, width, thickness)
print(result)
