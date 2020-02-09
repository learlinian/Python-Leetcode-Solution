class Solution(object):
    def maximumSum(self, arr):
        arr_len = len(arr)
        dp0 = list(arr)
        dp1 = list(arr)

        for i in range(1, arr_len):
            dp0[i] = max(dp0[i-1] + arr[i], dp0[i])
            dp1[i] = max(dp1[i-1] + arr[i], dp1[i])
            if i >= 2:
                dp1[i] = max(dp1[i], dp0[i-2] + arr[i])
            print(dp1)
        return max(dp1)


# arr = [2, 1, -2, -5, -2]
# arr = [11,-10,-11,8,7,-6,9,4,11,6,5,0]
arr = [1,-2,-2,3]
print(Solution().maximumSum(arr))
