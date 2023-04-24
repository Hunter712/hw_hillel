def to_dict(lst):
    new_dict = {}

    if len(lst) % 2 != 0:       #проверяю на четность элементов в листе
        return "wrong list"

    check_for_odd_index = 1
    for i in range(len(lst)):
        if check_for_odd_index % 2 != 0:
            new_dict[lst[i]] = lst[i + 1]
        check_for_odd_index += 1
    return new_dict


my_list = [2, 1, 3, 4, 6, 5, 7, 8]
print(to_dict(my_list))
