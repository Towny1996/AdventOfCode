import string
import re

class PartOne:

    def DoWork(self):
        input_file = open('Input.txt', 'r')
        return self.CalcCalibrationValues(input_file.readlines())

    def CalcCalibrationValues(self, lines: list[string]) -> int:
        lineValues = []
        for i in lines:
            ints = []
            for c in i:
                if c.isdigit():
                    ints.append(c)
                        
            if(len(ints) == 0): continue

            lineValues.append(int(ints[0] + '' + ints[-1]))

        return sum(lineValues)

class PartTwo:
    number_mapper_dict = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine' }

    def DoWork(self):
        input_file = open('Input.txt', 'r')
        return self.CalcCalibrationValues(input_file.readlines())

    def CalcCalibrationValues(self, lines: list[string]) -> int:


print(PartOne().DoWork())
