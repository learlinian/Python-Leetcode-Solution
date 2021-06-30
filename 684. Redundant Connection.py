class Solution(object):
    def findRedundantConnection(self, edges):
        number = len(edges)
        connection_dict = {}

        for i in range(1, number + 1):
            connection_dict[i] = []
        for node1, node2 in edges:
            connection_dict[node1].append(node2)
            connection_dict[node2].append(node1)

        def dfs(current_node, target, visited):
            if current_node in visited:
                return False
            elif current_node == target:
                return True
            else:
                connections = connection_dict[current_node].copy()
                if not visited:
                    connections.remove(target)
                visited.append(current_node)
                for node in connections:
                    if node in visited:
                        continue
                    if dfs(node, target, visited):
                        return True
                return False

        for i in range(number - 1, -1, -1):
            ans =  dfs(edges[i][0], edges[i][1], [])
            if ans is True:
                return edges[i]
        return None


if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(Solution().findRedundantConnection(edges))
