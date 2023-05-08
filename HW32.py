from inspect import signature
import copy


def custom_map(function, *sequences):
    new_sequence = []
    result_list = []

    # формирую новый список списков
    for i in sequences:
        new_sequence.append(copy.deepcopy(i))

    # определяю количество елементов в минимальной последовательности что бы избежать ексепшина в дальнейшем
    min_length_list = min(len(x) for x in new_sequence)
    for index in range(min_length_list):
        arguments = []
        for list in new_sequence:
            arguments.append(list[index])
        result_list.append(function(*arguments))

    return result_list



def test(a, b, c, d):
    return a + b + c + d


print(custom_map(len, [[1, 2, 3], [4, 5, 3]]))
print(custom_map(sum, [[1, 4, 3], [4, 1]]))  # с этой функцией не работает, как и с многими другими built-in,
# пока не знаю как решить, если это не обязательно для этой задачи то супер
print(custom_map(lambda x, y, z: x + y + z, [1, 4, 3], [4, 5], [1, 2]))
print(custom_map(test, [1, 2, 3, 4], [4, 5, 6], [11, 22, 1], [2, 0, 1]))
