from collections import Counter


# Solution 1 Runtime: 13% memory 7%
class Solution(object):
    def minWindow(self, s, t):
        t_len = len(t)
        if t_len == 0:
            return ''

        checked_len = t_len
        recorded_index = []
        result = ''

        chars = dict(Counter(t))

        for i in range(len(s)):
            if chars.get(s[i]) is not None:
                chars[s[i]] -= 1
                recorded_index.insert(0, i)

                if chars[s[i]] >= 0:
                    checked_len -= 1
                    if checked_len == 0:
                        while recorded_index and chars[s[recorded_index[-1]]] < 0:
                            chars[s[recorded_index[-1]]] += 1
                            recorded_index.pop()

                        del_index = recorded_index.pop()
                        if not result:
                            result = s[del_index: i+1]
                        elif i - del_index + 1 < len(result):
                            result = s[del_index: i+1]
                        chars[s[del_index]] += 1
                        checked_len += 1
        return result


# Solution 2 Runtime: 13% memory 7%
class Solution2(object):
    def minWindow(self, s, t):
        t_len = len(t)
        if t_len == 0:
            return ''
        remainings = t_len
        s_len = len(s)

        left = right = min_left = 0
        min_len = float('inf')

        chars = dict(Counter(t))

        while right < s_len:
            if chars.get(s[right]) is not None:
                if chars[s[right]] > 0:
                    remainings -= 1
                chars[s[right]] -= 1
                if remainings == 0:
                    while chars.get(s[left]) is None or chars[s[left]] < 0:
                        if chars.get(s[left]) and chars[s[left]] < 0:
                            chars[s[left]] += 1
                        left += 1
                    if right - left < min_len:
                        min_left = left
                        min_len = right - left + 1
                    chars[s[left]] += 1
                    left += 1
                    remainings += 1
            right += 1

        return s[min_left:min_left + min_len] if min_len != float('inf') else ''


if __name__ == '__main__':
    # S = "ADOBECODEBANC"
    # T = "ABC"
    S = 'a'
    T = 'aa'
    s = Solution2()
    print(s.minWindow(S, T))
