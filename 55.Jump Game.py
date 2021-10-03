# solution 1: BFS
# run time: 47%; memory: 7%


class Solution(object):
    def canJump(self, nums):
        nums_len = len(nums)
        result_arr = [False] * nums_len
        result_arr[0] = True
        current_true_i = 0

        for i in range(nums_len):
            if nums[i] >= 1 and result_arr[i]:
                if i + nums[i] > current_true_i:
                    result_arr[current_true_i:i + nums[i] + 1] = [True] * (i + nums[i] + 1 - current_true_i)
                    current_true_i = i + nums[i]
        return result_arr[-1]


# solution 2: DFS
# unaccepted: exceed time limit
class Solution2(object):
    def canJump(self, nums):
        nums_len = len(nums)
        result_arr = [False] * nums_len

        def dfs(stack, current_i):
            if current_i == nums_len - 1:
                return True
            if result_arr[current_i] is True:
                return False
            if not stack:
                return False
            result_arr[current_i] = True
            val = stack.pop()
            if val == 0:
                return False
            for i in range(1, val + 1):
                if current_i + i >= nums_len:
                    return False
                stack.append(nums[current_i + i])
                if dfs(stack, current_i + i) is True:
                    return True
            return False

        return dfs([nums[0]], 0)


if __name__ == '__main__':
    nums = [0]
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # nums = [0, 2, 3]
    print(Solution2().canJump(nums))
