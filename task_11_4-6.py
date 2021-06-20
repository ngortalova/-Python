class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self, storage_name):
        self.storage_name = storage_name
        self.storage_code = {}
        self.dep_account_code = {}
        self.broken_dict = {}

    def broken_lst(self):
        print(f"выбыло {self.broken_dict}\n")

    def add_to_storage(self, equipment):
        self.storage_code.setdefault(equipment.code, [equipment.types, equipment.model, equipment.year])
        print(f"на склад пришло оборудование: {equipment} \n")

    def give_to_dep(self, equip):
        self.dep_account_code.setdefault(equip.code, self.storage_code.pop(equip.code))
        print(f"со склада отгружено в бухгалтерию: {equip} \n")

    def current_status(self):
        print(f'*** на текущий момент на складе {self.storage_code} \n \n ***в бухгалтерии {self.dep_account_code}\n')

    def broken(self, equip):
        self.broken_dict.setdefault(equip.code, [equip.types, equip.model, equip.year])
        print(f"выбыл {equip}")
        try:
            self.storage_code.pop(equip.code)
        except KeyError:
            try:
                self.dep_account_code.pop(equip.code)
            except KeyError:
                print(f"*{equip} не на балансе*")
        Storage.broken_lst(self)


class Equipment:
    def __init__(self, model, code, year, types=""):
        self.model = model
        self.code = code
        self.year = year
        self.types = types
        if type(self.code) == str:
            while not self.code.isdigit():
                try:
                    if not self.code.isdigit():
                        raise OwnError("Код должен быть цифровой.объект не записан")
                except OwnError as err:
                    print(err)
                    self.code = input("введите код объекта: ")
            self.code = int(self.code)

    def __str__(self):
        return f"{self.types}-{self.model}-{self.code}-{self.year}"


class Printer(Equipment):
    def __init__(self, model, code, year):
        super().__init__(model, code, year, types="printer")


class Scanner(Equipment):
    def __init__(self, model, code, year):
        super().__init__(model, code, year, types='scanner')


class Xerox(Equipment):
    def __init__(self, model, code, year):
        super().__init__(model, code, year, types='xerox')


s = Storage("general")
printer_Hp090 = Printer("Hp090", 890980, 2017)
scanner_Hp8978 = Scanner("Hp8978", 560, 2019)
xerox_1 = Xerox("Xerox01", 2093840, 2007)
s.add_to_storage(printer_Hp090)
s.add_to_storage(scanner_Hp8978)
s.add_to_storage(xerox_1)
s.give_to_dep(scanner_Hp8978)
xerox_2 = Xerox("Xerox02", 290940, 2007)
xerox_3 = Xerox("Xerox03", 90903840, 2007)
s.add_to_storage(xerox_2)
s.add_to_storage(xerox_3)
s.give_to_dep(xerox_2)
s.current_status()
s.broken(xerox_1)
s.current_status()
s.broken_lst()
s.broken(xerox_2)
s.current_status()
xerox_4 = Xerox("Xerox04", 8, 2012)
s.broken(xerox_4)
scanner_01 = Scanner("HAha909", "oipo", 2014)
s.add_to_storage(scanner_01)
s.current_status()
s.broken(xerox_1)
