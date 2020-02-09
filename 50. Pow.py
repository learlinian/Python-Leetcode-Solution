class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        tmp = abs(n)
        while (tmp):
            if tmp % 2 == 1:
                ret *= x
                tmp -= 1
            else:
                x *= x
                tmp /= 2

        return ret if n > 0 else 1 / ret


print(Solution().myPow(2, 2))