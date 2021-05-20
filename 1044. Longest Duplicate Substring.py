import functools

class Solution(object):
    def longestDupSubstring(self, S):
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(length):
            p = pow(26, length)
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:length])
            seen = {cur}
            for i in range(length, len(S)):
                cur = (cur * 26 + A[i] - A[i - length] * p) % mod
                if cur in seen: return i - length + 1
                seen.add(cur)

        res, L, R = 0, 0, len(S)
        while L < R:
            mi = (L + R + 1) // 2
            pos = test(mi)
            if pos:
                L = mi
                res = pos
            else:
                R = mi - 1
        return S[res:res + L]


if __name__ == '__main__':
    print(Solution().longestDupSubstring('banana'))