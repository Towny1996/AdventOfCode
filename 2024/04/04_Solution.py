def GetInput():
    input = open('Input.txt', 'r').readlines()
    matrix = [[0 for x in range(len(input))] for y in range(len(input[0]) - 1)]
    for lineindex, line in enumerate(input):
        for charindex, char in enumerate(line.strip()):
            matrix[lineindex][charindex] = char
    return matrix

# BEGIN: spaghetti #
class PartOne:
    def DoWork(self):
        input = GetInput()
        organised_sets = {}
        count = 0

        for i1, line in enumerate(input):
            for i2, row in enumerate(line):
                organised_sets[f'{i1}{i2}'] = {'right': [], 'down': [], 'left_down': [], 'right_down': []}
                if (i2 + 3) <= len(line) - 1:
                    organised_sets[f'{i1}{i2}'].update({ 'right': [input[i1][i2], input[i1][i2 + 1], input[i1][i2 + 2], input[i1][i2 + 3]] })
                if (i1 + 3) <= len(line) - 1:
                    organised_sets[f'{i1}{i2}'].update({ 'down': [input[i1][i2], input[i1 + 1][i2], input[i1 + 2][i2], input[i1 + 3][i2]] })
                if ((i1 + 3) <= len(line) - 1) and (i2 - 3) >= 0:
                    organised_sets[f'{i1}{i2}'].update({ 'left_down': [input[i1][i2], input[i1 + 1][i2 - 1], input[i1 + 2][i2 - 2], input[i1 + 3][i2 - 3]]})
                if ((i1 + 3) <= len(line) - 1) and (i2 + 3) <= len(line) - 1:
                    organised_sets[f'{i1}{i2}'].update({ 'right_down': [input[i1][i2], input[i1 + 1][i2 + 1], input[i1 + 2][i2 + 2], input[i1 + 3][i2 + 3]]})

                for key, value in organised_sets[f'{i1}{i2}'].items():
                    match value:
                        case ['S', 'A', 'M', 'X']:
                            count += 1
                            continue
                        case ['X', 'M', 'A', 'S']:
                            count += 1
                            continue
        return count

# BEGIN: spaghetti #
class PartTwo:
    def DoWork(self):
        input = GetInput()
        organised_sets = {}
        count = 0

        for i1, line in enumerate(input):
            for i2, row in enumerate(line):
                organised_sets[f'{i1}-{i2}'] = {'left_down': [], 'right_down': []}
                if ((i1 + 2) <= len(line) - 1) and (i2 - 2) >= 0:
                    organised_sets[f'{i1}-{i2}'].update({ 'left_down': [input[i1][i2], input[i1 + 1][i2 - 1], input[i1 + 2][i2 - 2]]})
                if ((i1 + 2) <= len(line) - 1) and (i2 + 2) <= len(line) - 1:
                    organised_sets[f'{i1}-{i2}'].update({ 'right_down': [input[i1][i2], input[i1 + 1][i2 + 1], input[i1 + 2][i2 + 2]]})

        for key,value in organised_sets.items():
            for sub_key, sub_value in value.items():
                if sub_key == 'right_down' and (sub_value == ['M', 'A', 'S'] or sub_value == ['S', 'A', 'M']):
                    if f"{key.split('-')[0]}-{int(key.split('-')[1]) + 2}" in organised_sets:
                        check_x_partner = organised_sets[f"{key.split('-')[0]}-{int(key.split('-')[1]) + 2}"]['left_down']
                        if check_x_partner == ['M', 'A', 'S'] or check_x_partner == ['S', 'A', 'M']:
                            count += 1

        return count

print(PartOne().DoWork())
print(PartTwo().DoWork())