class Solution(object):
    def merge(self, intervals):
        # sort intervals with the starting value
        intervals = sorted(intervals)
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                if interval[0] > result[-1][1] or interval[1] < result[-1][0]:
                    result.append(interval)
                elif result[-1][0] <= interval[0] <= result[-1][1]:
                    if interval[1] > result[-1][1]:
                        result[-1] = [result[-1][0], interval[1]]
        return result


if __name__ == '__main__':
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    intervals2 = [[1, 4], [4, 5]]
    intervals3 = [[1,4],[0,4]]
    print(Solution().merge(intervals3))