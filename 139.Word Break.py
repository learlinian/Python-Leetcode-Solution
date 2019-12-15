class Solution(object):
    def wordBreak(self, s, wordDict):
        if s == "":
            return True

        n = len(s)
        OPT = [False] * (n + 1)
        OPT[0] = True

        for i in range(1, n + 1):
            best = False
            for j in range(0, i):
                if s[j:i] in wordDict and OPT[j]:
                    best = True
                    break
            OPT[i] = best
        return OPT[n]


if __name__ == '__main__':
    # s = 'catsandog'
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    # s = "cars"
    # wordDict = ["car", "ca", "rs"]
    print(Solution().wordBreak(s, wordDict))
