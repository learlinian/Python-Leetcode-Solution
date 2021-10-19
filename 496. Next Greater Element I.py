# solution: stack
# runtime: 51%; memory: 13%

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        mapping = {}
        stack = []
        result = [-1] * len(nums1)
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
        for i, num in enumerate(nums1):
            if num in mapping:
                result[i] = mapping[num]
        return result


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))
