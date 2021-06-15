class Cell:
    def __init__(self, cells_in_the_cell):
        self.cells = cells_in_the_cell

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return self.cells - other.cells
        else:
            return f'The second Cell is bigger and the result is not satisfying (less or equal to zero)'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_a_raw):
        self.raw = cells_in_a_raw
        if self.raw >= self.cells:
            return f'{"*" * self.cells}'
        else:
            return "\n".join([("\n".join(("*" * self.raw) for i in range(self.cells//self.raw))),
                              ("*" * (self.cells % self.raw))])


a = Cell(5)
b = Cell(3)
print(a)
c = a + b
print(c)
print(c.cells)
d = a * b
print(a - b)
print(b - a)
print(d)
print(d.cells)
f = d // a
print(f)
print(f.cells)
print(d.make_order(4))
print(f.make_order(1))
print(a.make_order(2))
