class AttributePrinterMixin:
    def get_class_atributes(self):
        class_name = self.__class__.__name__
        dict_with_atrs = self.__dict__
        resulted_str = f"{class_name}: \u007b\n"

        # формирую список, каждый элемент которого будет сожержать имя поля и его значение в одной строке
        result_list = [str(k) + ": " + str(v) for k, v in dict_with_atrs.items()]

        # вырезаю символы связанные с доступами к полям, из элементов списка
        for index in range(len(result_list)):
            if result_list[index][0] == "_":
                if result_list[index][1] == class_name:
                    result_list[index] = result_list[index][4:]
                else:
                    result_list[index] = result_list[index][1:]

        # формирую результирующу строку
        for i in result_list:
            resulted_str += "\t" + i + "\n"
        return resulted_str + "\u007d"


class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

    def method(self):
        pass


a = A()
print(a.get_class_atributes())
