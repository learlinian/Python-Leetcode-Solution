class Solution(object):
    def matrixBlockSum(self, mat, k):
        row_len = len(mat)
        col_len = len(mat[0])
        result = []
        col_data = [0] * col_len

        # calculate the result for the first row
        for i in range(col_len):
            for j in range(k+1):
                col_data[i] += sum(mat[j][max(0, i-k):min(col_len, i+k+1)])
        result.append(col_data.copy())
        
        for i in range(1, row_len):
            if i + k < row_len:
                for j in range(col_len):
                    col_data[j] += sum(mat[i + k][max(0, j-k):min(col_len, j+k+1)])
            if i - k > 0:
                for j in range(col_len):
                    col_data[j] -= sum(mat[i - k - 1][max(0, j-k):min(col_len, j+k+1)])
            result.append(col_data.copy())
        return result

if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 2
    print(Solution().matrixBlockSum(mat, k))