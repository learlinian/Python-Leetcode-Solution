"""Given a set of candidate numbers (candidates) (without duplicates) and a target number (target)
,find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times."""
class Solution(object):
    def combinationSum(self, candidates, target):
        self.result = []
        self.findCombinator([], candidates, target)
        return self.result

        def findCombinator(self, temp, candidates, target):     # iteration function to find all solutions
        if target >= 0:           # break the loop if target is smaller than 0
            for item in candidates:
                if item > target:   # break the loop if smallest item in candidates is greater than target
                    break
                temp.append(item)   # append the item
                print(temp)
                if item == target:
                    self.result.append(temp.copy())     # append the result
                    temp.pop()
                    break
                else:
                    index = candidates.index(item)
                    self.findCombinator(temp, candidates[index:], target - item)
                temp.pop()      # pop item in temp list


if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    s = Solution()
    result = s.combinationSum(nums, 7)
    print(result)
