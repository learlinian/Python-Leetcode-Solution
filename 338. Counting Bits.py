class Solution(object):
    def countBits(self, num):
        result = [0]
        for i in range(1, num+1):
            result.append(result[i & i-1]+1)
        return result


if __name__ == "__main__":
    num = 5
    s = Solution()
    print(s.countBits(num))