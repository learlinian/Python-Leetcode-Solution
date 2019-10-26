class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        iter = 5

        while iter <= n:
            count += n//iter
            iter *= 5

        return count


if __name__ == '__main__':
    print(Solution().trailingZeroes(100))


