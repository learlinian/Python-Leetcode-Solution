class Solution(object):
    def maximalRectangle(self, matrix):
        # check if the matrix is empty
        try:
            row_len = len(matrix)
            column_len = len(matrix[0])
            if row_len == 0 or column_len == 0:
                return 0
        except:
            return 0

        # collect matrix information in terms of histogram
        max_area = 0
        for row_index in range(row_len):
            heights = [int(i) for i in matrix[row_index]]
            for column in range(column_len):
                row = row_index - 1
                while matrix[row_index][column] == '1' and row >= 0 and matrix[row][column] == '1':
                    heights[column] += 1
                    row -= 1
            # print(heights)

            # same code as Leetcode problem 84
            stack = []
            h_len = len(heights)
            for i in range(h_len + 1):
                if i == h_len:
                    current_h = -1
                else:
                    current_h = heights[i]

                while stack and heights[stack[-1]] > current_h:
                    index = stack.pop()
                    left_index = stack[-1] if stack else -1
                    max_area = max(max_area, (i - left_index - 1) * heights[index])

                if i != h_len:
                    stack.append(i)
        return max_area


if __name__ == '__main__':
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(Solution().maximalRectangle(matrix))