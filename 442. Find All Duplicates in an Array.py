# solution 1: hacking solution. Sort first then return answer
# runtime: 70%; memory: 97%
class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        return [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i - 1] and (i == 1 or nums[i] != nums[i - 2])]


# solution 2: use tricky nums index position
# runtime: 74%; memory: 70%
class Solution2(object):
    def findDuplicates(self, nums):
        result = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution2().findDuplicates(nums))
