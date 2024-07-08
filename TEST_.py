import math


class Figure:
    def __init__(self, __color=(0, 0, 0), sides_count=0, __sides=None, filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
         for c in (r, g, b):
             if isinstance(c, int) or c < 0 or c > 255:
                 return True
             else:
                 return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            return True
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    def __init__(self, radius=0):
        super().__init__()
        self._radius = radius

    def get_square(self):
        return self._radius ** 2 * math.pi

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value





if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    # cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    # cube1.set_color(300, 70, 15)
    # print(cube1.get_color())

    # cube1.set_sides(5, 3, 12, 4, 5)
    # print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))
    # print(cube1.get_volume())