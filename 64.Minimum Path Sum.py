class Solution(object):
    def minPathSum(self, grid):
        row = len(grid)
        column = len(grid[0])
        if row == 1 or column == 1:
            min_path = 0
            for sub_grid in grid:
                min_path += sum(sub_grid)
            return min_path

        val = [[grid[0][0]]]

        for i in range(1, column):
            val[0].append(val[0][i-1] + grid[0][i])

        for i in range(1, row):
            val.append([val[i-1][0] + grid[i][0]])

        def find(i, j):
            try:
                min_val = grid[i][j] + min(val[i-1][j], val[i][j-1])
                val[i].append(min_val)
                if i + 1 < row:
                    find(i+1, j)
                if j + 1 < column:
                    find(i, j+1)
            except:
                pass
        find(1, 1)
        return val[-1][-1]


if __name__ == '__main__':
    # grid = [[1,3,1],
    #       [1,5,1],
    #       [4,2,1]]
    grid = [[1, 2], [1, 1]]
    print(Solution().minPathSum(grid))
