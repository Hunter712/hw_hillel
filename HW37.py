class AttributePrinterMixin:
    def __str__(self):
        resulted_str = f"{self.__class__.__name__}: \u007b\n"

        # формирую список, каждый элемент которого будет сожержать имя поля и его значение в одной строке
        result_list = [str(k) + ": " + str(v) for k, v in self.__dict__.items()]

        # вырезаю символы связанные с доступами к полям, из элементов списка
        for index in range(len(result_list)):
            if result_list[index][0] == "_":
                if result_list[index].find('__') != -1:
                    result_list[index] = result_list[index][result_list[index].find('__') + 2:]
                else:
                    result_list[index] = result_list[index][1:]

        # формирую результирующу строку
        for i in result_list:
            resulted_str += "\t" + i + "\n"
        return resulted_str + "\u007d"


class Bbbb:
    def __init__(self):
        self.__private_in_B = 'private_in_B'
        self._private1_in_B = 'private1_in_B'


class A(Bbbb, AttributePrinterMixin):
    def __init__(self):
        Bbbb.__init__(self)
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

    def method(self):
        pass


a = A()
print(a)
