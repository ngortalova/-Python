class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        # print("При вызове метода calculation запомните параметры: 1) масса асфальта для покрытия одного кв. метра"
        #       " асфальтом, толщина в 1 см; 2) число см толщины полотна")

    def calculation(self, m, sm):
        self.m = m
        self.sm = sm
        print(self._length * self._width * m * sm/1000, "тонн")


a = Road(20, 5000)
a.calculation(25, 5)
