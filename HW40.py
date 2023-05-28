def cash(function):
    ARGS = 0
    KWARGS = 1
    FUNCCTION_RESULT = 2

    # сравниваю аргументы первой выполненной функции и текущей, не зависимо от их позиции
    def compare_elements(arg1, arg2, arg3):
        new_list = []
        for element in arg1[ARGS]:
            if element in arg2:
                new_list.append(element)

        if arg1[KWARGS] == {}:
            if len(new_list) == len(arg1[ARGS]):
                return True
            else:
                return False
        else:
            if len(new_list) == len(arg1[ARGS]) and arg1[KWARGS] == arg3:
                return True
            else:
                return False

    def wrapper(*args, **kwargs):
        if wrapper.func_data == {}:
            # сохраняю аргументы первого выполнения функции
            # и результат выполнения функции
            func_result = function(*args, **kwargs)
            wrapper.func_data[function.__name__] = [list(args), kwargs, func_result]

            return func_result
        elif function.__name__ in wrapper.func_data:
            # проверяю совпадает ли функция и ее аргументы
            if compare_elements(wrapper.func_data[function.__name__], args, kwargs):
                # если аргументы совпадают то возвращаю сохраненный результат
                return wrapper.func_data[function.__name__][FUNCCTION_RESULT]
            else:
                # если не совпадают то выполняю функцию
                return function(*args, **kwargs)

    wrapper.func_data = {}
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


@cash
def func_with_kwargs(title, **kwargs):
    print(f"Calculated for {title} {kwargs}")
    return sum([kwargs[key] for key in kwargs])


print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', a=100, b=4))  # !!!тоже 7, а должно быть 104
print(func_with_kwargs('second', a=100, b=4))
