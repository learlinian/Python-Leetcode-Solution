# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        self.result = True

        def check(node, min_thresh, max_thresh):
            if (node.left and node.val <= node.left.val) or (node.right and node.val >= node.right.val) or node.val <= min_thresh or node.val >= max_thresh:
                self.result = False
            else:
                if node.left:
                    check(node.left, min_thresh, node.val)
                if node.right:
                    check(node.right, node.val, max_thresh)
        if root:
            check(root, -1e9, 1e9)
        return self.result


if __name__ == '__main__':
    root = TreeNode(5)

    a1 = TreeNode(1)
    a2 = TreeNode(4)

    b1 = TreeNode(3)
    b2 = TreeNode(6)

    root.left = a1
    root.right = a2

    a2.left = b1
    a2.right = b2

    print(Solution().isValidBST(root))