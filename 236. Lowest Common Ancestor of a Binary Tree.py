class TreeNode(object):
    """Tree Node Definition"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """First Solution, LCA is the node that (current node + left node + right node) has 2 True values"""
    def __init__(self):
        self.ans = None  # store answer

    def lowestCommonAncestor(self, root, p, q):
        def recursive(current_node):
            if current_node is None:
                return False
            left_val = recursive(current_node.left)     # check left branch
            right_val = recursive(current_node.right)   # check right branch
            current_val = p == current_node or q == current_node    # check current node

            if [left_val, right_val, current_val].count(True) == 2:  # if 2 branches are True
                self.ans = current_node
            else:
                return left_val or right_val or current_val  # know whether is True or False
        recursive(root)
        return self.ans


class Solution2(object):
    def __init__(self):
        self.LCA_index = None   # store the LCA index
        self.visited_node = []  # record the index for LCA in visited node list

    def find_LCA(self, p, q):
        if self.visited_node:
            # print([i.val for i in self.visited_node], self.LCA_index)
            check_node = self.visited_node[-1]
            if check_node in [p, q]:
                if self.LCA_index is None:
                    self.LCA_index = len(self.visited_node) - 1    # init root node index
                elif self.LCA_index is not None:
                    return self.visited_node[self.LCA_index]       # return here

            for next_node in [check_node.left, check_node.right]:  # left * right node checking
                if next_node:
                    self.visited_node.append(next_node)
                    temp = self.find_LCA(p, q)  # check whether index is found
                    if temp is not None:
                        return temp
                    else:
                        if self.LCA_index == len(self.visited_node) - 1:    # index node has been found
                            self.LCA_index -= 1
                        self.visited_node.pop()

    def lowestCommonAncestor(self, root, p, q):
        self.visited_node.append(root)  # append the root first
        return self.find_LCA(p, q)


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    b.left = d
    b.right = e

    node = Solution2().lowestCommonAncestor(a, b, d)
    print(node.val)
