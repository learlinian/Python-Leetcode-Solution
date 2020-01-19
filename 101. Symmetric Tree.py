class Solution(object):
    def isSymmetric(self, root):
        # empty case
        if root is None:
            return True

        # function to return values for leaf nodes. Return None if doesn't exist
        def get_val(node):
            if node.left and node.right:
                return [node.left.val, node.right.val]
            elif node.left:
                return [node.left.val, None]
            elif node.right:
                return [None, node.right.val]
            return [None, None]

        nodes = [root]  # array to store all parent nodes
        while nodes:
            arr = []    # array to store values in each layer
            nodes_len = len(nodes)
            for node_index in range(nodes_len):
                # print(arr)
                node = nodes[node_index]
                arr = arr + get_val(node)

                # append leaf node values to variable nodes
                if node.left and node.right:
                    nodes += [node.left, node.right]
                elif node.left:
                    nodes += [node.left]
                elif node.right:
                    nodes += [node.right]

            nodes = nodes[nodes_len:]
            print(arr, nodes)
            arr_rev = list(arr)
            arr.reverse()
            if arr_rev != arr:
                return False
        return True


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    """case 1"""
    a = TreeNode(1)

    b1 = TreeNode(2)
    b2 = TreeNode(2)

    c1 = TreeNode(3)
    c2 = TreeNode(4)
    c3 = TreeNode(4)
    c4 = TreeNode(3)

    a.left = b1
    a.right = b2
    b1.left = c1
    b1.right = c2
    b2.left = c3
    b2.right = c4

    """case 2"""
    # a = TreeNode(1)
    #
    # b1 = TreeNode(2)
    # b2 = TreeNode(2)
    #
    # c1 = TreeNode(3)
    # c2 = TreeNode(3)
    #
    # a.left = b1
    # a.right = b2
    # b1.right = c1
    # b2.right = c2

    print(Solution().isSymmetric(a))
