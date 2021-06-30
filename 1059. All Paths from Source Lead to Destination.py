class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        edges_dict = {}
        for edge in edges:
            if edge[0] not in edges_dict:
                edges_dict[edge[0]] = [edge[1]]
            else:
                edges_dict[edge[0]].append(edge[1])

        def dfs(node, visited):
            if node in visited:
                return False
            visited.append(node)
            if node not in edges_dict:
                if node == destination:
                    return True
                else:
                    return False
            for v in edges_dict[node]:
                if dfs(v, visited) is False:
                    return False
                visited.pop()
            return True

        return dfs(source, [])


if __name__ == '__main__':
    n = 4
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    source = 0
    destination = 3
    print(Solution().leadsToDestination(n, edges, source, destination))
