class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recursive(current_node):
            if current_node is None:
                return False
            current_left = recursive(current_node.left)
            current_right = recursive(current_node.right)
            current = current_node == p or current_node == q
            if current_left + current_right + current >= 2:
                self.ans = root

            return current_left or current_right or current

        recursive(root)
        return self.ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e

node = Solution().lowestCommonAncestor(a, c, d)
print(node.val)