from day_one.Food import Food


class Elf:
    _number: int
    _food_list: list
    _total_calories: int

    def __init__(self, number, food_list):
        self.number = number
        self.food_list = food_list
        self.total_calories = self.calculate_total_calories()

    def calculate_total_calories(self):
        total = 0
        for food_item in self.food_list:
            total += food_item.calories

        return total

    def add_food_item(self, calories):
        self.food_list.append(Food(calories))

    @property
    def food_list(self):
        return self._food_list

    @food_list.setter
    def food_list(self, food_list):
        foods = []
        for calorie_number in food_list:
            foods.append(Food(calorie_number))
        self._food_list = foods

    @property
    def total_calories(self):
        return self._total_calories

    @total_calories.setter
    def total_calories(self, total_calories):
        self._total_calories = total_calories

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number
