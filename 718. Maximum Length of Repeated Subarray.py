# runtime: 85%; memory: 98%

class Solution(object):
    def findLength(self, A, B):
        result = 0
        memo = [0] * (len(B) + 1)
        for i in range(len(A) - 1, -1, -1):
            temp_memo = [0] * (len(B) + 1)
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    temp_memo[j] = memo[j+1] + 1
            result = max(result, max(temp_memo))
            memo = temp_memo.copy()

        return result


if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    print(Solution().findLength(nums1, nums2))
