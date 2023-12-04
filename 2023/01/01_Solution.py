import string

class PartOne:
    def DoWork(self):
        input_file = open('Input.txt', 'r')
        return self.CalcCalibrationValues(input_file.readlines())

    def CalcCalibrationValues(self, lines: [string]) -> int:
        lineValues = []
        for i in lines:
            ints = [str(x) for x in i if x.isdigit()]
            if(any(ints)): lineValues.append(int(ints[0] + '' + ints[-1]))

        return sum(lineValues)

class PartTwo:
    number_mapper_dict = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

    def DoWork(self):
        input_file = open('Input.txt', 'r')
        return self.CalcCalibrationValues(input_file.readlines())

    def CalcCalibrationValues(self, lines: [string]) -> int:
        lineValues = []
        for l in lines:
            ints = self.RecursiveTextDigitParse(l, 0, 1, [])
            if(any(ints)): lineValues.append(int(ints[0] + '' + ints[-1]))
            
        return sum(lineValues)

    def RecursiveTextDigitParse(self, text: string, start: int, end: int, lineints: []) -> []:
        for index, char in enumerate(text[start:end]):
            if(char.isdigit()):
                lineints.append(char)
                start = ((index + 1) + start)
            else:
                for key in self.number_mapper_dict:
                    if text[start:end].find(key) != -1:
                        lineints.append(str(self.number_mapper_dict[key]))
                        start = (index + (end - 1))

        if(end == len(text)): return lineints
        else: return self.RecursiveTextDigitParse(text, start, (end + 1), lineints)


print(PartTwo().DoWork())
