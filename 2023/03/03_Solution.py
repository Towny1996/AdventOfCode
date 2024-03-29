import string
import re
import math

class PartOne:
    special_chars = ['*', '&', '#', '/', '+', '$', '%', '@', '-', '=']

    def DoWork(self) -> int:
        input_file = open('input.txt', 'r')
        return self.GetSchematicSum(input_file.read().splitlines())

    def GetSchematicSum(self, lines: [string]) -> int:
        digit_locations = {}
        for row, line in enumerate(lines):
            digits = re.findall(r'\d+', line)
            indexes = [range(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]

            digit_locations[row] = [{'number': int(x), 'location': indexes[index]} for index, x in enumerate(digits)]

        close_nums = []

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char in self.special_chars:
                    close_nums_before = [x['number'] for x in digit_locations[row-1] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    close_nums_on = [x['number'] for x in digit_locations[row] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    close_nums_after = [x['number'] for x in digit_locations[row+1] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    
                    close_nums.append([*close_nums_before, *close_nums_on, *close_nums_after])

        return sum([sum(x) for x in close_nums])

class PartTwo:
    def DoWork(self):
        input_file = open('input.txt', 'r')
        return self.GetActualSchematicSum(input_file.read().splitlines())

    def GetActualSchematicSum(self, lines: [string]) -> int:
        sum_tracker = 0
        digit_locations = {}
        for row, line in enumerate(lines):
            digits = re.findall(r'\d+', line)
            indexes = [range(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
                                                                                                               
            digit_locations[row] = [{'number': int(x), 'location': indexes[index]} for index, x in enumerate(digits)]

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "*":
                    close_nums = []
                    close_nums_before = [x['number'] for x in digit_locations[row-1] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    close_nums_on = [x['number'] for x in digit_locations[row] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    close_nums_after = [x['number'] for x in digit_locations[row+1] if (col - 1) in x['location'] or col in x['location'] or (col + 1) in x['location']]
                    
                    close_nums.append([*close_nums_before, *close_nums_on, *close_nums_after])

                    if(len(close_nums[0]) == 2):
                        sum_tracker += math.prod([int(x) for x in close_nums[0]])

        return sum_tracker


print(PartOne().DoWork())
print(PartTwo().DoWork())
