string_with_data_in_file = ""

with open("text.txt", "r") as file:
    string_with_data_in_file = file.read()

list_with_data_in_file = string_with_data_in_file.split("\n")   #разбил каждую новую строку файла по элементам списка
dict_with_calculated_symbols = {}

for i in list_with_data_in_file:    #прохожу по каждому элементу списка, подсчитываю количество элементов строки, формирую словарь где ключи это количество символов строки, значение это сама строка
    count_symbols = 0
    for j in i:
        count_symbols += 1
    dict_with_calculated_symbols[count_symbols] = i

max_symbol_numbers = 0
for i in dict_with_calculated_symbols:  #вывожу самую большую строку сравнивая по ключам в словаре
    if i > max_symbol_numbers:
        max_symbol_numbers = i

print(dict_with_calculated_symbols[max_symbol_numbers])
