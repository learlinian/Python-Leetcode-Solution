"""
It is natural to consider an array W of each interval's sum, where each interval is the given length k.
To create W, we can either use prefix sums, or manage the sum of the interval as a window slides along the array.

From there, we approach the reduced problem: Given some array W and an integer k, what is the lexicographically smallest
tuple of indices (i, j, l) with i + k <= j and j + k <= l that maximizes W[i] + W[j] + W[l]?
"""


# runtime: 76%; memory: 88%

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        W = []  # array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                W.append(curr_sum)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, l
        return ans


if __name__ == '__main__':
    # nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    # k = 2
    nums = [4, 5, 10, 6, 11, 17, 4, 11, 1, 3]
    k = 1
    print(Solution().maxSumOfThreeSubarrays(nums, k))
