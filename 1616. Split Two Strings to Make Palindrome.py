# brutal force
# class Solution(object):
#     def checkPalindromeFormation(self, a, b):
#         def checkPalindrome(s):
#             for i in range(len(s)//2):
#                 if s[i] != s[-i-1]:
#                     return False
#             return True
#
#         for i in range(min(len(a), len(b))):
#             if checkPalindrome(a[:i] + b[i:]) or checkPalindrome(b[:i] + a[i:]):
#                 return True
#         return False

class Solution(object):
    def checkPalindromeFormation(self, a, b):
        if a == a[::-1] or b == b[::-1]:
            return True

        def helper(a, b):
            i = 0
            while a[i] == b[-i-1]:
                i += 1
            i -= 1
            if len(a) - 1 <= 2*(i+1) or b[i+1:len(a)-i-1] == b[i+1:len(a)-i-1][::-1] or a[i+1:len(a)-i-1] == a[i+1:len(a)-i-1][::-1]:
                return True
            return False

        return helper(a, b) or helper(b, a)


if __name__ == '__main__':
    a = "ulacfd"
    b = "jizalu"
    print(Solution().checkPalindromeFormation(a, b))