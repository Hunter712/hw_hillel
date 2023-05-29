def cash(function):
    ARGS = 0
    KWARGS = 1
    FUNCCTION_RESULT = 2

    def compare_elements(cash_list, args, kwargs):
        # проверяю есть ли аргументы в кеше, если нет то возвращаю None что бы первые данные записались в кеш
        if cash_list:
            result = None
            # пробегаюсь по списку закешированных списков аргументов
            for list_with_args in cash_list:
                # беру текущий список, достаю из него закешированные args и сравниваю с новыми args
                # формирую новый список из совпавших елементов из args
                compared_list = [x for x in list_with_args[ARGS] if x in args]
                # сравнниваю по длинне список compared_list с текущим закешированным списком,
                # если совпадают по длинне, значит args идентичны
                # после чего сравниваю kwargs
                # если args и kwargs совпадают, присваиваю result закешированный список и возвращаю его
                # если не совпадают то иду дальше по списку закешированных списков
                if len(compared_list) == len(list_with_args[ARGS]) and list_with_args[KWARGS] == kwargs:
                    result = list_with_args
            return result
        else:
            return None

    def wrapper(*args, **kwargs):
        # проверяю совпадают ли *args, **kwargs с закешированными аргументами
        compare = compare_elements(wrapper.func_data, args, kwargs)
        # если аргументы совпадают то возвращаю закешированный результат выполнения функции и проваливаюсь в if
        if compare is not None:
            # возвращаю закешированный результат выполненния функции
            return compare[FUNCCTION_RESULT]
        else:
            # если аргументы не совпадают то выполняю функцию и добавляю новые данные в кеш
            func_result = function(*args, **kwargs)
            # записываю в кеш список с тремя елементами:
            # elem1 - список args
            # elem2 - список kwargs
            # elem3 - результат выполненния функции
            wrapper.func_data.append([list(args), kwargs, func_result])
            return func_result

    wrapper.func_data = []
    return wrapper


@cash
def sum_numbers(a, b):
    return a + b


@cash
def sum_lists(a, b):
    return a + b


print("result = ", sum_numbers(2, 3))
print("result = ", sum_numbers(3, 2))
print("result = ", sum_numbers(3, 1))
print("result = ", sum_numbers(1, 3))

print("result = ", sum_lists([1, 2, 3], [4, 5, 6]))
print("result = ", sum_lists([1, 2, 2], [4, 1, 6]))
print("result = ", sum_lists([4, 5, 6], [1, 2, 3]))


@cash
def func_with_kwargs(title, **kwargs):
    print(f"Calculated for {title} {kwargs}")
    return sum([kwargs[key] for key in kwargs])


print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', b=4, a=3))
print(func_with_kwargs('first', a=100, b=4))
print(func_with_kwargs('first', a=100, b=4))
print(func_with_kwargs('first', a=3, b=4))
