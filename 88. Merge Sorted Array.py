class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        return nums1

class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        start_i = 0
        end_i = m - 1
        for i in range(n):
            if nums1[end_i] <= nums2[i]:
                nums1[end_i+1:] = nums2[i:]
                return nums1
            while nums1[start_i] < nums2[i] and start_i < end_i:
                start_i += 1
            nums1.insert(start_i, nums2[i])
            nums1.pop()
            end_i += 1
        return nums1

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(Solution2().merge(nums1, m, nums2, n))