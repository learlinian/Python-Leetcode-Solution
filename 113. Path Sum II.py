# runtime: 39%; memory: 6%
# solution: DFS

class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, current_sum):
            if node is None:
                return
            path.append(node.val)
            if current_sum + node.val == targetSum and node.left == node.right is None:
                result.append(path.copy())
                return
            dfs(node.left, path.copy(), current_sum + node.val)
            dfs(node.right, path.copy(), current_sum + node.val)

        dfs(root, [], 0)
        return result
