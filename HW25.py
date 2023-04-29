from pathlib import Path

filePath = Path("data.txt")
filePath.touch(exist_ok=True)


def call_counter(file_name):
    def read_from_file():
        with open(file_name, "r") as file:
            file_str = file.read()
        return file_str

    def write_in_file(file_str):
        with open(file_name, "w") as file:
            file.write(file_str)

    def string_parser(function):
        data_from_file = read_from_file()
        if data_from_file:  # проверяю на пустой файл
            file_list = data_from_file.split("\n")

            for line in range(len(file_list)):  # прохожу по каждой строке файла
                if function.__name__ in file_list[line]:  # проверяю есть ли в строке текущая функция
                    file_str = file_list[line].split(" ")  # формирую новый лист из строки, нахожу число,
                    file_str[4] = str(int(file_str[4]) + 1)  # перезаписываю на одно больше и кладу обратно в файл
                    file_list[line] = ' '.join(file_str)

            if data_from_file.count(function.__name__) == 0:
                file_list.append(
                    f"Function {function.__name__} was called 1 times")  # если функция ранее не записывалась в файл то записываю ее
            write_in_file('\n'.join(file_list))
        else:  # если файл пустой записываю функцию
            write_in_file(f"Function {function.__name__} was called 1 times")

    def inner(function):
        def wrapper(*args, **kwargs):
            string_parser(function)
            return function(*args, **kwargs)

        return wrapper

    return inner


@call_counter(filePath)
def add(a, b):
    return a + b


@call_counter(filePath)
def odd(a, b, c):
    return a + b + c


add(3, 4)
odd(3, 4, 5)
