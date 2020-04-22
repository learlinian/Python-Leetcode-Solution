class Solution(object):
    def minAddToMakeValid(self, S):
        S_len = len(S)
        adding = count = 0

        for i in range(S_len):
            if S[i] == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                adding += 1

        adding += count
        return adding


if __name__ == '__main__':
    string = "()))(("
    s = Solution()
    print(s.minAddToMakeValid(string))
