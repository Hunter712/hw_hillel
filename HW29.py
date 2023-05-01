def linearize_list(lst):
    if lst:
        if isinstance(lst[0], list):
            linearize_list(lst[0])
            return linearize_list(lst[1:])
        elif isinstance(lst[0], int):
            new_lst.append(lst[0])
            return linearize_list(lst[1:])


lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
new_lst = []
linearize_list(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(new_lst)
