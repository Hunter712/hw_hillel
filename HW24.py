def second_largest_number_in_list(lst):
    if len(lst) == 0:
        return None

    max_number = lst[0]
    second_max_number = lst[0]
    for element in lst:
        if element > max_number:  # ищу самый большой элемент в списке
            # если нашел элемент больше максимального, значит тот что находится в
            # max_number будет вторым по величине, кладу его в second_max_number а в max_number кладу новый самый
            # большой елемент
            second_max_number = max_number
            max_number = element

        # обрабатываю ситуацию когда нахожусь не в конце списка а
        # максимальный элемент уже найден, таким образом ищу 2й по счету самый большой элемент
        if max_number > element > second_max_number:
            second_max_number = element

    return second_max_number


my_list = [1, 1, 3, 5, 18, 4, 3, 2, 15, 0]
print(second_largest_number_in_list(my_list))
