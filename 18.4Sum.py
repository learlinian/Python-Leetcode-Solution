# 1st item index: i; 2nd item index: j; 3rd item index: k; 4th item index: h;

class Solution:    
    def fourSum(self, nums, target):
        result = []
        nums.sort()
        length = len(nums)-1
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:          # if 1st index is duplicate, continue
                continue
            for j in range(i+1, length-1):
                if j > i+1 and nums[j] == nums[j-1]:    # if 2nd index is duplicate, continue
                    continue
                k = j+1
                h = length
                while k < h:                            # while 3rd index is smaller than the 4th index
                    curr = nums[i] + nums[j] + nums[k] + nums[h]
                    if curr == target:
                        result.append([nums[i], nums[j], nums[k], nums[h]])
                        while k < h and nums[k] == nums[k+1]:
                            k += 1
                        while k < h and nums[h] == nums[h-1]:
                            h -= 1
                        k += 1
                        h -= 1
                    elif curr > target:
                        h -= 1
                    else:
                        k += 1
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
