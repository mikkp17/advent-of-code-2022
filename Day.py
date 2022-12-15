import re


class Day:
    def __init__(self):
        pass

    def print(self, solution, second_solution):
        self.initialize()
        self.print_solution(solution)
        self.print_second_solution(second_solution)
        self.cleanup()

    def initialize(self):
        print()
        print('Advent of Code 2022!')
        print()
        print('Running solution for' + self.sentence_case() + '!')
        print('-----------------------------------------')
        print()

        return

    def print_solution(self, solution):
        pass

    def print_second_solution(self, solution):
        pass

    def cleanup(self):
        print()
        print('-----------------------------------------')
        print()

    def run(self):
        pass

    def read_file(self, file_name):
        file = open(file_name, 'r')
        data = file.read()
        data = data.replace('\r', '')

        return data

    def sentence_case(self):
        string = str(self.__class__.__name__)
        if string != '':
            result = re.sub('([A-Z])', r' \1', string)
            return result.lower()
        return
