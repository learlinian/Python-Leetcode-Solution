# solution: iterative dp
# runtime: 93%; memory: 87%

class Solution(object):
    def maxProfit(self, k, prices):
        prices_len = len(prices)
        if k >= prices_len // 2:
            return sum([v - u for u, v in zip(prices, prices[1:]) if v - u >= 0])

        profits = [0] * prices_len

        for i in range(k):
            max_profits = -float('inf')
            new_profits = [0] * prices_len
            for j in range(1, prices_len):
                max_profits = max(max_profits, profits[j - 1] - prices[j - 1])
                new_profits[j] = max(new_profits[j - 1], prices[j] + max_profits)
            profits = list(new_profits)

        return max(profits)


if __name__ == '__main__':
    # prices = [3,2,6,5,0,3]
    prices = [5, 11, 3, 50, 60, 90]
    print(Solution().maxProfit(2, prices))
