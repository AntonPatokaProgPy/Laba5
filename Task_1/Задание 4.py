import geometry

length = 5
width = 3
radius = 2
base = 4
height = 6

rectangle_area = geometry.rectangle_area(length, width)
circle_area = geometry.circle_area(radius)
triangle_area = geometry.triangle_area(base, height)

print("Площадь прямоугольника:", rectangle_area)
print("Площадь круга:", circle_area)
print("Площадь треугольника:", triangle_area)
