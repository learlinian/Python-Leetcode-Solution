# runtime: 90%; memory: 84%

class Solution:
    def minKnightMoves(self, x, y):
        cache = {(0, 0): 0, (1, 1): 2, (0, 2): 2, (2, 0): 2}

        def dfs(x, y):
            if (x, y) in cache:
                return cache[(x, y)]
            else:
                val = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
                cache[(x, y)] = val
                return val

        return dfs(abs(x), abs(y))


if __name__ == '__main__':
    x = 300
    y = 0
    print(Solution().minKnightMoves(x, y))
