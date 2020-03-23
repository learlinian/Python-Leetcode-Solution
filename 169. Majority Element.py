class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        max_count, key = 0, -1
        for num in nums:
            if counts.get(num) is None:
                counts[num] = 1
            else:
                counts[num] += 1
            if counts[num] > max_count:
                max_count = counts[num]
                key = num
        return key


nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
