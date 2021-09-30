# runtime: 99%, memory: 92%

class Solution:
    def canPartitionKSubsets(self, arr, k):
        n = len(arr)

        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = [False] * n

        def backtrack(index, count, curr_sum):
            n = len(arr)

            # We made k - 1 subsets with target_sum and the last subset must also have target_sum.
            if count == k - 1:
                return True

            # No need to proceed further.
            if curr_sum > target_sum:
                return False

            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                return backtrack(0, count + 1, 0)

            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if not taken[j]:
                    # Include this element in current subset.
                    taken[j] = True

                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    # Backtrack step.
                    taken[j] = False

            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            return False

        return backtrack(0, 0, 0)


if __name__ == '__main__':
    # nums = [4, 3, 2, 3, 5, 2, 1]
    nums = [1, 1, 1, 1, 2, 2, 2, 2]
    k = 2
    print(Solution().canPartitionKSubsets(nums, k))
