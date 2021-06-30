class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1

        length = len(str(k))
        prev_remainder = 10 ** length % k
        diffs = set()

        val = int("1" * length)
        while val % k != 0:
            length += 1
            val = (val + prev_remainder) % k
            if val == 0:
                return length
            diff = k - val
            prev_remainder = prev_remainder * 10 % k
            if prev_remainder == 0 or diff in diffs:
                return -1
            diffs.add(diff)

        return length


if __name__ == '__main__':
    print(Solution().smallestRepunitDivByK(61))
