"""not efficient"""


# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         row = len(matrix)
#         if row < 1:
#             return False
#         col = len(matrix[0])
#         i = 0
#         while i < row:
#             j = 0
#             while j < col:
#                 if matrix[i][j] == target:
#                     return True
#                 if matrix[i][j] > target:
#                     col = j
#                     if j == 0:
#                         row = i
#                 j += 1
#             i += 1
#         return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if rows < 1:
            return False
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return False


arr = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20

print(Solution().searchMatrix(arr, target))
