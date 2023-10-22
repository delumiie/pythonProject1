class Figure:
    unit = "cm"

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.__side_length

    def info(self):
        print(f"Square side length: {self.__side_length}{self.unit}, perimeter: "
              f"{self.calculate_perimeter()}{self.unit},  area: {self.calculate_area()}{self.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def info(self):
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit},"
              f" perimeter: {self.calculate_perimeter()}{self.unit}, area: {self.calculate_area()}{self.unit}.")


square1 = Square(6)
square2 = Square(7)
rectangle1 = Rectangle(2, 9)
rectangle2 = Rectangle(8, 6)
rectangle3 = Rectangle(11, 12)

figures_list = [square1, square2, rectangle1, rectangle2, rectangle3]

for figure in figures_list:
    figure.info()
