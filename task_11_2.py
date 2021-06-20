class ZDev(Exception):
    def __init__(self, txt):
        self.txt = txt


x = input("Введите число x: ")
y = input("Введите число y: ")

try:
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZDev("ZDE на ноль делить нееезяя")
except ZDev as err:
    print(err)
except ValueError:
    print("вы ввели не число")
else:
    print(f"x / y = {x / y}")
