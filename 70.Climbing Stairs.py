class Solution(object):
    def __init__(self):
        self.ways = 0
        self.save = {}

    def climbStairs(self, n):
        def climb(val):
            if val == 0:
                self.ways += 1
            else:
                for i in [1, 2]:
                    if val - i >= 0:
                        if val - i in self.save:
                            self.ways += self.save[val - i]
                        else:
                            climb(val - i)
                            self.save[val - i] = self.ways

        climb(n)
        return self.ways


# runtime: 6%; memory: 64%
# new solution: dynamic programming
class Solution2(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0] * 45
        dp[0] = 1
        dp[1] = 2
        i = 2
        while i < n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().climbStairs(2))
