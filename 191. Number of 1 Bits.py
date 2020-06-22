class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        while n:
            ans += n % 2
            n = n >> 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(4))