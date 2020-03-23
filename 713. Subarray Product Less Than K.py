class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


nums = [10, 5, 2, 6]
# nums = [1, 1, 1]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))