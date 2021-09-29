# run time: 41%, memory: 20%

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        length = len(nums)
        sums = [0] * length
        sums[0] = nums[0]
        sum_dict = {0: 0}
        max_len = 0

        for i in range(1, length):
            sums[i] = (sums[i - 1] + nums[i])

        for i in range(length):
            diff = sums[i] - k
            if diff in sum_dict:
                current_length = i - sum_dict[diff] + 1 if diff == 0 else i - sum_dict[diff]
                max_len = max(max_len, current_length)
            if sums[i] not in sum_dict:
                sum_dict[sums[i]] = i

        return max_len


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    print(Solution().maxSubArrayLen(nums, k))
