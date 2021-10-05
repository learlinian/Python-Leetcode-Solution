# runtime: 17%; memory: 84%
# solution: DFS

class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, current_sum):
            if node is None:
                return False
            if current_sum + node.val == targetSum and node.left == node.right is None:
                return True
            if dfs(node.left, current_sum + node.val):
                return True
            if dfs(node.right, current_sum + node.val):
                return True
            return False

        return dfs(root, 0)
