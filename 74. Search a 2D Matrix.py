class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        rows = len(matrix)
        cols = len(matrix[0]) - 1
        for row in range(rows):
            if matrix[row][-1] < target:
                continue
            while cols >= 0:
                if matrix[row][cols] == target:
                    return True
                if matrix[row][cols] > target:
                    cols -= 1
                elif matrix[row][cols] < target:
                    return False
        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 17
print(Solution().searchMatrix(matrix, target))
