class Solution(object):
    def search(self, nums, target):
        print(nums)
        nums_len = len(nums)
        if nums_len == 0:
            return -1
        mid = nums_len // 2
        if nums[mid] == target:
            return mid
        elif nums_len == 1:
            return -1 if target != nums[0] else 0
        elif target < nums[mid]:    # target is smaller, need to find a larger value
            if mid < nums_len - 1 and (nums[mid] > nums[mid+1] or nums[mid+1] > nums[-1]):
                result = self.search(nums[mid+1:].copy(), target)
                print("result: ", result)
                if result != -1:
                    return result + mid + 1
            return self.search(nums[:mid].copy(), target)
        else:  # target is larger
            if mid > 0 and (nums[mid-1] > nums[mid] or nums[0] > nums[mid]):
                result = self.search(nums[:mid].copy(), target)
                if result != -1:
                    return result
            result = self.search(nums[mid + 1:].copy(), target)
            return mid + 1 + result if result != -1 else -1


if __name__ == '__main__':
    array = [4,5,6,7,0,1,2]
    target = 8
    print(Solution().search(array, target))
