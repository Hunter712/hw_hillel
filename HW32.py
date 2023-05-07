from inspect import signature
import copy


def custom_map(function, *sequences):
    new_sequence = []
    result_list = []

    # формирую новый список списков
    for i in sequences:
        new_sequence.append(copy.deepcopy(i))

    # проверка на то сколько списков пришло в функцию и сколько аргументов имеет поступившая функция
    if len(new_sequence) == 1 and len(signature(function).parameters) == 1:
        # передаю каждый элемент последовательности(например если на вход поступил только 1 список
        # но в нем есть вложенные списки) в функцию и формирую итоговый список
        for i in new_sequence[0]:
            result_list.append(function(i))

        return result_list
    # проверяю что бы количество аргументов функции равнялось количеству переданных последовательностей
    elif len(new_sequence) == len(signature(function).parameters):
        # определяю количество елементов в минимальной последовательности что бы избежать ексепшина в дальнейшем
        min_length_list = min(len(x) for x in new_sequence)
        for index in range(min_length_list):
            arguments = []
            for list in new_sequence:
                arguments.append(list[index])
            result_list.append(function(*arguments))

        return result_list
    else:
        return "Wrong argument numbers or wrong function used"


def test(a, b, c, d):
    return a + b + c + d


print(custom_map(len, [[1, 2, 3], [4, 5]]))
print(custom_map(sum, [[1, 2, 3], [4, 5]]))  # с этой функцией не работает, как и с многими другими built-in,
# пока не знаю как решить, если это не обязательно для этой задачи то супер
print(custom_map(lambda x, y, z: x + y + z, [1, 2, 3], [4, 5], [1, 2]))
print(custom_map(test, [1, 2, 3], [4, 5], [11, 22], [2, 0]))
