class DB:
    ORDER_ID = 0
    NAME = 1
    ADDRESS = 2
    ORDER = 3
    PAYMENT_TYPE = 4
    STATUS = 5

    def __init__(self, path_to_DB):
        self.path_to_DB = path_to_DB

    def read_from_file(self):
        with open(self.path_to_DB, "r") as file:
            string_with_data_in_file = file.read()
        return string_with_data_in_file.split("\n")

    # читаю строки с файла ипроверяю есть ли там айдишник нового заказа, если нет то добавляю заказ
    def save_new_order_to_DB(self, order_id, name, address, order, payment_type, status):
        with open(self.path_to_DB, "r") as file:
            string_with_data_in_file = file.read()

        if string_with_data_in_file.find(str(order_id)) == -1:
            with open(self.path_to_DB, "a") as file:
                file.write(f"{order_id}, {name}, {address}, {order}, {payment_type}, {status}\n")

    # вытаскиваю из файла все заказы, и формирую каждый из заказов в отдельный элемент списка
    def get_all_orders_from_DB(self):
        users = self.read_from_file()
        resulted_list = []
        for index in range(len(users) - 1):
            resulted_list.append(users[index].split(", "))
        return resulted_list

    # вытаскиваю из файла заказы со статусом new,
    # и формирую каждый из заказов в отдельный элемент списка
    def get_new_orders_from_DB(self):
        users = self.read_from_file()
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            if user_data[self.STATUS] == "new":
                resulted_list.append(user_data)
        return resulted_list

    # вытаскиваю из файла заказы со статусом done,
    # и формирую каждый из заказов в отдельный элемент списка
    def get_done_orders_from_DB(self):
        users = self.read_from_file()
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            if user_data[self.STATUS] == "done":
                resulted_list.append(user_data)
        return resulted_list

    # вытаскиваю из файла все заказы, обновляю статус заказа для соответствующего order_id
    # перезаписываю все данные в файл
    def update_order(self, order_id, status):
        users = self.read_from_file()
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            resulted_list.append(user_data)

        for user in resulted_list:
            if user[self.ORDER_ID] == str(order_id):
                user[self.STATUS] = status

        result = ""
        for user in resulted_list:
            result += f"{user[self.ORDER_ID]}, {user[self.NAME]}, {user[self.ADDRESS]}, " \
                      f"{user[self.ORDER]}, {user[self.PAYMENT_TYPE]}, {user[self.STATUS]}\n"
        with open(self.path_to_DB, "w") as file:
            file.write(result)
