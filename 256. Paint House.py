# runtime: 12%; memory: 80%

class Solution(object):
    def minCost(self, costs):
        prev_dp = costs[0]
        dp = [0, 0, 0]
        for i in range(1, len(costs)):
            for j in range(3):
                dp[j] = min([prev_dp[k] for k in range(3) if k != j]) + costs[i][j]
            prev_dp = dp.copy()
        return min(prev_dp)


if __name__ == '__main__':
    costs = [[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]]
    print(Solution().minCost(costs))
