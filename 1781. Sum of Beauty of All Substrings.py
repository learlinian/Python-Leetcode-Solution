class Solution(object):
    def beautySum(self, s):
        d = {}
        ans = 0
        for i in range(len(s)):
            try:
                d[s[i]] += 1
            except:
                d[s[i]] = 1
            c = d.copy()
            for j in range(i):
                ans += max(c.values()) - min(c.values())
                c[s[j]] -= 1
                if c[s[j]] == 0:
                    del c[s[j]]
                if len(c) <= 1:
                    break
        return ans


if __name__ == '__main__':
    s = "aabcb"
    print(Solution().beautySum(s))