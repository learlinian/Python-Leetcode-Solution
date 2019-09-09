class Solution(object):
    def __init__(self):
        self.combination = 0

    def numRollsToTarget(self, d, f, target):
        MOD = 10 ** 9 + 7
        if d == 1:
            if target <= f:
                self.combination += 1
                self.combination %= MOD
        else:
            for i in range(1, d):
                for val in range(1, f+1):
                    self.numRollsToTarget(d-i, f, target-val)

        return self.combination


class Solution2(object):
    def numRollsToTarget(self, d, f, target):
        mod = 10 ** 9 + 7
        memo = {}

        def helper(dd, tt):
            if tt <= 0: return 0
            if dd * f < tt: return 0
            if dd == 1 and 1 <= tt <= f: return 1
            if (dd, tt) in memo: return memo[(dd, tt)]

            res = 0
            for i in range(1, f + 1):
                res += helper(dd - 1, tt - i)
                res %= mod

            memo[(dd, tt)] = res
            return res

        return helper(d, target) % mod


if __name__ == '__main__':
    d = 30
    f = 30
    target = 500

    S = Solution2()
    print(S.numRollsToTarget(d, f, target))
