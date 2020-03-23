"""time: 39%    memory: 50%"""
class Solution(object):
    def circularArrayLoop(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            return False
        for i in range(nums_len):
            visited = [False] * nums_len
            if visited[i] is False:
                visited[i] = True
                j = (i + nums[i]) % nums_len
                while visited[j] is False:
                    if nums[j] * nums[i] < 0:
                        break
                    visited[j] = True
                    j = (j + nums[j]) % nums_len
                if i == j and (i + nums[i]) % nums_len != i:
                    return True
        return False


# nums = [2,-1,1,2,2]
# nums = [-1, 2]
# nums = [-2,-1,-2,-2]
nums = [2,-1,1,-2,-2]
# nums = [1, 1, 2]
print(Solution().circularArrayLoop(nums))