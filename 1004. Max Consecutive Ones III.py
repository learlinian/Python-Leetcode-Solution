class Solution(object):
    def longestOnes(self, nums, k):
        count = 0
        ans = 0
        k_indexed = []
        for i in range(len(nums)):
            if nums[i] == 1:
                if i == 0:
                    count = 1
                else:
                    count += 1
            elif nums[i] == 0:
                if k > 0:
                    count += 1
                    k -= 1
                    k_indexed.append(i)
                elif k_indexed:
                    count = i - k_indexed[0]
                    del k_indexed[0]
                    k_indexed.append(i)
                else:
                    count = 0
            ans = max(ans, count)
        return ans


if __name__ == '__main__':
    nums = [1,1,1,0,0,0,1,1,1,1]
    k = 0
    print(Solution().longestOnes(nums, k))
