"""inefficient solution"""
# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         nums_len = len(nums)
#         counts = []
#         ans = 0
#         for i in range(nums_len):
#             if nums[i] % 2 == 1:
#                 for j in range(len(counts)-1, -1, -1):
#                     if counts[j] < k:
#                         counts[j] += 1
#                     elif counts[j] == k:
#                         del counts[:j+1]
#                         break
#                 counts.append(1)
#             else:
#                 counts.append(0)
#             ans += counts.count(k)
#
#         return ans


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        nums_len = len(nums)
        counts = [0] * (k+1)
        ans = 0
        for i in range(nums_len):
            if nums[i] % 2 == 1:
                del counts[-1]
                counts.insert(0, 0)
                counts[1] += 1
            else:
                counts[0] += 1
            ans += counts[-1]
        return ans


nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(Solution().numberOfSubarrays(nums, k))
