def linearize_list(lst):
    if lst:
        if isinstance(lst[0], list):    # проверяю текущий элемент на список
            linearize_list(lst[0])      # если попался список передаю его еще раз что бы углубиться на уровень
            return linearize_list(lst[1:])  # передаю остаток списка после текщуго списка
        elif isinstance(lst[0], int):   # проверяю текущий элемент на число
            new_lst.append(lst[0])      # если число то добавляю его в новую строку
            return linearize_list(lst[1:])  # передаю остаток списка после числа


lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
new_lst = []
linearize_list(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(new_lst)
