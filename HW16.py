lst = [3.5, 2, 4, 6.2, 8]

for index in range(len(lst) - 1, 0, -1):
    average_number = (lst[index] + lst[index - 1]) / 2
    lst.insert(index, average_number)

print(lst)
