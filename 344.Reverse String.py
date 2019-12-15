class Solution(object):
    def reverseString(self, s):
        s_len = len(s)
        times = (s_len+1) // 2
        for i in range(times):
            s[i], s[s_len-i-1] = s[s_len-i-1], s[i]
        return s


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    print(Solution().reverseString(s))