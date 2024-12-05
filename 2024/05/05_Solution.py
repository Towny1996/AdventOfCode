def GetInput() -> ({}, []):
    rules = {}
    instructions = []
    processing_instructions = False
    for i in open('Input.txt').readlines():
        i = i.strip()
        if not i:
            processing_instructions = True
            continue
        if not processing_instructions:
            rule = i.split('|')
            if int(rule[0]) in rules:
                rules[int(rule[0])].append(int(rule[1]))
            else:
                rules.update({ int(rule[0]): [int(rule[1])]})
            continue
        instructions.append([int(x) for x in i.split(',')])
    return rules, instructions

class PartOne():
    def DowWork(self):
        input = GetInput()
        count = 0
        for instruction in input[1]:
            is_valid = True
            for index, val in enumerate(instruction):
                if val in input[0] and set(input[0][val]) & set(instruction[:index]):
                    is_valid = False

            if is_valid:
                count += instruction[len(instruction) // 2]
        return count

class PartTwo():
    count = 0
    input = ({}, [])

    def __init__(self):
        self.input = GetInput()

    def DoWork(self):
        for instruction in self.input[1]:
            is_valid_instruction = self.CheckValidInstruction(instruction)
            if not is_valid_instruction[0]:
                self.ReorderInvalidInstruction(instruction, is_valid_instruction[1])

        return self.count

    def CheckValidInstruction(self, instruction: []):
        for index, val in enumerate(instruction):
            if val in self.input[0] and set(self.input[0][val]) & set(instruction[:index]):
                return False, index

        return True, 0

    def ReorderInvalidInstruction(self, instruction: [], index: int):
        is_valid_instruction = self.CheckValidInstruction(self.RearrangeArray(instruction, index))
        if not is_valid_instruction[0]:
            self.ReorderInvalidInstruction(instruction, is_valid_instruction[1])
        else:
            self.count += instruction[len(instruction) // 2]

    def RearrangeArray(self, array: [], index: int) -> []:
        if index > 0:
            array[index - 1], array[index] = array[index], array[index - 1]
        return array

print(PartOne().DowWork())
print(PartTwo().DoWork())