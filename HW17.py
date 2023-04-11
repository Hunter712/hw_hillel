lst = [['a', 'c', 'd'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

revert_to_90grad_lst = []
sorted_lst = []
final_lst = []
for i in range(len(lst) - 1):   #выхватываю по одному элементу по очереди из каждого списка и кладу их в отдельный список, тем самым преобразуя столбцы в строки
    new_lst = []
    for j in range(len(lst)):
        new_lst.append(lst[j][i])
    revert_to_90grad_lst.append(new_lst)

for i in revert_to_90grad_lst:          #сортирую каждый вложенный список и кладу его в отдельный список, фирмирую тем самым вложенный список с отсортированными списками внутри
    sorted_lst.append(sorted(i))

for i in range(4):      #выхватываю по одному элементу по очереди из каждого списка и кладу их в отдельные списки, тем самым преобразуя строки в столбцы
    new_lst = []
    for j in range(len(sorted_lst)):
        new_lst.append(sorted_lst[j][i])
    final_lst.append(new_lst)

for i in final_lst:
    print(i)
