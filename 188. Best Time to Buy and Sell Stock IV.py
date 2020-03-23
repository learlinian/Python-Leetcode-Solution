class Solution(object):
    def maxProfit(self, k, prices):
        prices_len = len(prices)
        if k >= prices_len // 2:
            return sum([v - u for u, v in zip(prices, prices[1:]) if v - u >= 0] or [0])

        profits_prev = [0] * prices_len
        profits = [0] * prices_len

        for i in range(k):
            max_profits_prev = -float('inf')
            profits = [0] * prices_len
            for j in range(1, prices_len):
                max_profits_prev = max(max_profits_prev, profits_prev[j-1]-prices[j-1])
                profits[j] = max(profits[j-1], prices[j] + max_profits_prev)
            print(profits_prev, profits)
            profits_prev = list(profits)

        return max(profits)


# prices = [3,2,6,5,0,3]
prices = [5, 11, 3, 50, 60, 90]
print(Solution().maxProfit(200, prices))
