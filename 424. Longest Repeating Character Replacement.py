"""solution does not fit for the case when need to change the first item. i.e. "ABBB" """
# class Solution(object):
#     def characterReplacement(self, s, k):
#         s_len = len(s)
#         max_len = 0
#         if s_len <= 1:
#             return s_len
#         start = end = 0
#         while start < s_len and end < s_len-1:
#             count = first_diff = 0
#             end = start
#             while end < s_len and count <= k:
#                 if s[end] == s[start]:
#                     end += 1
#                     continue
#                 if count == 0:
#                     first_diff = end
#                 count += 1
#                 if count <= k:
#                     end += 1
#             print(start, end, count)
#             max_len = max(max_len, end-start)
#             start = first_diff
#         return max_len

class Solution(object):
    def characterReplacement(self, s, k):
        window = {}
        s_len = len(s)
        max_len = start = end = 0
        while start < s_len and end < s_len:
            if window.get(s[end]) is None:
                window[s[end]] = 1
            else:
                window[s[end]] += 1
            values = list(window.values())
            print(start, end, window)
            if sum(values) - max(values) > k:
                max_len = max(max_len, end-start)
                window[s[start]] -= 1
                start += 1
            end += 1
        max_len = max(max_len, end - start)
        return max_len


s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))