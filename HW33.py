def custom_zip(*sequences, full=True, default=None):
    new_sequence = []
    result_list = []
    for i in sequences:  # формирую новый список списков
        new_sequence.append(i)

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
        for max_list_indexes in range(max_length_list):
            get_elem_from_lists_by_index = []
            for lists in new_sequence:
                get_elem_from_lists_by_index.append(lists[max_list_indexes])
            result_list.append(tuple(get_elem_from_lists_by_index))
        return result_list
    else:
        # нахожу список с найменьшим количеством элементов
        min_length_list = min(len(x) for x in new_sequence)

        # прохожу по всем спискам, вытаскиваю елементы по соответствующему индексу и формирую новый tuple
        for min_list in range(min_length_list):
            get_elem_from_lists_by_index = []
            for lst in new_sequence:
                get_elem_from_lists_by_index.append(
                    lst[min_list])
            result_list.append(
                tuple(get_elem_from_lists_by_index))
        return result_list


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
seq3 = [1, 3, 4, 5]

print(custom_zip(seq1, seq2, seq3, full=True, default="Q"))
