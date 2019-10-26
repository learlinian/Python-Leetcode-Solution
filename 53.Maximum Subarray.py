class Solution(object):
    def maxSubArray(self, nums):
        max_sum = 0
        current_sum = 0
        for item in nums:
            current_sum += item
            if current_sum < 0:
                current_sum = 0
            if current_sum > max_sum:
                max_sum = current_sum

        if max_sum == 0:
            max_sum = max(nums)
        return max_sum


if __name__ == '__main__':
    a = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(a))
