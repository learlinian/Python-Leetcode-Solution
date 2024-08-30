class Solution:
    def __init__(self):
        self.max_profit = 0
        self.visited_nodes = []

    def maximumProfit(self, present, future, budget):
        for i in range(len(present)):
            profit = future[i] - present[i]
            if profit <= 0 or present[i] > budget:
                continue
            self.visited_nodes.append(profit)
            self.max_profit = max(self.max_profit, sum(self.visited_nodes))
            self.maximumProfit(present[i + 1:], future[i + 1:], budget - present[i])
            self.visited_nodes.pop()
        return self.max_profit

# present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10 # 6
# present = [2,2,5], future = [3,4,10], budget = 6 # 5
# present = [3,3,12], future = [0,3,15], budget = 10 # 0
if __name__  == '__main__':
    print(Solution().maximumProfit([3,3,12], [0,3,15], 10))