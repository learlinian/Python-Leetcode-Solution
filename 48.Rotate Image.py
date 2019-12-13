class Solution(object):
    def rotate(self, matrix):
        temp = list()
        for row in matrix:
            temp.append(list(row))
        row_length = len(temp[0])
        row_count = row_length - 1
        for row in temp:
            for i in range(row_length):
                matrix[i][row_count] = row[i]
            row_count -= 1

        return matrix


if __name__ == '__main__':
    matrix = [[ 5, 1, 9,11],
              [ 2, 4, 8,10],
              [13, 3, 6, 7],
              [15,14,12,16]]

    print(Solution().rotate(matrix))
