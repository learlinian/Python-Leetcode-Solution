# runtime: 29%; memory: 13%

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def find_node(node):
            if node is None:
                return None, False
            is_node_flag = False
            if node.val == p.val or node.val == q.val:
                is_node_flag = True
            node_left, is_left = find_node(node.left)
            node_right, is_right = find_node(node.right)
            if node_left:
                return node_left, True
            if node_right:
                return node_right, True
            if is_left + is_right + is_node_flag == 2:
                return node, True
            if is_left + is_right + is_node_flag == 1:
                return None, True
            return None, False

        node, found = find_node(root)
        if found is False:
            return None
        return node
