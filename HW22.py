def read_last_elements(file_path, symbol_number):

    with open(file_path, "r") as file:
        string_with_data_in_file = file.read()

    # разбил каждую новую строку файла по элементам списка
    list_with_data_in_file = string_with_data_in_file.split("\n")
    # прохожу по строкам в списке, проверяю на наличие строки,
    # если строка есть то слайсами вывожу последние елементы
    for elements in list_with_data_in_file:
        if elements != "":
            print(elements[-symbol_number:])


read_last_elements('text.txt', 6)
