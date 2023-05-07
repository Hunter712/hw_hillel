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

    def animal_age_predict(self):
        """ Предуагадываю сколько теоретически осталось жить животному"""

        if self.breed_of_animal in self.animals:
            if self.is_pet and self.good_month_analyses:
                return self.animals.get(self.breed_of_animal) - self.age
            else:
                return (self.animals.get(self.breed_of_animal) - self.age) / 2
        else:
            return random.randint(3, 15)

    def calculate_best_month_to_meet_couple(self):
        """Рассчитываю в каком месяце лучше сводить животных в зависимости от породы"""
        if self.breed_of_animal == "Cat":
            return random.randint(3, 5)
        elif self.breed_of_animal == "Dog":
            return random.randint(6, 9)
        else:
            return random.randint(1, 12)


class IsCouple:
    best_shops = {"petslike": 2, "pethouse": 1, "petchoice": 5, "shinshilka": 1}

    def __init__(self, animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2

    def compare_couple(self):
        """Сравниваю животных в зависимости от того совпадают у них месяцы или нет"""
        if self.animal1.calculate_best_month_to_meet_couple() == self.animal2.calculate_best_month_to_meet_couple():
            return True
        else:
            return False

    def best_shop_for_animal(self):
        """Предискиваю лучший зоо магазин"""
        return max(self.best_shops, key=self.best_shops.get)

    @staticmethod
    def generate_name_for_baby_animal():
        """Генератор случайных имен для животного"""
        return names.get_first_name()


my_animal1 = Animal("Lui", 3, "Cat", True)
my_animal2 = Animal("Kristina", 5, "Cat", True)

couple = IsCouple(my_animal1, my_animal2)
if couple.compare_couple():
    print(f"{my_animal1.name} and {my_animal2.name} is perfect couple")
else:
    print(f"They are bad couple")
