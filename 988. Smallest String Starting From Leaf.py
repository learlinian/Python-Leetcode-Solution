class Solution(object):
    def smallestFromLeaf(self, root):
        self.ans = "~"

        def dfs(node, node_list):
            if node:
                node_list.append(chr(node.val + ord('a')))
                if node.left is None and node.right is None:
                    self.ans = min(self.ans, ''.join(node_list)[::-1])
                dfs(node.left, node_list)
                dfs(node.right, node_list)
                _ = node_list.pop()

        dfs(root, [])
        return self.ans