class Rectangle:
    __sideA = 0
    __sideB = 5

    def __init__(self, a, b=__sideB):
        self.a = float(a)
        self.b = float(b)

    def get_A(self):
        return self.a

    def get_B(self):
        return self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def square(self):
        return self.a == self.b

    def swap(self):
        self.a, self.b = self.b, self.a
        return self.a, self.b


rec = Rectangle(7)
print(rec.a, rec.b)
print(rec.get_A(), rec.get_B())
print(rec.perimeter(), rec.area())
print(rec.square())

rec = Rectangle(5)
print(rec.a, rec.b)
print(rec.square())
print(rec.swap())
