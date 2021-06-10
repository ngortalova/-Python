class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        self.full_name = f"{self.surname} {self.name}"
        return self.full_name

    def get_total_income(self):
        self.total_income = self._income["wage"] + self._income["bonus"]
        return self.total_income


ivanov = Position("Ivan", "Ivanov", "hardworker", 1000, 12)
print(ivanov.get_full_name())
print(ivanov.get_total_income())
