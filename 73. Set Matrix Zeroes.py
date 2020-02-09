class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        is_row = is_col = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                    if row == 0:
                        is_row = True
                    if col == 0:
                        is_col = True

        for row in range(1, rows):
            if matrix[row][0] == 0:
                matrix[row] = cols * [0]

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0
        if is_row:
            matrix[0] = [0] * cols
        if is_col:
            for col in range(rows):
                matrix[col][0] = 0
        return matrix


if __name__ == '__main__':
    # matrix = [[1,1,1], [1,0,1], [1,1,1]]
    # matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    matrix = [[1, 0, 3]]
    print(Solution().setZeroes(matrix))