class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        negative = False
        if x < 0:
            negative = True
            x = -x
        x = [i for i in str(x)]
        x.reverse()
        while x and x[0] == '0':
            del x[0]
        x = int(''.join(x))
        if abs(x) > 2**31:
            return 0
        return -x if negative else x


if __name__ == '__main__':
    num = 120
    print(Solution().reverse(num))