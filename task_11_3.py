class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_number = 0
num_list = []
while inp_number != "stop":
    inp_number = input("Введите число: ")
    try:
        float(inp_number)
    except ValueError:
        try:
            if inp_number[0] == '-':
                if not inp_number[1:].isdigit():
                    raise OwnError("Вы ввели не число")
            elif not inp_number.isdigit():
                raise OwnError("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            number = int(inp_number)
            print(f"Все хорошо. Ваше число {number} добавлено в список")
            num_list.append(number)
    else:
        number = float(inp_number)
        print(f"Все хорошо. Ваше число {number} добавлено в список")
        num_list.append(number)

print(f"ваш список: {num_list}")
