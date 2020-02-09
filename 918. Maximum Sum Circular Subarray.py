class Solution(object):
    def maxSubarraySumCircular(self, A):
        A_len = len(A)
        if A_len == 0:
            return 0

        min_sum = max_sum = current_max_sum = current_min_sum = 0

        for i in range(A_len):
            current_max_sum += A[i]
            current_min_sum += A[i]

            if current_max_sum < 0:
                current_max_sum = 0
            else:
                max_sum = max(max_sum, current_max_sum)

            if current_min_sum > 0:
                current_min_sum = 0
            else:
                min_sum = min(min_sum, current_min_sum)

            # print(min_sum, max_sum, current_max_sum, current_min_sum)
        if max_sum == 0:
            return max(A)

        return max(max_sum, sum(A)-min_sum)


# A = [-10,-7,9,-7,6,9,-9,-4,-8,-5]
A = [-2,-3,-1]
print(Solution().maxSubarraySumCircular(A))
