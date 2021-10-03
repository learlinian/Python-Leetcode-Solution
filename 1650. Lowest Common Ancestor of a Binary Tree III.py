# runtime: 99%; memory: 76%

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        visited = {p.val: True, q.val: True}
        while p.parent or q.parent:
            p_parent = p.parent
            q_parent = q.parent
            if p_parent:
                if p_parent.val in visited:
                    return p_parent
                visited[p_parent.val] = True
                p = p_parent
            if q_parent:
                if q_parent.val in visited:
                    return q_parent
                visited[q_parent.val] = True
                q = q_parent
