def GetInput():
    return open('Input.txt', 'r').read().split(',')

def Part_One():
    found_invalid = []

    for check in GetInput():
        for num in map(str, list(range(int(check.split('-')[0]), int(check.split('-')[1]) + 1))):
            if (len(str(num)) % 2) > 0:
                continue

            half = str(num[0:int(len(str(num)) / 2 )])
            if half + "" + half == str(num):
                found_invalid.append(num)

    return sum([int(x) for x in found_invalid])

def Part_Two():
    found_invalid = []

    for check in GetInput():
        for num in map(str, list(range(int(check.split('-')[0]), int(check.split('-')[1]) + 1))):
            for index, val in enumerate(num):
                if num.count(num[0:index + 1]) > 1:
                    if num[0:index + 1] * num.count(num[0:index + 1]) == num:
                        found_invalid.append(num)
                        break

    return sum([int(x) for x in found_invalid])

print(Part_One())
print(Part_Two())
