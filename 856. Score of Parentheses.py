class Solution(object):
    def scoreOfParentheses(self, S):
        S_len = len(S)
        if S_len == 2:
            return 1
        else:
            count = 1
            for i in range(1, S_len):
                count = count+1 if S[i] == '(' else count-1
                if count == 0:
                    break
            if i == 1:
                return 1 + self.scoreOfParentheses(S[i+1:])
            elif i < S_len-1:
                return 2 * self.scoreOfParentheses(S[1:i]) + self.scoreOfParentheses(S[i+1:])
            else:
                return 2 * self.scoreOfParentheses(S[1:i])


if __name__ == '__main__':
    string = "(()(()))"
    s = Solution()
    print(s.scoreOfParentheses(string))
