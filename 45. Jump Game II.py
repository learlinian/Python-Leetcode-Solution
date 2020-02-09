"""Not efficient solution but easy to understand"""
# class Solution(object):
#     def jump(self, nums):
#         nums_len = len(nums)
#         steps = [-1] * nums_len
#         steps[0] = 0
#
#         for i in range(1, nums_len):
#             for j in range(i):
#                 if j+nums[j] >= i and steps[j] != -1:
#                     if steps[i] == -1:
#                         steps[i] = steps[j] + 1
#                     else:
#                         steps[i] = min(steps[i], steps[j] + 1)
#         return steps[-1]


"""
h is head which means possible slowest method
t is tail which means possible farthest position
h is same as number of steps
"""
class Solution:
    def jump(self, nums):
        x = len(nums)
        h = t = 0
        while t < x-1:
            t = max([i + nums[i] for i in range(h, t+1)])
            h += 1
        return h


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().jump(nums))