class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        return [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i-1] and (i == 1 or nums[i] != nums[i-2])]