class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = 1 if dividend > 0 else -1
        dividend *= sig
        sig2 = 1 if divisor > 0 else -1
        divisor *= sig2

        if dividend < divisor:
            return 0

        q = 0
        while dividend >= divisor:
            shift = 0
            tmp_divisor = divisor
            while dividend >= (tmp_divisor << 1):
                shift += 1
                tmp_divisor = (tmp_divisor << 1)
            dividend -= tmp_divisor
            q += (1 << shift)

        q = q * sig * sig2

        return max(-2 ** 31, min(2 ** 31 - 1, q))


print(Solution().divide(7, -3))