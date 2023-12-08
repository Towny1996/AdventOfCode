import string 
import re
import math

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

class PartTwo:
    def DoWork(self) -> int:
        input_file = open('input.txt', 'r')
        return self.CalcScratchCardCount(input_file.read().splitlines())

    def CalcScratchCardCount(self, lines: [string]) -> int:
        booklet = {}

        for line in lines:
            card_number = int(re.findall(r'\d+', line.split(':')[0])[0])
            matching_numbers = set(re.findall(r'\d+', line.split('|')[1])).intersection(set(re.findall(r'\d+', line.split('|')[0].split(':')[1])))
           
            booklet[card_number] = {'matches': len(matching_numbers), 'instances': (booklet.get(card_number, {}).get('instances', 0) + 1)}

            for index, amnt in enumerate(range(1, (len(matching_numbers) + 1))):
                index = ((index + 1) + card_number) 
                booklet[index] = { 'instances': (booklet.get(index, {}).get('instances', 0) + booklet[card_number]['instances']) }
            
        return sum([x['instances'] for x in booklet.values()])

print(PartOne().DoWork())
print(PartTwo().DoWork())
