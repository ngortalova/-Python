from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_calc(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.size = v

    @property
    def fabric_calc(self):
        self.calc_fabric = self.size/6.5 + 0.5
        return self.calc_fabric

    def __add__(self, other):
        return self.calc_fabric + other.calc_fabric

    def __str__(self):
        return self.calc_fabric


class Suit(Clothes):
    def __init__(self, h):
        self.height = h

    @property
    def fabric_calc(self):
        self.calc_fabric = 2 * self.height + 0.3
        return self.calc_fabric

    def __add__(self, other):
        return self.calc_fabric + other.calc_fabric

    def __str__(self):
        return self.calc_fabric


a = Suit(10)
print(a.fabric_calc)
b = Coat(20)
print(b.fabric_calc)
print(a + b)
