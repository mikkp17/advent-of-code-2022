from Day import Day
from day_one.Elf import Elf


class DayOne(Day):
    def __init__(self):
        super().__init__()

    def run(self):
        calorie_data = self.read_file('day_one/data/calories')
        calorie_array = self.build_calorie_array(calorie_data)

        elf_array = []
        for (number, food_list) in enumerate(calorie_array):
            elf = Elf(number+1, food_list)
            elf_array.append(elf)

        winner = self.find_elf_with_most_calories(elf_array)
        winners = self.find_top_3_elves_with_most_calories(elf_array)

        self.print(winner, winners)

    def print_solution(self, elf):
        print('The elf with the most calories is elf number ' + str(elf.number) +
              '! And he was carrying ' + str(elf.total_calories) + ' calories!')

    def print_second_solution(self, elves):
        print('The top three elves with the most calories are:')
        print('1. Elf number ' + str(elves[0].number) + ' with ' + str(elves[0].total_calories) + ' calories')
        print('2. Elf number ' + str(elves[1].number) + ' with ' + str(elves[1].total_calories) + ' calories')
        print('3. Elf number ' + str(elves[2].number) + ' with ' + str(elves[2].total_calories) + ' calories')
        print()
        print('The total amount of calories carried by the top three elves is: '
              + (str((elves[0].total_calories + elves[1].total_calories + elves[2].total_calories))))

    def build_calorie_array(self, calorie_string):
        calorie_array = calorie_string.split('\n\n')

        for (key, elf) in enumerate(calorie_array):
            calorie_array[key] = elf.split('\n')

        return calorie_array

    def find_elf_with_most_calories(self, elves):
        winner = None

        for elf in elves:
            if not winner:
                winner = elf
            else:
                if elf.total_calories > winner.total_calories:
                    winner = elf

        return winner

    def find_top_3_elves_with_most_calories(self, elves):
        elves.sort(key=lambda x: x.total_calories, reverse=True)

        return elves
