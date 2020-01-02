class Solution(object):
    def coinChange(self, coins, amount):
        coin_combination = [float('inf')] * (amount+1)
        coin_combination[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                coin_combination[i] = min(coin_combination[i-coin]+1, coin_combination[i])
                print(coin_combination)
        return coin_combination[amount] if coin_combination[amount] < float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))