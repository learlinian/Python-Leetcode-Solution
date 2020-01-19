class Solution(object):
    def subsets(self, nums):
        nums.sort()
        self.result = [[]]
        self.queue = []

        def find(lists):
            for item in lists:
                self.queue.append(item)
                self.result.append(list(self.queue))
                list_temp = list(lists)
                item_index = list_temp.index(item)
                list_temp = list_temp[item_index+1:] if item_index+1 < len(list_temp) else []
                if list_temp:
                    find(list_temp)
                del self.queue[-1]

        find(nums)
        return self.result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))