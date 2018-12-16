'''Given an array nums of n integers, are there elements a, b, c
in nums such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        length = len(nums)-1
        nums.sort()

        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # print(i)
            j = i+1
            k = length
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if not temp:
                    solution.append([nums[i], nums[j], nums[k]])
                    # print('i = ' + str(i) + ' j = ' + str(j) + ' k = ' + str(k))
                    while nums[j] == nums[j+1] and j < k:
                        j += 1
                    while nums[k] == nums[k-1] and j < k:
                        k -= 1
                    j += 1
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        return solution


nums = [-1, 0, 1, 2, -1, -4]
x = Solution()
print(x.threeSum(nums))
