class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        ans = []
        to_find = set([i for i in range(n)])
        edge_pointed = set([point[1] for point in edges])

        ans += list(to_find.difference(edge_pointed))

        return ans

