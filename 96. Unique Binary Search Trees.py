class Solution(object):
    def __init__(self):
        self.record = {0: 1, 1: 1, 2: 2}  # dict to store all combinations; key: num of remaining node; val: combination

    def numTrees(self, n):
        if n in self.record.keys():
            return self.record[n]
        node_num = nums = 0
        while node_num < n:
            left_choices = self.numTrees(node_num)
            right_choices = self.numTrees(n-node_num-1)
            nums = nums + left_choices * right_choices      # current node combination = combinations of left node * right node
            node_num += 1
        self.record[n] = nums
        return self.record[n]      # largest key value node


if __name__ == '__main__':
    print(Solution().numTrees(3))
