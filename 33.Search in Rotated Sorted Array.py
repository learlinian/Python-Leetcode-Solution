class Solution1(object):
    def b_search(self, num, target, low, high):
        check_index = (low+high) // 2
        print(num, check_index)
        if low == high and num[check_index] != target:
            return -1
        if num[check_index] == target:
            return check_index

        if num[check_index] < target:
            return self.b_search(num, target, check_index, high)
        else:
            return self.b_search(num, target, low, check_index)

    def findPivot(self, nums, low, high):
        if nums[low] <= nums[high]:
            return -1
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            return mid-1
        if nums[mid] > nums[high]:
            return self.findPivot(nums, mid+1, high)
        return self.findPivot(nums, low, mid - 1)

    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1
        pivot = self.findPivot(nums, 0, length-1)
        if pivot == -1:
            return self.b_search(nums, target, 0, length-1)
        elif nums[pivot+1] <= target <= nums[-1]:
            return self.b_search(nums, target, pivot+1, length-1)
        return self.b_search(nums, target, 0, pivot)


class Solution2(object):
    def search(self, nums, l, r, target):
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        if l > r:
            return -1
        if nums[l] <= nums[mid]:
            if nums[l] <= target <= nums[mid]:
                return self.search(nums, l, mid-1, target)
            return self.search(nums, mid+1, r, target)
        if nums[mid] >= target >= nums[r]:
            return self.search(nums, mid + 1, r, target)
        # return self.search(nums, l, mid - 1, target)


if __name__ == '__main__':
    array = [4,5,6,7,0,1,2]
    target = 2
    # a = [1,2,3,4,5]
    print(Solution2().search(array, 0, len(array)-1, target))
