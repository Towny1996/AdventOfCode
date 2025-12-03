import heapq

def GetInput():
    return open('Input.txt', 'r').readlines()

class Solution():
    def DoWorK(self, wanted) -> int:
        valid_voltages = []
        for line in [x.rstrip() for x in GetInput()]:
            nums = [int(line[i:i + 1]) for i in range(0, len(line), 1)]
            valid_voltages.append(self.GetHighestSequence(max(nums), nums, '', wanted, 1))

        return sum([int(x) for x in valid_voltages])

    def GetHighestSequence(self, highest, nums, found, wanted, index) -> []:
        if abs(nums.index(highest) - (len(nums) - 1)) < ((wanted - 1) - (len(found) - 1)):
            return self.GetHighestSequence(heapq.nlargest(index + 1, nums)[index], nums, found, wanted, index + 1)

        found = found + str(highest)
        if len(found) - 1 == wanted:
            return found

        return self.GetHighestSequence(max(nums[nums.index(highest) + 1:]), nums[nums.index(highest) + 1:], found, wanted, 1)


print(Solution().DoWorK(1))
print(Solution().DoWorK(11))