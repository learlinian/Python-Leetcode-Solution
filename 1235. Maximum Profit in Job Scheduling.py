# Solution: dynamic programming
# runtime: 5%; memory: 17%


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(endTime, startTime, profit))
        length = jobs[-1][0]
        dp = [0] * (length + 1)

        for end_time, start_time, p in jobs:
            i = end_time
            while i > 0 and dp[i] == 0:
                i -= 1
            for k in range(i, end_time + 1):
                dp[k] = dp[i]
            if start_time >= i:
                dp[end_time] = dp[i] + p
                continue
            dp[end_time] = max(dp[start_time] + p, dp[end_time])
        return dp[-1]


if __name__ == '__main__':
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(Solution().jobScheduling(startTime, endTime, profit))
