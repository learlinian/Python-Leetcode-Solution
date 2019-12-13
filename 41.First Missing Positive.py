class Solution(object):
    def firstMissingPositive(self, nums):
        positive_min = 0
        nums.sort()
        if not nums or nums[0] > 1:
            return 1

        for i in range(len(nums)):
            if nums[i] >= 1:
                if i-1 >= 0 and nums[i-1] + 1 < nums[i] and nums[i] > 1:
                    return positive_min+1
                positive_min = nums[i]
        return max(positive_min, 0) + 1


if __name__ == '__main__':
    nums = [-1, 3, 4, 1]
    print(Solution().firstMissingPositive(nums))
