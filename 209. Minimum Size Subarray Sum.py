class Solution(object):
    def minSubArrayLen(self, s, nums):
        nums_len = len(nums)
        nums_sum = [0] * (nums_len+1)
        min_len = 0

        for i in range(1, nums_len+1):
            nums_sum[i] = nums_sum[i-1] + nums[i-1]
        print(nums_sum)
        for i in range(1, nums_len+1):
            if min_len == 0:
                if nums_sum[i] >= s:
                    min_len = i
            if nums_sum[i] - nums_sum[i-min_len] >= s:
                while nums_sum[i] - nums_sum[i-min_len] >= s:
                    min_len -= 1
                min_len += 1
            print(i, min_len)
        return min_len


nums = [1,2,3,4,5]
s = 11
print(Solution().minSubArrayLen(s, nums))