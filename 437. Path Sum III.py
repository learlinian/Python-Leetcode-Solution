# runtime: 58%; memory: 6%
# solution: dfs


class Solution(object):
    def __init__(self):
        self.result = 0

    def pathSum(self, root, targetSum):
        def dfs(node, current_sums):
            if node is None:
                return
            if targetSum - node.val in current_sums:
                self.result += current_sums[targetSum - node.val]
            new_sums = {}
            for k, v in current_sums.items():
                new_sums[k + node.val] = v
            new_sums[0] = 1 if 0 not in new_sums else new_sums[0] + 1
            dfs(node.left, new_sums)
            dfs(node.right, new_sums)

        dfs(root, {0: 1})
        return self.result
