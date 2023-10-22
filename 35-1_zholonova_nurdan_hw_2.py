class Figure:
    unit = "cm"

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return round(3.14 * self.__radius ** 2, 2)

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit},"
              f" area: {self.calculate_area()}{self.unit}.")


circle1 = Circle(7)
circle2 = Circle(13)

triangle1 = RightTriangle(17, 6)
triangle2 = RightTriangle(12, 4)
triangle3 = RightTriangle(25, 10)

figures_list = [circle1, circle2, triangle1, triangle2, triangle3]

for figure in figures_list:
    figure.info()
