
def cash(function):
    # сравниваю аргументы первой выполненной функции и текущей, не зависимо от их позиции
    def compare_elements(arg1, arg2):
        new_list = []
        for element in arg1:
            if element in arg2:
                new_list.append(element)

        if len(new_list) == len(arg1):
            return True
        else:
            return False

    def wrapper(*args, **kwargs):

        if wrapper.func_data == {} or function.__name__ not in wrapper.func_data:
            # сохраняю аргументы первого выполнения функции
            # и результат выполнения функции
            func_result = function(*args, **kwargs)
            wrapper.func_data[function.__name__] = list(args)
            wrapper.func_result[function.__name__] = func_result

            return func_result

        elif function.__name__ in wrapper.func_data:
            # проверяю совпадает ли функция и ее аргументы
            if compare_elements(wrapper.func_data[function.__name__], args):
                # если аргументы совпадают то возвращаю сохраненный результат
                return wrapper.func_result[function.__name__]
            else:
                # если не совпадают то выполняю функцию
                return function(*args, **kwargs)

    wrapper.func_data = {}
    wrapper.func_result = {}
    return wrapper


@cash
def sum_numbers(a, b):
    return a + b


@cash
def sum_symbols(a, b, c):
    return a + b + c


@cash
def sum_lists(a, b):
    return a + b


print("result = ", sum_numbers(2, 3))
print("result = ", sum_numbers(3, 2))
print("result = ", sum_numbers(3, 1))

print("result = ", sum_symbols("a", "b", "c"))
print("result = ", sum_symbols("a", "b", "s"))
print("result = ", sum_symbols("c", "b", "a"))

print("result = ", sum_lists([1, 2, 3], [4, 5, 6]))
print("result = ", sum_lists([1, 2, 2], [4, 1, 6]))
print("result = ", sum_lists([4, 5, 6], [1, 2, 3]))
