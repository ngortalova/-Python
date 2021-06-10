class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуска отрисовки ручкой")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуска отрисовки маркером")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуска отрисовки карандашом")


a = Stationery("вся")
print(a.title)
a.draw()
b = Pen("ручка")
print(b.title)
b.draw()
c = Handle("маркер")
print(c.title)
c.draw()
d = Pencil("карандаш")
print(d.title)
d.draw()
