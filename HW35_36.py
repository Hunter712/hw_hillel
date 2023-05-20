from abc import ABC, abstractmethod
import my_DB


class Client(ABC):
    @abstractmethod
    def make_order(self):
        pass

    @abstractmethod
    def give_feeback(self):
        pass


class Service(ABC):
    @abstractmethod
    def receive_new_orders(self):
        pass

    @abstractmethod
    def make_order(self, current_order_id):
        pass

    @abstractmethod
    def receive_orders_which_is_ready(self):
        pass

    @abstractmethod
    def receive_money_from_clients(self, current_order_id):
        pass


class User(Client):
    def __init__(self, order_id, name, address, order, payment_type, status):
        self.order_id = order_id
        self.name = name
        self.address = address
        self.order = order
        self.payment_type = payment_type
        self.status = status
        self.data = my_DB.DB()

    # клиент делает заказ
    def make_order(self):
        self.data.save_new_order_to_DB(self.order_id, self.name, self.address, self.order,
                                       self.payment_type, self.status)

    def give_feeback(self):
        pass


class Kitchen(Service):
    def __init__(self):
        self.data = my_DB.DB()

    # сотрудники кухни получают все новые заказы
    def receive_new_orders(self):
        users_list = self.data.get_new_orders_from_DB()
        for user in users_list:
            print(user)

    # сотрудники кухни выполняют заказы и меняют им статусы на done
    def make_order(self, current_order_id):
        self.data.update_order(current_order_id, "done")


class Delivery(Kitchen):

    # сотрудник доставки получает заказы которые уже сделали на кухне
    def receive_orders_which_is_ready(self):
        users_list = self.data.get_done_orders_from_DB()
        for user in users_list:
            print(user)

    # сотрудник доставки апдейтит статус заказа клиента на paid после доставки
    def receive_money_from_clients(self, current_order_id):
        self.data.update_order(current_order_id, "paid")


user1 = User(11, "Vlad", "Kharkiv Pr. Peremogy 66", "Salo i Vodka", "cash", "new")
user1.make_order()
user2 = User(22, "Anna", "New York  4", "Borsch", "card", "new")
user2.make_order()
user3 = User(33, "Sam", "Berlin Hallo str 34", "Zesar", "cash", "new")
user3.make_order()

delivery_order = Delivery()
delivery_order.receive_new_orders()
delivery_order.make_order(11)

delivery_order.receive_orders_which_is_ready()
delivery_order.receive_money_from_clients(11)
