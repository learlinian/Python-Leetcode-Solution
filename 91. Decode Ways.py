class Solution(object):
    def __init__(self):
        self.record = {}

    def numDecodings(self, s):
        s_len = len(s)

        if s_len == 1:
            return 0 if s == '0' else 1
        if s_len == 0:
            return 1

        if s[0] == '0':
            return 0
        elif int(s[:2]) <= 26:
            if s_len - 1 in self.record.keys() and s_len - 2 in self.record.keys():
                result = self.record[s_len - 1] + self.record[s_len - 2]
            elif s_len - 2 in self.record.keys():
                result = self.numDecodings(s[1:]) + self.record[s_len - 2]
            else:
                result = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        else:
            result = self.numDecodings(s[1:])
        self.record[s_len] = result
        return result


"""better solution"""
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         length = len(s)
#         if "00" in s  : return 0
#         if s[0] == "0": return 0
#         if length == 1: return 1
#         dp = [0] * length
#         dp[0] = 1
#         if s[1] > "0":
#             if int(s[0:2]) <= 26:
#                 dp[1] = 2
#             else:
#                 dp[1] = 1
#         else:
#             if s[0] > "2":
#                 return 0
#             else:
#                 dp[1] = 1
#         for i in range(2, length):
#             if s[i] > "0":
#                 dp[i] += dp[i-1]
#             elif s[i-1] > "2":
#                 return 0
#             if int(s[i-1:i+1]) <= 26 and s[i-1] > "0":
#                 dp[i] += dp[i-2]
#
#         print(dp)
#         return dp[length-1]


s = '12120'
print(Solution().numDecodings(s))