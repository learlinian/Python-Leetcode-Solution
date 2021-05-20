class Solution(object):
    def __init__(self):
        self.cache = {}

    def countVowels(self, n, m):
        if n == 0:
            return 1
        key = str(n) + str(m)
        if key in self.cache.keys():
            return self.cache[key]

        count = 0
        for i in range(m):
            count += self.countVowels(n-1, m-i)
        self.cache[key] = count
        return count

    def countVowelStrings(self, n):
        return self.countVowels(n, 5)

class Solution2(object):
    def countVowelStrings(self, n):
        if n == 1:
            return 5
        dp = [5, 4, 3, 2, 1]
        if n == 2:
            return sum(dp)
        while n - 2 > 0:
            for j in range(5):
                dp[j] += sum(dp[j+1:])
            n -= 1
        return sum(dp)

if __name__ == '__main__':
    print(Solution2().countVowelStrings(33))