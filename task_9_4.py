class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("GO GO GOOOOOOOOOO")

    def turn(self, direction):
        self.direction = direction
        print(f"Оп. новый поворот {self.direction}")

    def stop(self):
        print("Стопэ")

    def show_speed(self):
        print(f"Скорость {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость {self.speed}")
        if self.speed > 60:
            print(f"Воу ту мач... тормози до 60")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Скорость {self.speed}")
        if self.speed > 40:
            print(f"Воу ту мач... тормози до 40")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = Car(90, "green", "one", False)
b = TownCar(70, "red", "two", False)
c = WorkCar(40, "yellow", "three", True)
d = PoliceCar(100, "white", "oneonly", True)
e = SportCar(200, "black", "Black Panter", False)
a.go()
print(f"набрали скорость {a.speed}")
a.show_speed()
a.turn("to the right")
a.stop()
print(f"это полицейская машина - {a.is_police}")
b.go()
b.show_speed()
b.turn("to the right")
b.stop()
a.go()
print(f" цвет {a.color}")
a.show_speed()
a.turn("to the right")
a.stop()
print(f"имя авто - {a.name} ")