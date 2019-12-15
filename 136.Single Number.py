class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))
