class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = [0]

        def toggle(num):
            for i in range(n):
                if num ^ (2**i) not in result:
                    num = num ^ (2 ** i)
                    result.append(num)
                    toggle(num)
        toggle(0)

        return result


print(Solution().grayCode(2))