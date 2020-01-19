class Solution(object):
    def sortColors(self, nums):
        front_index = 0
        end_index = len(nums)-1
        for i in range(len(nums)):
            print(nums, i, front_index, end_index)
            if i > end_index:
                break
            if nums[i] == 0:
                while nums[front_index] == 0 and front_index < i:
                    front_index += 1
                nums[front_index], nums[i] = nums[i], nums[front_index]
                front_index += 1
                if nums[i] == 2:
                    nums[i], nums[end_index] = nums[end_index], nums[i]
                    end_index -= 1
            elif nums[i] == 2:
                while nums[end_index] == 2 and end_index > i:
                    end_index -= 1
                nums[i], nums[end_index] = nums[end_index], nums[i]
                end_index -= 1
                if nums[i] == 0:
                    nums[front_index], nums[i] = nums[i], nums[front_index]
                    front_index += 1
        return nums


if __name__ == '__main__':
    # array = [2,0,2,1,1,0]
    # array = [2, 0, 1]
    # array = [1, 0]
    # array = [1, 2, 0]
    array = [2, 1, 2]
    print(Solution().sortColors(array))