# runtime: 63%; memory: 6%

class Solution(object):
    def nextGreaterElements(self, nums):
        results = [-1] * len(nums)
        stack = [0]
        records = {}

        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                records[j] = i
            stack.append(i)

        while stack:
            index = stack.pop()
            next_index = (index + 1) % len(nums)
            while next_index in records and nums[next_index] <= nums[index]:
                next_index = records[next_index]
            if nums[next_index] > nums[index]:
                records[index] = next_index
        for i in range(len(nums)):
            if i in records:
                results[i] = nums[records[i]]
        return results


if __name__ == '__main__':
    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(Solution().nextGreaterElements(nums))
