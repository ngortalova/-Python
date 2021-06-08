from functools import wraps


def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        msg = f'Тип значения функции {result} {type(result)}; {func.__name__}'
        if kwargs:
            print(f'{msg}({kwargs.get("x")}: {type(kwargs.get("x"))})')
        elif len(args) == 1:
            result = result[0]
            msg = f'Тип значения функции {result} {type(result)}; {func.__name__}'
            print(f'{msg}({args[0]}: {type(args[0])})')
        else:
            print(f'{msg}({", ".join(map(str, [f"{arg}: {type(arg)}" for arg in args]))})')

        return result

    return wrapper


def simple_boo(func):
    @wraps(func)
    def wrapper(*args):
        boo = func(*args)
        return boo

    return wrapper


@type_logger
@simple_boo
def calc_calc(x, y):
    return x ** y


@type_logger
def calc_cube(*args):
    return tuple(map(lambda x: x ** 2, [*args]))


@type_logger
def calc_cube1(x=None):
    return x ** 2


a = calc_calc(5, 6)
b = calc_cube(6, 4, 4)
c = calc_cube(23)
d = calc_cube1(x=3)

print(a, b, c, d)
