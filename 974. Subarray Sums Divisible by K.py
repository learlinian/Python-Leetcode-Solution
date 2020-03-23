import collections


"""inefficient solution"""
"""
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        A_len = len(A)
        dp = [0] * (A_len+1)
        count = 0

        for i in range(1, A_len+1):
            dp[i] = dp[i-1] + A[i-1]

        for i in range(1, A_len+1):
            val = dp[i]
            if val >= S:
                diff = val-S
                count += dp[:i].count(diff)

        return count
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        A_len = len(A)
        dp = [0] * (A_len+1)
        count = 0

        for i in range(1, A_len+1):
            dp[i] = (dp[i-1] + A[i-1]) % K

        counts = collections.Counter(dp)
        for item in counts.values():
            count += (item-1)*item/2

        return count


A = [4,5,0,-2,-3,1]
K = 5
print(Solution().subarraysDivByK(A, K))
