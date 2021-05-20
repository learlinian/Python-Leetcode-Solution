from collections import defaultdict

class Solution:
    def largestNumber(self, cost, target):
        memo = defaultdict(lambda: float('-inf'))
        table = {}
        for i, c in enumerate(cost):
            table[c] = i

        def dp(target):
            if target < 0:
                return float('-inf')
            if target == 0:
                return 0
            if target not in memo:
                for c in table:
                    d = table[c] + 1
                    memo[target] = max(memo[target], 10 * dp(target - c) + d)
            return memo[target]

        return str(max(0, dp(target)))


if __name__ == '__main__':
    cost = [70,84,55,63,74,44,27,76,34]
    target = 659
    print(Solution().largestNumber(cost, target))