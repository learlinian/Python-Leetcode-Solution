# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_sum = float('-inf')    # initial setup

    def maxPathSum(self, root):
        if root.left is None and root.right is None:
            return root.val
        self.calculate(root)
        return self.max_sum

    def calculate(self, root):
        if root.left:
            self.calculate(root.left)
        if root.right:
            self.calculate(root.right)

        if root.left and root.right:    # has both children nodes case
            self.max_sum = max(self.max_sum, root.val, root.val + max(root.left.val, root.right.val), root.left.val + root.right.val + root.val)
            root.val = max(root.left.val, root.right.val, 0) + root.val
        elif root.left:     # has left node case
            self.max_sum = max(self.max_sum, root.val, root.left.val + root.val)
            root.val = max(root.left.val, 0) + root.val
        elif root.right:    # has right node case
            self.max_sum = max(self.max_sum, root.val, root.right.val + root.val)
            root.val = max(root.right.val, 0) + root.val
        else:   # leaf node case
            self.max_sum = max(self.max_sum, root.val)


if __name__ == '__main__':
    n1 = TreeNode(-10)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print(Solution().maxPathSum(n1))
