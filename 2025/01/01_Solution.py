import math

def GetInput():
    return open('Input.txt', 'r').readlines()

def Solution(count_passes):
    input = GetInput()
    dial = 50
    zeros = 0

    for i in input:
        direction = i[0]
        turns = int(i[1:])

        if turns > 99:
            if count_passes:
                zeros = zeros + math.floor((turns/100))
            turns = turns % 100

        match direction:
            case 'R':
                if dial + turns > 99:
                    dial = (dial + turns) - 100
                    if count_passes and dial != 0:
                        zeros = zeros + 1
                else:
                    dial = dial + turns
            case 'L':
                if dial - turns < 0:
                    if count_passes and dial != 0:
                        zeros = zeros + 1
                    dial = 100 - abs(dial - turns)

                else:
                    dial = dial - turns

        if dial == 0:
            zeros = zeros + 1

    return zeros

print(Solution(False))
print(Solution(True))