class Solution(object):
    def maxProduct(self, nums):
        res, mx, mn = -float('inf'), 1, 1
        for n in nums:
            if n < 0: mx, mn = mn, mx
            mx = max(mx * n, n)
            mn = min(mn * n, n)
            res = max(res, mx)
            print(mx, mn, res)
        return res


nums = [2,-5,0,-4,3]
print(Solution().maxProduct(nums))
