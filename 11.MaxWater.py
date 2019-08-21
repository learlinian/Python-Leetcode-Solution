# first solution: brutal force
class Solution1(object):
    def maxArea(self, height):
        volume = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                v = min(height[i], height[j]) * (j-i)
                if volume < v:
                    volume = v
        return volume


# second solution: find the max volume value by shifting the pointer
class Solution2(object):
    def maxArea(self, height):
        volume = 0
        i = 0                   # the first index of the height array
        j = len(height) - 1     # the last index of the height array
        while i < j:
            v = min(height[i], height[j]) * (j - i)
            if volume < v:
                volume = v
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return volume


if __name__ == '__main__':
    s = Solution2()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

