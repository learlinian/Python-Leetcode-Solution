class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        dp = []
        for _ in range(m):
            dp.append([0] * n)
        dp[startRow][startColumn] = 1
        result = 0

        def checkout(i, j):
            ans = 0
            if i == 0:
                ans += 1
            if i == m - 1:
                ans += 1
            if j == 0:
                ans += 1
            if j == n - 1:
                ans += 1
            return ans

        for step in range(maxMove):
            temp = []
            for _ in range(m):
                temp.append([0] * n)
            for i in range(m):
                for j in range(n):
                    if dp[i][j] > 0:
                        result = (result + checkout(i, j) * dp[i][j]) % (10 ** 9 + 7)
                        if i > 0:
                            temp[i - 1][j] += dp[i][j]
                        if i < m - 1:
                            temp[i + 1][j] += dp[i][j]
                        if j > 0:
                            temp[i][j - 1] += dp[i][j]
                        if j < n - 1:
                            temp[i][j + 1] += dp[i][j]
            dp = temp
        return result


if __name__ == '__main__':
    print(Solution().findPaths(2, 3, 8, 1, 0))
