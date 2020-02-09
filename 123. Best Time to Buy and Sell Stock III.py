class Solution(object):
    def maxProfit(self, prices):
        prices_len = len(prices)
        if prices_len < 2:
            return 0

        max_profits = [0] * prices_len  # array to store max profit could be made through only 1 transaction at time i
        max_profit = max(prices[1] - prices[0], 0)
        min_price = prices[0]
        for i in range(1, prices_len):
            max_profit = max(max_profit, prices[i] - min_price)
            max_profits[i] = max_profit
            if min_price > prices[i]:
                min_price = prices[i]

        max_price = prices[-1]
        for i in range(prices_len-2, -1, -1):
            max_profit = max(max_profit, max_price - prices[i] + max_profits[i])
            if max_price < prices[i]:
                max_price = prices[i]

        return max_profit


# prices = [3,3,5,0,0,3,1,4]
# prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
# prices = [6,1,3,2,4,7]
# prices = [2, 1, 2, 0, 1]
# prices = [1,2,4,2,5,7,2,4,9,0]
# prices = [1,2,4,2,5,7,2,4,9,0,9]
# prices = [1,3,5,4,3,7,6,9,2,4]
# prices = [8,6,4,3,3,2,3,5,8,3,8,2,6]
# prices = [5,5,4,9,3,8,5,5,1,6,8,3,4]
print(Solution().maxProfit(prices))