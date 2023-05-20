class DB:
    # читаю строки с файла ипроверяю есть ли там айдишник нового заказа, если нет то добавляю заказ
    @staticmethod
    def save_new_order_to_DB(order_id, name, address, order, payment_type, status):
        with open("data.txt", "r") as file:
            string_with_data_in_file = file.read()

        if string_with_data_in_file.find(str(order_id)) == -1:
            with open("data.txt", "a") as file:
                file.write(f"{order_id}, {name}, {address}, {order}, {payment_type}, {status}\n")

    # вытаскиваю из файла все заказы, и формирую каждый из заказов в отдельный элемент списка
    @staticmethod
    def get_all_orders_from_DB():
        with open("data.txt", "r") as file:
            string_with_data_in_file = file.read()
        users = string_with_data_in_file.split("\n")
        resulted_list = []
        for index in range(len(users) - 1):
            resulted_list.append(users[index].split(", "))
        return resulted_list

    # вытаскиваю из файла заказы со статусом new,
    # и формирую каждый из заказов в отдельный элемент списка
    @staticmethod
    def get_new_orders_from_DB():
        with open("data.txt", "r") as file:
            string_with_data_in_file = file.read()
        users = string_with_data_in_file.split("\n")
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            if user_data[5] == "new":
                resulted_list.append(user_data)
        return resulted_list

    # вытаскиваю из файла заказы со статусом done,
    # и формирую каждый из заказов в отдельный элемент списка
    @staticmethod
    def get_done_orders_from_DB():
        with open("data.txt", "r") as file:
            string_with_data_in_file = file.read()
        users = string_with_data_in_file.split("\n")
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            if user_data[5] == "done":
                resulted_list.append(user_data)
        return resulted_list

    # вытаскиваю из файла все заказы, обновляю статус заказа для соответствующего order_id
    # перезаписываю все данные в файл
    @staticmethod
    def update_order(order_id, status):
        with open("data.txt", "r") as file:
            string_with_data_in_file = file.read()
        users = string_with_data_in_file.split("\n")
        resulted_list = []
        for index in range(len(users) - 1):
            user_data = users[index].split(", ")
            resulted_list.append(user_data)

        for user in resulted_list:
            if user[0] == str(order_id):
                user[5] = status

        result = ""
        for user in resulted_list:
            result += f"{user[0]}, {user[1]}, {user[2]}, {user[3]}, {user[4]}, {user[5]}\n"
        with open("data.txt", "w") as file:
            file.write(result)
