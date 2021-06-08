def val_checker(condition):
    def _val_checker(func):
        def wrapper(*args):
            result = func(*args)
            if condition(*args):
                return result
            else:
                raise ValueError(f'Wrong value: {args}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
