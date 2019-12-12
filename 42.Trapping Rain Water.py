class Solution(object):
    def trap(self, height):
        total_num = len(height)
        water = 0
        jump = 0

        for i in range(total_num):
            find = False
            if i < jump:    # skip if it has not reach the bar which has been calculated
                continue

            # find whether there is a bar higher than the current one
            for j in range(i + 1, total_num):
                if height[j] >= height[i]:
                    water = water + (j - i - 1) * height[i] - sum(height[i + 1: j])
                    jump = j
                    find = True
                    break
            # if no bar is higher, find the max one and use the last occurrence of this
            # max bar as the reference
            if not find and i+1 < total_num:
                max_val = max(height[i+1:])
                for max_i in range(total_num-1, i+1, -1):
                    if height[max_i] == max_val:
                        water = water + (max_i - i - 1) * max_val - sum(height[i + 1: max_i])
                        jump = max_i
                        break
        return water


if __name__ == '__main__':
    array = [4, 2, 3]
    print(Solution().trap(array))   # answer: 6
