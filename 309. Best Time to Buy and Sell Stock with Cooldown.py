# solution: simple dp; need to trace back n times. Complexity: O(n^2)
# runtime: 8%; memory: 10%
class Solution(object):
    def maxProfit(self, prices):
        # [buy, hold, sell]
        dp = []
        for _ in range(len(prices)):
            dp.append([0, 0, 0])

        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = max(dp[i - 1])
            max_val = 0
            for j in range(i):
                max_val = max(max_val, prices[i] - prices[j] + dp[j][0])
            dp[i][2] = max_val
        return max(dp[-1])


# solution: more intelligent dp; store prev min every time. Complexity: O(n)
# runtime: 46%; memory: 15%
class Solution2(object):
    def maxProfit(self, prices):
        # [buy, hold, sell]
        dp = [0, 0, 0]
        for _ in range(len(prices)):
            dp.append([0, 0, 0])

        prev_max = dp[0][0] - prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = max(dp[i - 1])
            dp[i][2] = prices[i] + prev_max
            prev_max = max(prev_max, dp[i][0] - prices[i])
        return max(dp[-1])


# solution: state machine; actually the simplified version of solution 2. time complexity: O(n)
# runtime: 95%; memory: 88%
class Solution3(object):
    def maxProfit(self, prices):
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Alternative: the calculation is done in parallel.
            # Therefore no need to keep temporary variables
            # sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)


if __name__ == '__main__':
    # prices = [1, 4, 2]
    # prices = [1,2,3,0]
    # prices = [4, 1, 2]
    prices = [6, 1, 3, 2, 4, 7]
    print(Solution2().maxProfit(prices))
