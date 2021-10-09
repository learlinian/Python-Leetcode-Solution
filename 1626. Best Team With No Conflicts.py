# solution: dp, sort by scores
# runtime: 72%; memory: 55%

class Solution:
    def bestTeamScore(self, scores, ages):
        arr = []
        for i in range(len(ages)):
            arr.append([scores[i], ages[i]])
        arr.sort()
        dp = [0] * len(ages)
        for i in range(len(ages)):
            sm = 0
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    sm = max(sm, dp[j])
            dp[i] = sm + arr[i][0]
        return max(dp)


# solution: dp, sort by ages
class Solution2:
    def bestTeamScore(self, scores, ages):
        arr = []
        for i in range(len(ages)):
            arr.append([ages[i], scores[i]])
        arr.sort()
        dp = [0] * len(ages)
        for i in range(len(ages)):
            sm = 0
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    sm = max(sm, dp[j])
            dp[i] = sm + arr[i][1]
        return max(dp)


if __name__ == '__main__':
    scores = [1, 2, 3, 5]
    ages = [8, 9, 10, 1]
    print(Solution2().bestTeamScore(scores, ages))
