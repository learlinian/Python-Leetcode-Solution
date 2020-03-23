class Solution:
    def numSubarraysWithSum(self, A, S):
        num_zeros = list(map(len, ''.join(map(str, A)).split('1')))
        if S < 0:
            return 0
        if S == 0:
            return sum(i*(i+1)//2 for i in num_zeros)
        return sum((num_zeros[i]+1) * (num_zeros[i+S]+1) for i in range(len(num_zeros)-S))


A = [1,0,1,0,1]
S = 2
# A = [0,0,0,0,0,0,1,0,0,0]
# S = 0
print(Solution().numSubarraysWithSum(A, S))
