import math


"""solution 1"""
# class Solution(object):
#     def numSquares(self, n):
#         dp = [i for i in range(n+1)]
#
#         for i in range(1, n+1):
#             for j in range(1, int(math.sqrt(i))+1):
#                 dp[i] = min(dp[i], dp[i-j*j]+1)
#
#         print(dp)
#         return dp[n]


"""time not enough"""
# class Solution(object):
#     def __init__(self):
#         self.record = {0: 0, 1: 1}
#
#     def numSquares(self, n):
#         for i in range(1, int(math.sqrt(n)) + 1):
#             if self.record.get(n-i*i) is None:
#                 self.numSquares(n - i * i)
#             self.record[n] = self.record[n-i*i] + 1 if n not in self.record else min(self.record[n-i*i] + 1, self.record[n])
#         return self.record[n]


print(Solution().numSquares(13))
