class Polygon:
    def area(self):
        pass   


class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base      
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height

class Square(Polygon):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side


class Pentagon(Polygon):
    def __init__(self, side, apothem):
        self.__side = side
        self.__apothem = apothem

    def area(self):
        perimeter = 5 * self.__side
        return (perimeter * self.__apothem) / 2


class Decagon(Polygon):
    def __init__(self, side, apothem):
        self.__side = side
        self.__apothem = apothem

    def area(self):
        perimeter = 10 * self.__side
        return (perimeter * self.__apothem) / 2


shapes = [
    Triangle(10, 5),
    Square(4),
    Pentagon(6, 4),
    Decagon(5, 7)
]

names = ["Triangle", "Square", "Pentagon", "Decagon"]

for name, shape in zip(names, shapes):
    print("Area of", name, "is:", shape.area())
