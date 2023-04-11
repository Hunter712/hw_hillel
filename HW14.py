list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

elem_divided_by_3 = []
for i in list_of_numbers:
    if i != 0 and i % 3 == 0 and i % 5 != 0:
        elem_divided_by_3.append(i)
print(elem_divided_by_3)

elem_divided_by_5 = []
for i in list_of_numbers:
    if i != 0 and i % 5 == 0 and i % 3 != 0:
        elem_divided_by_5.append(i)
print(elem_divided_by_5)

elem_divided_by_3_and_5 = []
for i in list_of_numbers:
    if i % 5 == 0 and i % 3 == 0:
        elem_divided_by_3_and_5.append(i)
print(elem_divided_by_3_and_5)









