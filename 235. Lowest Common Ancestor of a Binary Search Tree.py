# runtime: 92%; memory: 25%

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        node = root
        p_val = p.val
        q_val = q.val
        p_val, q_val = min(p_val, q_val), max(p_val, q_val)
        while node:
            if p_val <= node.val <= q_val:
                return node
            if q_val < node.val:
                node = node.left
            else:
                node = node.right

