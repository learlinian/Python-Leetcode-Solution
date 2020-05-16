class Solution(object):
    def search(self, nums, target):
        # print(nums)   # print current list in iteration
        nums_len = len(nums)
        if nums_len == 0:
            return False
        mid = nums_len // 2
        result = False  # check whether checked array contains target
        if nums[mid] == target:
            return True
        elif nums_len == 1:
            return target == nums[0]
        elif target < nums[mid]:  # target is smaller, need to find a larger value
            if mid < nums_len - 1 and (nums[mid] > nums[mid + 1] or nums[mid + 1] > nums[-1]):
                result = self.search(nums[mid + 1:].copy(), target)
            return result if result is True else self.search(nums[:mid].copy(), target)
        else:  # target is larger
            if mid > 0 and (nums[mid - 1] > nums[mid] or nums[0] > nums[mid]):
                result = self.search(nums[:mid].copy(), target)
            return result if result is True else self.search(nums[mid + 1:].copy(), target)


if __name__ == '__main__':
    array = [4, 5, 6, 7, 0, 1, 2]
    for target in [4, 5, 6, 7, 0, 1, 2, 10]:
        print(Solution().search(array, target))
