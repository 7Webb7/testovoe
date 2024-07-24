import math

class Shape:
    def area(self):
        raise NotImplementedError("Требуется абстрактный метод")
class Circle(Shape):
    def __init__(self, radius):
        self.raidus = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.real_triangle():
            raise ValueError("Невозможно.")


    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.b))

    def real_triangle(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)



    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

def compute_area(shape: Shape):
    return shape.area()

if __name__ == "__main__":
    circle = Circle(5)
    print(f"Площадь круга: {circle.area()}")

    triangle = Triangle(3, 4, 5)
    print(f"Площадь треугольника: {triangle.area()}")
    print(f"Правильный ли треугольник? {'Да' if triangle.is_right_triangle() else 'Нет'}")
