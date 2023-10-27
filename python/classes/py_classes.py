class Circle:
    def __init__(self, radius):  # constructor
        print(f"Initializing with radius of {radius}")
        self.circle_radius = radius

    def calc_area(self):
        a = 22/7 * self.circle_radius ** 2
        print(f"Area is {round(a)}")

    def calc_perimeter(self):
        p = 22/7 * 2 * self.circle_radius
        print(f"Circumference is {round(p)}")


c1 = Circle(10)
c2 = Circle(14)
c3 = Circle(13.25)

c1.calc_perimeter()
c1.calc_area()

c2.calc_area()