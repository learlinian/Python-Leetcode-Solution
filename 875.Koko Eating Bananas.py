import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        min_K = math.ceil(sum(piles)/H)
        min_K = max(min_K, 1)
        hour = -1
        while hour == -1 or hour > H:
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/min_K)
            min_K += 1

        return int(min_K)-1


if __name__ == '__main__':
    piles = [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
    H = 823855818
    print(Solution().minEatingSpeed(piles, H))
