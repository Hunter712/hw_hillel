import random


# формирую строку из рандомных символов, добавляю туда A-Za-z0-9 по очереди,
# что бы в строке были намешаны по порядку разные символы
# тк строка получается в 3 раза больше, возвращаю срез который равен string_length
def get_random_string(string_length):
    result_string = ""
    for i in range(string_length):
        result_string += chr(random.randint(48, 57)) + chr(random.randint(65, 90)) + chr(random.randint(97, 122))
    return result_string[:string_length]


print(get_random_string(5))
