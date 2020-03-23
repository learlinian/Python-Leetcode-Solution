class Solution(object):
    def removeDuplicates(self, nums):
        nums_len = len(nums)
        if nums_len <= 2:
            return nums_len

        for i in range(nums_len-3, -1, -1):
            if nums[i] == nums[i+2]:
                del nums[i]

        return len(nums)


# nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))
