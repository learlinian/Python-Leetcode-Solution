class Solution(object):
    def myAtoi(self, s):
        find_num = False
        result = ""
        for i in range(len(s)):
            c = s[i]
            if c == " " and find_num is False:
                continue
            if (c == "-" or c == "+") and find_num is False:
                find_num = True
                result = c
            elif ord("0") <= ord(c) <= ord("9"):
                find_num = True
                result += c
            else:
                break
        try:
            val = int(result)
        except:
            return 0

        if val > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if val < -2 ** 31:
            return -2 ** 31
        return val


if __name__ == '__main__':
    s = " +0 123"
    print(Solution().myAtoi(s))
