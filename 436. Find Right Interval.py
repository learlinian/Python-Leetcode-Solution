class Solution(object):
    def findRightInterval(self, intervals):
        sorted_intervals = []
        sorted_intervals += [(v[0], 'S', i) for i, v in enumerate(intervals)]
        sorted_intervals += [(v[1], 'E', i) for i, v in enumerate(intervals)]
        sorted_intervals.sort()

        ans = [-1] * len(intervals)
        end_index = []
        for interval in sorted_intervals:
            if interval[1] == 'E':
                end_index.append(interval[2])
            else:
                for index in end_index:
                    ans[index] = interval[2]
                end_index.clear()
        return ans


if __name__ == '__main__':
    intervals = [[3, 4], [2, 3], [1, 2]]
    print(Solution().findRightInterval(intervals))