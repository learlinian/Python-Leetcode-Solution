# run time: 30%; memory: 20%
class Solution(object):
    def findLonelyPixel(self, picture):
        row_len = len(picture)
        col_len = len(picture[0])
        visited = []
        ans = 0

        def visited_all_points(row, col):
            visited[row] = [True] * col_len
            for k in range(row_len):
                visited[k][col] = True

        for _ in range(row_len):
            visited.append([False] * col_len)
        for row in range(row_len):
            for col in range(col_len):
                if visited[row][col] is True:
                    if picture[row][col] == 'B':
                        visited_all_points(row, col)
                    continue
                visited[row][col] = True
                if picture[row][col] == 'W':
                    continue
                is_lonely = True
                j = col + 1
                while j < col_len:
                    visited[row][j] = True
                    if picture[row][j] == 'B':
                        is_lonely = False
                        break
                    j += 1
                if j < col_len:
                    visited_all_points(row, col)
                    continue
                i = row + 1
                while i < row_len:
                    visited[i][col] = True
                    if picture[i][col] == 'B':
                        is_lonely = False
                        break
                    i += 1
                if i < row_len:
                    visited_all_points(row, col)
                elif is_lonely:
                    ans += 1
        return ans


if __name__ == '__main__':
    picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
    # picture = [["W","B","W","W"],["W","B","B","W"],["W","W","W","W"]]
    print(Solution().findLonelyPixel(picture))
