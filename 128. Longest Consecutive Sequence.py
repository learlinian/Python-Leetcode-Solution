# runtime: 65%; memory: 95%
# solution: sort and find the consecutive numbers. Time complexity: O(nlogn). Space complexity: O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        last_v = 10 ** 9
        ans = 1
        current_len = 1
        for i in range(len(nums)):
            if nums[i] == last_v + 1:
                current_len += 1
            elif nums[i] != last_v:
                current_len = 1
            ans = max(ans, current_len)
            last_v = nums[i]
        return ans


if __name__ == '__main__':
    nums = [1, 3, 5, 2, 4]
    print(Solution().longestConsecutive(nums))
