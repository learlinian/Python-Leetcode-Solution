class Solution(object):
    def minimumTotal(self, triangle):
        rows = len(triangle)
        results = [0] * rows
        # results[0] = triangle[0][0]

        for array in triangle:
            array_len = len(array)
            last_arr = list(results)
            for i in range(array_len):
                if i == 0:
                    results[0] += array[0]
                elif i == array_len - 1:
                    results[i] = array[i] + last_arr[i - 1]
                else:
                    results[i] = array[i] + min(last_arr[i - 1], last_arr[i])
            print(results)
        return min(results)


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(Solution().minimumTotal(triangle))
