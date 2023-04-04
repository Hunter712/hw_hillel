list_of_numbers = [int(input("Enter first number:")), int(input("Enter second number:")),
                   int(input("Enter third number:"))]

max_number = 0
for i in list_of_numbers:               # беру по очереди каждый элемент списка
    for j in list_of_numbers:
        if i > j and i > max_number:    # сравниваю i со всеми остальными элементами списка,
            max_number = i              # если i больше всех остальных элементов и больше предыдущего
                                        # записанного в max_number то присваиваю значение и вывожу

print(max_number)
