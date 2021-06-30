# time complexity O(n!)
# class Solution(object):
#     def __init__(self):
#         self.cache = {(1, 0): 1, (2, 0): 1, (2, 1): 1}
#
#     def kInversePairs(self, n, k):
#         if (n, k) in self.cache:
#             return self.cache[(n, k)]
#         if (n - 1) * n / 2 < k:
#             return 0
#         ans = 0
#         for i in range(min(k, n-1), -1, -1):
#             result = self.kInversePairs(n - 1, k - i)
#             if result == 0:
#                 break
#             ans = (ans + result) % 1000000007
#         self.cache[(n, k)] = ans % 1000000007
#         return ans


# time complexity: O(n)
# class Solution(object):
#     def kInversePairs(self, n, k):
#         if k == 0:
#             return 1
#         if n == 1 and k > 0:
#             return 0
#         first_dp = [0] * (k + 1)
#         first_dp[0] = 1
#         second_dp = [0] * (k + 1)
#         for i in range(1, n):
#             for j in range(k+1):
#                 second_dp[j] = sum(first_dp[max(0, j - i):j + 1]) % 1000000007
#             first_dp = second_dp.copy()
#         return second_dp[-1]

# optimized dp version
class Solution(object):
    def kInversePairs(self, n, k):
        if k == 0:
            return 1
        if n == 1 and k > 0:
            return 0
        first_dp = [0] * (k + 1)
        first_dp[0] = 1
        second_dp = [0] * (k + 1)
        for i in range(1, n):
            for j in range(k+1):
                if j == 0:
                    second_dp[j] = 1
                    continue
                diff = 0
                if j - i - 1 >= 0:
                    diff = first_dp[j - i - 1]
                second_dp[j] = (second_dp[j-1] + first_dp[j] - diff) % 1000000007
            first_dp = second_dp.copy()
        return second_dp[-1]


if __name__ == '__main__':
    print(Solution().kInversePairs(3, 1))
