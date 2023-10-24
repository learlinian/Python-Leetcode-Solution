import collections

class Solution(object):
    def maximumDetonation(self, bombs):
        graph = collections.defaultdict(list)
        n = len(bombs)

        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        # DFS to get the number of nodes reachable from a given node cur
        def dfs(cur, visited):
            visited.add(cur)
            for neib in graph[cur]:
                if neib not in visited:
                    dfs(neib, visited)
            return len(visited)

        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))

        return answer


if __name__ == '__main__':
    # bombs = [[7, 26, 7], [7, 18, 4], [3, 25, 10]]
    bombs = [[2,1,3],[6,1,4]]
    print(Solution().maximumDetonation(bombs))
