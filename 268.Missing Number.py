class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        if nums[0] > 0:
            return 0
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] > nums[i-1] + 1:
                return nums[i-1] + 1

        return nums[-1] + 1


if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(arr))
