def to_dict(lst):
    new_dict = {}

    if len(lst) % 2 != 0:       #проверяю на четность элементов в листе
        return "wrong list"

    #в условии задачи не сказано можем менять входной список или нет,
    # если можем то можно отсортировать и скомпоновать в словарь все эелементы,
    # если менять порядок списка нельзя то эту сортировку можно убрать,
    # тогда в словарь будут попадать только элементы где первым идет не четное и за ним сразу следует четное
    lst.sort()

    # пробегаюсь по отсортированному списку, определяю не четные числа в качестве ключей и формирую новый словарь
    for i in range(len(lst)):
        try:
            if lst[i] % 2 != 0 and lst[i + 1] % 2 == 0:
                new_dict[lst[i]] = lst[i + 1]
        except IndexError:
            print("IndexError when we have few odd elements at the end of the list")
    return new_dict


my_list = [2, 1, 3, 4, 6, 5, 7, 8]
print(to_dict(my_list))
