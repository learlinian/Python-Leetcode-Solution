class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        array = []

        def get_next(sub_arr):
            if sorted(array) not in result:
                result.append(list(sorted(array)))
            for i in range(len(sub_arr)):
                array.append(sub_arr[i])
                get_next(sub_arr[i+1:])
                array.pop()

        get_next(nums)
        return result


nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))