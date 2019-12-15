class Solution(object):
    def canJump(self, nums):
        nums_len = len(nums)
        result_arr = [False] * nums_len
        result_arr[0] = True
        current_true_i = 0

        for i in range(nums_len):
            # print(result_arr)
            if nums[i] >= 1 and result_arr[i]:
                if i+nums[i] > current_true_i:
                    result_arr[current_true_i:i+nums[i]+1] = [True] * (i+nums[i]+1-current_true_i)
                    current_true_i = i+nums[i]
        return result_arr[-1]


if __name__ == '__main__':
    # nums = [0]
    # nums = [3,2,1,0,4]
    nums = [0, 2, 3]
    print(Solution().canJump(nums))
