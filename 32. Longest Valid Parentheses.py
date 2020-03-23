# """dp approach"""
# class Solution(object):
#     def longestValidParentheses(self, s):
#         s_len = len(s)
#         if s_len <= 1:
#             return 0
#         dp = [0] * s_len
#         for i in range(1, s_len):
#             if s[i] == '(':
#                 continue
#             if s[i-1] == '(':
#                 dp[i] = 2
#                 if i-2 >= 0:
#                     dp[i] += dp[i-2]
#             else:
#                 if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
#                     dp[i] = dp[i-1] + 2
#                     if i - 2 - dp[i - 1] >= 0:
#                         dp[i] += dp[i-2-dp[i-1]]
#         print(dp)
#         return max(dp)


"""stack method"""
class Solution(object):
    def longestValidParentheses(self, s):
        s_len = len(s)
        stack = [-1]
        result = 0

        for i in range(s_len):
            if s[i] == '(':
                stack.append(i)
            else:
                _ = stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        return result

# s = "(()"
# s = ")()())"
# s = "()(())"
# s = "()((()"
# s = "(()))())("
# s = "(()(((()"
s= "()((()))"
print(Solution().longestValidParentheses(s))
