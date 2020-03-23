class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k <= 0:
            return []
        result = [max(nums[:k])]
        for i in range(1, len(nums)-k+1):
            if result[i-1] != nums[i-1]:
                result.append(max(result[i-1], nums[i+k-1]))
            else:
                result.append(max(nums[i:i+k]))
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
