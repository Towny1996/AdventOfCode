from part_one import PartOne
import sys

sys.setrecursionlimit(10000)

def GetInput():
    return open('Input.txt', 'r').readlines()

print(PartOne(GetInput()).DoWork())