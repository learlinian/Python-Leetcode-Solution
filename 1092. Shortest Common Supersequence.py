# runtime: 70%; memory: 61%
# solution: find the longest common subsequence first then back trace

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        str1_len = len(str1)
        str2_len = len(str2)
        dp = [[0 for _ in range(str1_len + 1)] for _ in range(str2_len + 1)]
        for i in range(1, str2_len + 1):
            for j in range(1, str1_len + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if str2[i - 1] == str1[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        ans = ''
        str1_i = str1_len
        str2_i = str2_len
        while str2_i >= 1 and str1_i >= 1:
            if dp[str2_i][str1_i] == dp[str2_i-1][str1_i]:
                ans = str2[str2_i-1] + ans
                str2_i -= 1
            elif dp[str2_i][str1_i] == dp[str2_i][str1_i-1]:
                ans = str1[str1_i - 1] + ans
                str1_i -= 1
            else:
                ans = str2[str2_i - 1] + ans
                str2_i -= 1
                str1_i -= 1
        ans = str2[:str2_i] + ans
        ans = str1[:str1_i] + ans
        return ans


if __name__ == '__main__':
    # str1 = "abac"
    # str2 = "cab"

    # str1 = "aaa"
    # str2 = "aa"

    # str1 = "bbbaaaba"
    # str2 = "bbababbb"
    # str1 = "accabcba"
    # str2 = "aacbbbbbaa"
    str1 = "baaacbcbc"
    str2 = "bacbcaca"
    print(Solution().shortestCommonSupersequence(str1, str2))
