class Solution(object):
    def __init__(self):
        self.ways = 0
        self.save = {}

    def climbStairs(self, n):
        def climb(val):
            if val == 0:
                self.ways += 1
            else:
                for i in [1, 2]:
                    if val - i >= 0:
                        if val-i in self.save:
                            self.ways += self.save[val-i]
                        else:
                            climb(val-i)
                            self.save[val-i] = self.ways

        climb(n)
        return self.ways




if __name__ == '__main__':
    print(Solution().climbStairs(2))