import regex as re
from functools import reduce


def GetInput():
    return open('Input.txt', 'r').read()

class PartOne():
    def DoWork(self) -> int:
        total_sum = 0
        sums = re.findall('mul\(([0-9]+,[0-9]+)\)', GetInput())
        for sum in sums:
            total_sum += reduce(lambda z, y: z * y, [int(x) for x in sum.split(',')])
        return total_sum

class PartTwo():
    def DoWork(self):
        total_sum = 0
        sums = re.findall('mul\(([0-9]+,[0-9]+)\)', ''.join(re.findall('(?:^|do\(\))(.*?)(?=don\'t\(\))', GetInput())))
        for sum in sums:
            total_sum += reduce(lambda z, y: z * y, [int(x) for x in sum.split(',')])
        return total_sum

print(PartOne().DoWork())
print(PartTwo().DoWork())