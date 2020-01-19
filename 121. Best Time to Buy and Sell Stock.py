class Solution(object):
    def maxProfit(self, prices):
        """stupid method"""
        # price_len = len(prices)
        # if price_len <= 1:
        #     return 0
        #
        # profits = []
        # for i in range(1, price_len):
        #     profits.append(prices[i] - prices[0])
        # max_profit = max(0, max(profits))
        #
        # del profits[0]
        # check_index = 1
        # while profits:
        #     temp = list(profits)
        #     max_temp = max(temp)
        #     if prices[check_index] < prices[0]:
        #         max_profit = max(max_profit, max_temp + prices[0] - prices[check_index])
        #     check_index += 1
        #     del profits[0]
        # return max_profit

        price_len = len(prices)
        if price_len <= 1:
            return 0
        max_profit = 0
        min_val = prices[0]
        for i in range(1, price_len):
            if prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
            if min_val > prices[i]:
                min_val = prices[i]
        return max_profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))