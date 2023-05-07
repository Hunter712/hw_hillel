import random
import names


class Animal:
    animals = {"Dog": 15, "Cat": 12, "Hamster": 4}

    def __init__(self, name, age, breed_of_animal, is_pet=False, good_month_analyses=None):
        self.name = name
        self.age = age
        self.breed_of_animal = breed_of_animal
        self.is_pet = is_pet
        self.good_month_analyses = good_month_analyses

    """Предуагадываю сколько теоретически осталось жить животному"""
    def calculate_animal_age_predict(self):
        if self.breed_of_animal in self.animals:
            if self.is_pet and self.good_month_analyses:
                return self.animals.get(self.breed_of_animal) - self.age
            else:
                return (self.animals.get(self.breed_of_animal) - self.age) / 2
        else:
            return random.randint(3, 15)

    """Рассчитываю в каком месяце лучше сводить животных в зависимости от породы"""
    def calculate_best_month_to_meet_couple(self):
        if self.breed_of_animal == "Cat":
            return random.randint(3, 5)
        elif self.breed_of_animal == "Dog":
            return random.randint(6, 9)
        else:
            return random.randint(1, 12)


class FindPerfectCouple:
    best_shops = {"petslike": 2, "pethouse": 1, "petchoice": 5, "shinshilka": 1}

    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2

    """Ищу пару для животного в зависимости от того совпадают у них месяцы или нет"""
    def find_couple(self):
        if self.animal1.calculate_best_month_to_meet_couple() == self.animal2.calculate_best_month_to_meet_couple():
            return f"{self.animal1.name} and {self.animal2.name} is perfect couple"
        else:
            return "Bad couple"

    """Предискиваю лучший зоо магазин"""
    def best_shop_for_animal(self):
        return max(self.best_shops, key=self.best_shops.get)

    """Генератор случайных имен для животного"""
    @staticmethod
    def generate_name_for_baby_animal():
        return names.get_first_name()


my_animal1 = Animal("Lui", 3, "Cat", True)
my_animal2 = Animal("Kristina", 5, "Cat", True)

find_couple = FindPerfectCouple(my_animal1, my_animal2)
print(find_couple.best_shop_for_animal())
