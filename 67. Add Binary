"""Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0."""


class Solution(object):
    def __init__(self):
        self.result = []

    def addBinary(self, a, b):
        if len(a) < len(b):
            a = abs(len(a) - len(b)) * '0' + a
        elif len(a) > len(b):
            b = abs(len(a) - len(b)) * '0' + b
        add_one = False
        while a and b:
            #             print('a[-1]: {}; b[-1]: {}'.format(a[-1], b[-1]))
            #             print((a[-1] == '1'))
            if add_one:
                self.result.append(str(int(a[-1]) ^ int(b[-1]) ^ 1))
            #                 print('add_one: {}'.format(~int(a[-1]) ^ int(b[-1])))
            else:
                self.result.append(str(int(a[-1]) ^ int(b[-1])))
            #                 print('no add_one: {}'.format(int(a[-1]) ^ int(b[-1])))
            if (a[-1] == '1' and b[-1] == '1') or (add_one == True and (a[-1] == '1' or b[-1] == '1')):
                add_one = True
            else:
                add_one = False
            #             print('a: {}; b: {}'.format(a, b))
            a = a[0:len(a) - 1]
            b = b[0:len(b) - 1]
        #             print(self.result)

        if add_one:
            self.result.append('1')

        self.result.reverse()
        result = ''.join(self.result)
        return result


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(Solution().addBinary(a, b))
