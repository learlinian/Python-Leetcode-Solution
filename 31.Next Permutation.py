# this problem is about in-place replacement

class Solution(object):
    def nextPermutation(self, nums):
        temp = list(nums)
        temp = sorted(temp)
        temp.reverse()
        if nums == temp:
            nums.reverse()
            return False

        nums_len = len(nums)
        for i in range(nums_len - 2, -1, -1):
            # print(nums)
            if nums[i] < nums[i + 1]:
                for j in range(i + 1, nums_len):
                    val = nums[i] + 1
                    while val not in nums[i + 1:]:
                        val += 1
                    j = nums[i + 1:].index(val) + i + 1
                    nums[i], nums[j] = nums[j], nums[i]
                    print(nums, i)
                    nums[i + 1:] = sorted(nums[i + 1:])
                    return True


if __name__ == '__main__':
    arr = [1, 3, 2]
    print(Solution().nextPermutation(arr))
