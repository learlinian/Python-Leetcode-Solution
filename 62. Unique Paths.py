class Solution(object):
    def uniquePaths(self, m, n):
        """brutal force"""
        # self.total_num = 0
        #
        # def go(current_m, current_n):
        #     if current_m == m-1 and current_n == n-1:
        #         self.total_num += 1
        #     if current_m < m - 1:
        #         go(current_m+1, current_n)
        #     if current_n < n - 1:
        #         go(current_m, current_n+1)
        #
        # go(0, 0)
        # return self.total_num
        
        array = m * [1]
        for _ in range(n-1):
            temp = list(array)
            for i in range(1, m):
                array[i] = sum(temp[:i+1])
            print(array)
        return array[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(7, 3))
