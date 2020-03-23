class Solution(object):
    def generateMatrix(self, n):
        result = [[0] * n for _ in range(n)]
        result[0][0] = 1

        i = j = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 2

        while count <= n*n:
            for direction in directions:
                while i + direction[0] < n and j + direction[1] < n and result[i + direction[0]][j + direction[1]] == 0:
                    i += direction[0]
                    j += direction[1]
                    result[i][j] = count
                    count += 1
        return result

print(Solution().generateMatrix(4))
