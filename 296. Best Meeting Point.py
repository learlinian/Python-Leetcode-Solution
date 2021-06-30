class Solution(object):
    def minTotalDistance(self, grid):
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        def min_1d_grid(arr, origin):
            result = 0
            for v in arr:
                result += abs(v-origin)
            return result

        cols.sort()
        return min_1d_grid(rows, rows[len(rows) // 2]) + min_1d_grid(cols, cols[len(cols) // 2])


if __name__ == '__main__':
    grid = [[0,0,1],[0,0,0],[1,0,0]]
    print(Solution().minTotalDistance(grid))
