class Solution(object):
    def islandPerimeter(self, grid):
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        count -= 1
                    if i + 1 < row and grid[i + 1][j] == 1:
                        count -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        count -= 1
                    if j + 1 < col and grid[i][j + 1] == 1:
                        count -= 1

        return count


arr = [[0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0]]

print(Solution().islandPerimeter(arr))
