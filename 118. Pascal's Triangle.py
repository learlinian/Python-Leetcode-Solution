class Solution(object):
    def generate(self, numRows):
        results = []
        for _ in range(numRows):
            if not results:
                results.append([1])
            elif len(results[-1]) == 1:
                results.append([1, 1])
            else:
                result = [1]
                last = results[-1]
                for i in range(1, len(last)):
                    result.append(last[i]+last[i-1])
                result.append(1)
                results.append(result)
        return results

print(Solution().generate(1))
