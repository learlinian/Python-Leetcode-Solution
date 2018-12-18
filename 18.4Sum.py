class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()     # sort the array first
        result = []
        for i in range(len(nums) - 3):      # the first index must less than list length minus 4
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1                       # initialize the second index based on first index
            while j <= len(nums) - 3:
                k = j + 1                   # initialize the third index based on second index
                r = len(nums) - 1           # initialize the 4th index to rear
                while k < r:
                    temp = nums[i] + nums[j] + nums[k] + nums[r]
                    if temp == target:
                        result.append([nums[i], nums[j], nums[k], nums[r]])
                        while nums[k] == nums[k+1]:
                            k += 1
                        while nums[r] == nums[r-1]:
                            r -= 1
                        k += 1
                        r -= 1
                    elif temp < target:
                        k += 1
                    else:
                        r -= 1
                j += 1
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
