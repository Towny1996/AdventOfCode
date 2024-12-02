class Report(object):
    levels = []
    direction = string = ''

    def __init__(self, levels):
        self.levels = levels
        self.direction = self.GetDirection(self.levels[0], self.levels[1])

    ## Preserve method for part_one ##
    def CheckValidReport(self) -> bool:
        for index, level in enumerate(self.levels):
            if index >= (len(self.levels) - 1):
                continue

            if not self.GetIsValidStep(level, self.levels[index + 1]):
                return False

        return True

    ## Altered bruteforce for part_two ##
    def CheckValidReport_Task_Two(self, index_popped: int, array: [int]) -> bool:
        self.direction = self.GetDirection(array[0], array[1])
        for index, level in enumerate(array):
            if index >= (len(array) - 1):
                continue

            if not self.GetIsValidStep(level, array[index + 1]):
                if index_popped >= (len(array) + 1):
                    return False

                new_arr = self.levels.copy()
                new_arr.pop(index_popped)
                return self.CheckValidReport_Task_Two(index_popped + 1, new_arr)

        return True

    def GetDirection(self, start: int, end: int) -> string:
        return 'up' if start < end else 'down'

    def GetIsValidStep(self, start: int, end: int) -> bool:
        if (abs(start - end) < 1 or abs(start - end) > 3) or self.GetDirection(start, end) is not self.direction:
            return False
        return True