class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        if digits[i] != 9:
            digits[i] += 1
        else:
            digits[i] = 0
            while i-1 >= 0 and digits[i-1] == 9:
                digits[i-1] = 0
                i -= 1
            i -= 1
            if digits[0] == 0:
                digits.insert(0, 1)
            else:
                digits[i] += 1
        return digits


if __name__ == '__main__':
    arr = [1, 9, 9]
    print(Solution().plusOne(arr))