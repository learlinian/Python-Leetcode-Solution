"""Brutal Force, not efficient"""
# class Solution(object):
#     def maximalSquare(self, matrix):
#         row = len(matrix)
#         if row == 0:
#             return 0
#         col = len(matrix[0])
#         max_area = 0
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == '0':
#                     continue
#                 max_area = max(max_area, 1)
#                 length = 1
#                 while i + length < row and j + length < col:
#                     if '0' in matrix[i + length][j: j + length + 1] or '0' in [x[j + length] for x in matrix[i:i + length + 1]]:
#                         break
#                     length += 1
#                     max_area = max(max_area, length ** 2)
#         return max_area

"""most efficient way: 90% runtime + 100% memory"""
class Solution(object):
    def maximalSquare(self, matrix):
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        count = []
        for i in range(row):
            count.append(col*[0])
            count[i][0] = int(matrix[i][0])
        count[0] = [int(i) for i in matrix[0]]
        # print(count)
        for j in range(1, col):
            for i in range(1, row):
                if matrix[i][j] == '1' and (i-1 > 0 or j-1 < col - 1):
                    count[i][j] = min(count[i-1][j], count[i][j-1], count[i-1][j-1]) + 1
        # print(count)
        return max([max(i) for i in count])**2
