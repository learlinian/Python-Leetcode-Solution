class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        i = j = 0
        row_range = [0, len(matrix)-1]
        col_range = [0, len(matrix[0])-1]
        maxtrix_items = len(matrix) * len(matrix[0])
        while len(result) < maxtrix_items:
            if col_range[0] <= j <= col_range[1]:
                while col_range[0] <= j <= col_range[1]:
                    result.append(matrix[i][j])
                    j += 1
                row_range[0] += 1
                if row_range[0] > row_range[1]:
                    break
                j -= 1
            i += 1
            if row_range[0] <= i <= row_range[1]:
                while row_range[0] <= i <= row_range[1]:
                    result.append(matrix[i][j])
                    i += 1
                col_range[1] -= 1
                if col_range[0] > col_range[1]:
                    break
                i -= 1
            j -= 1
            if col_range[0] <= j <= col_range[1]:
                while col_range[0] <= j <= col_range[1]:
                    result.append(matrix[i][j])
                    j -= 1
                row_range[1] -= 1
                if row_range[0] > row_range[1]:
                    break
                j += 1
            i -= 1
            if row_range[0] <= i <= row_range[1]:
                while row_range[0] <= i <= row_range[1]:
                    result.append(matrix[i][j])
                    i -= 1
                col_range[0] += 1
                i += 1
            j += 1
        return result


if __name__ == '__main__':
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print(Solution().spiralOrder(matrix))
