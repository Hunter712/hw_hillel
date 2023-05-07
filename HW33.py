def custom_zip(*sequences, full=False, default=None):
    new_sequence = []

    for i in sequences:  # формирую новый список списков
        new_sequence.append(i.copy())

    # проверяю по длинной или короткой последовательностям нужно склеить
    if full:
        # нахожу список с найбольшим количеством элементов
        max_length_list = max(len(x) for x in new_sequence)

        # прохожу по всем спискам, если какой то список меньше максимального по размеру
        # то добавляю ему в конец элементы из 3го параметра
        for list_from_sequence in new_sequence:
            if max_length_list != len(list_from_sequence):
                for i in range(max_length_list - len(list_from_sequence)):
                    list_from_sequence.append(default)

        # прохожу по всем спискам, вытаскиваю елементы по соответствующему индексу и формирую новый tuple
        return create_resulted_tuple(new_sequence, max_length_list)
    else:
        # нахожу список с найменьшим количеством элементов
        min_length_list = min(len(x) for x in new_sequence)

        # прохожу по всем спискам, вытаскиваю елементы по соответствующему индексу и формирую новый tuple
        return create_resulted_tuple(new_sequence, min_length_list)


def create_resulted_tuple(new_sequence, length_list):
    result_list = []
    for max_list_indexes in range(length_list):
        get_elem_from_lists_by_index = []
        for lists in new_sequence:
            get_elem_from_lists_by_index.append(lists[max_list_indexes])
        result_list.append(tuple(get_elem_from_lists_by_index))
    return result_list

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

print(custom_zip(seq1, seq2, full=True, default="a"))
print(custom_zip(seq1, seq2, full=False, default="a"))
