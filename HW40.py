def cash(function):
    def wrapper(*args, **kwargs):
        new_calculation = function(*args, **kwargs)
        if wrapper.result is None:
            # записываю первый результат выполнения функции
            wrapper.result = new_calculation
            return wrapper.result
        elif wrapper.result == new_calculation:
            # если первый записанный результат совпадает с новым то вывожу самый первый результат
            return wrapper.result
        else:
            # если первый записанный результат не совпадает с новым,
            # то просто вывожу новый результат выполения функции
            return new_calculation

    wrapper.result = None
    return wrapper


@cash
def sum_numbers(a, b):
    return a + b


print(sum_numbers(2, 3))
print(sum_numbers(1, 3))
print(sum_numbers(2, 3))
print(sum_numbers(22, 3))
