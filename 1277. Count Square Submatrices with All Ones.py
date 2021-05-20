class Solution(object):
    def countSquares(self, matrix):
        row_len = len(matrix)
        if row_len == 0:
            return 0
        col_len = len(matrix[0])
        result = 0
        for i in range(1, row_len):
            for j in range(1, col_len):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i - 1][j-1], matrix[i - 1][j], matrix[i][j - 1])
            result += sum(matrix[i])
        result += sum(matrix[0])
        return result
