# runtime: 6%; memory: 39%

class Solution(object):
    def reverseWords(self, s):
        words = []
        i, j = 0, 0
        while j < len(s):
            if s[j] == ' ':
                if i < j:
                    words.append(s[i:j])
                while j < len(s) and s[j] == ' ':
                    j += 1
                i = j
            j += 1
        if i + 1 < j:
            words.append(s[i:j])
        elif i < len(s) and s[i] != ' ':
            words.append(s[i])
        words.reverse()
        return ' '.join(words)


if __name__ == '__main__':
    s = "  hello world  "
    print(Solution().reverseWords(s))
