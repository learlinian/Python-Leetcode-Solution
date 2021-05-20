class Solution(object):
    def minDistance(self, word1, word2):
        if not word2:
            return len(word1)
        if not word1:
            return len(word2)

        dp1 = [i for i in range(len(word2)+1)]
        dp2 = [0] * (len(word2) + 1)

        for i in range(0, len(word1)):
            for j in range(len(word2)):
                dp2[0] = dp1[0] + 1
                if word1[i] == word2[j]:
                    dp2[j+1] = dp1[j]
                else:
                    dp2[j+1] = min(dp2[j], dp1[j+1]) + 1
            dp1 = dp2.copy()
        return dp2[-1]


if __name__ == '__main__':
    w1 = 'sea'
    w2 = 'eat'
    print(Solution().minDistance(w1, w2))