# solution: greedy search
# runtime: 38%; memory: 42%

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        max_profit = 0
        buy_price = 10 ** 4
        sell_price = -1
        for i in range(len(prices)):
            if sell_price == -1:
                if prices[i] <= buy_price:
                    buy_price = prices[i]
                else:
                    sell_price = prices[i]
            else:
                if prices[i] > sell_price:
                    sell_price = prices[i]
                else:
                    max_profit += sell_price - buy_price
                    sell_price = -1
                    buy_price = prices[i]
        if sell_price > buy_price:
            max_profit += sell_price - buy_price
        return max_profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
