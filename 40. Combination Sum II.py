class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        candidates.reverse()
        self.results = []

        def test(candidates, target, combination):
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                # print(combination, target)
                combination.append(candidates[i])
                if candidates[i] == target:
                    temp = list(combination)
                    temp.sort()
                    # print('temp: ' + str(temp))
                    if temp not in self.results:
                        self.results.append(temp)
                elif candidates[i] < target:
                    test(candidates[i+1:], target-candidates[i], combination)
                if combination:
                    del combination[-1]

        test(candidates, target, [])
        return self.results


if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    print(Solution().combinationSum2(candidates, target))
