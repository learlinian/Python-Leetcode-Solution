class Solution(object):
    def sumSubarrayMins(self, A):
        A_len = len(A)
        left = [-1] * A_len
        right = [A_len] * A_len
        stack = []
        total_sum = 0

        for i in range(A_len):
            while stack and A[stack[-1]] >= A[i]:
                prev_index = stack.pop()
                right[prev_index] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        print(left, right)
        for i in range(A_len):
            total_sum = (total_sum + A[i] * (i - left[i]) * (right[i]-i)) % (10**9 + 7)
        return total_sum


A = [48,87,27]
print(Solution().sumSubarrayMins(A))