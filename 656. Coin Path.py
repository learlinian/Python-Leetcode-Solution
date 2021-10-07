# solution: dynamic programming + DFS
# runtime: 92%; memory: 57%

class Solution(object):
    def cheapestJump(self, coins, maxJump):
        max_val = 100001
        dp = [0] * len(coins)
        dp[0] = coins[0]
        paths = {}

        for i in range(1, len(coins)):
            if coins[i] == -1:
                dp[i] = max_val
                continue
            prev_min = min(dp[max(0, i - maxJump):i])
            if prev_min == max_val:
                return []
            dp[i] = prev_min + coins[i]
            for j in range(max(0, i - maxJump), i):
                if dp[j] == prev_min:
                    try:
                        paths[j].append(i)
                    except:
                        paths[j] = [i]

        def dfs(index, result):
            if index == len(coins) - 1:
                return result, True
            if index not in paths:
                return [], False
            for v in paths[index]:
                ans, ok = dfs(v, result + [v+1])
                if ok:
                    return ans, True
            return [], False

        ans, ok = dfs(0, [])
        return [1] + ans if ok else []


if __name__ == '__main__':
    # coins = [1,2,4,-1,2]
    # maxJump = 2

    # coins = [0, 0, 0, 0, 0, 0]
    # maxJump = 3

    # coins = [0, -1, -1, -1]
    # maxJump = 5

    coins = [1,2,3,4,5]
    maxJump = 2

    # coins = [1]
    # maxJump = 1

    # coins = [28, 44, 71, -1, 99, 59, 78, 60, 80, 18, 71, 1, 68, 6, 19, 66, 62, 74, 7, 67, 18, 70, 22, 15, 6, 58, 95, 26,
    #          52, 38,
    #          80, 60, 34, 56, 9, 8, 34, 3, 25, 33, 45, 35, 15, 27, 97, 22, 2, 2, 71, 91, 44, 28, 91, 93, 25, 2, 53, 54,
    #          15, 14,
    #          56, 97, 51, 36, 81, 29, 15, 58, 97]
    # maxJump = 42
    print(Solution().cheapestJump(coins, maxJump))
