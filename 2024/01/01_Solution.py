class Utils:
    def GetOrganisedInput(self):
        input_file = open("Input.txt", 'r')

        list_one = []
        list_two = []

        for i in input_file.readlines():
            list_one.append(int(i.split()[0]))
            list_two.append(int(i.split()[1]))

        return list_one, list_two

class PartOne:
    def DoWork(self):
        list_one, list_two = Utils().GetOrganisedInput()
        list_one.sort()
        list_two.sort()

        return self.CalcDistance(list_one, list_two)


    def CalcDistance(self, list_one: [int], list_two: [int]) -> int:
        sum = 0
        for index, item in enumerate(list_one):
            sum += abs(item - list_two[index])

        return sum

class PartTwo:
    def DoWork(self):
        list_one, list_two = Utils().GetOrganisedInput()
        return self.CalcSimilarity(list_one, list_two)

    def CalcSimilarity(self, list_one: [int], list_two: [int]) -> int:
        similarity_score = 0
        for item in list_one:
            similarity_score += item * list_two.count(item)

        return similarity_score


print(PartOne().DoWork())
print(PartTwo().DoWork())
