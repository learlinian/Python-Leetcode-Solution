# runtime: 81%; memory: 72%
# solution: dynamic programming

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        col_len = len(dungeon)
        row_len = len(dungeon[0])
        dp_row = [0] * row_len
        dp = []
        for _ in range(col_len):
            dp.append(dp_row.copy())
        for i in range(col_len - 1, -1, -1):
            for j in range(row_len - 1, -1, -1):
                if i == col_len - 1:
                    if j == row_len - 1:
                        dp[i][j] = max(1, 1 - dungeon[i][j])
                    else:
                        dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                else:
                    if j == row_len - 1:
                        dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                    else:
                        dp[i][j] = max(1, min(dp[i][j + 1] - dungeon[i][j], dp[i + 1][j] - dungeon[i][j]))
        return dp[0][0]


if __name__ == '__main__':
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(dungeon))
