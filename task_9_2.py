class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def calculation(self, m, sm):
        self.m = m
        self.sm = sm
        return self._length * self._width * m * sm/1000


a = Road(20, 5000)
print(a.calculation(25, 5))
