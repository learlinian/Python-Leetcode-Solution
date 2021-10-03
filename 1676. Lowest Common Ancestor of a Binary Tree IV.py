# runtime: 47%; memory: 10%

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        total_len = len(nodes)
        vals = {}
        for node in nodes:
            vals[node.val] = True

        def find_node(node):
            if node is None:
                return None, 0
            is_node_flag = False
            if node.val in vals:
                is_node_flag = True
            node_left, left_count = find_node(node.left)
            node_right, right_count = find_node(node.right)
            if node_left:
                return node_left, left_count
            if node_right:
                return node_right, right_count
            count = left_count + right_count + is_node_flag
            if count == total_len:
                return node, count
            return None, count

        node, count = find_node(root)
        if count < total_len:
            return None
        return node
