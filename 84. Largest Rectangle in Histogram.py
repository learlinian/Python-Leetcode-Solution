class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        h_len = len(heights)
        for i in range(h_len+1):
            if i == h_len:
                current_h = -1
            else:
                current_h = heights[i]

            # print(stack)

            while stack and heights[stack[-1]] > current_h:
                index = stack.pop()
                left_index = stack[-1] if stack else -1
                max_area = max(max_area, (i-left_index-1)*heights[index])

            if i != h_len:
                stack.append(i)
        return max_area


if __name__ == '__main__':
    h = [1,2,3,4,5,3,3,2]
    heights = [2,1,2]
    print(Solution().largestRectangleArea(heights))
