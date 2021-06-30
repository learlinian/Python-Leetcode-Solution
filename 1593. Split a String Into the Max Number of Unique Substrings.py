class Solution(object):
    def maxUniqueSplitIter(self, s, sub_strings):
        ans = 0

        for i in range(1, len(s) + 1):
            x = s[:i]
            if x in sub_strings:
                continue
            sub_strings.add(x)
            ans = max(ans, self.maxUniqueSplitIter(s[i:], sub_strings) + 1)
            sub_strings.remove(x)
        return ans

    def maxUniqueSplit(self, s):
        s_len = len(s)
        if s_len == 0:
            return 0

        return self.maxUniqueSplitIter(s, set())


if __name__ == '__main__':
    s = "wwwzfvedwfvhsww"
    print(Solution().maxUniqueSplit(s))
