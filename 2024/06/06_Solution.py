from part_one import PartOne
from part_two import PartTwo

import sys

sys.setrecursionlimit(10000)

def GetInput():
    return open('Input.txt', 'r').readlines()

print(PartOne(GetInput()).DoWork())
print(PartTwo(GetInput()).DoWork())