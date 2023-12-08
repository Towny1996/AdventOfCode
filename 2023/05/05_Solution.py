import string
import re

class PartOne:
    almanac = {}

    def DoWork(self) -> int:
        input_file = open('input.txt', 'r')
        return self.GetLowestLocation(input_file.read().splitlines())
    
    def GetLowestLocation(self, lines: [string]) -> int:
        seeds = re.findall(r'\d+', lines[0])

        current_index = 0
        for line in lines[1:]:
            if not line: continue

            if(len(re.findall('([a-z]*[-]{1}[a-z]*[-]{1}[a-z]*)', line)) > 0):
                current_index = current_index + 1
                continue

            digits = re.findall(r'\d+', line)
            if len(digits) == 0: continue
            
            if current_index in self.almanac: self.almanac[current_index].append([[int(digits[0]), (int(digits[0]) + int(digits[2])) - 1], [int(digits[1]), (int(digits[1]) + int(digits[2])) - 1]])
            else: self.almanac[current_index] = [[[int(digits[0]), (int(digits[0]) + int(digits[2])) - 1], [int(digits[1]), (int(digits[1]) + int(digits[2])) - 1]]]

        seed_locations = []
        for seed in seeds:
            seed_locations.append(self.GetDestination(int(seed), 1))

        return min(seed_locations)

    def GetDestination(self, seed: int, index: int) -> int:
        if index not in self.almanac: return seed

        for ranges in self.almanac[index]:
            if ranges[1][0] <= seed <= ranges[1][1]:
                destination = ranges[0][0] + (seed - ranges[1][0])
                return self.GetDestination(destination, index + 1)

        return self.GetDestination(seed, index + 1)
    
print(PartOne().DoWork())