import string 
import re

class PartOne:
    def DoWork(self) -> int:
        input_file = open('input.txt', 'r')
        return self.CalcScratchPoints(input_file.read().splitlines())

    def CalcScratchPoints(self, lines: [string]) -> int:
        points = []
        for line in lines:
            similar_numbers = set(re.findall(r'\d+', line.split('|')[1])).intersection(set(re.findall(r'\d+', line.split('|')[0].split(':')[1])))

            if not any(similar_numbers): continue

            geometric_progression_formula = pow(2, (len(similar_numbers) - 1))
            points.append(geometric_progression_formula)

        return sum(points)

print(PartOne().DoWork())