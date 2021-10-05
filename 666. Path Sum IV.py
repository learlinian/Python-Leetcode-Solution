# runtime: 11%; memory: 37%
# solution: store all node in dictionary then add occurrence from leaf nodes

import math


class Solution(object):
    def pathSum(self, nums):
        # format: dict[(depth, level)] =  [val, occurrence]
        nums_dict = {}
        for num in nums:
            val = num % 10
            num = num // 10
            level = num % 10
            depth = num // 10
            nums_dict[(depth, level)] = [val, 0]

        for depth, level in nums_dict.keys():
            if (depth + 1, level * 2) in nums_dict or (depth + 1, level * 2 - 1) in nums_dict:
                continue
            while depth > 1:
                parent_level = math.ceil(level / 2)
                if (depth - 1, parent_level) in nums_dict:
                    nums_dict[(depth - 1, parent_level)][1] += 1
                depth -= 1
                level = parent_level

        result = 0
        for val, count in nums_dict.values():
            result += val * max(count, 1)

        return result


if __name__ == '__main__':
    nums = [111, 217, 221, 315, 415]
    print(Solution().pathSum(nums))
