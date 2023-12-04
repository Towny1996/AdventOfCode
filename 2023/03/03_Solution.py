import string
import re

class PartOne:
    special_chars = ['*', '&', '#', '/', '+', '$', '%', '@', '=']
    def DoWork(self) -> int:
        input_file = open('input.txt', 'r')
        return self.GetSchematicSum(input_file.read().splitlines())

    def GetSchematicSum(self, lines: [string]) -> int:
        digit_locations = {}
        for row, line in enumerate(lines):
            digits = re.findall(r'\d+', line)
            indexes = [range(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
            digit_locations[row] = { 'numbers': digits, 'locations': indexes }

        close_nums = []

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char in self.special_chars:
                    close_nums_before = list(set([int(digit_locations[row-1]['numbers'][digit_locations[row-1]['locations'].index(x)]) for x in digit_locations[row-1]['locations'] for o in list(range(col-1, col+2)) if o in x]))
                    close_nums_on = list(set([int(digit_locations[row]['numbers'][digit_locations[row]['locations'].index(x)]) for x in digit_locations[row]['locations'] for o in list(range(col-1, col+2)) if o in x]))
                    close_nums_after = list(set([int(digit_locations[row+1]['numbers'][digit_locations[row+1]['locations'].index(x)]) for x in digit_locations[row+1]['locations'] for o in list(range(col-1, col+2)) if o in x]))

                    close_nums.append([*close_nums_before, *close_nums_on, *close_nums_after])
                    
        return (sum([sum(x) for x in close_nums if len(x) > 0]))


print(PartOne().DoWork())