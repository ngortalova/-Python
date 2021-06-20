class ComplexNum:
    def __init__(self, x, y):
        self.com_num = complex(x, y)
        print(self.com_num)
        self.x = x
        self.y = y

    def __add__(self, other):
        return complex((self.x + other.x), (self.y + other.y))

    def __mul__(self, other):
        return complex((self.x * other.x - self.y * other.y), (self.x*other.y + self.y * other.x))


a = ComplexNum(2, 9)
b = ComplexNum(3, 1)
print(a + b)
print(a * b)
