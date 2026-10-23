class Area:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w

B1 = Area(8, 4)
print("Area:", B1.calculate_area())
