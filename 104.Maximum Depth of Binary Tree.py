# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)

    t6 = TreeNode(15)
    t7 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t3.left = t6
    t3.right = t7
    print(Solution().maxDepth(t1))
