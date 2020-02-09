class Solution(object):
    def canReach(self, arr, start):
        arr_len = len(arr)
        reach = [False] * arr_len

        def check(i, distance):
            if i - distance >= 0 and not reach[i - distance]:
                reach[i - distance] = True
                check(i - distance, arr[i - distance])
            if i + distance < arr_len and not reach[i + distance]:
                reach[i + distance] = True
                check(i + distance, arr[i + distance])

        check(start, arr[start])
        zero_indexs = []
        for i in range(arr_len):
            if arr[i] == 0:
                zero_indexs.append(i)

        for zero_index in zero_indexs:
            if reach[zero_index] is True:
                return True
        return False


if __name__ == '__main__':
    arr = [0,3,0,6,3,3,4]
    start = 6
    print(Solution().canReach(arr, start))