class Solution(object):
    def mySqrt(self, x):
        checking_range = [0, x]
        while checking_range[0] < checking_range[1] - 1:
            # print(checking_range)
            check_val = sum(checking_range) // 2
            if check_val ** 2 > x:
                checking_range[1] = check_val
            elif check_val ** 2 < x:
                checking_range[0] = check_val
            else:
                return check_val
        return 1 if x == 1 else checking_range[0]


print(Solution().mySqrt(1))