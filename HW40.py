def cash(function):
    def wrapper(a, b):
        if wrapper.arg_1 is None and wrapper.arg_2 is None:
            # сохраняем аргументы первого выполнения функции
            # и результат выполнения функции
            wrapper.arg_1 = a
            wrapper.arg_2 = b

            wrapper.result = function(a, b)
            return wrapper.result
        elif wrapper.arg_1 == a and wrapper.arg_2 == b:
            # если аргументы совпадают то возвращаю сохраненный результат
            return wrapper.result
        elif wrapper.arg_1 == b and wrapper.arg_2 == a:
            # если аргументы совпадают то возвращаю сохраненный результат
            return wrapper.result
        else:
            # если аргументы НЕ совпадают то вычисляю функцию
            return function(a, b)

    wrapper.arg_1 = None
    wrapper.arg_2 = None
    wrapper.result = None
    return wrapper


@cash
def sum_numbers(a, b):
    return a + b


print(sum_numbers(2, 3))
print(sum_numbers(1, 3))
print(sum_numbers(2, 3))
print(sum_numbers(3, 2))
print(sum_numbers(22, 3))
