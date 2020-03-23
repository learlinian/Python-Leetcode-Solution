class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        results = {}
        visited = {}

        for num in nums:
            print(results)
            delete = False
            if visited.get(num) is None:
                if results.get(num+1):
                    results[num] = results[num+1] + 1
                    results[num+results[num+1]] = results[num]
                    if results[num+1] > 2:
                        del results[num+1]
                else:
                    results[num] = 1
                if results.get(num-1):
                    if results[num - 1] > 1:
                        delete = True
                    update_val = results[num - results[num - 1]] + results[num]
                    results[num - results[num - 1]] = update_val
                    results[num + results[num] - 1] = update_val
                    if delete:
                        del results[num-1]
                    del results[num]
                visited[num] = True
        print(results)
        return max(results.values())


nums = [1,3,5,2,4]
print(Solution().longestConsecutive(nums))
