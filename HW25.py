def call_counter(file_name):
    def read_number():
        with open(file_name, "r") as file:
            file_str = file.read()
        return file_str

    def write_number(file_str):
        with open(file_name, "w") as file:
            file.write(file_str)

    def inner(function):
        def wrapper(*args, **kwargs):
            if read_number():  # проверяю на пустой файл
                file_list = read_number().split("\n")
                find_unwritten_function = 0
                for line in range(len(file_list)):  # прохожу по каждой строке файла
                    if function.__name__ in file_list[line]:  # проверяю есть ли в строке текущая функция
                        file_str = file_list[line].split(" ")  # формирую новый лист из строки, нахожу число,
                        for i in range(len(file_str)):  # перезаписываю на одно больше и кладу обратно в файл
                            if file_str[i].isdigit():
                                file_str[i] = str(int(file_str[i]) + 1)
                        file_list[line] = ' '.join(file_str)

                if read_number().count(function.__name__) == 0:
                    file_list.append(
                        f"Function {function.__name__} was called 1 times")  # если функция ранее не записывалась в файл то записываю ее
                write_number('\n'.join(file_list))
            else:  # если файл пустой записываю функцию
                write_number(f"Function {function.__name__} was called 1 times")
            return function(*args, **kwargs)

        return wrapper

    return inner


@call_counter('data.txt')
def add(a, b):
    return a + b


@call_counter('data.txt')
def odd(a, b, c):
    return a + b + c


add(3, 4)
odd(3, 4, 5)
