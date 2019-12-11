class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive method
class Solution(object):
    def __init__(self):
        self.order = []

    def inorderTraversal(self, root):
        if not root:
            return None
        if root.left is None:
            self.order.append(root.val)
        else:
            self.inorderTraversal(root.left)

        if root.left is not None:
            self.order.append(root.val)  # append the middle node
        if root.right is not None:
            self.inorderTraversal(root.right)

        return self.order


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    print(Solution().inorderTraversal(t1))
