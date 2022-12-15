class Food:
    _calories: int

    def __init__(self, calories=0):
        self.calories = calories

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        if calories.isdigit():
            self._calories = int(calories)
        else:
            self._calories = 0
