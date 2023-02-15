class Solution(object):
    def addStrings(self, num1, num2):
        result = ''
        upper = False
        for i in range(max(len(num1), len(num2))):
            if i >= len(num1):
                value = int(num2[len(num2) - 1 - i]) + upper
                upper = True if value >= 10 else False
                result = str(value % 10) + result
            elif i >= len(num2):
                value = int(num1[len(num1) - 1 - i]) + upper
                upper = True if value >= 10 else False
                result = str(value % 10) + result
            else:
                value = int(num1[len(num1) - 1 - i]) + int(num2[len(num2) - 1 - i]) + upper
                upper = True if value >= 10 else False
                result = str(value % 10) + result
        if upper is True:
            result = '1' + result
        return result


if __name__ == '__main__':
    num1 = '17'
    num2 = '23'
    print(Solution().addStrings(num1, num2))
